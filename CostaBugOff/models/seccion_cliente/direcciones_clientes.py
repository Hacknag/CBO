import oracledb
from db import get_connection

def insertar_direcciones_clientes(ID_CLIENTE, ID_PROVINCIA, ID_CANTON, ID_DISTRITO, ID_ESTADO):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_DIRECCIONES_INSERT_SP", [
            ID_CLIENTE, ID_PROVINCIA, ID_CANTON, ID_DISTRITO, ID_ESTADO
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def actualizar_direcciones_clientes(ID_CLIENTE, ID_PROVINCIA, ID_PROVINCIA_NUEVA, ID_CANTON, ID_CANTON_NUEVO, ID_DISTRITO, ID_DISTRITO_NUEVO, ID_ESTADO):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_DIRECCIONES_UPDATE_SP", [
            ID_CLIENTE,
            ID_PROVINCIA,
            ID_PROVINCIA_NUEVA,
            ID_CANTON,
            ID_CANTON_NUEVO,
            ID_DISTRITO,
            ID_DISTRITO_NUEVO,
            ID_ESTADO
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def eliminar_direccion_clientes_logica(ID_CLIENTE, ID_PROVINCIA, ID_CANTON, ID_DISTRITO):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_DIRECCIONES_DELETE_SP", [
            ID_CLIENTE, ID_PROVINCIA, ID_CANTON, ID_DISTRITO
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def obtener_direcciones_clientes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM FIDE_DIRECCIONES_CLIENTES_ACTIVOS_V')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos