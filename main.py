# from selenium import webdriver
import selenium.webdriver
import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


@pytest.fixture()
def driver ():
    browser = webdriver.Chrome()
    browser.maximize_window()
    return browser

def open_page (browser):
    browser.get ('https://demoblaze.com/index.html')

def find_element_by_path (browser, path):
    samsung_card : WebElement = browser.find_element (By.XPATH, "//*[@id='tbodyid']/div[1]/div/div/h4/a")
    samsung_card.click()







