from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_item_to_cart(page):
    # Setup page objects
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # Execute UI
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_backpack_to_cart()

    # Verification
    assert inventory_page.get_cart_count() == "1"

def test_locked_out_user_error(page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")
    expected_error = "Epic sadface: Sorry, this user has been locked out."
    assert login_page.get_error_message() == expected_error

    