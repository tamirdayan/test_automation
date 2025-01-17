import pytest
from playwright.sync_api import Playwright

expected_title = "IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows"
expected_url = "https://www.imdb.com/"


class Test_Browser_Connection_01:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.imdb.com/")

    def test_verify_title(self):
        page.reload()
        title = page.title()
        assert title == expected_title

    def test_verify_url(self):
        url = page.url
        assert url == expected_url
