import requests
import os

class ClubManager:
    def __init__(self) -> None:
        self.SHEETY_URL="https://api.sheety.co/1658c67683f7eb7e1940e0a85f25f886/copieDeFlightDeals/users"
        self.SHEETY_BEAR=os.getenv("SHEETY_BEAR")
        self.header_sheety = {"Authorization": self.SHEETY_BEAR}
        self.data=[]
        
    def add_member(self,firstname, lastname, email):
        url=self.SHEETY_URL
        param={
            "user": {
                "firstName":firstname,
                "lastName":lastname,
                "email":email
            }
        }
        response = requests.post(url=url,json=param,headers=self.header_sheety)
        response.raise_for_status()

    def get_members(self) :
        response = requests.get(url=self.SHEETY_URL,headers=self.header_sheety)
        response.raise_for_status()
        self.data = response.json()["users"]
        members = []
        for member in self.data:
            members.append(member["email"])
        return members