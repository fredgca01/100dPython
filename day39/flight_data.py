from types import NoneType


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,flight) -> None:
        self.cityCodeTo = flight["cityCodeTo"]
        self.flyFrom = flight["cityFrom"]
        self.flyTo = flight["cityTo"]
        self.nightsNb = flight["nightsInDest"]
        self.price = flight["conversion"]["EUR"]
        if flight["availability"]["seats"] is None:
            self.seats_available=0
        else:
            self.seats_available=flight["availability"]["seats"]
        self.routes=[]
        for route in flight["route"]:
            data={}
            data["flyFrom"]=route["flyFrom"]
            data["flyTo"]=route["flyTo"]
            data["airline"]=route["airline"]
            data["local_departure"]=route["local_departure"]
            data["local_arrival"]=route["local_arrival"]
            self.routes.append(data)
    
    def is_available(self) -> bool:
        return self.seats_available != 0
    
    def getPrice(self) -> float:
        return self.price
    
    def getIataCode(self) -> str:
        return self.cityCodeTo
    
    def printSummary(self)->str:
        return f"{self.flyFrom} {self.flyTo} {self.price}€ {self.seats_available} seats remaining" 
    
    def printDetail(self)->str:
        detail = ""
        for route in self.routes:
            detail=detail+f"From: {route['flyFrom']} to: {route['flyTo']} by: {route['airline']} at: {route['local_departure']} to:{route['local_arrival']}\n"
        return detail 