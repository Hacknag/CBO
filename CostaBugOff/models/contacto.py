import smtplib
from email.message import EmailMessage
from datetime import datetime

MY_EMAIL = "costabugoffcostarica@gmail.com"
MY_PASSWORD = "dqldvflyvjmpysxd"


def enviar_correo_contacto(nombre, correo, asunto, mensaje):
    msg = EmailMessage()
    msg["Subject"] = f"📩 Nuevo mensaje de contacto: {asunto}"
    msg["From"] = f"CostaBugOff <{MY_EMAIL}>"
    msg["To"] = MY_EMAIL
    msg["Reply-To"] = correo

    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    plain_text = f"""
Tenemos un nuevo correo de: {nombre} ({correo})
El asunto es: {asunto}
Fecha: {fecha}

Mensaje:
{mensaje}
"""
    msg.set_content(plain_text)
    html = f"""\
    <!doctype html>
    <html>
      <body style="margin:0; padding:0; background:#F5F4EF; font-family: 'IBM Plex Sans', Arial, sans-serif; color:#1C2420;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#F5F4EF; padding:24px 0;">
          <tr>
            <td align="center">
              <table role="presentation" width="560" cellpadding="0" cellspacing="0" style="background:#FFFFFF; border:1px solid #DAD8CE; border-radius:6px; overflow:hidden;">
                <tr>
                  <td style="background:#2E4F37; padding:20px 28px;">
                    <span style="color:#F1EEE6; font-size:18px; font-weight:600; letter-spacing:.3px;">CostaBugOff</span>
                    <div style="color:#C6D6C9; font-size:12px; margin-top:2px;">Nuevo mensaje desde el formulario de Contacto</div>
                  </td>
                </tr>
                <tr>
                  <td style="padding:28px;">
                    <p style="margin:0 0 18px; font-size:15px;">
                      Tenemos un nuevo correo de <strong>{nombre}</strong> ({correo}) y el asunto es <strong>&ldquo;{asunto}&rdquo;</strong>.
                    </p>
    
                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse; margin-bottom:20px;">
                      <tr>
                        <td style="padding:6px 0; width:110px; color:#48544D; font-size:13px; vertical-align:top;">Nombre</td>
                        <td style="padding:6px 0; font-size:14px; font-weight:500;">{nombre}</td>
                      </tr>
                      <tr>
                        <td style="padding:6px 0; color:#48544D; font-size:13px; vertical-align:top;">Correo</td>
                        <td style="padding:6px 0; font-size:14px;">
                          <a href="mailto:{correo}" style="color:#3F6B4A; text-decoration:none; font-weight:500;">{correo}</a>
                        </td>
                      </tr>
                      <tr>
                        <td style="padding:6px 0; color:#48544D; font-size:13px; vertical-align:top;">Asunto</td>
                        <td style="padding:6px 0; font-size:14px; font-weight:500;">{asunto}</td>
                      </tr>
                      <tr>
                        <td style="padding:6px 0; color:#48544D; font-size:13px; vertical-align:top;">Fecha</td>
                        <td style="padding:6px 0; font-size:14px;">{fecha}</td>
                      </tr>
                    </table>
    
                    <div style="background:#F1EEE6; border-left:3px solid #3F6B4A; border-radius:3px; padding:16px 18px;">
                      <div style="font-size:12px; color:#48544D; text-transform:uppercase; letter-spacing:.4px; margin-bottom:6px;">Mensaje</div>
                      <div style="font-size:14px; line-height:1.6; white-space:pre-line;">{mensaje}</div>
                    </div>
    
                    <div style="margin-top:26px;">
                      <a href="mailto:{correo}?subject=Re: {asunto}"
                         style="display:inline-block; background:#3F6B4A; color:#FFFFFF; text-decoration:none; font-size:14px; font-weight:600; padding:10px 20px; border-radius:3px;">
                        Responder a {nombre}
                      </a>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td style="padding:14px 28px; background:#F1EEE6; border-top:1px solid #DAD8CE;">
                    <span style="font-size:11px; color:#48544D;">Este mensaje fue enviado automáticamente desde el formulario de Contacto de CostaBugOff.</span>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
        </table>
      </body>
    </html>
    """
    msg.add_alternative(html, subtype="html")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.send_message(msg)
