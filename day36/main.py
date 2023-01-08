import smtplib
import requests
from datetime import date,timedelta
import os

STOCK = "TSLA"
MY_EMAIL= os.environ.get("MY_MAIL")
MAIL_PWD= os.environ.get("MAIL_PWD")
STOCK_API_KEY=os.environ.get("STOCK_API_KEY")
NEWS_API_KEY=os.environ.get("NEWS_API_KEY")

URL_STOCK = "https://www.alphavantage.co/query"
PARAMS_STOCK = {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK,
    "apikey":STOCK_API_KEY
}

def send_email(to,subject, body):
    with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MAIL_PWD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=to,msg=f"Subject:{subject}\n\n{body}")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

date = date.today()
td = timedelta(1)
date_yesterday = date-td
if date_yesterday.weekday()==6:
    date_yesterday = date_yesterday-timedelta(2)
elif date_yesterday.weekday()==5:
    date_yesterday = date_yesterday-timedelta(1)
elif date_yesterday.weekday()==0:
    date_yesterday_2 = date_yesterday-timedelta(2)
else:
    date_yesterday_2 = date_yesterday-td
response = requests.get(url=URL_STOCK,params=PARAMS_STOCK)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

try:
    close_1 = stock_data[date_yesterday.isoformat()].get("4. close")
except KeyError:
    date_yesterday = date_yesterday-td
    date_yesterday_2 = date_yesterday-td
    close_1 = stock_data[date_yesterday.isoformat()].get("4. close")
try:    
    close_2 = stock_data[date_yesterday_2.isoformat()].get("4. close")
except KeyError:
    date_yesterday_2=date_yesterday_2-td
    close_2 = stock_data[date_yesterday_2.isoformat()].get("4. close")

close_1 = float(close_1)
close_2 = float(close_2)
print(close_1)
print(close_2)
ratio = ((close_1-close_2)/close_2)*100

if abs(ratio)>3:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    URL_NEWS = "https://newsapi.org/v2/everything"
    PARAM_NEWS = {
        "q":STOCK,
        "sortBy":"popularity",
        "apikey":NEWS_API_KEY,
        "from":date_yesterday_2,
        "language":"en",
        "searchIn":"title"
    }
    response = requests.get(url=URL_NEWS,params=PARAM_NEWS)
    response.raise_for_status()
    news_data = response.json()["articles"]
    nb=3
    for news_element in news_data:
        subject=f"{STOCK} {round(ratio,1)}%"
        title=news_element['title'].encode('utf-8')
        brief=news_element['description'].encode('utf-8')
        body=f"Headline: {title}\n Brief: {brief}"
        send_email(MY_EMAIL,subject,body)
        nb-=1
        if nb<0:
            break



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

