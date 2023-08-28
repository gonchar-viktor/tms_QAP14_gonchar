#  +++ Цикл for

# 1. Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до
# B включительно.
# (Целые числа — это все положительные, все отрицательные числа, ноль и которые
# не имеют дробной части)

def sum_of_integers(a, b):
    """
    Given two integers A and B (A < B). Find the sum of all integers from A to
    B inclusive.
    :param a: -2
    :param b: 4
    :return: 7
    """
    c = 0
    for i in range(a, b):
        c += i
    return c + b


print(sum_of_integers(-2, 4))


# 2. Найти сумму всех натуральных чисел от A до B (начинаются от единицы, могут
# иметь дробную часть)

def sum_of_natural_numbers(a, b):
    """
    Find the sum of all natural numbers from A to B (starting from one, may
    have a fractional part)
    :param a: 1
    :param b: 6
    :return: 14
    """
    c = 0
    for x in range(a, b):
        c = c + x
    return c - a


print(sum_of_natural_numbers(1, 6))


# 3. Найти произведение положительных, сумму и количество отрицательных из 10
# введенных целых значений.

def func1(*args):
    """
    Find the product of the positive, the sum and the number of negative of
     the 10 entered integer values.
    :param args: 1, 2, 3, 4, -5, -6, 7, 8, 9, 10
    :return: Сумма отрицательных чисел: -11
             Количество отрицательных чисел: 2
             Произведение положительных чисел: 120960
    """
    number_of_negative_numbers = 0
    summ_negative_numbers = 0
    the_product_of_numbers = 1
    for i in args:
        if i < 0:
            number_of_negative_numbers += 1
            summ_negative_numbers += i

        elif i >= 0:
            the_product_of_numbers *= i
    return f"Сумма отрицательных чисел: {summ_negative_numbers}\nКоличество "\
           f"отрицательных чисел: {number_of_negative_numbers}\nПроизведение "\
           f"положительных чисел: {the_product_of_numbers}"


print(func1(1, 2, 3, 4, -5, -6, 7, 8, 9, 10))


# 4. Дан словарь пловцов с их результатами. Напечатать лучший результат
# заплыва среди 6 участников.

# Бекиш Александр - 21,07
# Будник Алексей - 20,34
# Гребень Анастасия - 22,12
# Давидович Татьяна - 30
# Дешук Дмитрий - 24.01
# Казак Анна - 28,17
def best_result1():
    """
    A dictionary of swimmers with their results is given. Print the best result
    of the swim among 6 participants.
    :return: 20.34
    """
    g = {"Бекиш Александр": 21.07,
         "Будник Алексей": 20.34,
         "Гребень Анастасия": 22.12,
         "Давидович Татьяна": 30,
         "Дешук Дмитрий": 24.01,
         "Казак Анна": 28.17
         }
    g = g.values()
    h = min(g)
    return f"лучший результат, 1 метод: {h}"


print(best_result1())


# or

def best_result2():
    """
    A dictionary of swimmers with their results is given. Print the best result
    of the swim among 6 participants.
    :return: 20.34
    """
    g2 = {"Бекиш Александр": 21.07,
          "Будник Алексей": 20.34,
          "Гребень Анастасия": 22.12,
          "Давидович Татьяна": 30,
          "Дешук Дмитрий": 24.01,
          "Казак Анна": 28.17
          }
    b = sum(g2.values())
    for r in g2.values():
        if r < b:
            b = r
    return f"лучший результат, 2 метод: {b}"


print(best_result2())
