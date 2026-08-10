import oracledb
from db import get_connection


def insertar_correo_proveedor(id_proveedor, correo, tipo, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_CORREOS_PROVEEDORES_INSERT_SP", [
            id_proveedor, correo, tipo, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def actualizar_correo_proveedor(ID_PROVEEDOR, CORREO, CORREO_NUEVO, TIPO, ID_ESTADO):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_CORREOS_PROVEEDORES_UPDATE_SP", [
            ID_PROVEEDOR, CORREO, CORREO_NUEVO, TIPO, ID_ESTADO
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def eliminar_correo_proveedor_logico(id_proveedor, correo):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_CORREOS_PROVEEDORES_DELETE_SP", [
            id_proveedor, correo
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def obtener_correos_proveedores(id_estado=None):
    conn = get_connection()
    cursor = conn.cursor()
    if id_estado:
        cursor.execute(
            'SELECT * FROM FIDE_CORREOS_PROVEEDORES_V WHERE "ID ESTADO" = :id_estado ORDER BY "ID PROVEEDOR"',
            {"id_estado": id_estado}
        )
    else:
        cursor.execute('SELECT * FROM FIDE_CORREOS_PROVEEDORES_V ORDER BY "ID PROVEEDOR"')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos
