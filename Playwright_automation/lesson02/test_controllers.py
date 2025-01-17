
import pytest
from playwright.sync_api import Playwright

FIRST_NAME = "Tamir"
LAST_NAME = "Dayan"

class Test_Locators_Advanced_Swaglabs:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/ex_controllers.html")

    def teardown_class(self):
        context.close()
        browser.close()

    def test_swaglabs(self):
        page.locator("[name='firstname']").fill(FIRST_NAME)
        page.locator("[name='lastname']").fill(LAST_NAME)

        continents_selector = "[id='continents']"
        page.select_option(continents_selector, value="europe")

        page.locator("[id='sex-0']").click()
        page.locator("[id='exp-2']").click()

        page.locator("[id='datepicker']").click()
        date_widget = page.locator("[id='ui-datepicker-div']")
        cells = date_widget.locator("td")
        for i in range(cells.count()):
            if cells.nth(i).text_content() == "14":
                cells.nth(i).click()
                break

        page.locator("[id='submit']").click()

        """date_string = page.url.split("datepicker=")[1].split()
        date_arr = date_string.split("%")
        month = date_arr[0].split("%")
        day = date_arr[1].split("%2f")[1].split("%2F")
        year = date_arr[2].split("%2f")[1].split("&")
        print("day: %s month: %s year: %s", day, month, year)""" # TODO

        if FIRST_NAME and LAST_NAME in page.url:
            print("Test Passed")
        else:
            print("Test Failed")

