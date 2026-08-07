import oracledb
from db import get_connection


def insertar_permiso(id_permiso, nombre, descripcion, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.SP_FIDE_PERMISOS_INSERT", [
            id_permiso, nombre, descripcion, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def actualizar_permiso(id_permiso, nombre, descripcion, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.SP_FIDE_PERMISOS_UPDATE", [
            id_permiso, nombre, descripcion, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def eliminar_permiso(id_permiso):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.SP_FIDE_PERMISOS_DELETE", [
            id_permiso
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def obtener_permisos(id_estado=None):
    conn = get_connection()
    cursor = conn.cursor()
    if id_estado:
        cursor.execute(
            'SELECT * FROM FIDE_PERMISOS_V WHERE "ID ESTADO" = :id_estado ORDER BY "ID PERMISO"',
            {"id_estado": id_estado}
        )
    else:
        cursor.execute('SELECT * FROM FIDE_PERMISOS_V ORDER BY "ID PERMISO"')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos
