import oracledb
from db import get_connection


def insertar_distrito(nombre, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_DISTRITOS_INSERT_SP", [
            nombre, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def actualizar_distrito(id_distrito, nombre, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_DISTRITOS_UPDATE_SP", [
            id_distrito, nombre, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def eliminar_distrito_logico(id_distrito):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_DISTRITOS_DELETE_SP", [
            id_distrito
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def obtener_distritos(id_estado=None):
    conn = get_connection()
    cursor = conn.cursor()
    if id_estado:
        cursor.execute(
            'SELECT * FROM FIDE_DISTRITOS_V WHERE "ID ESTADO" = :id_estado ORDER BY "DISTRITO ID"',
            {"id_estado": id_estado}
        )
    else:
        cursor.execute('SELECT * FROM FIDE_DISTRITOS_V ORDER BY "DISTRITO ID"')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos


# ---------------- Buscar CANTON ---------------- #
# ---------------- Buscar CANTON ---------------- #
# ---------------- Buscar CANTON ---------------- #
def buscar_distritos(query):
    """Consulta directamente la tabla clientes en Oracle Database y retorna una lista de diccionarios."""
    if not query:
        return []

    conexion = get_connection()
    cursor = conexion.cursor() 
    search_term = f"%{query}%"
    
    # Consulta directa a la TABLA clientes (Sintaxis Oracle SQL)
    sql = """
    SELECT 
        ID_DISTRITO, 
        TRIM(NOMBRE) AS DISTRITO
    FROM FIDE_DISTRITOS_TB 
    WHERE ID_ESTADO = 1
    AND LOWER(NOMBRE) LIKE LOWER(:1)
    FETCH FIRST 8 ROWS ONLY
    """
    
    cursor.execute(sql, (search_term,))
    resultados = cursor.fetchall()
    
    cursor.close()
    conexion.close()

    # Mapeo de la lista de tuplas de Oracle
    distritos = [
        {
            "id": row[0],
            "nombre": row[1]
        }
        for row in resultados
    ]
    
    return distritos