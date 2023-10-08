# +++ Строки

# 1. Свяжите переменную с любой строкой, состоящей не менее чем из 8
# символов. Извлеките из строки первый символ, затем последний, третий с
# начала и третий с конца. Измерьте длину вашей строки.
def actions_with_a_string():
    """
    Bind the variable to any string consisting of at least 8 characters.
    Extract the first character from the string, then the last, the third from
    the beginning and the third from the end. Measure the length of your
    string.
    """
    a = "12345678"
    first = a[0]
    last = a[-1]
    third = a[2]
    third_from_the_end = a[-3]
    b = first, last, third, third_from_the_end
    len_a = len(a)
    len_b = len(b)
    return f"длинна полной строки: {len_a}\nдлинна извлечённых символов: " \
           f"{len_b} "


print(actions_with_a_string())


# 2. Присвойте произвольную строку длиной 10-15 символов переменной и
# извлеките из нее следующие срезы:
# ● первые восемь символов
# ● четыре символа из центра строки
# ● символы с индексами кратными трем
# ● переверните строку
def slice_str():
    """
    Assign an arbitrary string 10-15 characters long to a variable and extract
    the following slices from it:
    ● The first eight characters
    ● four characters from the center of the string
    ● symbols with indexes that are multiples of three
    ● Flip the line
    """
    c = "qwertyuiop[]"
    v1 = (c[0:8])
    v2 = c[len(c)//2:]
    v3 = (c[3:12:3])
    v4 = (c[::-1])
    return f"строка: {c}\nпервые восемь символов: {v1}\nчетыре символа из " \
           f"центра строки: {v2[0:4]}\nсимволы с индексами кратными трем: " \
           f"{v3}\nпереверните строку: {v4}"


print(slice_str())


# 3. Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name”
# вставьте ваше имя.
def my_name():
    """
    There is a line: "my name is name". Type it, but instead of the 2nd "name"
    insert your name.
    """
    stroka1 = "my name is name"
    stroka2 = stroka1.split()
    stroka2[3] = "Viktor"
    stroka2 = " ".join(stroka2)
    return stroka2


print(my_name())


# 4. Есть строка: test_tring = "Hello world!", необходимо:
# ● напечатать на каком месте находится буква w
# ● кол-во букв l
# ● Проверить начинается ли строка с подстроки: “Hello”
# ● Проверить заканчивается ли строка подстрокой: “qwe”
def tes_tring():
    """
    There is a line: test_tring = "Hello world!", you need to:
    ● print where the letter w is located
    ● number of letters l
    ● Check whether the string starts with the substring: “Hello”
    ● Check whether the string ends with a substring: “qwe”
    """
    tring = "Hello world!"
    t1 = (tring.find("w"))
    t2 = (tring.count("l"))
    t3 = (tring.startswith("Hello"))
    t4 = (tring.endswith("qwe"))
    return f"w находится на месте под номером: {t1}\nкол-во букв 'l': {t2}\n" \
           f"начинается ли строка с подстроки: 'Hello': {t3}\nзаканчивается " \
           f"ли строка подстрокой: 'qwe': {t4}"


print(tes_tring())
