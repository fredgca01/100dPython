# from bs4 import BeautifulSoup

# with open("./day45/website.html",encoding='utf-8') as file:
#     contents = file.read()

# soup = BeautifulSoup(contents,"html.parser")
# #print(soup.title.string)
# #print(soup.prettify())
# #print(soup.a)
# all_tags = soup.find_all("a")
# for tag in all_tags:
#     print(tag.get("href"))

from bs4 import BeautifulSoup
import requests

def parse(website_data) -> list:
    data = []
    for title in website_data :
        # articles.append(title.find("a").getText())
        # links.append(title.find("a")["href"])
        # votes.append(int(title.find_next(class_="score").getText().split()[0]))
        data.append([title.find("a").getText(), title.find("a")["href"], int(title.find_next(class_="score").getText().split()[0])])
    return data

articles=[]
links=[]
votes=[]

for i in range(1,3):
    response = requests.get(f"https://news.ycombinator.com/news?p={i}")
    yc_web_page = response.text
    soup = BeautifulSoup(yc_web_page,"html.parser")
    titles = soup.find_all("span",class_="titleline")
    results = parse(titles)
    for result in results:
        articles.append(result[0])
        links.append(result[1])
        votes.append(result[2])

for i in range(0,3):
    index = votes.index(max(votes))
    print(articles[index])
    print(links[index])
    print(votes[index])
    votes.remove(votes[index])
    links.remove(links[index])
    articles.remove(articles[index])


    
