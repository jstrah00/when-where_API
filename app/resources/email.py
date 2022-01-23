from app.resources.credentials import EMAIL_ADDRESS, EMAIL_PORT, EMAIL_PASSWORD, APP_NAME, APP_URL, SUPPORT_EMAIL
import smtplib, ssl
from email.message import EmailMessage
from app.resources.templates import VERIFICATION_EMAIL_TEMPLATE, VERIFICATION_EMAIL_SUBJECT, VERIFICATION_EMAIL_TEMPLATE_EN, VERIFICATION_EMAIL_SUBJECT_EN, CHANGE_PASSWORD_TEMPLATE, CHANGE_PASSWORD_TEMPLATE_EN, CHANGE_PASSWORD_SUBJECT, CHANGE_PASSWORD_SUBJECT_EN, CHANGE_PASSWORD_ALERT_TEMPLATE, CHANGE_PASSWORD_ALERT_TEMPLATE_EN, CHANGE_PASSWORD_ALERT_SUBJECT, CHANGE_PASSWORD_ALERT_SUBJECT_EN

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

def send_change_password_email(send_to, code , lang="es"):
    change_pass_link = f"{APP_URL}/password_reset?code={code}"
    if lang=="en":
        message = CHANGE_PASSWORD_TEMPLATE_EN.format(VERIF_LINK=change_pass_link)
        subject = CHANGE_PASSWORD_SUBJECT_EN.format(APP_NAME=APP_NAME)
    else:
        message = CHANGE_PASSWORD_TEMPLATE.format(VERIF_LINK=change_pass_link)
        subject = CHANGE_PASSWORD_SUBJECT.format(APP_NAME=APP_NAME)
    send_email(send_to, subject, message)

def send_password_change_alert(send_to, lang="es"):
    if lang=="en":
        message = CHANGE_PASSWORD_ALERT_TEMPLATE_EN.format(APP_NAME=APP_NAME, SUPPORT_EMAIL=SUPPORT_EMAIL)
        subject = CHANGE_PASSWORD_ALERT_SUBJECT_EN.format(APP_NAME=APP_NAME)
    else:
        message = CHANGE_PASSWORD_ALERT_TEMPLATE.format(APP_NAME=APP_NAME, SUPPORT_EMAIL=SUPPORT_EMAIL)
        subject = CHANGE_PASSWORD_ALERT_SUBJECT.format(APP_NAME=APP_NAME)  
    send_email(send_to, subject, message)
