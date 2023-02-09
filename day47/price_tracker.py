import smtplib
from email.mime.text import MIMEText
import os
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

url="https://www.amazon.fr/dp/B082P2BT1G/?coliid=I2ZDIRBF0TJB3O&colid=2E95L16D2QWDW&psc=1&ref_=lv_ov_lig_dp_it_im"
target = 30
MY_EMAIL= os.environ.get("MY_MAIL")
MAIL_PWD= os.environ.get("MAIL_PWD")

header={
    "Accept-Language":"fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3", "userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
}

def send_email(to,subject, body):
        with smtplib.SMTP(host="smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MAIL_PWD)
            message = MIMEText(body)
            message["To"]=to
            message["From"]=MY_EMAIL
            message["Subject"]=subject
            connection.send_message(message)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    browser_context = browser.new_context(extra_http_headers=header)
    page = browser_context.new_page()
    page.goto(url)
    page.wait_for_timeout(1000)
    page.click("id=sp-cc-accept",delay=10)
    page.goto(url)
    page.wait_for_timeout(1000)

    bs = BeautifulSoup(page.content(), "lxml")
    price_tag = bs.find(class_="a-offscreen")
    price=float((price_tag.get_text().removesuffix("€")).replace(",","."))
    print(price)
    browser.close()
    
    if price<=target:
        send_email(MY_EMAIL,"Amazon price tracker",f"Prix en baisse, go: {url}")


