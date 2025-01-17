import pytest
import allure
from playwright.sync_api import Playwright


class Login_Page:
    def __init__(self, page):
        self.page = page
        self.username = self.page.locator("input[name='username2']")
        self.password = self.page.locator("input[name='password2']")
        self.submit_button = self.page.locator("input[id='submit']")

    @allure.step("Sign in")
    def sign_in(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.submit_button.click()
