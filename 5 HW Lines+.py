# +++ Строки
# 1. Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.Извлеките из строки первый символ, +
# затем последний, третий с начала и третий с конца. Измерьте длину вашей строки.
def actions_with_a_string():
    global a, first, last, third, third_from_the_end, b, len_a, len_b
    a = "12345678"
    first = a[0]
    last = a[-1]
    third = a[2]
    third_from_the_end = a[-3]
    b = first, last, third, third_from_the_end
    len_a = len(a)
    len_b = len(b)
    return len_b


print(actions_with_a_string())


# 2. Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из нее следующие срезы: +
# ● первые восемь символов
# ● четыре символа из центра строки
# ● символы с индексами кратными трем
# ● переверните строку
def slice_str():
    global c, v1, v2, v3, v4
    c = "qwertyuiop[]"
    v1 = print(c[0:8])
    v2 = print(c[5:9])
    v3 = print(c[3:12:3])
    v4 = print(c[::-1])
    return c, v1, v2, v3, v4


slice_str()


# 3. Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте ваше имя. +
def my_name():
    global stroka1
    global stroka2
    stroka1 = "my name is name"
    stroka2 = stroka1.split()
    stroka2[3] = "Viktor"
    stroka2 = " ".join(stroka2)
    return stroka2


print(my_name())


# 4. Есть строка: test_tring = "Hello world!", необходимо: +
# ● напечатать на каком месте находится буква w
# ● кол-во букв l
# ● Проверить начинается ли строка с подстроки: “Hello”
# ● Проверить заканчивается ли строка подстрокой: “qwe”
def tes_tring():
    global tring, t1, t2, t3, t4
    tring = "Hello world!"
    t1 = (tring.find("w"))
    print(t1)
    t2 = (tring.count("l"))
    print(t2)
    t3 = (tring.startswith("Hello"))
    print(t3)
    t4 = (tring.endswith("qwe"))
    print(t4)
    return t1, t2, t3, t4


print(tes_tring())
