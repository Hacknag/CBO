import oracledb
from db import get_connection
#tener cuidado con esto que con quitar una linea se pudre toda la pagina xddddddd
def insertar_metodos_pago(ID_METODO_PAGO, NOMBRE, ID_ESTADO):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_METODOS_PAGO_INSERT_SP", [
            ID_METODO_PAGO, NOMBRE, ID_ESTADO
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def actualizar_metodos_pago(ID_METODO_PAGO, NOMBRE, ID_ESTADO):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_METODOS_PAGO_UPDATE_SP", [
            ID_METODO_PAGO, NOMBRE, ID_ESTADO
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def eliminar_metodos_pago_logica(ID_METODO_PAGO):

    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_METODOS_PAGO_DELETE_SP", [
            ID_METODO_PAGO
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def obtener_metodos_pago_main():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM FIDE_METODOS_PAGO_V')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos


