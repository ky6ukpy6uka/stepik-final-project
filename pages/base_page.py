from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Первым делом добавим конструктор — метод, который вызывается, когда мы создаем объект. 
# Конструктор объявляется ключевым словом __init__. В него в качестве параметров мы передаем 
# экземпляр драйвера и url адрес. 
# Внутри конструктора сохраняем эти данные как аттрибуты нашего класса. 

from selenium.common.exceptions import NoSuchElementException   #(имя исключения)

class BasePage(object):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # для решения задачи в алерте
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

# Он должен открывать нужную страницу в браузере, используя метод get().
    def open(self):
        self.browser.get(self.url)

# Проверка наличия элемента используя исключения
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
# добавить в метод выше из файла локаторс вместо how what