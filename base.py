from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

WAIT_UNTIL = 5
def wait_for_visible(driver, locator):
    try:
        return WebDriverWait(driver, WAIT_UNTIL).until(EC.element_to_be_clickable((By.XPATH, locator)))
    except WebDriverException:
        assert False, f"Element {locator} not clicable"


def add_cookie(driver, name, value):
    driver.add_cookie({'name': name, 'value': value})
    driver.refresh()


def delete_cookies(driver):
    driver.delete_cookies()
    driver.refresh()


def assert_text_in_element(driver, locator, expected_result):
    element = driver.find_element(By.XPATH, locator)
    assert element.text == expected_result, "Text not the same"


def assert_value_in_element_attribute(driver, locator, attribute, expected_result):
    element = driver.find_element(By.XPATH, locator)
    value = element.get_attribute(attribute)
    assert value == expected_result, "Attribute value not the same"


def hard_click(driver, locator):
    element = driver.find_element(By.XPATH, locator)
    driver.execute_script("arguments[0].click();", element)


def fill(driver, locator, text):
    element = driver.find_element(By.XPATH, locator)
    element.clear()
    element.sendKeys(text)

