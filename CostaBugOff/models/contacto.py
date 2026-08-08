import smtplib
from email.message import EmailMessage

MY_EMAIL = "costabugoffcostarica@gmail.com"
MY_PASSWORD = "dqldvflyvjmpysxd"


def enviar_correo_contacto(nombre, correo, mensaje):
    msg = EmailMessage()
    msg["Subject"] = f"Nuevo mensaje de contacto de {nombre}"
    msg["From"] = MY_EMAIL
    msg["To"] = MY_EMAIL
    msg["Reply-To"] = correo

    plain_text = f"""
Nuevo mensaje desde el formulario de Contacto de CostaBugOff.

Nombre: {nombre}
Correo: {correo}

Mensaje:
{mensaje}
"""
    msg.set_content(plain_text)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.send_message(msg)
