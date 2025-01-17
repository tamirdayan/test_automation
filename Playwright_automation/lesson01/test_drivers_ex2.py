import pytest
from playwright.sync_api import Playwright


class Test_Browser_Connection_02:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.google.com/")
        page.goto("https://www.bing.com/")
        page.go_back()
        print(page.title())

    def test_bubble(self):
        html_content = page.content()
        if "bubble" in html_content:
            print("Exists")
        else:
            print("Not Exists")