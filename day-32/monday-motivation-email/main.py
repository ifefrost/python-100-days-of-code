import smtplib
import datetime as dt
from random import choice

my_email = "email@yahoo.com"
password = "secret"

now = dt.datetime.now()
if now.weekday() == 0:
    with open("quotes.txt", mode='r') as file:
        quotes = file.readlines()

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="email@email.com",
                            msg=f"Subject:You've got this\n\n{choice(quotes)}"
                            )