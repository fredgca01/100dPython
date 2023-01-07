from typing import Optional

class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flight) -> None:
        self.city_code_to = flight["cityCodeTo"]
        self.fly_from = flight["flyFrom"]
        self.fly_to = flight["flyTo"]
        self.city_from = flight["cityFrom"]
        self.city_to = flight["cityTo"]
        self.nights_nb = flight["nightsInDest"]
        self.price = flight["conversion"]["EUR"]
        if flight["availability"]["seats"] is None:
            self.seats_available = 0
        else:
            self.seats_available = flight["availability"]["seats"]
        self.routes = []
        for route in flight["route"]:
            data = {}
            data["flyFrom"] = route["flyFrom"]
            data["flyTo"] = route["flyTo"]
            data["airline"] = route["airline"]
            data["local_departure"] = route["local_departure"]
            data["local_arrival"] = route["local_arrival"]
            self.routes.append(data)

    def is_available(self) -> bool:
        return self.seats_available != 0

    def get_price(self) -> float:
        return self.price

    def get_iata_code(self) -> str:
        return self.city_code_to

    def print_summary(self) -> str:
        len(self.routes)
        return f"Low price ! from: {self.city_from}-{self.fly_from} to: {self.city_to}-{self.fly_to} for {self.price}€ {self.seats_available} seats remaining"

    def print_detail(self) -> str:
        detail = ""
        for route in self.routes:
            detail = detail + f"From: {route['flyFrom']} to: {route['flyTo']} by: {route['airline']} at: {route['local_departure']} to:{route['local_arrival']}\n"
        return detail
