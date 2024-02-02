from config import *
import requests

class DataManager:
    def __init__(self):
        self.sheet_endpoint = SHEETY_ENDPOINT
        self.header = {
            "Authorization": SHEETY_TOKEN
        }

    #This class is responsible for talking to the Google Sheet.
    def get_sheet_data(self):
        response = requests.get(url=self.sheet_endpoint, headers=self.header)
        data = response.json()["prices"]
        return data
