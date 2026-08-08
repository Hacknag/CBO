import oracledb
from db import get_connection


def insertar_usuario(id_usuario, usuario, contrasena, id_empleado, id_rol, id_estado, id_cliente):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.SP_FIDE_USUARIOS_INSERT", [
            id_usuario, usuario, contrasena, id_empleado, id_rol, id_estado, id_cliente
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def actualizar_usuario(id_usuario, usuario, contrasena, id_empleado, id_rol, id_estado, id_cliente):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.SP_FIDE_USUARIOS_UPDATE", [
            id_usuario, usuario, contrasena, id_empleado, id_rol, id_estado, id_cliente
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def eliminar_usuario(id_usuario):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.SP_FIDE_USUARIOS_DELETE", [
            id_usuario
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def obtener_usuarios(id_estado=None):
    conn = get_connection()
    cursor = conn.cursor()
    if id_estado:
        cursor.execute(
            'SELECT * FROM FIDE_USUARIOS_V WHERE "ID ESTADO" = :id_estado ORDER BY "ID USUARIO"',
            {"id_estado": id_estado}
        )
    else:
        cursor.execute('SELECT * FROM FIDE_USUARIOS_V ORDER BY "USUARIO ID"')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos
