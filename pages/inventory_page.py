class InventoryPage:
    def __init__ (self, page):
        self.page = page
        self.add_backpack_button = page.locator("#add-to-cart-sauce-labs-backpack")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")

    def add_backpack_to_cart(self):
        self.add_backpack_button.click()

    def get_cart_count(self):
        return self.shopping_cart_badge.text_content()