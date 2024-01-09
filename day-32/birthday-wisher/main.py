##################### Extra Hard Starting Project ######################

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
from random import randint
import smtplib

my_email = "email@yahoo.com"
password = "secret"

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today in birthday_dict:
    name = birthday_dict[today]["name"]
    with open(f"./letter_templates/letter_{randint(1,3)}.txt") as data:
        letter = data.read()
    email = letter.replace("[NAME]", name)
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="email@gmail.com",
                            msg=f"Subject:Happy Birthday\n\n{email}"
                            )
