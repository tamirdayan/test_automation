import requests
import pytest
from playwright.sync_api import Playwright

class Test_Json_Server:
    get_url = "http://localhost:3000/"
    post_url = "http://localhost:3000/posts"
    header = {'Content-type': 'application/json'}

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto(self.get_url)

    def teardown_class(self):
        context.close()
        browser.close()

    def verify_resources(self, resource, result):
        resources = {"posts": "#resources > div > ul > li:nth-child(1) > sup",
                     "comments": "#resources > div > ul > li:nth-child(2) > sup",
                     "albums": "#resources > div > ul > li:nth-child(3) > sup",
                     "photos": "#resources > div > ul > li:nth-child(4) > sup",
                     "users": "#resources > div > ul > li:nth-child(5) > sup",
                     "todos": "#resources > div > ul > li:nth-child(6) > sup",
                     }
        page.reload()
        fetched_resource = page.locator(resources.get(resource))
        assert (fetched_resource.inner_text() == str(result + "x"))

    def test_post_post(self):
        payload = {'userId': '10', 'title': 'Tamir', 'body': 'Dayan'}
        response = requests.post(self.post_url, json=payload, headers=self.header)
        response_json = response.json()
        print("response code: ", response)
        print("response body: ", response_json)

    def test_verify_post(self):
        page.reload()
        self.verify_resources("posts", "101")

    def test_put_post(self):
        id = '/101'
        payload = {'userId': '10', 'title': 'Tamirush', 'body': 'Dayan'}
        response = requests.put(self.post_url + id, json=payload, headers=self.header)
        response_json = response.json()
        print("response code: ", response)
        print("response body: ", response_json)
        assert (response.status_code == 200)

    def test_patch_post(self):
        id = '/101'
        payload = {'title': 'Tamirushkush'}
        response = requests.patch(self.post_url + id, json=payload, headers=self.header)
        response_json = response.json()
        print("response code: ", response)
        print("response body: ", response_json)
        assert (response.status_code == 200)

    def test_delete_student(self):
        id = '/101'
        response = requests.delete(self.post_url + id)
        print(response)
        page.reload()
        self.verify_resources("posts", "100")

    def test_verify_bonus(self):
        self.verify_resources("users", "10")
