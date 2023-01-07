import requests
import json
import os

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self) -> None:
        self.tequila_key = os.getenv("TEQUILA_KEY")
        self.tequila_url = "https://api.tequila.kiwi.com/v2/search"

    def search(
        self,
        location_from: str,
        location_to: str,
        date_from: str,
        date_to: str,
        return_from: str,
        return_to: str,
        adults: int = 2,
        children: int = 1,
    ) -> dict:
        header = {"apikey": self.tequila_key}

        search_param = {
            "fly_from": location_from,
            "fly_to": location_to,
            "dateFrom": date_from,
            "dateTo": date_to,
            "return_from": return_from,
            "return_to": return_to,
            "ret_from_diff_city": False,
            "ret_to_diff_city": False,
            "adults": adults,
            "children": children,
            "infants": 0,
            "max_fly_duration": 20,
            "ret_from_diff_city": False,
            "ret_to_diff_city": False,
            "flight_type": "round",
            "one_for_city": 0,
            "one_per_date": 0,
            "selected_cabins": "W",
            "mix_with_cabins": "M",
            "adult_hold_bag": "1,0",
            "adult_hand_bag": "1,1",
            "child_hold_bag": "0",
            "child_hand_bag": "1",
            "only_working_days": False,
            "only_weekends": False,
            "partner_market": "fr",
            "curr": "EUR",
            "max_stopovers": "2",
            "max_sector_stopovers": "2",
            "vehicle_type": "aircraft",
            "limit": 50,
        }
        response = requests.get(url=self.tequila_url, params=search_param, headers=header)
        response.raise_for_status()
        return response.json()["data"]
