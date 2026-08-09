import oracledb
from db import get_connection
#tener cuidado con esto que con quitar una linea se pudre toda la pagina xddddddd
def insertar_correos_clientes(ID_CLIENTE, CORREO, TIPO, ID_ESTADO):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_CORREOS_INSERT_SP", [
            ID_CLIENTE, CORREO, TIPO, ID_ESTADO
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def actualizar_correos_clientes(ID_CLIENTE, CORREO, TIPO, ID_ESTADO):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_CORREOS_UPDATE_SP", [
            ID_CLIENTE, CORREO, TIPO, ID_ESTADO
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def eliminar_correo_cliente_logica(ID_CLIENTE, CORREO):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_CORREOS_DELETE_SP", [
            ID_CLIENTE, CORREO
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def obtener_correos_clientes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM FIDE_CORREOS_CLIENTES_ACTIVOS_V')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos


