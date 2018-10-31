import json
import tweepy
import requests

import time
import datetime

response = requests.get('https://weather.cit.api.here.com/weather/1.0/report.json?product=forecast_astronomy&name=Ottawa&app_id=t883KznRyE8cWLnJaYkn&app_code=MnUR3KfQTWo1MDxu92e1BA')
data = json.loads(response.text)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

sunStuff = []

sunStuff.append(data["astronomy"]["astronomy"][1]["sunrise"])
sunStuff.append(data["astronomy"]["astronomy"][1]["sunset"])

count = 0
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

for change in sunStuff:
    if count == 0:
        change = st + "\nHello Today! Sunrise: " + change
    else:
        change = st + "\nGoodbye Today! Sunset: " + change
    count += 1
    api.update_status(change)