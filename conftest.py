from selenium import webdriver
import pytest
import os


@pytest.fixture()
def browser():
    Options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": f"{os.getcwd()}\\tests",
        "safebrowsing.enabled": True
    }
    Options.add_experimental_option("prefs", prefs)
    chrome_browser = webdriver.Chrome(options=Options)
    chrome_browser.implicitly_wait(10)
    return chrome_browser
