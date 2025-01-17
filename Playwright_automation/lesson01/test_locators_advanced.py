
import pytest
from playwright.sync_api import Playwright

class Test_Locators_Advanced:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/ex_locators.html")

    def test_playwright(self):
        print(page.locator("//*[@id='locator_id']"))
        print(page.locator("/html/body/div[2]/div/div/div/div/span"))
        print(page.locator("//p[text()='Find my locator (3)']"))
        print(page.locator("//div[contains(@class, 'locator_class' and @text,'Find my locator (4)')]"))
        print(page.locator())
        print(page.locator())
        print(page.locator())
        print(page.locator())



