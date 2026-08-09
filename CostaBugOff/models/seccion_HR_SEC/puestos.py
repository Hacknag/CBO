import oracledb
from db import get_connection

def insertar_puesto(nombre, descripcion, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_PUESTOS_INSERT_SP", [
            nombre, descripcion, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def actualizar_puesto(id_puesto, nombre, descripcion, id_estado=1):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_PUESTOS_UPDATE_SP", [
            id_puesto, nombre, descripcion, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def eliminar_puesto_logico(id_puesto):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_PUESTOS_DELETE_SP", [
            id_puesto
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def obtener_puestos_general(id_estado=None):
    conn = get_connection()
    cursor = conn.cursor()
    if id_estado:
        cursor.execute(
            'SELECT * FROM FIDE_PUESTOS_V WHERE "ID_ESTADO" = :id_estado ORDER BY "PUESTO ID"',
            {"id_estado": id_estado}
        )
    else:
        cursor.execute('SELECT * FROM FIDE_PUESTOS_V ORDER BY "PUESTO ID"')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos