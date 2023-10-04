# Написать модульные тесты для 3, 4 задания из HW6 использую pytest
#
# 1 Параметризация
#
# 2 Чтение информации из файлов поместить в фикстуру
#
# 3 Использовать mark для разного запуска тестов

import string
import pytest


FILE = 'C:/Users/Repear-PC/PycharmProjects/tms_qap14_gonchar/tests/' \
       'hw18_file_for_task1.txt'


def func_for_hw17_task_1():

    with open(FILE, "r") as f:
        b = list(map(float, f.readline().split()))

    def float_to_int():
        c = []
        for i in b:
            d = i ** 2
            d = round(d, 2)
            c.append(d)

        print(c)
        c = str(c)
        c = c.replace("[", "")
        c = c.replace("]", "")
        c = c.replace(",", "")

        print(c)
        with open(FILE, "w") as file:
            file.write(str(c))

    # enter values - 1.1 2.2 3.3 4.4 5.5
    float_to_int()


#
# pytest -s -v -m squaring tests/test_task_1_hw18
#


@pytest.mark.squaring
def test_check_squaring_numbers(reading_information):
    """
    Checking for squaring numbers
    Проверяю на возведение чисел в квадрат;
    """
    param_before = reading_information[0]

    param_before_squaring_numbers = list(
        round((i ** 2), 2) for i in param_before)

    param_after = reading_information[1]

    assert param_after == param_before_squaring_numbers


#
# pytest -s -v -m empty tests/test_task_1_hw18
#

@pytest.mark.empty
def test_check_empty_data(reading_information):
    """
    Check that the list is not empty
    Проверяю, что список не пуст
    """
    param = reading_information
    assert (param is not None) and (len(param) != 0)


#
# pytest -s -v -m special tests/test_task_1_hw18
#

@pytest.mark.special
def test_check_special_characters(reading_information):
    """
    Checking for special characters
    Проверяю на наличие спецсимволов
    """
    param = reading_information
    if any(string.punctuation) in (i for i in param):
        val_bool = False
    else:
        val_bool = True

    assert val_bool is True


#
# pytest -s -v -m type tests/test_task_1_hw18
#

@pytest.mark.type
def test_check_a_list_to_work_with(reading_information):
    """
    Checking so that as a result we get a list to work with
    Проверяю, чтобы в результате я получил кортеж для работы
    """
    param = reading_information
    assert type(param) is tuple


@pytest.mark.skip
def test_skip(reading_information):
    print('...')


@pytest.mark.xfail(reason="fixing this bug right now")
def test_2(reading_information):
    print('...')


#
# pytest -s -v -m parametrize tests/test_task_1_hw18
#

@pytest.mark.parametrize('data', ["\t1.str", '\t2.float', '\t3.set'])
def test_check_a_list_to_work_with(data):
    """
    Не придумал как использовать параметризацию в этом задании, поэтому просто
    сделаю вывод нескольких входных параметров
    """
    print(data)
