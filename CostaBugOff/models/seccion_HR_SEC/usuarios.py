import oracledb
from db import get_connection

# ---------------- Usuarios (vista con id_usuario, rol, nombre y estado) ---------------- #
# ---------------- Usuarios (vista con id_usuario, rol, nombre y estado) ---------------- #

def obtener_usuarios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM FIDE_USUARIOS_V ORDER BY "USUARIO ID"')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos

def eliminar_usuario_logico(id_usuario):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_USUARIOS_DELETE_SP", [
            id_usuario
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()
