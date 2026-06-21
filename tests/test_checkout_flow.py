import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckOutPage
pytestmark = [pytest.mark.smoke, pytest.mark.regression]

def test_user_checkout(page):
    
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckOutPage(page)

    # User logins in
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # User picks a product and checks the cart
    inventory_page.add_backpack_to_cart()
    inventory_page.shopping_cart_badge.click()

    # Checkout Process
    checkout_page.click_checkout_button()
    checkout_page.checkout("John", "Doe", "55555")
    checkout_page.click_finish_button()

    expect(checkout_page.success_message_locator).to_contain_text("Thank")