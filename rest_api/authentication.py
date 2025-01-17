import requests
import pytest
from playwright.sync_api import Playwright


class Test_Authentication:
    url = "http://admin:admin@localhost:3000/api/teams/"
    header = {'Content-type': 'application/json',
              'Authorization': 'Bearer glsa_Lp52toZsO9eBMyNtUNxmOfl4vAESjLJl_88e8dbd5'}

    def test_create_teams(self):
        payload = {
            "name": "MyTestTeam",
            "email": "email2@test.com",
            "orgId": 3
        }
        response = requests.post(self.url, json=payload, headers=self.header)
        response_json = response.json()
        print("\nresponse code: ", response)
        print("]\nresponse body: ", response_json)

    def test_get_teams(self):
        response = requests.get(self.url + "search", headers=self.header)
        response_json = response.json()
        for team in response_json["teams"]:
            print("\nid: ", team["id"])
            print("name: ", team["name"])
            print("email:  ", team["email"])
        assert response_json["totalCount"] == 4

    def test_create_multiple_teams(self):
        for i in range(4):
            payload = {
                "name": "MyTestTeam" + str(i),
                "email": "email" + str(i) + "@test.com"
            }
            response = requests.post(self.url, json=payload, headers=self.header)
            response_json = response.json()
            print("\nresponse code: ", response)
            print("]\nresponse body: ", response_json)
