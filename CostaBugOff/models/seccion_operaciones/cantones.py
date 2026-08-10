import oracledb
from db import get_connection


def insertar_canton(nombre, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_CANTONES_INSERT_SP", [
            nombre, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def actualizar_canton(id_canton, nombre, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_CANTONES_UPDATE_SP", [
            id_canton, nombre, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def eliminar_cantones_logico(id_canton):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_CANTONES_DELETE_SP", [
            id_canton
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def obtener_cantones(id_estado=None):
    conn = get_connection()
    cursor = conn.cursor()
    if id_estado:
        cursor.execute(
            'SELECT * FROM FIDE_CANTONES_V WHERE "ID ESTADO" = :id_estado ORDER BY "CANTON ID"',
            {"id_estado": id_estado}
        )
    else:
        cursor.execute('SELECT * FROM FIDE_CANTONES_V ORDER BY "CANTON ID"')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos



# ---------------- Buscar CANTON ---------------- #
# ---------------- Buscar CANTON ---------------- #
# ---------------- Buscar CANTON ---------------- #
def buscar_cantones(query):
    """Consulta directamente la tabla clientes en Oracle Database y retorna una lista de diccionarios."""
    if not query:
        return []

    conexion = get_connection()
    cursor = conexion.cursor() 
    search_term = f"%{query}%"
    
    # Consulta directa a la TABLA clientes (Sintaxis Oracle SQL)
    sql = """
    SELECT 
        ID_CANTON, 
        TRIM(NOMBRE) AS CANTON
    FROM FIDE_CANTONES_TB 
    WHERE ID_ESTADO = 1
    AND LOWER(NOMBRE) LIKE LOWER(:1)
    FETCH FIRST 8 ROWS ONLY
    """
    
    cursor.execute(sql, (search_term,))
    resultados = cursor.fetchall()
    
    cursor.close()
    conexion.close()

    # Mapeo de la lista de tuplas de Oracle
    cantones = [
        {
            "id": row[0],
            "nombre": row[1]
        }
        for row in resultados
    ]
    
    return cantones