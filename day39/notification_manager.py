from email.mime.text import MIMEText
import os
import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.    

    def __init__(self) -> None:
        self.MY_EMAIL= os.environ.get("MY_MAIL")
        self.MAIL_PWD= os.environ.get("MAIL_PWD")

    def send_email(self,to,subject, body):
        with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=self.MY_EMAIL,password=self.MAIL_PWD)
            #connection.sendmail(from_addr=MY_EMAIL,to_addrs=to,msg=f"Subject:{subject}\n\n{body}")
            message = MIMEText(body)
            message["To"]=self.MY_EMAIL
            message["From"]=self.MY_EMAIL
            message["Subject"]=subject
            connection.send_message(message)
