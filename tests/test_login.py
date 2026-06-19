from pages.login_page import LoginPage

# Happy path

def test_login_success(page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in page.url


# Sad path

def test_locked_out_user(page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")

    assert "locked out" in login_page.get_error_message().lower()


def test_invalid_user(page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("wrong_user", "secret_sauce")

    assert "do not match" in login_page.get_error_message().lower()