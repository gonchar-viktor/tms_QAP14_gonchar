from base import wait_for_visible

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver

    driver.close()
    driver.quit()


def test_alert(driver):
    driver.get("https://learn.javascript.ru/task/simple-page#")
    element = wait_for_visible(driver, '//*[text()="Запустить демо"]')
    element.click()

    alert = driver.switch_to.alert

    alert.send_keys("Viktor")
    alert.accept()

    alert2 = driver.switch_to.alert



    assert alert2.text == 'Viktor'
    alert.accept()