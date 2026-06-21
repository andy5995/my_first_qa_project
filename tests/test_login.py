import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
pytestmark = [pytest.mark.smoke, pytest.mark.regression]

# Happy path
def test_login_success(page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

# Sad path
def test_locked_out_user(page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")

    expect(login_page.error_message_locator).to_contain_text("locked out", ignore_case=True)

# Validate error message
def test_invalid_user(page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("wrong_user", "secret_sauce")

    expect(login_page.error_message_locator).to_contain_text("do not match", ignore_case=True)