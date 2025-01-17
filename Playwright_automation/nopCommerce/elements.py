import allure

class Elements:
    def __init__(self, page):
        self.page = page
        self.top_menu_electronic = page.locator("a[href*='electronics']")
        self.camera_and_photo = page.locator("a[href*='camera-photo']")
        self.item_grid = page.locator("h2[class='product-title']>a")

    @allure.step("Click \"Camera & Photo\" Button")
    def navigate_to_camera_and_photo_page(self):
        self.page.mouse.move(self.top_menu_electronic.first.bounding_box()['x'],
                             self.top_menu_electronic.first.bounding_box()['y'])
        self.camera_and_photo.first.click()

    @allure.step("Click \"Camera & Photo\" Button")
    def sort_by_price_low_to_high(self):
        sort_by_selector = "[id='products-orderby']"
        self.page.select_option(sort_by_selector, value="10")

    @allure.step("verify_num_of_items(")
    def verify_num_of_items(self):
        return self.item_grid.count()