from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage
from .locators import CartPageLocators
import pytest

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
    
    # def go_to_cart(self):
    #     cart_link = self.browser.find_element(*MainPageLocators.CART_LINK)
    #     cart_link.click()

    # def should_not_be_items_in_cart(self):
    #     assert self.is_not_element_present(*CartPageLocators.ITEMS_LINK), "cart isn't empty"
    
    # def should_be_empty_cart_text(self):
    #     assert (*CartPageLocators.EMPTY_CART_TEXT).text == 'Your basket is empty.', "Cart is not empty"

# # create new class inheritance from base
# class MainPage(BasePage): 
#     # в методе, который осуществляет переход к странице логина, проинициализировать новый объект Page и вернуть его
#     def go_to_login_page(self):
#         link = self.browser.find_element(*MainPageLocators.LOGIN_LINK_INVALID)
#         link.click()
#         alert = self.browser.switch_to.alert
#         alert.accept()
#         #return LoginPage(browser=self.browser, url=self.browser.current_url) # переходы между страницами

#     def should_be_login_link(self):
#         #self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
#         assert self.is_element_present (*MainPageLocators.LOGIN_LINK), "Login link is not presented"
   