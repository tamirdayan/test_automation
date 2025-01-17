from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = self.page.locator('[data-test="username"]')
        self.password_input = self.page.locator('[data-test="password"]')
        self.login_button = self.page.locator('[data-test="login-button"]')
        self.error_message = self.page.locator('[data-test="error"]')

    def load(self, base_url: str):
        """Loads the login page."""
        self.page.goto(base_url)

    def login(self, username: str, password: str):
        """Performs login with provided username and password."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        """Returns the error message text."""
        return self.error_message.text_content()