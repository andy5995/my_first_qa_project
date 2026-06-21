# run: pytest debug/
import pytest
pytestmark = [pytest.mark.smoke, pytest.mark.regression]

def test_force_fail(page):
    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    assert page.url == "https://www.saucedemo.com/inventory.html"
    
    assert False, "FORCED FAILURE FOR DEBUGGING"