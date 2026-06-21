class LoginPage:
    def __init__(self, page):
        self.page = page
        self.error_message_locator = page.locator("[data-test='error']")
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_container = page.locator("[data-test='error']")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        self.error_container.wait_for(state="visible")
        return self.error_container.inner_text()