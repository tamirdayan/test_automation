from ..config import BASE_URL


class CartPage:
    def __init__(self, page):
        self.page = page
        self.url = f"{BASE_URL}/cart.html"


    def click_checkout(self):
        self.page.locator("[data-test='checkout']").click()