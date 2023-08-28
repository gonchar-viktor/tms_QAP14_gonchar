# +++
# 1. Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.Извлеките из строки первый символ, +
# затем последний, третий с начала и третий с конца. Измерьте длину вашей строки.
a = "12345678"
first = a[0]
last = a[-1]
third = a[2]
third_from_the_end = a[-3]
b = first, last, third, third_from_the_end
print(first, last, third, third_from_the_end)
print(len(a))
print(len(b))

# 2. Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из нее следующие срезы: +
# ● первые восемь символов
# ● четыре символа из центра строки
# ● символы с индексами кратными трем
# ● переверните строку
c = "qwertyuiop[]"  # 12
print(c[0:8])
print(c[5:9])
print(c[3:12:3])
print(c[::-1])
# 3. Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте ваше имя. +
stroka1 = "my name is name"
stroka2 = stroka1.split()
stroka2[3] = "Viktor"
print(" ".join(stroka2))

# 4. Есть строка: test_tring = "Hello world!", необходимо: +
# ● напечатать на каком месте находится буква w
# ● кол-во букв l
# ● Проверить начинается ли строка с подстроки: “Hello”
# ● Проверить заканчивается ли строка подстрокой: “qwe”
test_tring = "Hello world!"
print(test_tring.find("w"))
print(test_tring.count("l"))
print(test_tring.startswith("Hello"))
print(test_tring.endswith("qwe"))








