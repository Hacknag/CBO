import oracledb
from db import get_connection

def insertar_servicio_realizado(id_servicio_realizado, ubicacion, informe, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_SERVICIOS_REALIZADOS_INSERT_SP", [
            id_servicio_realizado, ubicacion, informe, id_estado
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
            id_servicio_realizado, ubicacion, informe, id_estado
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
    cursor = conn.cursor()
    if id_estado:
        cursor.execute(
            'SELECT * FROM FIDE_SERVICIOS_REALIZADOS_V WHERE "ID ESTADO" = :id_estado ORDER BY "ID SERVICIO" DESC',
            {"id_estado": id_estado}
        )
    else:
        cursor.execute('SELECT * FROM FIDE_SERVICIOS_REALIZADOS_V ORDER BY "ID SERVICIO" DESC')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos