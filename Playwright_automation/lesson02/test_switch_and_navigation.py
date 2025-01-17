import pytest
from playwright.sync_api import Playwright

ALERT_MSG = "Alert is gone."
MY_FIRST_NAME = "Tamir"
IFRAME_MSG = "This is an IFrame !"

class Test_Switch_And_Navigation:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://atidcollege.co.il/Xamples/ex_switch_navigation.html")

    def teardown_class(self):
        context.close()
        browser.close()

    def handle_alert(self, dialog):
        print("Alert text is: " + dialog.message)
        dialog.accept()

    def handle_prompt(self, dialog, text):
        print("Prompt text is: " + dialog.message)
        dialog.accept(text)

    def test_verify_alert(self):
        page.once("dialog", lambda dialog: self.handle_alert(dialog))
        page.locator("[id='btnAlert']").click()
        assert page.locator("[id='output']").inner_text() == ALERT_MSG

    def test_verify_prompt(self):
        page.once("dialog", lambda dialog: self.handle_prompt(dialog, MY_FIRST_NAME))
        page.locator("[id='btnPrompt']").click()
        assert page.locator("[id='output']").inner_text() == MY_FIRST_NAME

    def test_verify_iframe(self):
        #TODO
        page.once("dialog", lambda dialog: self.handle_prompt(dialog, MY_FIRST_NAME))
        page.locator("[id='btnPrompt']").click()
        assert page.locator("[id='output']").inner_text() == MY_FIRST_NAME
