
import pytest
from playwright.sync_api import Playwright

user_name = "standard_user"
password = "secret_sauce"
expected_title = "PRODUCTS"

class Test_Trace_Viewer:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        # Start tracing before creating / navigating a page.
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        page.goto("https://www.saucedemo.com/")

    def teardown_class(self):
        # Stop tracing and export it into a zip archive.
        context.tracing.stop(path="trace.zip")
        context.close()
        browser.close()

    def test_trace_viewer(self):
        page.locator("[id='user-name']").fill(user_name)
        page.locator("[id='password']").fill(password)
        page.locator("[id='login-button']").click()

        actual_title = page.locator("span[class='title']").inner_text()
        assert actual_title == expected_title
