import time
import pytest_check as check

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


contacts_selector = (By.LINK_TEXT, "Контакты")
tensor_selector = (By.CLASS_NAME, "sbisru-Contacts__logo-tensor")
patern_strength_is_in_people_selector = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content")
images_selector_selector = (By.CSS_SELECTOR, "img.tensor_ru-About__block3-image")
region_oglavl_selector = (By.CSS_SELECTOR, "span.sbis_ru-Region-Chooser__text")
list_partners_selector = (By.ID, "city-id-2")
region_41_selector = (By.XPATH, "//span[contains(text(), '41 Камчатский край')]")


class ContactsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_sbis_go_contacts(self):
        self.browser.get("https://sbis.ru/")
        self.find(contacts_selector).click()

    def click_tensor_go_tensor(self):
        self.find(tensor_selector).click()
        self.browser.switch_to.window(self.browser.window_handles[1])

    def check_strength_is_in_people(self):
        element = self.find(patern_strength_is_in_people_selector)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        check.equal(element.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__card-title").text, "Сила в людях")

    def click_details_check_about(self):
        element = self.find(patern_strength_is_in_people_selector)
        element.find_element(By.LINK_TEXT, "Подробнее").click()
        check.is_in("https://tensor.ru/about", self.browser.current_url)

    def check_working_image(self):
        elements = self.find_els(images_selector_selector)
        fl = "0"
        for i in range(elements.__len__() - 1):
            self.browser.execute_script("arguments[0].scrollIntoView(true);", elements[i])
            if elements[i].get_attribute("width") != elements[i + 1].get_attribute("width") or elements[i].get_attribute("height") != elements[i + 1].get_attribute("height"):
                fl = "1"
        check.equal(fl, "0")

    def check_my_regoin(self):
        check.equal(self.find(region_oglavl_selector).text, "Костромская обл.")
        check.equal(self.find(list_partners_selector).text, "Кострома")

    def chenge_region(self):
        self.find(region_oglavl_selector).click()
        time.sleep(2)
        self.find(region_41_selector).click()

    def check_41_regoin(self):
        time.sleep(2)
        check.equal(self.find(region_oglavl_selector).text, "Камчатский край")
        check.not_equal(self.find(list_partners_selector).text, "Кострома")
        check.is_in("Камчатский край", self.browser.title)
        check.is_in("41-kamchatskij-kraj", self.browser.current_url)

