import allure
import pytest
from playwright.sync_api import Playwright
from automation_final_project.ultimateqa.elements import Elements

EXPECTED_NUM_OF_BUTTONS = 12
EXPECTED_FACEBOOK_URL = "https://www.facebook.com/Ultimateqa1/"
NAME = "Tamir Dayan"
EMAIL = "tamir.dayan@ridewithvia.com"
MESSAGE = "Take me to your leader!"
CONTACT_US_FORM_SUBMITTED_EXPECTED_MESSAGE = "Thanks for contacting us"


class Test_Ultimateqa:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page, home
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(6000)
        page.goto("https://ultimateqa.com/complicated-page")
        home = Elements(page)

    def teardown_class(self):
        context.close()
        browser.close()

    @allure.title("Section of Buttons: Count All Buttons")
    @allure.description("This test counts all buttons in \"Section of Buttons\"")
    def test_count_all_buttons(self):
        actual_num_of_buttons = home.step_get_num_of_buttons()
        assert actual_num_of_buttons == EXPECTED_NUM_OF_BUTTONS

    @allure.title("Section of Social Media Follows: Verify Facebook Buttons' Links")
    @allure.description("This test verifies that all Facebook buttons' Links in \"Section of Social Media Follows\" "
                        "equal to \"https://www.facebook.com/Ultimateqa1/\"")
    def test_verify_facebook_buttons_links(self):
        facebook_buttons = home.step_get_facebook_buttons()
        for i in range(facebook_buttons.count()):
            assert facebook_buttons.nth(i).get_attribute("href") == EXPECTED_FACEBOOK_URL

    @allure.title("Section of Random Stuff: Submit Contact Us (First) Form")
    @allure.description("This test fills in all the fields (name, email, message and captcha math exercise) \n "
                        "of the first form in \"Section of Random Stuff\", clicks on \"Submit\" button \n"
                        "and verifies \"Thanks for contacting us\" message is displayed.")
    def test_verify_form_submitted_text(self):
        home.step_fill_name(NAME)
        home.step_fill_email(EMAIL)
        home.step_fill_message(MESSAGE)
        home.step_fill_captcha()
        assert home.step_submit_form() == CONTACT_US_FORM_SUBMITTED_EXPECTED_MESSAGE
