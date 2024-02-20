from config import *
import requests
from datetime import datetime, timedelta
from flight_data import FlightData


class FlightSearch:
    def __init__(self):
        self.flight_api = KIWI_API
        self.header = {
            "apikey": KIWI_KEY
        }

    # This class is responsible for talking to the Flight Search API.
    def get_city_code(self, city):
        param = {
            "term": city
        }
        response = requests.get(url=f"{self.flight_api}/locations/query", headers=self.header, params=param)
        data = response.json()["locations"][0]["code"]
        return data

    def get_flight_data(self, city_code):
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        six_months_time = (datetime.now() + timedelta(days=(6 * 30))).strftime("%d/%m/%Y")
        params = {
            "fly_from": "YTO",
            "fly_to": city_code,
            "date_from": tomorrow,
            "date_to": six_months_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0,
            "curr": "CAD",
            "one_for_city": 1
        }

        response = requests.get(url=f"{self.flight_api}/v2/search", headers=self.header, params=params)
        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flight found for {city_code}")
            return None
        flight_data = FlightData(
            data['price'],
            data['cityFrom'],
            data['flyFrom'],
            data['cityTo'],
            data['flyTo'],
            data['route'][0]['local_departure'].split('T')[0],
            data['route'][1]['local_departure'].split('T')[0]
        )
        return flight_data

