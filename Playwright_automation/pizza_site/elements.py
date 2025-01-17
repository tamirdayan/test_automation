from time import sleep
import allure


class Elements:
    def __init__(self, page):
        self.page = page
        self.first_name = self.page.locator("input[name='input_22.3']")
        self.last_name = self.page.locator("input[name='input_22.6']")
        self.price = self.page.locator("span[class='ginput_total ginput_total_5']")
        self.delivery = self.page.locator("//*[@id='input_5_21']/option[2]")
        self.coupon = self.page.frame_locator("iframe[src='coupon.html']").locator(
            "div[id='coupon_Number']")
        self.additional_comments = self.page.locator("//*[@id='input_5_20']")
        self.submit_button = self.page.locator("input[id='gform_submit_button_5']")
        self.dialog_text = ""

    def handle_alert(self, dialog):
        sleep(1)
        self.dialog_text = dialog.message
        dialog.accept()

    @allure.step("Get Price")
    def get_price(self):
        return self.price.inner_text()

    @allure.step("Fill Full Name")
    def fill_full_name(self, first_name, last_name):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)

    @allure.step("Choose Delivery")
    def choose_delivery(self):
        self.page.select_option("[id='input_5_21']", value="Delivery|3")
        return self.delivery.inner_text().strip()

    @allure.step("Get Updated Price")
    def get_updated_price(self):
        updated_price = self.page.locator("span[class='ginput_total ginput_total_5']").inner_text()
        return updated_price

    @allure.step("Get Coupon")
    def get_coupon(self):
        return self.coupon.inner_text()

    @allure.step("Insert Coupon")
    def insert_coupon(self):
        return self.additional_comments.fill(self.coupon.inner_text())

    @allure.step("Click Submit Your Order Button")
    def submit_your_order(self):
        self.submit_button.click()
