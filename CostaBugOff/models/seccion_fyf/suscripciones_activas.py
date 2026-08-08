import oracledb
from db import get_connection


def obtener_suscripciones_activas():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT ID_CLIENTE_SUSCRIPCION, ID_CLIENTE, NOMBRE_CLIENTE, PLAN,
                   FECHA_INICIO, FECHA_PROXIMA_RENOVACION, METODO_PAGO, ESTADO
            FROM FIDE_SUSCRIPCIONES_ACTIVAS_V
        ''')
        columnas = [c[0] for c in cursor.description]
        filas = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return [dict(zip(columnas, fila)) for fila in filas]
