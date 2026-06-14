import pytest
from pages.login_page import LoginPage

# Tells python to repeat the test with different data
@pytest.mark.parametrize(
    "username, password, error_msg",
    [
        ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
        ("wrong_user", "secret_sauce", "Epic sadface: Username and password do not match any user in this service")
    ]
)

# Tests actual error message against whats expected
def test_login_failures(page, username, password, error_msg):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login(username, password)

    assert login_page.get_error_message() == error_msg