import json
import tweepy
import requests

response = requests.get('https://weather.cit.api.here.com/weather/1.0/report.json?product=forecast_astronomy&name=Ottawa&app_id=t883KznRyE8cWLnJaYkn&app_code=MnUR3KfQTWo1MDxu92e1BA')
data = json.loads(response.text)

CONSUMER_KEY = '7UWJW9IkNa327CRjhzsO3jpTy'
CONSUMER_SECRET = 'gXBZjJoNe0N4KKDh4MKFzssrovfjAmaVkmGo31XPP11ueGgMqP'
ACCESS_TOKEN = '1057381018460667905-w96HxDTAcnEtppLQPVZIJwWCUH7rzh'
ACCESS_TOKEN_SECRET = 'ndMlDYM7DectSwEfFX7cZYhf96NQUkoODFT9k9vIrSo6k'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

sunStuff = []

sunStuff.append(data["astronomy"]["astronomy"][1]["sunrise"])
sunStuff.append(data["astronomy"]["astronomy"][1]["sunset"])

count = 0

for change in sunStuff:
    if count == 0:
        change = "Hello Today! Sunrise: " + change
    else:
        change = "Goodbye Today! Sunset: " + change
    api.update_status(change)