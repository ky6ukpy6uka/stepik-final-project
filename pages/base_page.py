
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
