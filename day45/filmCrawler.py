from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-century/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page,"html.parser")

titles = soup.find_all("img", class_="jsx-952983560")
with open(f"./day45/billboard.txt",mode="w") as writer:
    for title in titles:
        writer.write(title.get("alt")+"\n")

    