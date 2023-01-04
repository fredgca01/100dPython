import requests
import os

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.SHEETY_URL="https://api.sheety.co/1658c67683f7eb7e1940e0a85f25f886/copieDeFlightDeals/prices"
        self.SHEETY_BEAR=os.getenv("SHEETY_BEAR")
        self.header_sheety = {"Authorization": self.SHEETY_BEAR}
        self.data=[]
        self.init_IATAcode()

    def get_search_list(self) -> list:
        iata={}
        for flight in self.data:
            iata[flight["iataCode"]]=flight["lowestPrice"]
        return iata
    
    def get_lowest_price(self,flight_price, code) -> bool:
        for flight in self.data:
            if flight["iataCode"]==code:
                if int(flight["lowestPrice"])>=flight_price:
                    return True

    def init_IATAcode(self) -> None:
        response = requests.get(url=self.SHEETY_URL,headers=self.header_sheety)
        response.raise_for_status()
        self.data = response.json()["prices"]
        for flight in self.data:
            if flight["iataCode"]=="":
                code = self.update_IATA(flight,self.retrieve_IATA(flight["city"]))
                flight["iataCode"]=code

    def retrieve_IATA(self,city) -> str:
        TEQUILA_KEY=os.getenv("TEQUILA_KEY")
        TEQUILA_URL="https://api.tequila.kiwi.com/locations/query"
        header_tequila = {"apikey":TEQUILA_KEY}

        location_param={
            "term":city,
            "location_types":"city",
            "limit":1
        }
        response = requests.get(url=TEQUILA_URL,params=location_param, headers=header_tequila)
        response.raise_for_status()
        location =  response.json()["locations"]
        return location[0]["code"]

    def update_IATA(self,search,code) -> str:
        update_url=self.SHEETY_URL+"/"+str(search["id"])
        param={
            "price": {
                "city":search["city"],
                "iataCode":code,
                "lowestPrice":search["lowestPrice"]
            }
        }
        response = requests.put(url=update_url,json=param,headers=self.header_sheety)
        response.raise_for_status()
        return code

