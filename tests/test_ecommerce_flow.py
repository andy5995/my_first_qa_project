import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
pytestmark = [pytest.mark.smoke, pytest.mark.regression]

def test_add_item_to_cart(page):
    
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()

    expect(inventory_page.shopping_cart_badge).to_have_text("1")

def test_locked_out_user_error(page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")

    expected_error = "Epic sadface: Sorry, this user has been locked out."
    
    expect(login_page.error_message_locator).to_have_text(expected_error, ignore_case=True)
