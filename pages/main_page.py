from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage


# create new class inheritance from base
class MainPage(BasePage): 
    # в методе, который осуществляет переход к странице логина, проинициализировать новый объект Page и вернуть его
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK_INVALID)
        link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url) 

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        #self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        assert self.is_element_present (*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    