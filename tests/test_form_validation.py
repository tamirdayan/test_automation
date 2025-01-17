import pytest
from playwright.sync_api import Playwright
from ..pages.login_page import LoginPage
from ..pages.inventory_page import InventoryPage
from ..pages.cart_page import CartPage
from ..pages.checkout_step_one_page import CheckoutStepOnePage
from ..pages.checkout_step_two_page import CheckoutStepTwoPage
from ..pages.checkout_complete_page import CheckoutCompletePage
from ..config import VALID_USERNAME, VALID_PASSWORD, BASE_URL

# test data
# Error Messages
EXPECTED_ERROR_MISSING_FIRST_NAME = "Error: First Name is required"
EXPECTED_ERROR_MISSING_LAST_NAME = "Error: Last Name is required"
EXPECTED_ERROR_MISSING_POSTAL_CODE = "Error: Postal Code is required"

# Test Data
VALID_FIRST_NAME = "Lady"
VALID_LAST_NAME = "Gaga"
VALID_POSTAL_CODE = "12345"

MISSING_FIRST_NAME = ""
MISSING_LAST_NAME = ""
MISSING_POSTAL_CODE = ""
# TODO: currently the website supports only error validation of missing fields. Add invalid values when implemented.


class TestFormValidation:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        """Setup browser, context, and page for the tests."""
        global browser, context, page, login_page, inventory_page, cart_page, checkout_step_one_page, checkout_step_two_page, checkout_complete_page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        # Initialize page objects
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)
        cart_page = CartPage(page)
        checkout_step_one_page = CheckoutStepOnePage(page)
        checkout_step_two_page = CheckoutStepTwoPage(page)
        checkout_complete_page = CheckoutCompletePage(page)

        # Perform login
        login_page.load(BASE_URL)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        assert page.url == inventory_page.url, "Failed to login or navigate to the inventory page"

    def teardown_class(self):
        """Close browser and context after tests."""
        context.close()
        browser.close()

    @pytest.mark.parametrize("first_name, last_name, zip_code, expected_error", [
        (VALID_FIRST_NAME, VALID_LAST_NAME, VALID_POSTAL_CODE, None),
        (MISSING_FIRST_NAME, VALID_LAST_NAME, VALID_POSTAL_CODE, EXPECTED_ERROR_MISSING_FIRST_NAME),
        (VALID_FIRST_NAME, MISSING_LAST_NAME, VALID_POSTAL_CODE, EXPECTED_ERROR_MISSING_LAST_NAME),
        (VALID_FIRST_NAME, VALID_LAST_NAME, MISSING_POSTAL_CODE, EXPECTED_ERROR_MISSING_POSTAL_CODE),
        (MISSING_FIRST_NAME, MISSING_LAST_NAME, VALID_POSTAL_CODE, EXPECTED_ERROR_MISSING_FIRST_NAME),
        (MISSING_FIRST_NAME, VALID_LAST_NAME, MISSING_POSTAL_CODE, EXPECTED_ERROR_MISSING_FIRST_NAME),
        (VALID_FIRST_NAME, MISSING_LAST_NAME, MISSING_POSTAL_CODE, EXPECTED_ERROR_MISSING_LAST_NAME),
        (MISSING_FIRST_NAME, MISSING_LAST_NAME, MISSING_POSTAL_CODE, EXPECTED_ERROR_MISSING_FIRST_NAME),
    ])
    def test_form_validation(self, first_name, last_name, zip_code, expected_error):
        """Test form validation with various input combinations."""
        # Navigate to the cart and proceed to checkout
        inventory_page.add_item_to_cart(item_name="sauce-labs-bike-light")
        inventory_page.go_to_cart()
        cart_page.click_checkout()

        # Fill the checkout form
        checkout_step_one_page.fill_form(first_name, last_name, zip_code)
        checkout_step_one_page.click_continue()

        if expected_error:
            error_message = checkout_step_one_page.get_error_message()
            assert error_message == expected_error, (
                f"Expected error message '{expected_error}', but got '{error_message}'"
            )
            page.goto(inventory_page.url)
            inventory_page.remove_item_from_cart(item_name="sauce-labs-bike-light")
        else:
            if not first_name or not last_name or not zip_code:
                pytest.fail("Validation missing for empty or invalid input fields")

            # Proceed to the next step
            assert page.url == checkout_step_two_page.url, (
                f"Expected URL '{checkout_step_two_page.url}', but got '{page.url}'"
            )

            # Complete the checkout process
            checkout_step_two_page.click_finish()
            assert page.url == checkout_complete_page.url, (
                f"Expected URL '{checkout_complete_page.url}', but got '{page.url}'"
            )

            actual_message = checkout_complete_page.get_success_message()
            assert actual_message == checkout_complete_page.expected_message, \
                f"Expected message '{checkout_complete_page.expected_message}', but got '{actual_message}'"

            page.goto(inventory_page.url)