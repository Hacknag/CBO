import oracledb
from db import get_connection


def insertar_correo_empleado(ID_EMPLEADO, CORREO, TIPO, ID_ESTADO):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_CORREOS_EMPLEADOS_INSERT_SP", [
            ID_EMPLEADO, CORREO, TIPO, ID_ESTADO
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def actualizar_correo_empleado(id_empleado, correo, tipo, id_estado):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_CORREOS_EMPLEADOS_UPDATE_SP", [
            id_empleado, correo, tipo, id_estado
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def eliminar_correo_empleado_logico(ID_EMPLEADO, CORREO):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_CORREOS_EMPLEADOS_DELETE_SP", [
            ID_EMPLEADO, CORREO
        ])
        conexion.commit()
    except Exception as e:

        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def obtener_correos_empleados(id_estado=None):
    conn = get_connection()
    cursor = conn.cursor()
    if id_estado:
        cursor.execute(
            'SELECT * FROM FIDE_CORREOS_EMPLEADOS_V WHERE "ID ESTADO" = :id_estado ORDER BY "ID EMPLEADO"',
            {"id_estado": id_estado}
        )
    else:
        cursor.execute('SELECT * FROM FIDE_CORREOS_EMPLEADOS_V ORDER BY "ID EMPLEADO"')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos
