import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#parser cmnd

def pytest_addoption(parser):

    parser.addoption("--language", action="store", default="en",
                     help="Set requests language")



#function open the browserx
@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("--language")
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

