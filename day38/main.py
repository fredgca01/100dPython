import requests
from datetime import datetime
import time
import os

NUTRI_KEY=os.getenv("NUTRI_KEY")
NUTRI_ID=os.getenv("NUTRI_ID")
NUTRI_URL="https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_URL="https://api.sheety.co/1658c67683f7eb7e1940e0a85f25f886/copieDeMyWorkouts/workouts"
SHEETY_BEAR=os.getenv("SHEETY_BEAR")

headers={
    "x-app-id":NUTRI_ID,
    "x-app-key":NUTRI_KEY,
    "x-remote-user-id":"0"
}

query = input("What exercize did you do today ? ")

exercize_param = {
 "query": query
}

response = requests.post(url=NUTRI_URL,json=exercize_param,headers=headers)

headers = {"Authorization": SHEETY_BEAR}
timestamp = time.time()
now = datetime.fromtimestamp(timestamp)
for data in response.json()["exercises"] :
    data = {
        "workout": {
            "date": now.strftime("%x"),
            "time": now.strftime("%X"),
            "exercise": data["name"],
            "duration": data["duration_min"],
            "calories": data["nf_calories"]
        }
    }
    response = requests.post(url=SHEETY_URL,json=data, headers=headers)
    print(response.text)

