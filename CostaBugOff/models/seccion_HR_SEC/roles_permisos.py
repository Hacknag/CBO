import oracledb
from db import get_connection

# ---------------- Roles y Permisos (vista de que permisos tiene cada rol) ---------------- #
# ---------------- Roles y Permisos (vista de que permisos tiene cada rol) ---------------- #

def obtener_roles_permisos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM FIDE_ROLES_PERMISOS_V ORDER BY "ROL ID"')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos

def obtener_roles():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT ID_ROL, NOMBRE FROM FIDE_ROLES_TB WHERE ID_ESTADO = 1 ORDER BY NOMBRE')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos

def obtener_permisos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT ID_PERMISO, NOMBRE FROM FIDE_PERMISOS_TB WHERE ID_ESTADO = 1 ORDER BY NOMBRE')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos

def insertar_permiso_x_rol(id_rol, id_permiso, id_estado=1):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_PERMISOS_X_ROL_INSERT_SP", [
            id_rol, id_permiso, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def eliminar_permiso_x_rol_logico(id_rol, id_permiso):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_PERMISOS_X_ROL_DELETE_SP", [
            id_rol, id_permiso
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()
