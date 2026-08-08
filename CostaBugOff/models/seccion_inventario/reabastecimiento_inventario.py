import oracledb
from db import get_connection

def insertar_reabastecimiento(id_reabastecimiento, cantidad, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_REABASTECIMIENTO_INVENTARIO_INSERT_SP", [
            id_reabastecimiento, cantidad, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def actualizar_reabastecimiento(id_reabastecimiento, cantidad, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_REABASTECIMIENTO_INVENTARIO_UPDATE_SP", [
            id_reabastecimiento, cantidad, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def eliminar_reabastecimiento_logico(id_reabastecimiento):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_REABASTECIMIENTO_INVENTARIO_DELETE_SP", [
            id_reabastecimiento
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def obtener_reabastecimientos(id_estado=None):
    conn = get_connection()
    cursor = conn.cursor()
    if id_estado:
        cursor.execute(
            'SELECT * FROM FIDE_REABASTECIMIENTO_INVENTARIO_V WHERE "ID ESTADO" = :id_estado ORDER BY "REABASTECIMIENTO ID"',
            {"id_estado": id_estado}
        )
    else:
        cursor.execute('SELECT * FROM FIDE_REABASTECIMIENTO_INVENTARIO_V ORDER BY "REABASTECIMIENTO ID"')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos
