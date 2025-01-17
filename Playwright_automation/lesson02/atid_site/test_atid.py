import pytest
from playwright.sync_api import Playwright
from Playwright_automation.lesson02.atid_site.login_page import Login_Page

USERNAME = "selenium"
PASSWORD = "webdriver"

class Test_Atid:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page, home
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/webdriveradvance.html")
        home = Login_Page(page)

    def teardown_class(self):
        context.close()
        browser.close()

    def test_login_page(self):
        home.sign_in(USERNAME, PASSWORD)

