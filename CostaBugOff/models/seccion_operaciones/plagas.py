import oracledb
from db import get_connection
#tener cuidado con esto que con quitar una linea se pudre toda la pagina xddddddd
def insertar_plaga(id_plaga, tipo, nombre, descripcion, unidades_necesarias, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.SP_FIDE_PLAGAS_INSERT", [
            id_plaga, tipo, nombre, descripcion, unidades_necesarias, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def actualizar_plaga(id_plaga, tipo, nombre, descripcion, unidades_necesarias, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.SP_FIDE_PLAGAS_UPDATE", [
            id_plaga, tipo, nombre, descripcion, unidades_necesarias, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def eliminar_plaga_logica(id_plaga):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.SP_FIDE_PLAGAS_DELETE", [
            id_plaga
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def obtener_plagas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM FIDE_PLAGAS_V ORDER BY "PLAGA ID"')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos