import oracledb
from db import get_connection


def insertar_servicio(NOMBRE, ID_PLAGA, ID_ESTADO, ID_USUARIO=1, ID_SERVICIO_REALIZADO=1):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_SERVICIOS_INSERT_SP", [              # Se envía None/NULL para que aplique la secuencia DEFAULT en Oracle
            NOMBRE,
            int(ID_PLAGA) if ID_PLAGA else None,
            int(ID_USUARIO),
            int(ID_SERVICIO_REALIZADO),
            int(ID_ESTADO)
        ])
        conexion.commit()
    except Exception as e:  
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def actualizar_servicio(ID_SERVICIO, NOMBRE, ID_PLAGA, ID_ESTADO, ID_USUARIO=1, ID_SERVICIO_REALIZADO=1):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_SERVICIOS_UPDATE_SP", [
            int(ID_SERVICIO),
            NOMBRE,
            int(ID_PLAGA) if ID_PLAGA else None,
            int(ID_USUARIO),
            int(ID_SERVICIO_REALIZADO),
            int(ID_ESTADO)
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def eliminar_servicio_logico(id_servicio):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_SERVICIOS_DELETE_SP", [
            id_servicio
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def obtener_servicios(id_estado=None):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM FIDE_SERVICIOS_DISPONIBLES_V')
        datos = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return datos
