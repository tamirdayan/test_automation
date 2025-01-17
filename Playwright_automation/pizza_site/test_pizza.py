import allure
import pytest
from playwright.sync_api import Playwright
from Playwright_automation.pizza_site.elements import Elements

INITIAL_PRICE = "$7.50"
FIRST_NAME = "Tamir"
LAST_NAME = "Dayan"
DELIVERY_METHOD = "Delivery"
DELIVERY_PRICE = "$10.50"
COUPON_CODE = "088-234"
EXPECTED_ALERT_MESSAGE = FIRST_NAME + " " + LAST_NAME + " " + COUPON_CODE


class Test_Pizza:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page, home
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/pizza/")
        home = Elements(page)

    def teardown_class(self):
        context.close()
        browser.close()

    @allure.title("Verify Initial Price")
    @allure.description("This test verifies the initial price is $7.50")
    def test_initial_price(self):
        actual_price = home.get_price()
        assert actual_price == INITIAL_PRICE

    @allure.title("Fill Full Name")
    @allure.description("This test fills first name and last name")
    def test_login(self):
        home.fill_full_name(FIRST_NAME, LAST_NAME)

    @allure.title("Choose Delivery Method")
    @allure.description("This test chooses the option \"Delivery\" from the combobox \"Is This Pickup or Delivery?\"")
    def test_choose_delivery(self):
        assert home.choose_delivery() == DELIVERY_METHOD

    @allure.title("Verify Delivery Price")
    @allure.description("This test verifies the updated price is $10.50")
    def test_delivery_price(self):
        actual_price = home.get_updated_price()
        assert actual_price == DELIVERY_PRICE

    @allure.title("Get Coupon")
    @allure.description("This test verifies the coupon number is 088-234")
    def test_get_coupon(self):
        assert home.get_coupon() == COUPON_CODE

    @allure.title("Insert Coupon")
    @allure.description("This test inserts coupon to \"Additional Comments\" field")
    def test_insert_coupon(self):
        home.insert_coupon()

    @allure.title("Submit Your Order")
    @allure.description("This test clicks on \"Submit Your Order\" button and verifies the data inserted correctly")
    def test_verify_alert_text(self):
        try:
            page.on("dialog", lambda dialog: home.handle_alert(dialog))
            home.submit_your_order()
            assert home.dialog_text == EXPECTED_ALERT_MESSAGE
        except Exception as e:
            pytest.fail("Test failed, see details", e)
