import oracledb
from db import get_connection
#tener cuidado con esto que con quitar una linea se pudre toda la pagina xddddddd
def insertar_plaga(tipo, nombre, descripcion, unidades_necesarias, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_PLAGAS_INSERT_SP", [
            tipo, nombre, descripcion, unidades_necesarias, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def actualizar_plaga(tipo, nombre, descripcion, unidades_necesarias, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_PLAGAS_UPDATE_SP", [
            tipo, nombre, descripcion, unidades_necesarias, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def eliminar_plaga_logica(id_plaga):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_PLAGAS_DELETE_SP", [
            id_plaga
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def obtener_plagas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM FIDE_PLAGAS_V ORDER BY "PLAGA ID"')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos


def buscar_plagas(query):
    if not query:
        return []

    conexion = None
    try:
        conexion = get_connection()
        cursor = conexion.cursor() 
        search_term = f"%{query}%"
        
        sql = """
        SELECT 
            ID_PLAGA, 
            TRIM(NOMBRE) AS PLAGA
        FROM FIDE_PLAGAS_TB 
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
        print(f"Error en buscar_plagas: {e}")
        return [] # Garantiza retornar una lista vacía si falla la BD
    finally:
        if conexion:
            conexion.close()