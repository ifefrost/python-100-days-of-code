from config import *
import requests


class FlightSearch:
    def __init__(self):
        self.flight_api = KIWI_API
        self.header = {
            "apikey": KIWI_KEY
        }

    #This class is responsible for talking to the Flight Search API.
    def get_city_code(self, city):
        param = {
            "term": city
        }
        response = requests.get(url=f"{self.flight_api}/locations/query", headers=self.header, params=param)
        data = response.json()["locations"][0]["code"]
        return data


