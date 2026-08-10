import oracledb
from db import get_connection

def insertar_servicio_realizado(ubicacion, informe, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        # Se envía None (NULL) para que la BD aplique el DEFAULT de la secuencia
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_SERVICIOS_REALIZADOS_INSERT_SP", [            
            ubicacion,
            informe,
            int(id_estado)
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def actualizar_servicio_realizado(id_servicio_realizado, ubicacion, informe, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_SERVICIOS_REALIZADOS_UPDATE_SP", [
            int(id_servicio_realizado),
            ubicacion,
            informe,
            int(id_estado)
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def eliminar_servicio_realizado_logico(id_servicio_realizado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_SERVICIOS_REALIZADOS_DELETE_SP", [
            id_servicio_realizado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def obtener_servicios_realizados(id_estado=None):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM FIDE_SERVICIOS_REALIZADOS_V ORDER BY "ID SERVICIO"')
        datos = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return datos