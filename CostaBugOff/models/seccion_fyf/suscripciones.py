import oracledb
from db import get_connection
#tener cuidado con esto que con quitar una linea se pudre toda la pagina xddddddd
def insertar_suscripcion(id_suscripcion, fecha_inicio, fecha_fin, id_pago, Estado, precio):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_SUSCRIPCIONES_INSERT_SP", [
            id_suscripcion, fecha_inicio, fecha_fin, id_pago, Estado, precio
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def actualizar_suscripcion(id_suscripcion, fecha_inicio, fecha_fin, id_pago, Estado, precio):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_SUSCRIPCIONES_UPDATE_SP", [
            id_suscripcion, fecha_inicio, fecha_fin, id_pago, Estado, precio
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def eliminar_suscripcion(id_suscripcion):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_SUSCRIPCIONES_DELETE_SP", [
            id_suscripcion
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def obtener_suscripciones():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM FIDE_SUSCRIPCIONES_V ORDER BY "SUSCRIPCION ID"')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos

# ---------------- Buscar SUSCRIPCIONES ---------------- #
# ---------------- Buscar SUSCRIPCIONES ---------------- #
# ---------------- Buscar SUSCRIPCIONES ---------------- #

def buscar_suscripciones(query):
    if not query:
        return []

    conexion = None
    try:
        conexion = get_connection()
        cursor = conexion.cursor() 
        search_term = f"%{query}%"
        
        sql = """
        SELECT 
            ID_SUSCRIPCION, 
            TRIM(NOMBRE) AS SUSCRIPCION
        FROM FIDE_SUSCRIPCIONES_TB 
        WHERE ID_ESTADO = 1
        AND LOWER(NOMBRE) LIKE LOWER(:1)
        FETCH FIRST 8 ROWS ONLY
        """
        
        cursor.execute(sql, (search_term,))
        resultados = cursor.fetchall()
        cursor.close()

        # Formatear el resultado en una lista de diccionarios
        return [{"id": fila[0], "nombre": fila[1]} for fila in resultados]

    except Exception as e:
        print(f"Error en buscar_suscripciones: {e}")
        return [] # Garantiza retornar una lista vacía si falla la BD
    finally:
        if conexion:
            conexion.close()