import requests
from config import *
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "graph01"
graph_params = {
    "id": GRAPH_ID,
    "name": "Coding graph",
    "unit": "Days",
    "type": "int",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
DATE = today.strftime("%Y%m%d")
pixel_params = {
    "date": DATE,
    "quantity": "4"
}

# response = requests.post(url=pixel_endpoint, headers=headers, json=pixel_params)
# print(response.text)
put_endpoint = f"{pixel_endpoint}/{DATE}"
put_params = {
    "quantity": "20"
}
# response = requests.put(url=put_endpoint, headers=headers, json=put_params)
# print(response.text)

response = requests.delete(url=put_endpoint, headers=headers)
print(response.text)
