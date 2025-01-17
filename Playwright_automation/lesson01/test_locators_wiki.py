
import pytest
from playwright.sync_api import Playwright

class Test_Locators_Wiki:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.wikipedia.org/")

    def test_playwright(self):
        print(page.locator("[class='footer-sidebar-text jsl10n']"))
        print(page.locator("[id='searchInput']"))
        print(page.locator("[id='searchLanguage']"))
        print(page.locator("[class='central-featured-logo']"))
