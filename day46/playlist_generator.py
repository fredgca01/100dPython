
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

url= "https://www.billboard.com/charts/hot-100/2013-03-13"

#travel_date = input("Which year will you to travel to ? (YYYY-MM-DD)")
# url = "https://www.billboard.com/charts/hot-100/"+travel_date

response = requests.get(url)
response.raise_for_status()
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page,"html.parser")

rows = soup.select(".o-chart-results-list__item.lrv-u-flex-grow-1.lrv-u-flex-direction-column")
# o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light  lrv-u-padding-l-1@mobile-max
# o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max
# o-chart-results-list__item // a-chart-color u-width-72 u-width-55@mobile-max u-width-55@tablet-only lrv-u-flex lrv-u-flex-shrink-0 lrv-u-align-items-center lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light u-background-color-white-064@mobile-max u-hidden@mobile-max

spotify_list=[title.get_text(separator=";",strip=True) for title in rows]
#print(spotify_list)

SPOTIFY_ID=os.environ.get("SPOTIFY_ID") 
SPOTIFY_KEY=os.environ.get("SPOTIFY_KEY") 

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-public",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_KEY,
        show_dialog=True,
        cache_path="./day46/token.txt"
    )
)

playlist = sp.user_playlist_create(sp.me()["id"],"Axel's Birth 2")

results=[]
for item in spotify_list:
    record = item.split(";")
    track=record[0]
    singer=record[1]
    item = sp.search(q=f"track:{track} artist:{singer}", limit=1, market="FR", type="track")
    if len(item["tracks"]["items"])>0:
        results.append(item["tracks"]["items"][0]["uri"])
    else:
        print(f"not found {singer} - {track}")
sp.playlist_add_items(playlist_id=playlist["id"],items=results)


