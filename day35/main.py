from email.mime.text import MIMEText
import requests
import os
import smtplib
from datetime import datetime

API_KEY=os.environ.get("OWM_API_KEY")
URL_LOC="http://api.openweathermap.org/geo/1.0/direct"
URL_WEATHER = "https://api.openweathermap.org/data/2.5/forecast"
MY_EMAIL= os.environ.get("MY_MAIL")
MAIL_PWD= os.environ.get("MAIL_PWD")
EMAILS=os.environ.get("EMAILS")

PARAMS_LOC = {
    "q":"Paris,FR",
    "limit":"1",
    "appid":API_KEY
}

if datetime.now().weekday()==5 or datetime.now().weekday()==6:
    print("Weekend")
else:

    response = requests.get(url=URL_LOC, params=PARAMS_LOC)
    response.raise_for_status()
    lat = response.json()[0]["lat"]
    lon = response.json()[0]["lon"]

    PARAMS_WEATHER = {
        "lat":lat,
        "lon":lon,
        "appid":API_KEY,
        "units":"metric",
        "lang":"FR",
        "cnt":3
    }

    response = requests.get(url=URL_WEATHER, params=PARAMS_WEATHER)
    response.raise_for_status()
    data = response.json()["list"]
    raining = False
    weather_alert=""
    temp_feel=0

    for weather_slot in data:
        detailled_temp = weather_slot["main"]
        temp_feel += float(detailled_temp.get("feels_like"))
        detailled_weather = weather_slot["weather"]
        weather_type = int(detailled_weather[0].get("id"))
        icon_txt = detailled_weather[0].get("icon")
        icon_url = "http://openweathermap.org/img/wn/"+icon_txt+"@2x.png"
        if weather_type>=500 and weather_type<521 and not raining:
            weather_alert = f"Penses au parapluie: {icon_url}\n "
            raining=True
        elif weather_type>=200 and weather_type<300 and not raining:
            weather_alert = f"Il vaudrait mieux ne pas sortir en fait, orage attendu ...{icon_url}\n"
            raining=True
        elif weather_type>=521 and weather_type<600 and not raining:
            weather_alert = f"Il vaudrait mieux ne pas sortir en fait, ca va tomber dru ...{icon_url}\n "
            raining=True

    temp_feel=temp_feel/3
    weather_alert+=f"La temperature sera de: {round(temp_feel,1)}°"
    print(weather_alert)

    def send_email(to,subject, body):
        with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MAIL_PWD)
            #connection.sendmail(from_addr=MY_EMAIL,to_addrs=to,msg=f"Subject:{subject}\n\n{body}")
            message = MIMEText(body)
            message["To"]=to
            message["From"]=MY_EMAIL
            message["Subject"]=subject
            connection.send_message(message)

    send_email(EMAILS,"Meteo",weather_alert)