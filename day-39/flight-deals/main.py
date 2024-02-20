from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_sheet_data()

if sheet_data[0]['iataCode'] == '':
    for item in sheet_data:
        item['iataCode'] = flight_search.get_city_code(item['city'])

    for item in sheet_data:
        data = {
            "price": {
                "iataCode": item['iataCode']
            }
        }
        data_manager.update_city(data, item['id'])

for item in sheet_data:
    flight = flight_search.get_flight_data(item['iataCode'])
    try:
        flight.price
    except AttributeError:
        pass
    else:
        if flight.price and flight.price < item['lowestPrice']:
            notification_manager.send_message(flight)
