# +
from tests.test_for_lesson.basic import wait_for_visible, wait_for_visible2
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# по id = #overlay
# по class = .modal-dialog
# по любому атрибуту = [class='modal-dialog'] [type='button']
# более сложные локаторы = li[class="promo-menu__item item"] a[class=
# "item__title"], li.promo-menu__item.item
# по частичному совпадению = div[class*='info']
#
#
# по относительному тегу = //select
# по тегу в теге = //select/option
# по любому тегу = //*/option
# по атрибуту = //*[@name="fromPort"], //select[@name="fromPort"],
# //*[@name='tr_name']/td
# по тексту = //*[text()='Economy class ']
# по частичному совпадению = //*[contains(text(),'class')]
#  итерация по элементам = (//*[contains(text(),'class')])[3]
# абсолютный путь = /html/head....
# по атрибуту = //input[@type]


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver

    driver.close()
    driver.quit()


def test_1_css(driver):
    driver.get("https://www.bbc.com/news")
    wait_for_visible(driver, '[class="gs-c-promo-image gs-u-mb gs-u-mb0@xs '
                             'gs-u-float-right@m gel-2/3@m gs-u-display-block'
                             '"]>[class="gs-o-media-island"]')


def test_1_xpath(driver):
    driver.get("https://www.bbc.com/news")
    wait_for_visible2(driver, '(//div[@class="gs-o-media-island"])[1]')


def test_2_css(driver):
    driver.get("https://www.bbc.com/news")
    wait_for_visible(driver, '[viewBox="0 0 112 32"]')


def test_2_xpath(driver):
    driver.get("https://www.bbc.com/news")
    wait_for_visible2(driver, '//*[@viewBox="0 0 112 32"]')


def test_3_css(driver):
    driver.get("https://www.bbc.com/news")
    wait_for_visible(driver, 'header>div>div>nav>ul>li>[href='
                             '"https://www.bbc.com/sport"]')


def test_3_xpath(driver):
    driver.get("https://www.bbc.com/news")
    wait_for_visible2(driver, '//header//div//div//nav//ul//li//a[@href='
                              '"https://www.bbc.com/sport"]')



def test_4_css(driver):
    driver.get("https://www.bbc.com/news")
    wait_for_visible(driver, 'header>div>div>div>nav>ul>li>[href="/news"]')
    wait_for_visible(driver, 'header>div>div>div>nav>ul>li>[href="/news/scienc'
                             'e-environment-56837908"]')
    wait_for_visible(driver, 'header>div>div>div>nav>ul>li>'
                             '[href="/news/world"]')
    wait_for_visible(driver, 'header>div>div>div>'
                             'nav>ul>li>[href="/news/business"]')
    wait_for_visible(driver, 'header>div>div>div>nav>ul>li>[href="/news/'
                             'science_and_environment"]')
    wait_for_visible(driver, 'header>div>div>div>nav>ul>li>[href="/news/'
                             'health"]')
    wait_for_visible(driver, 'header>div>div>div>nav>ul>li>[href="/n'
                             'ews/in_pictures"]')


def test_4_xpath(driver):
    driver.get("https://www.bbc.com/news")
    wait_for_visible2(driver, '(//a[@href="/news"])[2]')
    wait_for_visible2(driver, '(//a[@href="/news/science-'
                              'environment-56837908"])[1]')
    wait_for_visible2(driver, '(//a[@href="/news/world"])[1]')
    wait_for_visible2(driver, '(//a[@href="/news/business"])[1]')
    wait_for_visible2(driver, '(//a[@href="/news/science_and_environment"]'
                              ')[1]')
    wait_for_visible2(driver, '(//a[@href="/news/health"])[1]')
    wait_for_visible2(driver, '(//a[@href="/news/in_pictures"])[1]')
