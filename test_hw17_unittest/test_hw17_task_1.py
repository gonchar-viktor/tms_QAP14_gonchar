#
# Написать модульные тесты для 3, 4 задания из HW6 используя unittest
import unittest


def func_for_hw17_task_1():

    # A function of 6 hw for hw17 unit testing
    with open("file_for_hw17_task_11.txt", "r") as f:
        b = list(map(float, f.readline().split()))

    def float_to_int():
        global c
        c = []
        d = 0
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
        with open("file_for_hw17_task_11.txt", "w") as file:
            file.write(str(c))

    # enter values - 1.1 2.2 3.3 4.4 5.5
    # getting values - 1.21 4.84 10.89 19.36 30.25
    float_to_int()


# func_for_hw17_task_1()


def func_assert(input_values):
    if all(isinstance(i, float) for i in input_values):
        # func_for_hw17_task_1()
        with open("file_for_hw17_task_11.txt", "r") as file:
            res = file.read()
            return res
    else:
        return 'Error'


class TestList(unittest.TestCase):
    def test_check_float_numbers(self):
        self.assertEqual(func_assert([1.1, 2.2, 3.3, 4.4, 5.5]), [
            1.21, 4.84, 10.89, 19.36, 30.25])
        # no successfully


    def test_check_empty_data(self):
        self.assertEqual(func_assert([None]), 'Error')

    def test_check_str(self):
        self.assertEqual(func_assert(['bim_bim']), 'Error')

    def test_check_special_characters(self):
        self.assertEqual(func_assert([']', '%', '1', '-']), 'Error')


if __name__ == '__main__':
    unittest.main()

















# def func_assert22(input_values):
#     if all(isinstance(i, float) for i in input_values):
#         res = []
#         for i in input_values:
#             i = i ** 2
#             i = round(i, 2)
#             res.append(i)
#         return res
#     else:
#         return 'Error'
#
#
# class TestList(unittest.TestCase):
#     def test_check_float_numbers(self):
#         self.assertEqual(func_assert22([1.1, 2.2, 3.3, 4.4, 5.5]), [
#             1.21, 4.84, 10.89, 19.36, 30.25])
#         """successfully"""
#
#     def test_check_empty_data(self):
#         self.assertEqual(func_assert22([None]), 'Error')
#         """successfully"""
#
#     def test_check_str(self):
#         self.assertEqual(func_assert22(['bim_bim']), 'Error')
#         """successfully"""
#
#     def test_check_special_characters(self):
#         self.assertEqual(func_assert22([']', '%', '1', '-']), 'Error')
#         """successfully"""