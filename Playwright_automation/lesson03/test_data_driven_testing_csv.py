import csv

import pytest
from playwright.sync_api import Playwright

keys = "search_word, expected_title"

class Test_Data_Driven_Testing_Csv:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        # Start tracing before creating / navigating a page.
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

    def teardown_class(self):
        # Stop tracing and export it into a zip archive.
        context.tracing.stop(path="trace.zip")
        context.close()
        browser.close()

    def get_data_from_csv():
        file_list = []
        with open("data.csv", newline='') as f:
            reader = csv.reader(f)
            file_list = [tuple(row) for row in reader]
            return file_list

    @pytest.mark.parametrize(keys, get_data_from_csv())
    def test_data_driven_testing_csv(self, search_word, expected_title):
        page.goto("https://www.wikipedia.org/")
        page.locator("[id='searchInput']").fill(search_word)
        page.locator("button[class='pure-button pure-button-primary-progressive']").click()
        actual_title = page.locator("[id='firstHeading']").inner_text()
        assert actual_title == expected_title
