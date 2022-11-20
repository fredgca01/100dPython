import requests
import json
import os


API_KEY=os.environ.get("OWM_API_KEY")
URL_LOC="http://api.openweathermap.org/geo/1.0/direct"
URL_WEATHER = "https://api.openweathermap.org/data/2.5/forecast"

PARAMS_LOC = {
    "q":"Paris,FR",
    "limit":"1",
    "appid":API_KEY
}

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

# https://business.facebook.com/settings/system-users/100087678714205?business_id=5431964390266258
# https://developers.facebook.com/docs/whatsapp/cloud-api/get-started

phone_number_id = os.environ.get("WHTSP_PHONE_ID") # Phone number ID provided
access_token=os.environ.get("WHTSP_ACCESS_TOKEN") 
recipient_phone_number = "33662251612" # Your own phone number
recipient_phone_number2 = "33664626482"
url = f"https://graph.facebook.com/v15.0/{phone_number_id}/messages"
headers = {
    "Authorization": f"Bearer {access_token}",
    'Content-Type': 'application/json'
}

# https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#text-messages
parameters_tmpl = {
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": recipient_phone_number,
    "type": "template",
    "template": {"name": "hello_world", "language": {"code": "en_US"}}
}

# il faut que le receveur reponde à un msg avant de pouvoir recevoir autre chose que le template hello world ...
parameters_txt = {
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": recipient_phone_number2,
    "type": "text",
    "text": {
        "preview_url": 'true',
        "body": weather_alert
    }
}

response = requests.post(
    url,
    headers=headers,
    data=json.dumps(parameters_txt)
)

response.raise_for_status()
