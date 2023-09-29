#  +++ Цикл while
# 1. Дано число N. Найти произведение всех чисел от 0 до N.
def the_product_of_numbers():
    """
    Given the number N. Find the product of all numbers from 0 to N.
    """
    n = 7
    i = 0
    o = 0
# если от 0, то в любом случае результат будет (0) или же поставить сюда (1)
    while i < n:
        i += 1
        o *= i
    return f"произведение чисел от 0 до n = {o}"


print(the_product_of_numbers())


# 2. Поле засеяли цветами двух сортов на площади S1 и S2. Каждый год
# площадь цветов первого сорта увеличивается вдвое, а площадь второго сорта
# увеличивается втрое. Через сколько лет площадь первых сортов будет
# составлять меньше 10% от площади вторых сортов.
#          ---  Процент от числа = (число * процент) / 100
def flower_area():
    """
    The field was sown with flowers of two varieties on the area S1 and S2.
    Every year, the area of flowers of the first grade is doubled, and the area
    of the second grade is tripled. After how many years the area of the first
    varieties will be less than 10% of the area of the second varieties.
    """
    s1 = int(input("Введите S1: "))
    s2 = int(input("Введите S2: "))
    year = 0
    s3 = (s2 * 10) / 100  # 10% от S2
    while s1 > s3:
        s1 = s1 * 2
        s2 = s2 * 3
        s3 = (s2 * 10) / 100
        year += 1
    return f"Результат:через {year} лет площадь первых сортов будет" \
           f" составлять меньше 10% от площади вторых сортов"


print(flower_area())


# 3. Дано целое число N (>0). Используя операции деления нацело и взятия
# остатка от деления, найти количество и сумму его цифр.

def operations_on_a_number():
    """
    Given an integer N (>0). Using the operations of dividing completely and
    taking the remainder of the division, find the number and sum of its
    digits.
    """
    n = int(input("Введите целое число которое больше нуля: "))
    if n <= 0:
        print("Error: число не подходит, повторите попытку!")
    summ_result = 0
    kolvo_result = 0
    h = 0
    while n > 0:
        if n > 0:
            h = n % 10
            kolvo_result += 1
            summ_result += h
            n = n // 10
    return f"кол-во чисел: {kolvo_result}\nсумма чисел: {summ_result}"


print(operations_on_a_number())


# 4. Деду M лет, а внуку N лет. Через сколько лет дед станет вдвое старше
# внука. И сколько при этом лет будет деду и внуку
# ded_age = 78
# vnuk_age = 38

def age_difference():
    """
    The grandfather is M years old, and the grandson is N years old. After how
    many years the grandfather will be twice the grandson's age. And how old
     will the grandfather and grandson be at the same time
    """
    ded_age = int(input("Введите сколько лет деду: "))
    vnuk_age = int(input("Введите сколько лет внуку: "))
    year = 0
    while ded_age / vnuk_age != 2:
        ded_age += 1
        vnuk_age += 1
        year += 1
    return f"Результат: дед станет вдвое старше внука через столько лет" \
           f" - {year}\nдеду будет столько лет -  {ded_age}\nвнуку будет" \
           f" столько лет -  {vnuk_age}"


print(age_difference())
