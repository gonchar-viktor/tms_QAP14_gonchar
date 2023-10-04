# Для хранения часто употребимых фикстур и хранения глобальных настроек
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    # открытие и закрытие хром браузера

    print("\nstart browser for test..")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    print("\nquit browser..")

    driver.close()
    driver.quit()


##
@pytest.fixture(scope='function')
def browser(request):
    # другой метод открытия и закрытия хром браузера, с выводом сообщений

    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser

    def fin():
        print("\nquit browser..")

    browser.quit()
    request.addfinalizer(fin)

#####


FILE = 'C:/Users/Repear-PC/PycharmProjects/tms_qap14_gonchar/tests/' \
       'hw18_file_for_task1.txt'


@pytest.fixture(scope='function')
def reading_information():
    """
    Фикстура возвращает кортеж из которого можно по индексу взять элемент
    полученный до и после выполнения функции
    """
    # for hw18
    with open(FILE, "w+") as f:
        f.write('1.1 2.2 3.3 4.4 5.5')

    with open(FILE, "r") as file:
        result_before = list(map(float, file.readline().split()))

        from tests.test_hw18_task1 import func_for_hw17_task_1
        func_for_hw17_task_1()

    with open(FILE, "r") as file2:
        result_after = list(map(float, file2.readline().split()))

    os.remove(FILE)

    return result_before, result_after


#####


FILE_BIN1 = 'C:/Users/Repear-PC/PycharmProjects/tms_qap14_gonchar/tests/' \
            'hw18_file_for_task2_1.bin'
FILE_BIN2 = 'C:/Users/Repear-PC/PycharmProjects/tms_qap14_gonchar/tests/' \
            'hw18_file_for_task2_2.bin'


@pytest.fixture(scope='function')
def reading_information_bin():
    # for hw18

    lst1 = 1, 2, 3, 4, 5  # в первый сперва записываются цифры
    lst2 = "a", "b", "c", "d"  # во второй сперва записываются буквы

    with open(FILE_BIN1, "wb+") as file1:
        for i in lst1:
            file1.write(str(i).encode())

            # i = str(i)
            # p = i.encode()
            # file1.write(p)

    with open(FILE_BIN2, "wb+") as file2:
        for u in lst2:
            file2.write(str(u).encode())

            # u = str(u)
            # k = u.encode()
            # file2.write(k)

    with open(FILE_BIN1, "rb") as f:
        param_1 = f.read()

    with open(FILE_BIN2, "rb") as f2:
        param_2 = f2.read()

    from tests.test_hw18_task2 import func_for_hw18
    func_for_hw18()

    with open(FILE_BIN1, "rb") as f:
        param_3 = f.read()

    with open(FILE_BIN2, "rb") as f2:
        param_4 = f2.read()

    os.remove(FILE_BIN1), os.remove(FILE_BIN2)
    return param_1, param_2, param_3, param_4
