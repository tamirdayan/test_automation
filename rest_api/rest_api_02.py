import json
import requests


url = "https://api.openweathermap.org/data/2.5/weather"
city = "Jerusalem"
api_key = "42bd4b24c24c49bd574239449b91d064"
params = dict(appid=api_key, q=city, units='metric')
response = requests.get(url, params)
response_json = response.json()


def test_response():
    print(json.dumps(response_json, indent=2))
    print("\n ********************** \n")


def test_status_code():
    print(response.status_code)
    assert(response.status_code == 200)


def test_date():
    print(response.headers.get('Date'))


def test_content():
    content_type = response.headers.get('content-type')
    print(content_type)
    assert("application/json" in content_type)


