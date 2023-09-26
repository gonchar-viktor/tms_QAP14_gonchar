#

from tests.basic import wait_for_visible


def test_1(driver):
    driver.get("https://thedemosite.co.uk/login.php")

    wait_for_visible(driver, "strong [href=\"getyourowndbonline.php\"]")


# pip install webdriver-manager
