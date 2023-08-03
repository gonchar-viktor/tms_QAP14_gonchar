# +
# Шифр Цезаря — один из древнейших шифров. При шифровании каждый
# символ заменяется другим, отстоящим от него в алфавите на
# фиксированное число позиций.
# Примеры:
#   ● hello world! -> khoor zruog!
#   ● this is a test string -> ymnx nx f yjxy xywnsl
# Напишите две функции - encode и decode принимающие как параметр
# строку и число - сдвиг.
# Бонусные очки
#   ● Шифр работает на нескольких языках (русский, английский, etc.)
#   ● Шифр сохраняет исходный регистр и знаки препинания
#   ● Можно ли обойтись одной функцией для зашифровки и
#     дешифровки?
#   ● Придумайте свой шифр

# через три буквы --

# chr() - используется для преобразования целого числа
# в его символ Юникода и возвращает его

# ord() - эта функция принимает строку единичной длины в
# качестве аргумента и возвращает эквивалентность Юникода
# переданного аргумента

def encoding(text, shift):
    # def f(text=str(input()), shift=int(input())) - если нужно вводить данные
    lst = []
    strings = ""
    for i in text:
        if ord(i) >= 65 and ord(i) <= 90:
            strings = chr((((ord(i) - 65) + shift) % 26) + 65)
            lst.append(strings)
        elif ord(i) >= 97 and ord(i) <= 122:
            strings = chr((((ord(i) - 97) + shift) % 26) + 97)
            lst.append(strings)
        else:
            lst.append(i)
    return "".join(lst)


print(encoding("hello_HELLO world_WORLD!", 3))
a = encoding("hello_HELLO world_WORLD!", 3)


def decoding(text, shift):
    lst2 = []
    string2 = ""
    for o in text:
        if ord(o) >= 65 and ord(o) <= 90:
            string2 = chr((((ord(o) - 65) - shift) % 26) + 65)
            lst2.append(string2)
        elif ord(o) >= 97 and ord(o) <= 122:
            string2 = chr((((ord(o) - 97) - shift) % 26) + 97)
            lst2.append(string2)
        else:
            lst2.append(o)
    return "".join(lst2)


print(decoding(a, 3))
