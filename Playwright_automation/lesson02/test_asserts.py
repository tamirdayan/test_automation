import pytest
from playwright.sync_api import Playwright

my_weight = "93"
my_height = "167"
your_bmi_expected_result = "33"
it_means_expected_result = "That you have overweight."


class Test_Locators_Advanced_Calculator:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/bmi/")

    def teardown_class(self):
        context.close()
        browser.close()

    def test_fill_fields(self):
        page.locator("[name='weight']").fill(my_weight)
        page.locator("[name='height']").fill(my_height)
        page.locator("[id='calculate_data']").click()

    def test_bmi(self):
        your_bmi = page.locator("[id='bmi_result']").input_value()
        assert your_bmi == your_bmi_expected_result

    def test_it_means(self):
        it_means = page.locator("[id='bmi_means']").input_value()
        assert it_means == it_means_expected_result

    def test_calculate_data(self):
        calculate_bmi_button = page.locator("[id='calculate_data']")
        # TODO
