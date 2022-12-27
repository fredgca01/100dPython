import requests
from datetime import datetime
import os

PIXELA_URL="https://pixe.la/v1/users"
PIXELA_KEY=os.environ.get("PIXELA_KEY")
USERNAME="fredgca"

# USER_PARAM = {
#     "token":PIXELA_KEY,
#     "username":USERNAME,
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }

# response=requests.post(url=PIXELA_URL,json=USER_PARAM)
# print(response.text)

GRAPH_URL =f"{PIXELA_URL}/{USERNAME}/graphs"
GRAPH_ID="graph1fredgca"

# GRAPH_CONFIG = {
#     "id":GRAPH_ID,
#     "name":"Sport graph",
#     "unit":"Session",
#     "type":"int",
#     "color":"sora"
# }

# headers={
#     "X-USER-TOKEN":PIXELA_KEY
# }

#response=requests.post(url=GRAPH_URL,json=GRAPH_CONFIG,headers=headers)
#print(response.text)

# SESSION_CONFIG = {
#     "date":datetime(year=2022,month=12,day=23).strftime("%Y%m%d"),
#     "quantity":"1"
# }

# headers={
#     "X-USER-TOKEN":PIXELA_KEY
# }


# response=requests.post(url=f"{GRAPH_URL}/{GRAPH_ID}",json=SESSION_CONFIG,headers=headers)
# print(response.text)

SESSION_CONFIG = {
    "quantity":"25"
}

headers={
    "X-USER-TOKEN":PIXELA_KEY
}

date=datetime(year=2022,month=12,day=23).strftime("%Y%m%d")
#response=requests.put(url=f"{GRAPH_URL}/{GRAPH_ID}/{date}",json=SESSION_CONFIG,headers=headers)
response=requests.delete(url=f"{GRAPH_URL}/{GRAPH_ID}/{date}",headers=headers)

print(response.text)
