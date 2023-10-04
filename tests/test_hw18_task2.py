# Написать модульные тесты для 3, 4 задания из HW6 использую pytest
#
# 1 Параметризация
#
# 2 Чтение информации из файлов поместить в фикстуру
#
# 3 Использовать mark для разного запуска тестов
import string

import pytest


FILE_BIN1 = 'C:/Users/Repear-PC/PycharmProjects/tms_qap14_gonchar/tests/' \
            'hw18_file_for_task2_1.bin'
FILE_BIN2 = 'C:/Users/Repear-PC/PycharmProjects/tms_qap14_gonchar/tests/' \
            'hw18_file_for_task2_2.bin'


def func_for_hw18():
    """
    Two files of any type are given. Swap their contents
    """

    with open(FILE_BIN1, "rb") as rep_1:
        bb = rep_1.read()

    with open(FILE_BIN2, "rb") as rep_2:
        nn = rep_2.read()

    with open(FILE_BIN1, "wb") as rep_1:
        rep_1.write(nn)

    with open(FILE_BIN2, "wb") as rep_2:
        rep_2.write(bb)


def test_data_verification(reading_information_bin):
    """
    Checking that the data from the files is equal to the expected
    """
    param_1_before = reading_information_bin[0].decode()
    param_2_before = reading_information_bin[1].decode()

    assert param_1_before == '12345' and param_2_before == 'abcd'


def test_type_data(reading_information_bin):
    """
    Checking that the data in the files is written in bytes
    """
    param_1_before = reading_information_bin[0]
    param_2_before = reading_information_bin[1]

    assert type(param_1_before) and type(param_2_before) is bytes


@pytest.mark.swapp
def test_data_swapped(reading_information_bin):
    """
    Checking that the data from the files have been swapped
    """
    param_1_before, param_2_before, param_1_after, param_2_after = \
        reading_information_bin[0], reading_information_bin[1], \
        reading_information_bin[2], reading_information_bin[3]

    assert param_1_before == param_2_after and param_2_before == param_1_after


@pytest.mark.empty
def test_not_empty(reading_information_bin):
    """
    Checking that the files are not empty
    """
    param_1_before = reading_information_bin[0]
    param_2_before = reading_information_bin[1]

    assert param_1_before and param_2_before is not None
    assert len(param_1_before) and len(param_2_before) != 0


@pytest.mark.special
def test_check_special_characters(reading_information_bin):
    """
    Checking for special characters
    """
    param_1_before = reading_information_bin[0]
    param_2_before = reading_information_bin[1]

    if any(string.punctuation) in (
            i for i in param_1_before and param_2_before):
        val_bool = False
    else:
        val_bool = True

    assert val_bool is True


@pytest.mark.parametrize('data', ["\t1.str", '\t2.float', '\t3.set'])
def test_check_a_list_to_work_with(data):
    """
    Не придумал как использовать параметризацию в этом задании, поэтому просто
    сделаю вывод нескольких входных параметров
    """
    print(data)
