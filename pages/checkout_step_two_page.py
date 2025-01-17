from ..config import BASE_URL


class CheckoutStepTwoPage:
    def __init__(self, page):
        self.page = page
        self.url = f"{BASE_URL}/checkout-step-two.html"

    def click_finish(self):
        self.page.locator("[data-test='finish']").click()