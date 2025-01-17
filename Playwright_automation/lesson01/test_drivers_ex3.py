import pytest
from playwright.sync_api import Playwright

class Test_Drivers_03:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.webkit.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.ladygaga.com/")

    def test_Chromatica(self):
        html_content = page.content()
        if "Chromatica" in html_content:
            print("Exists")
        else:
            print("Not Exists")