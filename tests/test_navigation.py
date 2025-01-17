from playwright.sync_api import Playwright
import pytest
from ..config import BASE_URL, VALID_USERNAME, VALID_PASSWORD
from ..pages.login_page import LoginPage
from ..pages.inventory_page import InventoryPage

class Test_Navigation:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page, inventory_page
        browser = playwright.chromium.launch(headless=False, channel="chrome")
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL)

        login_page = LoginPage(page)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        assert page.url == f"{BASE_URL}/inventory.html", "Failed to login or navigate to the inventory page"

        inventory_page = InventoryPage(page)

    def teardown_class(self):
        context.close()
        browser.close()

    @pytest.mark.parametrize(
        "locator, expected_url, check_menu_visibility",
        [
            ("#shopping_cart_container > a", f"{BASE_URL}/cart.html", True),
            ("[data-test='inventory-sidebar-link']", f"{BASE_URL}/inventory.html", True),
            ("[data-test='about-sidebar-link']", "https://saucelabs.com/", False),
            ("[data-test='reset-sidebar-link']", f"{BASE_URL}/inventory.html", True),
            ("[data-test='logout-sidebar-link']", f"{BASE_URL}/", False),
            # Note: for performance purposes, the login will occur only at the test setup.
            # Therefore, add new test cases before the logout test, otherwise perform login.
        ]
    )
    def test_navigation(self, locator, expected_url, check_menu_visibility):
        inventory_page.click_and_verify_navigation(
            locator=locator,
            expected_url=expected_url,
            check_menu_visibility=check_menu_visibility
        )
        # Return to inventory page after each test
        page.goto(f"{BASE_URL}/inventory.html")