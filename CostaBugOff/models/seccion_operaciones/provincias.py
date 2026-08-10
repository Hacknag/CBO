import oracledb
from db import get_connection


def insertar_provincia(nombre, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_PROVINCIAS_INSERT_SP", [
            nombre, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def actualizar_provincia(id_provincia, nombre, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_PROVINCIAS_UPDATE_SP", [
            id_provincia, nombre, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def eliminar_provincia_logico(id_provincia):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_PROVINCIAS_DELETE_SP", [
            id_provincia
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def obtener_provincia(id_estado=None):
    conn = get_connection()
    cursor = conn.cursor()
    if id_estado:
        cursor.execute(
            'SELECT * FROM FIDE_PROVINCIAS_V WHERE "ID ESTADO" = :id_estado ORDER BY "PROVINCIA ID"',
            {"id_estado": id_estado}
        )
    else:
        cursor.execute('SELECT * FROM FIDE_PROVINCIAS_V ORDER BY "PROVINCIA ID"')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos
