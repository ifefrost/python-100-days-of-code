import requests
from twilio.rest import Client
from config import *
open_weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"


parameters = {
    "lat": 43.451637,
    "lon": -80.492531,
    "cnt": 4,
    "appid": api_key,
}
response = requests.get(open_weather_endpoint, params=parameters)
data = response.json()
full_list = data["list"]
weather_list = [item["weather"][0]["id"] for item in full_list]

will_rain = False
for item in weather_list:
    if int(item) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today, Bring your ☔",
        from_=twilio_num,
        to=my_num
    )

    print(message.status)

