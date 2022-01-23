from app.resources.credentials import EMAIL_ADDRESS, EMAIL_PORT, EMAIL_PASSWORD, APP_NAME, APP_URL
import smtplib, ssl
from email.message import EmailMessage
from app.resources.templates import VERIFICATION_EMAIL_TEMPLATE, VERIFICATION_EMAIL_SUBJECT, VERIFICATION_EMAIL_TEMPLATE_EN, VERIFICATION_EMAIL_SUBJECT_EN

smtp_server = "smtp.gmail.com"

def send_email(send_to, subject, message):
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = send_to
    context = ssl._create_unverified_context()
    with smtplib.SMTP_SSL(smtp_server, EMAIL_PORT, context=context) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

def send_verification_email(send_to, code , lang="es"):
    verify_link = f"{APP_URL}/verify_email?code={code}"
    if lang=="en":
        message = VERIFICATION_EMAIL_TEMPLATE_EN.format(APP_NAME=APP_NAME, VERIF_LINK=verify_link)
        subject = VERIFICATION_EMAIL_SUBJECT_EN.format(APP_NAME=APP_NAME)
    else:
        message = VERIFICATION_EMAIL_TEMPLATE.format(APP_NAME=APP_NAME, VERIF_LINK=verify_link)
        subject = VERIFICATION_EMAIL_SUBJECT.format(APP_NAME=APP_NAME)
    send_email(send_to, subject, message)