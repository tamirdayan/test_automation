
import pytest
from playwright.sync_api import Playwright

class Test_Locators_Advanced_Swaglabs:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")

    def teardown_class(self):
        context.close()
        browser.close()

    def test_swaglabs(self):
        print(page.locator("[class='bot-column']")) # image
        print(page.locator("[id='user-name']")) # username
        print(page.locator("[id='password']")) # password. data-test is a convention for automation
        print(page.locator("[id='login-button']")) # username
        print(page.locator("[class='login-logo']")) # logo