import time
import os
import pytest_check as check

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


donwload_selector = (By.LINK_TEXT, "Скачать локальные версии")
plugin_button_selector = (By.XPATH, "//div[contains(text(), 'СБИС Плагин')]")
web_installer_selector = (By.PARTIAL_LINK_TEXT, "Скачать (Exe")
filepath = f"{os.getcwd()}\\tests\\sbisplugin-setup-web.exe"


class DownloadPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_sbis_go_download(self):
        self.browser.get("https://sbis.ru/")
        element = self.find(donwload_selector)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def download_sbis_plugin(self):
        if os.path.exists(filepath):
            os.remove(filepath)
        time.sleep(1)
        Hover = ActionChains(self.browser).move_to_element(self.find(plugin_button_selector))
        Hover.click().perform()
        self.find(web_installer_selector).click()
        while not os.path.exists(filepath):
            time.sleep(1)

    def check_file_size(self):
        file_size = os.path.getsize(filepath)
        file_size_on_site = float(self.find(web_installer_selector).text[12:17])
        check.equal(round(file_size / 1024 / 1024, 2), file_size_on_site)
