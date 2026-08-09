import oracledb
from db import get_connection
#tener cuidado con esto que con quitar una linea se pudre toda la pagina xddddddd
def insertar_empleado(nombre, apellido_paterno, apellido_materno, id_puesto, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_EMPLEADOS_INSERT_SP", [
            nombre, apellido_paterno, apellido_materno, id_puesto, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def actualizar_empleados(id_empleado, nombre, apellido_paterno, apellido_materno, id_puesto, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_EMPLEADOS_UPDATE_SP", [
            id_empleado, nombre, apellido_paterno, apellido_materno, id_puesto, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

def eliminar_empleados_logica(id_empleado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_EMPLEADOS_DELETE_SP", [
            id_empleado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


# def obtener_empleados(id_estado=None):
#     conn = get_connection()
#     cursor = conn.cursor()
#     if id_estado:
#         cursor.execute(
#             'SELECT * FROM FIDE_EMPLEADOS_V WHERE "ID ESTADO" = :id_estado ORDER BY "EMPLEADO ID"',
#             {"id_estado": id_estado}
#         )
#     else:
#         cursor.execute('SELECT * FROM FIDE_EMPLEADOS_V ORDER BY "EMPLEADO ID"')
#     datos = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return datos

def obtener_empleados():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM FIDE_EMPLEADOS_ACTIVOS_V')
        datos = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return datos

def obtener_puestos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT ID_PUESTO, NOMBRE FROM FIDE_PUESTOS_TB WHERE ID_ESTADO = 1 ORDER BY NOMBRE')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos
