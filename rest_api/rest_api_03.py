import json
import requests


url = "https://api.openweathermap.org/data/2.5/weather"
city = "Jerusalem"
api_key = "42bd4b24c24c49bd574239449b91d064"
params = dict(appid=api_key, q=city, units='metric')
response = requests.get(url, params)
response_json = response.json()


def test_country():
    assert("IL" == response_json['sys']['country'])


def test_humidity():
    humidity = response_json['main']['humidity']
    print(humidity)
    assert(58 == humidity)
