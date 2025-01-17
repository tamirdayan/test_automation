import pytest
from playwright.sync_api import Playwright
from ..pages.inventory_page import InventoryPage
from ..config import BASE_URL, VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD
from ..pages.login_page import LoginPage

EXPECTED_SUCCESSFUL_LOGIN = "success" # Placeholder for successful login
EXPECTED_LOGIN_ERROR_MISMATCH_MESSAGE = "Epic sadface: Username and password do not match any user in this service"
EXPECTED_LOGIN_ERROR_MISSING_USERNAME_MESSAGE = "Epic sadface: Username is required"
EXPECTED_LOGIN_ERROR_MISSING_PASSWORD_MESSAGE = "Epic sadface: Password is required"


class TestLogin:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        """Setup logic executed once for the test class."""
        global browser, context, page, login_page, inventory_page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL)

        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)


    def teardown_class(self):
        """Teardown logic to close the browser and context."""
        context.close()
        browser.close()

    @pytest.mark.parametrize("username, password, expected_result", [
        (VALID_USERNAME, VALID_PASSWORD, EXPECTED_SUCCESSFUL_LOGIN),
        (VALID_USERNAME, INVALID_PASSWORD, EXPECTED_LOGIN_ERROR_MISMATCH_MESSAGE),
        (INVALID_USERNAME, VALID_PASSWORD, EXPECTED_LOGIN_ERROR_MISMATCH_MESSAGE),
        (INVALID_USERNAME, INVALID_PASSWORD, EXPECTED_LOGIN_ERROR_MISMATCH_MESSAGE),
    ])
    def test_login(self, username, password, expected_result):
        """Test login functionality for various username-password combinations."""
        login_page.load(BASE_URL)
        login_page.login(username, password)

        if expected_result == EXPECTED_SUCCESSFUL_LOGIN:
            assert page.url == inventory_page.url, "Failed to login or navigate to the inventory page"
        else:
            error_message = login_page.get_error_message()
            assert error_message == expected_result, (
                f"Expected error message '{expected_result}', but got '{error_message}'"
            )

    @pytest.mark.parametrize("username, password, expected_error", [
        ("", VALID_PASSWORD, EXPECTED_LOGIN_ERROR_MISSING_USERNAME_MESSAGE),  # Missing username
        (VALID_USERNAME, "", EXPECTED_LOGIN_ERROR_MISSING_PASSWORD_MESSAGE),  # Missing password
        ("", "", EXPECTED_LOGIN_ERROR_MISSING_USERNAME_MESSAGE),  # Missing both username and password
    ])
    def test_empty_fields(self, username, password, expected_error):
        """Test login functionality for empty username and/or password."""
        login_page.load(BASE_URL)
        login_page.login(username, password)

        error_message = login_page.get_error_message()
        assert error_message == expected_error, (
            f"Expected error '{expected_error}', but got '{error_message}'"
        )