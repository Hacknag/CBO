import oracledb
from db import get_connection
#tener cuidado con esto que con quitar una linea se pudre toda la pagina xddddddd
def insertar_visita(id_visita, nombre, fecha_programada, fecha_realizada, id_suscripcion,id_cliente, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_VISITAS_INSERT_SP", [
            id_visita, nombre, fecha_programada, fecha_realizada, id_suscripcion, id_cliente, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def actualizar_visita(id_visita, nombre, fecha_programada, fecha_realizada, id_suscripcion, id_cliente, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_VISITAS_UPDATE_SP", [
            id_visita, nombre, fecha_programada, fecha_realizada, id_suscripcion, id_cliente, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def eliminar_visita(id_visita):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_VISITAS_DELETE_SP", [
            id_visita
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def obtener_visitas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM FIDE_CITAS_PROGRAMADAS_V')
    datos = cursor.fetchall() 
    cursor.close()
    conn.close()
    return datos