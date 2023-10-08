from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

WAIT_UNTIL = 5


def wait_for_visible(driver, locator):
    try:
        return WebDriverWait(driver, WAIT_UNTIL).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
    except WebDriverException:
        assert False, f"Element {locator} not clicable"


def wait_for_visible2(driver, locator):
    try:
        return WebDriverWait(driver, WAIT_UNTIL).until(
            EC.element_to_be_clickable((By.XPATH, locator)))
    except WebDriverException:
        assert False, f"Element {locator} not clicable"

###


def radio_button_click(driver, locator):
    try:
        return WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, locator)))
    except WebDriverException:
        assert False, f"Element {locator} not clicable"




