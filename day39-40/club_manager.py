import requests
import os

class ClubManager:
    def __init__(self) -> None:
        self.sheety_url = "https://api.sheety.co/1658c67683f7eb7e1940e0a85f25f886/copieDeFlightDeals/users"
        self.sheety_bear = os.getenv("SHEETY_BEAR")
        self.header_sheety = {"Authorization": self.sheety_bear}
        self.data = []

    def add_member(self, first_name, last_name, email):
        url = self.sheety_url
        param = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(url=url, json=param, headers=self.header_sheety)
        response.raise_for_status()

    def get_members(self):
        response = requests.get(url=self.sheety_url, headers=self.header_sheety)
        response.raise_for_status()
        self.data = response.json()["users"]
        members = []
        for member in self.data:
            members.append(member["email"])
        return members
