from time import sleep
import allure


class Elements:
    def __init__(self, page):
        self.page = page
        self.buttons = self.page.locator(".et_pb_row.et_pb_row_2.et_pb_row_4col a")
        self.facebook_buttons = page.locator("a[title*='Follow on Facebook']")
        self.name = self.page.locator("input[id='et_pb_contact_name_0']")
        self.email = self.page.locator("input[id='et_pb_contact_email_0']")
        self.message = self.page.locator("textarea[id='et_pb_contact_message_0']")
        self.captcha_question = self.page.locator("[class ='clearfix']").first.inner_text()
        self.captcha_answer = self.page.locator("input[class='input et_pb_contact_captcha']").first
        self.submit_button = self.page.locator("button[class='et_pb_contact_submit et_pb_button']").first
        self.form_submitted_message = ""

    @allure.step("Get Number Of Buttons")
    def step_get_num_of_buttons(self):
        return self.buttons.count()

    @allure.step("Get Facebook Buttons")
    def step_get_facebook_buttons(self):
        return self.facebook_buttons

    @allure.step("Fill Full Name")
    def step_fill_name(self, name):
        self.name.fill(name)

    @allure.step("Fill Email")
    def step_fill_email(self, email):
        self.email.fill(email)

    @allure.step("Fill Message")
    def step_fill_message(self, message):
        self.message.fill(message)

    @allure.step("Fill Captcha")
    def step_fill_captcha(self):
        result = eval(str(self.captcha_question).replace("=", "").strip())
        self.captcha_answer.fill(str(result))

    @allure.step("Click On Submit Button")
    def step_submit_form(self):
        self.submit_button.click()
        sleep(3)
        self.form_submitted_message = self.page.locator("div[class='et-pb-contact-message']").first.inner_text()
        return self.form_submitted_message
