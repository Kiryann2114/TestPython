from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        WebDriverWait(self.browser, 15).until(ec.presence_of_element_located(args))
        return self.browser.find_element(*args)

    def find_els(self, args):
        WebDriverWait(self.browser, 15).until(ec.presence_of_element_located(args))
        return self.browser.find_elements(*args)
