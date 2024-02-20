from config import *
from twilio.rest import Client


class NotificationManager:
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_message(self, flight):
        message = self.client.messages.create(
            body=f"Low price alert! \n"
                 f"Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} "
                 f"to {flight.destination_city}-{flight.destination_airport}, "
                 f"from {flight.leave_date} to {flight.return_date}",
            from_=TWILIO_NUM,
            to=MY_NUM
        )
        print(message.sid)
