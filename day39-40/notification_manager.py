from email.mime.text import MIMEText
import os
import smtplib

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self) -> None:
        self.my_email = os.environ.get("MY_MAIL")
        self.mail_pwd = os.environ.get("MAIL_PWD")

    def send_email(self, to: str, subject: str, body: str) -> None:
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.mail_pwd)
            message = MIMEText(body)
            message["To"] = to
            message["From"] = self.my_email
            message["Subject"] = subject
            connection.send_message(message)
