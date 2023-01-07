import requests
import os

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.sheety_url = "https://api.sheety.co/1658c67683f7eb7e1940e0a85f25f886/copieDeFlightDeals/prices"
        self.sheety_bear = os.getenv("SHEETY_BEAR")
        self.header_sheety = {"Authorization": self.sheety_bear}
        self.data = []
        self.init_iata_code()

    def get_search_list(self) -> list:
        iata = {}
        for flight in self.data:
            iata[flight["iataCode"]] = flight["lowestPrice"]
        return iata

    def get_lowest_price(self, flight_price, code) -> bool:
        for flight in self.data:
            if flight["iataCode"] == code:
                if int(flight["lowestPrice"]) >= flight_price:
                    return True

    def init_iata_code(self) -> None:
        response = requests.get(url=self.sheety_url, headers=self.header_sheety)
        response.raise_for_status()
        self.data = response.json()["prices"]
        for flight in self.data:
            if flight["iataCode"] == "":
                code = self.update_iata(flight, self.retrieve_iata(flight["city"]))
                flight["iataCode"] = code

    def retrieve_iata(self, city) -> str:
        tequila_key = os.getenv("TEQUILA_KEY")
        tequila_url = "https://api.tequila.kiwi.com/locations/query"
        header_tequila = {"apikey": tequila_key}

        location_param = {
            "term": city,
            "location_types": "city",
            "limit": 1
        }
        response = requests.get(url=tequila_url, params=location_param, headers=header_tequila)
        response.raise_for_status()
        if response.json()["results_retrieved"] > 0:
            location = response.json()["locations"]
            return location[0]["code"]
        else:
            return ""

    def update_iata(self, search, code) -> str:
        update_url = self.sheety_url + "/" + str(search["id"])
        param = {
            "price": {
                "city": search["city"],
                "iataCode": code,
                "lowestPrice": search["lowestPrice"]
            }
        }
        response = requests.put(url=update_url, json=param, headers=self.header_sheety)
        response.raise_for_status()
        return code
