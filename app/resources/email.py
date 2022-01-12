from app.resources.credentials import EMAIL_PORT, EMAIL_ADDRESS, EMAIL_PASSWORD, APP_NAME, APP_URL
import smtplib, ssl
from app.resources.templates import VERIFICATION_EMAIL_TEMPLATE


smtp_server = "smtp.gmail.com"

def send_email(send_to, message):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, EMAIL_PORT, context=context) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, send_to, message)

def send_verification_email(send_to, code):
    verify_link = f"{APP_URL}/verify_email?code={code}"
    message = VERIFICATION_EMAIL_TEMPLATE.format(APP_NAME, verify_link)
    send_email(send_to, message)