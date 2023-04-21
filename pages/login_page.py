from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/ru/accounts/login/", "Url does not match "

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM_LINK), "Login form link is not presented"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM_LINK), "Register form link is not presented"
