import oracledb
from db import get_connection
from models.olvide_password import generar_password
import smtplib
from email.message import EmailMessage
# ---------------- Usuarios (vista con id_usuario, rol, nombre y estado) ---------------- #
# ---------------- Usuarios (vista con id_usuario, rol, nombre y estado) ---------------- #
MY_EMAIL = "costabugoffcostarica@gmail.com"
MY_PASSWORD = "dqldvflyvjmpysxd"

def send_email(destination_email, password):
    msg = EmailMessage()
    msg["Subject"] = "Bienvenido a CostaBugOff"
    msg["From"] = MY_EMAIL
    msg["To"] = destination_email
# Plain text version (fallback)
    plain_text = f"""
Hola,

Tu usuario ha sido registrado y tu nueva contraseña es: {password}

Si no solicitaste este cambio, por favor contáctanos de inmediato.

Atentamente,
El equipo de CostaBugOff
    """
    msg.set_content(plain_text)

    # HTML formatted version
    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Restablecer contraseña - CostaBugOff</title>
    </head>
    <body style="margin: 0; padding: 0; background-color: #F5F2EC; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; -webkit-font-smoothing: antialiased;">
      <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #F5F2EC; padding: 30px 15px;">
        <tr>
          <td align="center">
            <!-- Email Container Card -->
            <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 540px; background-color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.08); border: 1px solid #E2DACB;">
              
              <!-- Header with Logo Colors -->
              <tr>
                <td align="center" style="background-color: #122131; padding: 35px 20px 25px 20px; border-bottom: 5px solid #A82226;">
                  <h1 style="color: #F4E8C1; margin: 0; font-size: 28px; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase;">
                    CostaBugOff
                  </h1>
                  <p style="color: #C5D1D9; margin: 6px 0 0 0; font-size: 12px; text-transform: uppercase; letter-spacing: 3px; font-weight: 600;">
                    Pest Control
                  </p>
                </td>
              </tr>

              <!-- Main Content Body -->
              <tr>
                <td style="padding: 35px 30px; color: #2C3036; line-height: 1.6;">
                  <h2 style="color: #122131; margin-top: 0; font-size: 20px; font-weight: 700;">
                    Bienvenido a el equipo de CostaBugOff
                  </h2>
                  <p style="margin-bottom: 22px; color: #4A515A; font-size: 15px;">
                    Hola, un nuevo usuario ha sido registrado con este correo. Se ha generado una nueva contraseña para ti:
                  </p>
                  
                  <!-- Password Box -->
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="margin: 25px 0;">
                    <tr>
                      <td align="center" style="background-color: #FDFBF7; border: 2px dashed #A82226; border-radius: 8px; padding: 20px 15px;">
                        <span style="display: block; font-size: 11px; color: #7A828C; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 8px; font-weight: 600;">
                          Tu nueva contraseña es:
                        </span>
                        <span style="font-family: 'Courier New', Consolas, monospace; font-size: 28px; font-weight: bold; color: #A82226; letter-spacing: 3px;">
                          {password}
                        </span>
                      </td>
                    </tr>
                  </table>

                  <p style="margin-bottom: 25px; color: #4A515A; font-size: 14px;">
                    Te sugerimos copiar esta contraseña e iniciar sesión en la plataforma.
                  </p>

                  <!-- Notice Box -->
                  <div style="background-color: #FFF8EA; border-left: 4px solid #E3A008; padding: 12px 16px; border-radius: 4px; font-size: 13px; color: #73510D; line-height: 1.4;">
                    <strong>Nota:</strong> Si no solicitaste esto, por favor ignora este mensaje o ponte en contacto con nuestro equipo de soporte.
                  </div>
                </td>
              </tr>

              <!-- Footer -->
              <tr>
                <td align="center" style="background-color: #F5F2EC; padding: 20px; font-size: 12px; color: #7A828C; border-top: 1px solid #E2DACB;">
                  <p style="margin: 0 0 6px 0; font-weight: 600; color: #122131;">
                    CostaBugOff Pest Control
                  </p>
                  <p style="margin: 0;">
                    Este es un mensaje automático. Por favor no respondas a este correo.
                  </p>
                </td>
              </tr>

            </table>
          </td>
        </tr>
      </table>
    </body>
    </html>
    """
    
    # Attach HTML version
    msg.add_alternative(html_content, subtype="html")


    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        try:
            connection.send_message(msg)
        except Exception as e:
            print(f"Failed to send email to {destination_email}: {e}")


def obtener_usuarios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM FIDE_USUARIOS_V ORDER BY "USUARIO ID"')
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos

#INSERT
#INSERT
def existe_usuario(usuario):
    """Consulta si el usuario/correo ya existe en la base de datos."""
    conexion = None
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        sql = "SELECT COUNT(*) FROM FIDE_USUARIOS_TB WHERE LOWER(USUARIO) = LOWER(:1)"
        cursor.execute(sql, (usuario.strip(),))
        cantidad = cursor.fetchone()[0]
        cursor.close()
        return cantidad > 0
    except Exception as e:
        print(f"Error al verificar usuario: {e}")
        return False
    finally:
        if conexion:
            conexion.close()


def insertar_usuario(USUARIO, ID_ROL, ID_ESTADO):
    # 1. Validar que no exista
    if existe_usuario(USUARIO):
        raise ValueError(f"El usuario o correo '{USUARIO}' ya está registrado.")
    # 2. Contraseña predeterminada en formato String (VARCHAR2)
    CONTRASENA = generar_password()
    conexion = get_connection()
    send_email(USUARIO, CONTRASENA)
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_USUARIOS_INSERT_SP", [
            USUARIO, CONTRASENA, ID_ROL, ID_ESTADO
        ])
        conexion.commit()        
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()


#ELIMINAR
def eliminar_usuario_logico(id_usuario):
    conexion = get_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc("FIDE_PROYECTO_FINAL_PKG.FIDE_USUARIOS_DELETE_SP", [
            id_usuario
        ])
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        raise e
    finally:
        cursor.close()
        conexion.close()

