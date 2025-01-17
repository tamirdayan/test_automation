from ..config import BASE_URL


class CheckoutStepOnePage:
    def __init__(self, page):
        self.page = page
        self.url = f"{BASE_URL}/checkout-step-one.html"

    def fill_form(self, first_name: str, last_name: str, zip_code: str):
        self.page.fill("[data-test='firstName']", first_name)
        self.page.fill("[data-test='lastName']", last_name)
        self.page.fill("[data-test='postalCode']", zip_code)

    def click_continue(self):
        self.page.locator("[data-test='continue']").click()

    def get_error_message(self):
        return self.page.locator("[data-test='error']").text_content()