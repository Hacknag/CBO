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
