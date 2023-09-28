# Написать модульные тесты для 3, 4 задания из HW6 используя unittest
import unittest
import string


def func_for_hw17_task_1():
    """
    The code is old
    """

    # A function of 6 hw for hw17 unit testing
    with open("file_for_hw17_task_1.txt", "r") as f:
        b = list(map(float, f.readline().split()))

    def float_to_int():
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
        with open("file_for_hw17_task_1.txt", "w") as file:
            file.write(str(c))

    # enter values - 1.1 2.2 3.3 4.4 5.5
    # getting values - 1.21 4.84 10.89 19.36 30.25
    float_to_int()


class TestList(unittest.TestCase):
    """
    Given a file with real numbers - 1.1 2.2 3.3 4.4 5.5
    """

    def test_check_squaring_numbers(self):
        """
        Checking for squaring numbers
        """
        with open("file_for_hw17_task_1.txt", "r") as file:
            before_result = list(map(float, file.readline().split()))

        func_for_hw17_task_1()
        with open("file_for_hw17_task_1.txt", "r") as file:
            result = list(map(float, file.readline().split()))

            expected_result = list(round((i ** 2), 2) for i in before_result)

        # successfully
        self.assertEqual(result, expected_result)

    def test_check_empty_data(self):
        """
        Check that the list is not empty
        """
        with open("file_for_hw17_task_1.txt", "r") as file:
            result = list(map(float, file.readline().split()))

        # successfully
        self.assertNotEqual(len(result), 0)

    def test_check_a_list_to_work_with(self):
        """
        Checking so that as a result we get a list to work with
        """
        with open("file_for_hw17_task_1.txt", "r") as file:
            result = list(map(float, file.readline().split()))

        # successfully
        self.assertEqual(type(result), list)

    def test_check_special_characters(self):
        """
        f
        """
        with open("file_for_hw17_task_1.txt", "r") as file:
            result = list(map(float, file.readline().split()))
        if any(string.punctuation) in (i for i in result):
            val_bool = False
        else:
            val_bool = True

        self.assertTrue(val_bool)


if __name__ == '__main__':
    unittest.main()
