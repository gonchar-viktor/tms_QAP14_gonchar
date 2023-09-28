import unittest


def print_specific_elements(numbers):
    if len(numbers) < 4 or len(numbers) > 10 or (
        any(isinstance(i, (float, str)) for i in numbers)) or (
        any(i > 256 for i in numbers) or not numbers
    ):
        return 'Error'
    else:
        return numbers[0], numbers[1], numbers[-2], numbers[-1]


class TestListMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(print_specific_elements([1, 2, 3, 4]), (1, 2, 3, 4))

    def test_2(self):
        self.assertEqual(print_specific_elements([1, 2, 3]), 'Error')

    def test_3(self):
        self.assertEqual(
            print_specific_elements([1, 2, 3, 1, 2, 3, 1, 2, 3, 0, 1]),
            'Error')

    def test_4(self):
        self.assertEqual(print_specific_elements([1.9, 2, 3, 1, 2, 3, 1, 2]),
                         'Error')

    def test_5(self):
        self.assertEqual(print_specific_elements([257, 2, 3, 1, 2, 3]),
                         'Error')

    def test_6(self):
        self.assertEqual(print_specific_elements([]), 'Error')

    def test_7(self):
        self.assertEqual(print_specific_elements([257, 2, 3, 1.9]), 'Error')

    def test_8(self):
        self.assertEqual(print_specific_elements([25, 8]), 'Error')

    def test_9(self):
        self.assertEqual(print_specific_elements([25, 8, (1, 3)]), 'Error')

    def test_10(self):
        self.assertEqual(print_specific_elements(['Error']), 'Error')

    def test_11(self):
        self.assertEqual(print_specific_elements(['-', '2', '&', "]]"]),
                         'Error')

    def test_12(self):
        self.assertEqual(print_specific_elements([-4, -5, -5, -7, -5]),
                         (-4, -5, -7, -5))

    def test_13(self):
        self.assertEqual(print_specific_elements([1, 2, 1, 2, 3, 43, 4]),
                         (1, 2, 43, 4))


if __name__ == '__main__':
    unittest.main()