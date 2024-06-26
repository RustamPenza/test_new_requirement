from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        email_input.send_keys(email)
        password1_input = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD1)
        password1_input.send_keys(password)
        password2_input = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD2)
        password2_input.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url_check = self.url
        assert "login" in url_check, "Url does not contain 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login from is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
