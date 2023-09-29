import pytest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from hw22.base_page import BasePage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver

    driver.close()
    driver.quit()


def test_click_sign(driver):
    driver.get('https://www.canva.com/en_gb/')
    BasePage.f_driver()


    driver.close()


