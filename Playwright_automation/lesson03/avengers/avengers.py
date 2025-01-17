import csv
import pytest
from playwright.sync_api import Playwright

expected_total = 4
keys = "id, username, password, expected_rating"

def get_data_from_csv():
    with open("avengers.csv", newline='') as f:
        reader = csv.reader(f)
        file_list = [tuple(row) for row in reader]
        return file_list


class Test_Avengers:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/avengers/exercise/")

    def teardown_class(self):
        context.close()
        browser.close()

    def test_get_page_title(self):
        title_avenger = page.locator('//table/tbody/tr[1]/td')
        total_avenger = title_avenger.count()
        print('\n')
        for i in range(total_avenger):
            print(title_avenger.nth(i).inner_text())
        assert total_avenger == expected_total

    @pytest.mark.parametrize(keys, get_data_from_csv())
    def test_movie_rating(self, id, username, password, expected_rating):
        page.goto("https://atidcollege.co.il/avengers/exercise/")
        page.locator('//*[@id="' + id + '"]').click()
        page.locator('//*[@id="username"]').fill(username)
        page.locator('//*[@id="password"]').fill(password)
        page.locator('//*[@id="submit"]').click()
        rating = page.locator('#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-80d4314-0.fjPRnj > div.sc-db8c1937-0.eGmDjE.sc-80d4314-3.iBtAhY > div > div:nth-child(1) > a > div > div > div.sc-7ab21ed2-0.fAePGh > div.sc-7ab21ed2-2.kYEdvH > span.sc-7ab21ed2-1.jGRxWM').inner_text()
        assert rating == expected_rating
