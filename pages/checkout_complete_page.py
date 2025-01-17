from ..config import BASE_URL

class CheckoutCompletePage:
    def __init__(self, page, expected_message=None):
        self.page = page
        self.url = f"{BASE_URL}/checkout-complete.html"
        self.expected_message = expected_message or "Thank you for your order!"

    def get_success_message(self):
        return self.page.locator(".complete-header").text_content()

    def is_success_message_visible(self):
        return self.page.locator(".complete-header").is_visible()
