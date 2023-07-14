# +++ Цикл for
# 1. Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B включительно. +
def the_sum_of_the_numbers_from_A_to_B_inclusive():
    global A, B, c
    A = 2
    B = 6
    c = 0
    for i in range(A, B):
        c += i
    return c + B


print(the_sum_of_the_numbers_from_A_to_B_inclusive())

# 2. Найти сумму всех натуральных чисел от A до B +
def the_sum_of_all_natural_numbers_from_A_to_B():
    global A, B, c
    A = 2
    B = 6
    c = 0
    for x in range(A, B):
        c = c + x
    return c - A


print(the_sum_of_all_natural_numbers_from_A_to_B())


# 3. Найти произведение положительных, сумму и количество отрицательных из 10 введенных целых значений. +
def func1():
    global number_of_negative_numbers, summ_negative_numbers, the_product_of_numbers
    global q1, q2, q3, q4, q5, q6, q7, q8, q9, q10
    q1, q2, q3, q4, q5, q6, q7, q8, q9, q10 = 1, 2, 3, 4, -5, -6, 7, 8, 9, 10
    number_of_negative_numbers = 0
    summ_negative_numbers = 0
    the_product_of_numbers = 1
    for i in (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
        if i < 0:
            number_of_negative_numbers += 1
            summ_negative_numbers += i

        elif i >= 0:
            the_product_of_numbers *= i
    print("Сумма отрицательных чисел:", summ_negative_numbers)
    print("Количество отрицательных чисел:", number_of_negative_numbers)
    print("Произведение положительных чисел:", the_product_of_numbers)
    return


func1()


# 4. Дан словарь пловцов с их результатами. Напечатать лучший результат заплыва среди 6 участников. +
# Бекиш Александр - 21,07
# Будник Алексей - 20,34
# Гребень Анастасия - 22,12
# Давидович Татьяна - 30
# Дешук Дмитрий - 24.01
# Казак Анна - 28,17
def best_result1():
    global g
    g = {"Бекиш Александр": 21.07,
         "Будник Алексей": 20.34,
         "Гребень Анастасия": 22.12,
         "Давидович Татьяна": 30,
         "Дешук Дмитрий": 24.01,
         "Казак Анна": 28.17
         }
    g = g.values()
    print("лучший результат:", min(g))
    return


best_result1()


# or

def best_result2():
    global g2, b
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
    print("лучший результат 2 метод:", b)

best_result2()