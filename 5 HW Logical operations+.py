# +++ Логические операции
# 1. Присвойте двум переменным любые числовые значения. +
def variables():
    global a
    global b
    a = 10
    b = 20
    return a, b


variables()
print(a, b)

# 2. Составьте четыре сложных логических выражения с помощью оператора and, два из +
# которых должны давать истину, а два других - ложь.
def operator_and():
    q1 = print(a * 2 == 20 and b == 20)
    q2 = print(b < 21 and a > 1)
    q3 = print(a == b and b <= 10)
    q4 = print(a != 10 and b != 20)
    return q1, q2, q3, q4


operator_and()


# 3. Аналогично выполните п. 2, но уже используя оператор or. +
def operatot_or():
    q5 = print(a >= 15 or b > 15)
    q6 = print(a == 10 or b == 10 or b / 2 == 10)
    q7 = print(a >= b + 5 or b < 19)
    q8 = print(a == b ** 2 or b != 20)
    return q5, q6, q7, q8


operatot_or()

# 4. Попробуйте использовать в сложных логических выражениях работу с переменными строкового типа +
def hard_bool():
    w1 = print("hello" >= "14" or "1" >= "world")
    w2 = print("hello" != 11111 and a < b)
    w3 = print("11" <= "1" or "1" == "11")
    w4 = print("11" == 11 or "world" == 11)
    return w1, w2, w3, w4


hard_bool()