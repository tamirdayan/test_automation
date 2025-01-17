import allure
import pytest
from playwright.sync_api import Playwright
from Playwright_automation.nopCommerce.elements import Elements

camera_and_photo_items = 3

class Test_Nopcommerce:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page, home
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.nopcommerce.com/")
        home = Elements(page)

    def teardown_class(self):
        context.close()
        browser.close()

    @allure.title("Choose \"Camera & Photo\"")
    @allure.description("This test chooses from \"Electronics\" menu the option Choose \"Camera & Photo\"")
    def test_navigate_to_camera_and_photo_page(self):
        home.navigate_to_camera_and_photo_page()

    @allure.title("Sort by Price: Low to High")
    @allure.description("This test chooses from sort by menu the option \"Price: Low to High\" ")
    def test_sort_by_price_low_to_high(self):
        home.sort_by_price_low_to_high()

    @allure.title("verify_num_of_items")
    @allure.description("Verify number of items is equal to 3 ")
    def test_verify_num_of_items(self):
        assert camera_and_photo_items == home.verify_num_of_items()




