# from tkinter import *
# import requests

# # response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # response.raise_for_status()


# # longitude = response.json()["iss_position"]["longitude"]
# # latitude = response.json()["iss_position"]["latitude"]
# # iss_pos = (latitude,longitude)

# # print(iss_pos)

# URL = "http://api.kanye.rest"

# def get_quote():
#     #Write your code here.
#     response = requests.get(url=URL)
#     response.raise_for_status()
#     quote = response.json()["quote"]
#     canvas.itemconfig(quote_text,text=quote)



# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="./day33/background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="./day33/kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)

# window.mainloop()


# date = (datetime.datetime.fromisoformat(sunrise))
# print(date.strftime("%b %d %Y %H:%M:%S"))


from time import sleep
import requests
import datetime
import pytz
import smtplib


MY_LAT=48.856613
MY_LON=2.352222
MY_EMAIL="fredgca@gmail.com"
PWD=""

def is_night() -> bool:
    param = {"lat":MY_LAT,"lon":MY_LON, "formatted":0}
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=param)
    response.raise_for_status()
    sunset = response.json()["results"]["sunset"]
    night = datetime.datetime.fromisoformat(sunset)
    now = pytz.utc.localize(datetime.datetime.utcnow())
    return now > night

def check_iss_pos():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_lat = response.json()["iss_position"]["latitude"]
    iss_lon = response.json()["iss_position"]["longitude"]
    return {"lon" : float(iss_lon),"lat" : float(iss_lat)}

def check_look_up(iss_pos):
    if is_night() and abs(iss_pos["lon"])-abs(MY_LON)<5 and abs(iss_pos["lat"])-abs(MY_LAT)<5 :
        return True
    else :
        return False

def send_email(to,body):
    with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PWD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=to,msg=f"Subject:Look Up\n\n{body}")

while True : 
    iss_pos = check_iss_pos()
    if check_look_up(iss_pos):
        print(iss_pos)
        print("Look up!!")
        send_email(MY_EMAIL,f"Wake up ! Iss is above you {iss_pos}")
    else:
        print(iss_pos)
        
    sleep(600)