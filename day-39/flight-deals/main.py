from data_manager import DataManager
from flight_search import FlightSearch

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()

sheet = data_manager.get_sheet_data()
cities = [value['city'] for value in sheet]
city_codes = [flight_search.get_city_code(city) for city in cities]

print(city_codes)
