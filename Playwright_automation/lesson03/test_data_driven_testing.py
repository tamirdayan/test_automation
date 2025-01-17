
import pytest
from playwright.sync_api import Playwright

search_word = "Automation"

class Test_Data_Driven_Testing:
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

    @pytest.mark.parametrize("search_word, expected_title",
                             [
                                 ("Israel", "Israel"),
                                 ("Automation", "Automation"),
                                 ("blahblah", "Search results")
                             ])
    def test_data_driven_testing(self, search_word, expected_title):
        page.goto("https://www.wikipedia.org/")
        page.locator("[id='searchInput']").fill(search_word)
        page.locator("button[class='pure-button pure-button-primary-progressive']").click()
        actual_title = page.locator("[id='firstHeading']").inner_text()
        assert actual_title == expected_title
