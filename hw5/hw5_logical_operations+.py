#  +++ Логические операции

# 1. Присвойте двум переменным любые числовые значения.

def variables():
    """
    Assign any numeric values to the two variables.
    """
    global a
    global b
    a = 10
    b = 20
    return f"a={a}, b={b}"


print(variables())


# 2. Составьте четыре сложных логических выражения с помощью оператора and,
# два из которых должны давать истину, а два других - ложь.

def operator_and():
    """
    Compose four complex logical expressions using the and operator, two of
     which should give true, and the other two should give false.
    """
    q1 = (a * 2 == 20 and b == 20)
    q2 = (b < 21 and a > 1)
    q3 = (a == b and b <= 10)
    q4 = (a != 10 and b != 20)
    return f"1: {q1}, {q2}, {q3}, {q4}"


print(operator_and())


# 3. Аналогично выполните п. 2, но уже используя оператор or.

def operatot_or():
    """
    Compose four complex logical expressions using the or operator, two of
    which should give true, and the other two should give false.
    """
    q5 = (a >= 15 or b > 15)
    q6 = (a == 10 or b == 10 or b / 2 == 10)
    q7 = (a >= b + 5 or b < 19)
    q8 = (a == b ** 2 or b != 20)
    return f"2: {q5}, {q6}, {q7}, {q8}"


print(operatot_or())


# 4. Попробуйте использовать в сложных логических выражениях работу с
# переменными строкового типа

def hard_bool():
    """
    Try to use working with string-type variables in complex logical
     expressions
    """
    w1 = ("hello" >= "14" or "1" >= "world")
    w2 = ("hello" != 11111 and a < b)
    w3 = ("11" <= "1" or "1" == "11")
    w4 = ("11" == 11 or "world" == 11)
    return f"3: {w1}, {w2}, {w3}, {w4}"


print(hard_bool())
