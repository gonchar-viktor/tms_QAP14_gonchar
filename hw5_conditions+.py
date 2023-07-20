#  +++ Условия

# 1. Дано целое число. Если оно является положительным, то прибавить к нему 1;
# в противном случае не изменять его. Вывести полученное число.

def func2():
    """
    An integer is given. If it is positive, then add 1 to it; otherwise,
     do not change it. Print the resulting number.
    """
    a = -5
    if a >= 0:
        a += 1
        a = ("Число положительное:", a)
    else:
        a = a
        a = ("Число отрицательное:", a)
    return a


print(*func2())


# or

def func3():
    """
    An integer is given. If it is positive, then add 1 to it; otherwise, do
     not change it. Print the resulting number.
    """
    b = 5
    w = b
    if b >= 0:
        w += 1
        w = ("Число положительное:", w)
    else:
        w = b
        w = ("Число отрицательное", w)
    return w


print(*func3())


# 2. Даны три целых числа. Найти количество положительных чисел в
# исходном наборе.

def number_of_positive_numbers():
    """
    Three integers are given. Find the number of positive numbers in the
    original set.
    """
    b1 = [3, 4, -5]
    positive = 0
    negative = 0
    for i in b1:
        if i >= 0:
            positive += 1
        else:
            negative += 1
    return f"положительных: {positive}\nотрицательных: {negative}"


print(number_of_positive_numbers())


# 3. Дан номер года (положительное целое число). Определить количество дней в
# этом году, учитывая, что обычный год насчитывает 365 дней, а високосный
# — 366 дней. Високосным считается год, делящийся на 4, за исключением тех
# годов, которые делятся на 100 и не делятся на 400 (например, годы 300, 1300
# и 1900 не являются високосными, а 1200 и 2000 являются).
#                                            (o % 100 != 0) - не делится

def number_of_days_per_year():
    """
    Determine the number of days in this year, given that a normal year
    consists of 365 days, and a leap year consists of 366 days.
    """
    c = [2002]
    result = 0
    for o in c:
        if (o % 4 == 0) and (o % 100 != 0) or (o % 400 == 0):
            result = 365
            result = ("високостный: ", 365)
        else:
            result = 366
            result = ("не високостный: ", 366)
    return result


print(*number_of_days_per_year())


# 4. Дано целое число в диапазоне 1–7. Вывести строку — название дня недели,
# соответствующее данному числу (1 — «понедельник», 2 — «вторник» и т. д.).

def day_of_the_week():
    """
    An integer in the range 1-7 is given. Print the line — the name of the day
     of the week corresponding to this number
    """
    d = int(input("День недели 1-7: "))
    if d == 1:
        d = "Понедельник"
    elif d == 2:
        d = "Вторник"
    elif d == 3:
        d = "Среда"
    elif d == 4:
        d = "Четверг"
    elif d == 5:
        d = "Пятница"
    elif d == 6:
        d = "Суббота"
    elif d == 7:
        d = "Воскресенье"
    elif d <= 0 or d >= 8:
        d = "Error: введите число от 1 до 7!!!"
    return d


print(day_of_the_week())


# 5. Единицы массы пронумерованы следующим образом: 1 — килограмм,
# 2 — миллиграмм, 3 — грамм, 4 — тонна,5 — центнер. Дан номер единицы массы
# (целое число в диапазоне 1–5) и масса тела в этих единицах (вещественное
# число). Найти массу тела в килограммах.1-килограмм 2 = 1000000-миллиграмм
# 3 = 1000-грамм 4 = 0.001-тонна 5 = 0.01-центнер

def mass():
    """
    Find the body weight in kilograms.1-kilogram 2 = 1000000-milligrams
    3 = 1000-grams 4 = 0.001-ton 5 = 0.01-hundredweight
    """
    s = int(input("Введите № еденицы массы 1-5: "))
    if s <= 0 or s >= 6:
        print("Error: нужно ввести число от 1 до 5, или по стандарту выведет"
              " число в килограммах!")
    body_weight = int(input("Введите массу тела: "))
    if s == 1:
        body_weight = body_weight * 1
    elif s == 2:
        body_weight = body_weight / 1000000
    elif s == 3:
        body_weight = body_weight / 1000
    elif s == 4:
        body_weight = body_weight * 1000
    elif s == 5:
        body_weight = body_weight * 100
    return f"{body_weight} килограмм(а)"


print(mass())
