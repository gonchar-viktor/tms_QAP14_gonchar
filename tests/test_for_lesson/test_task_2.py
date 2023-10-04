#
import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from tests.basic import radio_button_click


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver

    driver.close()
    driver.quit()


def test_scroll(driver):
    """
    scroll
    """
    driver.get("https://demoqa.com/elements")
    scroll_height = 1000

    while True:
        # scroll
        driver.execute_script(f"window.scrollTo(0, {scroll_height});")
        time.sleep(2)
        scroll_height += 1000

        if scroll_height >= driver.execute_script(
                "return document.body.scrollHeight;"):
            break



    driver.close()
    driver.quit()


def test_radio_button(driver):
    driver.get("https://demoqa.com/radio-button")
    radio_button_click(driver, "yesRadio")

    driver.close()
    driver.quit()








    #radio_button.click()
    # [id = "yesRadio"]
    # if radio_button.is_selected():
    #     print("selected yes!")
    # else:
    #     print("couldn't choose")






# def test_fg():
#     # Создание экземпляра веб-драйвера
#     driver = webdriver.Chrome()
#
#     # Открытие веб-страницы
#     driver.get("https://demoqa.com/radio-button")
#
#     # Нахождение элемента радио-кнопки по ее атрибуту id
#     radio_button = driver.find_element(By.ID, 'yesRadio')
#
#     # Проверка, выбрана ли радио-кнопка
#     if not radio_button.is_selected():
#         # Клик по радио-кнопке для ее выбора
#         radio_button.click()
#
#     # Закрытие веб-драйвера
#     driver.quit()


##
#     def scroll_to_element(self, xpath):
#         element = self.get_element(xpath)
#         self.driver.execute_script('arguments[0].scrollIntoView();', element)
#
# WebElement_element = driver.findElement(By.ID, "my-id")