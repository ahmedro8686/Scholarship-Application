import smtplib
from email.mime.text import MIMEText
from config import Config

def send_email(to_email, subject, body):
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["From"] = Config.ADMIN_EMAIL
    msg["To"] = to_email

    with smtplib.SMTP("localhost") as server:
        server.send_message(msg)
