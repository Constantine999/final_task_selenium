from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")


class AddBasketToButton():
    BUTTON_ADD_BASKET_LINK = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
