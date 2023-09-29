from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self,driver,locator):
        self.driver = driver
        self.locator = locator
        self.driver.get('https://www.canva.com/en_gb/')
        self.locator = '[class="jV0Xtw"]>[class="_1QoxDw Qkd66A tYI0Vw' \
                       ' o4TrkA zKTE_w Qkd66A tYI0Vw lsXp_w cwOZMg zQlusQ' \
                       ' uRvRjQ"]'
    def f_driver(self):
        self.driver.find_element(By.CSS_SELECTOR, self.locator).click()