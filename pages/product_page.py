import math

from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import AddBasketToButton


class ProductPage(BasePage):

    def solve_quiz_and_get_code(self):
        self.browser.find_element(*AddBasketToButton.BUTTON_ADD_BASKET_LINK).click()
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
