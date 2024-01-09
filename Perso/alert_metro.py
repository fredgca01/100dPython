import requests
import os
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

MY_EMAIL= os.environ.get("MY_MAIL")
MAIL_PWD= os.environ.get("MAIL_PWD")
EMAILS= os.environ.get("EMAILS")
API_KEY=os.environ.get("RATP_API_KEY")
BUS_PARMENTIER="23636" #https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/acces
URL="https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring?MonitoringRef=STIF:StopPoint:Q:"+BUS_PARMENTIER+":"
PARAMS = {
    "Accept":"application/json",
    "apikey":API_KEY
}
response = requests.get(url=URL, headers=PARAMS)
response.raise_for_status()
metro_alert="Tes prochains bus sont à:\n"
data= response.json()["Siri"]["ServiceDelivery"]['StopMonitoringDelivery'][0]['MonitoredStopVisit']
for departure in data:
    gmt_date = datetime.strptime(departure.get("MonitoredVehicleJourney").get("MonitoredCall").get("ExpectedDepartureTime"), "%Y-%m-%dT%H:%M:%S.%fZ")
    # Décalage horaire de Paris par rapport à GMT (en heures)
    paris_offset = 1

    # Si l'heure d'été est en vigueur, ajoutez une heure supplémentaire
    # Note : cette méthode est simplifiée et peut ne pas être précise pour toutes les dates et tous les fuseaux horaires
    if (gmt_date.month > 3 and gmt_date.month < 11):
        paris_offset += 1
    local_date = gmt_date + timedelta(hours=paris_offset)
    metro_alert+=(datetime.strftime(local_date,"%H:%M"))
    metro_alert+="\n"
    print(metro_alert)

def send_email(to,subject, body):
    with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MAIL_PWD)
        message = MIMEText(body)
        message["To"]=to
        message["From"]=MY_EMAIL
        message["Subject"]=subject
        connection.send_message(message)

#send_email(EMAILS,"Bus",metro_alert)