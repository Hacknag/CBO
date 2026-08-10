import oracledb
from db import get_connection

def insertar_proveedor(nombre, id_reabastecimiento, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_PROVEEDORES_INSERT_SP", [
            nombre, id_reabastecimiento, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def actualizar_proveedor(id_proveedor, nombre, id_reabastecimiento, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_PROVEEDORES_UPDATE_SP", [
            id_proveedor, nombre, id_reabastecimiento, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def eliminar_proveedor_logico(id_proveedor):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_PROVEEDORES_DELETE_SP", [
            id_proveedor
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def obtener_proveedores(id_estado=None):
    conn = get_connection()
    cursor = conn.cursor()
    if id_estado:
        cursor.execute(
            'SELECT * FROM FIDE_PROVEEDORES_V WHERE "ID ESTADO" = :id_estado ORDER BY "PROVEEDOR ID"',
            {"id_estado": id_estado}
        )
    else:
        cursor.execute('SELECT * FROM FIDE_PROVEEDORES_V ORDER BY "PROVEEDOR ID"')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos