import oracledb
from db import get_connection
#tener cuidado con esto que con quitar una linea se pudre toda la pagina xddddddd

# ---------------- Insertar Clientes ---------------- #
# ---------------- Insertar Clientes ---------------- #
def insertar_cliente(nombre, apellido_paterno, apellido_materno, fecha_registro, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_CLIENTES_INSERT_SP", [
            nombre, apellido_paterno, apellido_materno, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

# ---------------- Actualizar Clientes ---------------- #
# ---------------- Actualizar Clientes ---------------- #
def actualizar_cliente(id_cliente, nombre, apellido_paterno, apellido_materno, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_CLIENTES_UPDATE_SP", [
            id_cliente, nombre, apellido_paterno, apellido_materno, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

# ---------------- Eliminar Clientes ---------------- #
# ---------------- Eliminar Clientes ---------------- #
def eliminar_cliente_logico(id_cliente):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_CLIENTES_DELETE_SP", [
            id_cliente
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

# ---------------- Obtener Clientes ---------------- #
# ---------------- Obtener Clientes ---------------- #
def obtener_clientes():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM FIDE_CLIENTES_ACTIVOS_V ORDER BY "CLIENTE ID"')
        datos = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return datos

# ---------------- Registrar Clientes ---------------- #
# ---------------- Registrar Clientes ---------------- #
def registrar_cliente(nombre, apellido_paterno, apellido_materno, correo, password):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        v_id_usuario = cursor.var(oracledb.NUMBER)
        v_id_cliente = cursor.var(oracledb.NUMBER)
        v_mensaje = cursor.var(str)
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_CLIENTES_REGISTRAR_SP", [
            nombre, apellido_paterno, apellido_materno, correo, password,
            v_id_usuario, v_id_cliente, v_mensaje
        ])
    finally:
        cursor.close()
        conexion.close()
    return v_id_usuario.getvalue(), v_id_cliente.getvalue(), v_mensaje.getvalue()