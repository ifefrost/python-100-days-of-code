from config import *
from datetime import datetime
import requests

prompt = input("What exercises did you do today? ")
moment = datetime.now()

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

params = {
    "query": prompt
}

response = requests.post(url=nutritionix_endpoint, headers=header, json=params)
workout = response.json()["exercises"][0]

sheet_header = {
    "Authorization": SHEET_TOKEN
}

workout_params = {
    "workout": {
        "date": moment.strftime("%d/%m/%Y"),
        "time": moment.strftime("%H:%M:%S"),
        "exercise": workout['user_input'].title(),
        "duration": workout['duration_min'],
        "calories": workout['nf_calories']
    }
}

response = requests.post(url=SHEET_ENDPOINT, headers=sheet_header, json=workout_params)
print(response.text)

