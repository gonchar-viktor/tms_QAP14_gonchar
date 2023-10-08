# Написать модульные тесты для 3, 4 задания из HW6 используя unittest
import unittest


# 4 Даны два файла произвольного типа. Поменять местами их
# содержимое. Файлы должны быть бинарного типа


def func4():
    """
    Two files of any type are given. Swap their contents
    """
    # код старый
    lst1 = 1, 2, 3, 4, 5  # в первый сперва записываются цифры
    lst2 = "a", "b", "c", "d"  # во второй сперва записываются буквы

    with open("file_for_task_2_hw17_bin_1.bin", "wb") as file1:
        for i in lst1:
            i = str(i)
            p = i.encode()
            file1.write(p)

    with open("file_for_task_2_hw17_bin_2.bin", "wb") as file2:
        for u in lst2:
            u = str(u)
            k = u.encode()
            file2.write(k)

    # чтобы проверить работу можно сделать всё, что ниже этой записи
    # комментарием

    with open("file_for_task_2_hw17_bin_1.bin", "rb") as rep_1:
        bb = rep_1.read()

    with open("file_for_task_2_hw17_bin_2.bin", "rb") as rep_2:
        nn = rep_2.read()

    with open("file_for_task_2_hw17_bin_1.bin", "wb") as rep_1:
        rep_1.write(nn)

    with open("file_for_task_2_hw17_bin_2.bin", "wb") as rep_2:
        rep_2.write(bb)


func4()


class TestForFunc4(unittest.TestCase):
    """
    A class for a set of unit tests
    Класс для набора модульных тестов
    """
    func4()

    def __init__(self, content1, content2):
        super().__init__()
        self.content1 = content1
        self.content2 = content2

    with open('file_for_task_2_hw17_bin_1.bin', "rb") as f1:
        content1 = f1.read()

    with open('file_for_task_2_hw17_bin_2.bin', "rb") as f2:
        content2 = f2.read()

    def test_check_bin_file_replace(self):
        """
        Checking that the files have been replaced
        Проверяю, что файлы заменились
        """

        # successfully

        self.assertEqual(self.content1, b'abcd')
        self.assertEqual(self.content2, b'12345')

    def test_check_that_the_files_exist(self):
        """
        Checking that the files exist
        Проверяю, что файлы существуют
        """

        # successfully
        self.assertTrue('file_for_task_2_hw17_bin_1.bin')
        self.assertTrue('file_for_task_2_hw17_bin_2.bin')

    def test_check_that_the_files_are_not_empty(self):
        """
        Checking that the files are not empty
        Проверяю, что файлы не пустые
        """

        # successfully
        self.assertNotEqual(len(self.content1), 0)
        self.assertNotEqual(len(self.content2), 0)
        # or
        self.assertIsNotNone('file_for_task_2_hw17_bin_1.bin')
        self.assertIsNotNone('file_for_task_2_hw17_bin_2.bin')


if __name__ == '__main__':
    unittest.main()
