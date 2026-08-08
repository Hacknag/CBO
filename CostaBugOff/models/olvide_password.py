import smtplib
import random
import oracledb
from db import get_connection

MY_EMAIL = "costabugoffcostarica@gmail.com"
MY_PASSWORD = "dqldvflyvjmpysxd"
values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
          'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
          '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+']

def generar_password():    
    password = ""
    for value in range(10):
        random_letter = random.choice(values)
        password += random_letter    
    return password

def actualizar_usuario(ID_USUARIO, NUEVA_CONTRASENA):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_USUARIOS_UPDATE_PASSWORD_SP", [
            ID_USUARIO, NUEVA_CONTRASENA
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


def send_email(destination_email, password):    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        try:
            connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=destination_email,
                            msg=f"Subject:Tu contraseña ha sido restablecida\n\nHola, tu contraseña ha sido restablecida. Tu nueva contraseña es: {password}")
        except Exception as e:
            print(f"Failed to send email to {destination_email}: {e}")


def get_usuario_id(user_email):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        user_id = cursor.callfunc(
                    "FIDE_PROYECTO_FINAL_PKG.FIDE_BUSCARID_USUARIOS_X_EMAIL_FN",
                    int,
                    [user_email],
                )
        if not user_id:
            raise ValueError(f"No user found for email: {user_email}")
        else:
            password = generar_password()        
            send_email(user_email, password)  # Llamada a la función para enviar el correo electrónico con la nueva contraseña
            actualizar_usuario(user_id, password)  # Llamada a la función para actualizar la contraseña del usuario
        
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()
