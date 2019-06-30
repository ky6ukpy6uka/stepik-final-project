from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators(object):
    # добавить селекторы к формам регистрации и логина
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators(object):
    CART_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CART_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) div strong")
    PAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info div p:nth-child(1) strong")

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
