import pytest
from playwright.sync_api import Playwright


class Test_Locators_Basic:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://playwright.dev/")

    def test_playwright(self):
        print(page.locator("[src='/img/playwright-logo.svg']"))
        print(page.locator("[class ='navbar__brand']"))
        print(page.locator("[class ='navbar__logo']"))

    def test_count_links(self):
        links = page.locator("a").count()
        print("number of links in page: " + str(links))
