import pandas
import datetime as dt
import smtplib
from random import randint

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

my_email="fredgca@gmail.com"
password="hcskgsnrhmzioiff"

def send_email(to,body):
    with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=to,msg=f"Subject:Happy Birthday\n\n{body}")

def prepare_mail(name) -> str:
    suffix = randint(1,3)
    with open(f"./day32/letter_templates/letter_{suffix}.txt",mode="r") as mail:
        body = mail.read()
    content = body.replace("[NAME]",name)
    return content

df = pandas.read_csv("./day32/birthdays.csv")
date = dt.date.today()
birthdays = df[(df["month"]==date.month) & (df["day"]==date.day)]
for index, row in birthdays.iterrows():
    name = row["name"]
    email = row["email"]
    body = prepare_mail(name)
    send_email(email,body)