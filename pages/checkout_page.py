class CheckOutPage:
    def __init__ (self, page):
        self.page = page
        self.success_message_locator = page.locator("[data-test='complete-header']")
        self.checkout_button = page.locator("#checkout")
        self.firstname_input = page.locator("#first-name")
        self.lastname_input = page.locator("#last-name")
        self.zipcode_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.success_message = page.locator(".complete-header")
    
    def click_checkout_button(self):
        self.checkout_button.click()
    
    def checkout(self, firstname, lastname, zipcode):
        self.firstname_input.fill(firstname)
        self.lastname_input.fill(lastname)
        self.zipcode_input.fill(zipcode)
        self.continue_button.click()

    def click_continue_button(self):
        self.continue_button.click()

    def click_finish_button(self):
        self.finish_button.click()

    def get_success_message(self):
        return self.success_message.text_content()