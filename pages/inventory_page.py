from ..config import BASE_URL


class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.url = f"{BASE_URL}/inventory.html"
        self.burger_menu_button = page.locator(".bm-burger-button")
        self.cart_button = page.locator("#shopping_cart_container > a")

    def open_burger_menu(self):
        """Open the navigation menu if it's not already open."""
        if self.burger_menu_button.is_visible():
            self.burger_menu_button.click()

    def click_and_verify_navigation(self, locator, expected_url, check_menu_visibility=True):
        """
        Click a navigation item and verify the URL and (optionally) the menu button visibility.
        """
        if locator == "#shopping_cart_container > a":
            # Skip opening the menu for the shopping cart button
            element = self.cart_button
        else:
            self.open_burger_menu()
            element = self.page.locator(locator)

        assert element.is_visible(), f"Navigation element '{locator}' is not visible"
        element.click()

        # Verify the URL
        current_url = self.page.url
        assert current_url == expected_url, (
            f"Expected URL '{expected_url}', but got '{current_url}'"
        )

        # Optionally verify navigation bar visibility
        if check_menu_visibility:
            assert self.burger_menu_button.is_visible(), (
                "Navigation bar is not visible on the page"
            )

    def add_item_to_cart(self, item_name: str):
        self.page.locator(f'#add-to-cart-{item_name}').click()

    def remove_item_from_cart(self, item_name: str):
        self.page.locator(f'#remove-{item_name}').click()

    def go_to_cart(self):
        self.page.locator("#shopping_cart_container > a").click()