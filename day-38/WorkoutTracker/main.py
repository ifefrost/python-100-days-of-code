from config import *
from datetime import datetime
import requests

# prompt = input("What exercises did you do today? ")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

# params = {
#     "query": prompt
# }

# response = requests.post(url=nutritionix_endpoint, headers=header, json=params)
# workout = response.json()["exercises"][0]
# print(workout)

sheety_post_endpoint = "https://api.sheety.co/c21512e9714ba8e73dd12b458b57354d/workoutTracking/workouts"
sheety_get_endpoint = "https://api.sheety.co/c21512e9714ba8e73dd12b458b57354d/workoutTracking/workouts"


# workout_params = {
#     "workout": {
#         "date": "21/07/2020",
#         "time": "15:00:00",
#         "exercise": workout['user_input'].title(),
#         "duration": workout['duration_min'],
#         "calories": workout['nf_calories']
#     }
# }

# response = requests.post(url=sheety_post_endpoint, json=workout_params)
# print(response.text)

print()
