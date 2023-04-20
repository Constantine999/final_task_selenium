import time
from selenium.webdriver.common.by import By


def test_items(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    result = browser.find_elements(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    assert bool(result) == True, "Отсутствует кнопка для добавления товара в корзину"


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    time.sleep(5)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
