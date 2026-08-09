import oracledb
from db import get_connection
#tener cuidado con esto que con quitar una linea se pudre toda la pagina xddddddd
def insertar_telefonos_clientes(ID_CLIENTE, TELEFONO, TIPO, ID_ESTADO):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_TELEFONOS_INSERT_SP", [
            ID_CLIENTE, TELEFONO, TIPO, ID_ESTADO
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def actualizar_telefonos_clientes(ID_CLIENTE, TELEFONO, TIPO, ID_ESTADO):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_TELEFONOS_UPDATE_SP", [
            ID_CLIENTE, TELEFONO, TIPO, ID_ESTADO
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def eliminar_telefono_cliente_logico(ID_CLIENTE, TELEFONO):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_TELEFONOS_DELETE_SP", [
            ID_CLIENTE, TELEFONO
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def obtener_telefonos_clientes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM FIDE_TELEFONOS_CLIENTES_ACTIVOS_V')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos