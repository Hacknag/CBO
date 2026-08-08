import oracledb
from db import get_connection

# =====================================================================
# Este modulo depende de procedimientos/vistas del paquete
# FIDE_PROYECTO_FINAL_PKG que Anthony todavia tiene pendientes:
#   - FIDE_DETALLE_TRANSACCIONES_INSERT_SP debe quedar con la firma nueva
#     (P_ID_DETALLE_TRANSACCION, P_ID_TRANSACCION, P_ID_PRODUCTO,
#      P_ID_SUSCRIPCION, P_CANTIDAD, P_PRECIO_UNITARIO)
#   - Las vistas FIDE_FACTURAS_V y FIDE_FACTURA_DETALLE_V
# Y de la parte de Charlie (ya lista o por confirmar):
#   - FIDE_FACTURAS_INSERT_SP con ID_CLIENTE / DIRECCION / TELEFONO / NUMERO OUT
#   - FIDE_DESCONTAR_STOCK_SP(P_ID_TRANSACCION) -> cursor que baja stock
# Mientras eso no este en la base, el checkout va a tronar. Es esperado.
# =====================================================================


def obtener_metodos_pago():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT ID_METODO_PAGO, NOMBRE
            FROM FIDE_METODOSDEPAGO_TB
            WHERE ID_ESTADO = 1
            ORDER BY ID_METODO_PAGO
        ''')
        datos = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return datos


def _siguiente_id(cursor, tabla, columna_id):
    cursor.execute(f'SELECT NVL(MAX({columna_id}), 0) + 1 FROM {tabla}')
    return cursor.fetchone()[0]


# Duracion por defecto de una suscripcion antes de que le toque renovar.
# Todos los planes del catalogo se facturan mensual, por eso 30 dias fijos.
DIAS_DURACION_SUSCRIPCION = 30


def procesar_checkout(id_cliente, id_metodo_pago, direccion, telefono, carrito):
    """
    carrito: lista de dicts, cada uno con:
        tipo: "producto" o "suscripcion"
        id: id_producto o id_suscripcion
        cantidad: int
        precio_unitario: float (el precio ya congelado, tomado del catalogo)
    Devuelve (id_factura, numero_factura)
    """
    if not carrito:
        raise ValueError("El carrito esta vacio")

    total = sum(item["cantidad"] * item["precio_unitario"] for item in carrito)

    conexion = get_connection()
    try:
        cursor = conexion.cursor()

        # 1. Pago
        id_pago = _siguiente_id(cursor, "FIDE_PAGOS_TB", "ID_PAGO")
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_PAGOS_INSERT_SP", [
            id_pago, id_metodo_pago, 1
        ])

        # 2. Transaccion (P_ID_DETALLE_TRANSACCION va en None, ese FK quedo
        # obsoleto desde que el detalle pasa a ser 1 factura -> muchas lineas)
        id_transaccion = _siguiente_id(cursor, "FIDE_TRANSACCIONES_TB", "ID_TRANSACCION")
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_TRANSACCIONES_INSERT_SP", [
            id_transaccion, id_pago, total, None, 1
        ])

        # 3. Factura
        id_factura = _siguiente_id(cursor, "FIDE_FACTURAS_TB", "ID_FACTURA")
        v_numero = cursor.var(str)
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_FACTURAS_INSERT_SP", [
            id_factura, id_cliente, total, id_transaccion, direccion, telefono, v_numero
        ])
        numero_factura = v_numero.getvalue()

        # 4. Detalle: una linea por cada item del carrito
        id_detalle = _siguiente_id(cursor, "FIDE_DETALLE_TRANSACCIONES_TB", "ID_DETALLE_TRANSACCION")
        for item in carrito:
            id_producto = item["id"] if item["tipo"] == "producto" else None
            id_suscripcion = item["id"] if item["tipo"] == "suscripcion" else None
            cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_DETALLE_TRANSACCIONES_INSERT_SP", [
                id_detalle, id_transaccion, id_producto, id_suscripcion,
                item["cantidad"], item["precio_unitario"]
            ])
            id_detalle += 1

        # 4.5. Si compro una suscripcion, ademas de la linea de la factura,
        # se crea/renueva su registro de suscripcion activa (para el modulo
        # de Renovaciones: cliente + plan + metodo de pago + fecha de vencimiento)
        for item in carrito:
            if item["tipo"] != "suscripcion":
                continue
            v_id_cliente_suscripcion = cursor.var(oracledb.NUMBER)
            cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_CLIENTES_SUSCRIPCIONES_INSERT_SP", [
                id_cliente, item["id"], id_metodo_pago,
                DIAS_DURACION_SUSCRIPCION, v_id_cliente_suscripcion
            ])

        # 5. Descontar stock (cursor de Charlie, recorre el detalle de la transaccion)
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_DESCONTAR_STOCK_SP", [
            id_transaccion
        ])

        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

    return id_factura, numero_factura


def obtener_factura(id_factura):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM FIDE_FACTURAS_V WHERE ID_FACTURA = :1', [id_factura])
        columnas = [c[0] for c in cursor.description]
        fila = cursor.fetchone()
    finally:
        cursor.close()
        conn.close()
    if fila is None:
        return None
    return dict(zip(columnas, fila))


def obtener_detalle_factura(id_factura):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM FIDE_FACTURA_DETALLE_V WHERE ID_FACTURA = :1', [id_factura])
        columnas = [c[0] for c in cursor.description]
        filas = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return [dict(zip(columnas, fila)) for fila in filas]


def obtener_todas_facturas():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM FIDE_FACTURAS_V ORDER BY FECHA DESC')
        columnas = [c[0] for c in cursor.description]
        filas = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return [dict(zip(columnas, fila)) for fila in filas]


def obtener_facturas_cliente(id_cliente):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM FIDE_FACTURAS_V WHERE ID_CLIENTE = :1 ORDER BY FECHA DESC', [id_cliente])
        columnas = [c[0] for c in cursor.description]
        filas = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return [dict(zip(columnas, fila)) for fila in filas]
