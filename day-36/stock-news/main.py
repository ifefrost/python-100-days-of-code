## API keys are kept secret in a separate file called config.py.

import requests
from config import *
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_PRICE_API
}

url = 'https://www.alphavantage.co/query'
r = requests.get(url, params=parameters)
data = r.json()
days = list(data['Time Series (Daily)'].keys())
new_price = float(data['Time Series (Daily)'][days[0]]['4. close'])
old_price = float(data['Time Series (Daily)'][days[1]]['4. close'])
diff = round(new_price - old_price, 2)
margin = round((diff/old_price) * 100)
positive = '🔺'
if margin < 0:
    positive = '🔻'

if abs(margin) > 5:
    news_params = {
        "apiKey": NEWS_API,
        "q": COMPANY_NAME,
    }

    news_url = "https://newsapi.org/v2/everything"
    news_r = requests.get(news_url, params=news_params)
    news_data = news_r.json()["articles"][:3]
    client = Client(account_sid, auth_token)
    for news in news_data:
        message = client.messages.create(
            body=f'{STOCK}: {positive}{abs(margin)}%\n'
                f'Headline: {news['title']}\n'
                f'Brief: {news['description']}',
            from_=twilio_num,
            to=my_num
        )

