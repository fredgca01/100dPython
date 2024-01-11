import requests
import os
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from enum import Enum

MY_EMAIL= os.environ.get("MY_MAIL")
MAIL_PWD= os.environ.get("MAIL_PWD")
EMAILS= os.environ.get("EMAILS")
API_KEY=os.environ.get("RATP_API_KEY")
BUS_PARMENTIER="23636" #https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/acces
URL_NEXT="https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring?MonitoringRef=STIF:StopPoint:Q:"+BUS_PARMENTIER+":"
URL_MSG_PREF="https://prim.iledefrance-mobilites.fr/marketplace/general-message?LineRef=STIF:Line::"
URL_MSG_SUFF=":&InfoChannelRef=Perturbation"
PARAMS = {
    "Accept":"application/json",
    "apikey":API_KEY
}

#https://prim.iledefrance-mobilites.fr/fr/jeux-de-donnees/referentiel-des-lignes
class Lines(Enum):
    M_2 = "C01372"
    RER_A = "C01742"
    BUS_56 = "C01093"

def send_email(to,subject, body):
    with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MAIL_PWD)
        message = MIMEText(body)
        message["To"]=to
        message["From"]=MY_EMAIL
        message["Subject"]=subject
        connection.send_message(message)

metro_alert=""
#looking for incidents
for line in Lines:
    current_line = line.value
    response = requests.get(url=URL_MSG_PREF+current_line+URL_MSG_SUFF, headers=PARAMS)
    response.raise_for_status()
    data= response.json()["Siri"]["ServiceDelivery"]["GeneralMessageDelivery"][0]["InfoMessage"]
    for message in data: 
        gmt_date_incident = datetime.strptime(message.get("RecordedAtTime"), "%Y-%m-%dT%H:%M:%S.%fZ")
        gmt_date_validity = datetime.strptime(message.get("ValidUntilTime"), "%Y-%m-%dT%H:%M:%S.%fZ")
        
        if(gmt_date_incident.day==datetime.now().day and gmt_date_validity.day<=datetime.now().day+1 ):
            content = message.get("Content").get("Message")[0].get("MessageText").get("value")
            metro_alert+=line.name+": "+content

#looking for next bus
#response = requests.get(url=URL_NEXT, headers=PARAMS)
#response.raise_for_status()
#metro_alert="Tes prochains bus sont à:\n"
#data= response.json()["Siri"]["ServiceDelivery"]['StopMonitoringDelivery'][0]['MonitoredStopVisit']
#for departure in data:
#    gmt_date = datetime.strptime(departure.get("MonitoredVehicleJourney").get("MonitoredCall").get("ExpectedDepartureTime"), "%Y-%m-%dT%H:%M:%S.%fZ")
#    metro_alert+=(datetime.strftime(gmt_date,"%H:%M"))
#    metro_alert+="\n"
#    print(metro_alert)

if(len(metro_alert)>0):
    send_email(EMAILS,"Transports du matin",metro_alert)