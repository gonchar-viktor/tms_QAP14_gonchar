# +++ Списки
# 1. Создайте два любых списка и свяжите их с переменными. +
def two_spis():
    global a
    global b
    a = ["1a", "1b", "1c", "1d"]
    b = ["2a", "2b", "2c", "2d"]
    return a, b


two_spis()
print(a)
print(b)

# 2. Извлеките из первого списка второй элемент. +
def izvl():
    aa = (a[1])
    return aa


print(izvl())


# 3. Измените во втором списке последний элемент. Выведите список на экран. +
def new_last_element():
    global b
    b[-1] = "3d"
    return b


new_last_element()
print(b)


# 4. Соедините оба списка в один, присвоив результат новой переменной. Выведите получившийся список на экран. +
def summ_spiskov():
    global c
    c = a + b
    return c


print(summ_spiskov())


# 5. "Снимите" срез из соединенного списка так, чтобы туда попали некоторые части обоих первых списков. +
# Срез свяжите с очередной новой переменной. Выведите значение этой переменной.
def slice():
    global d
    d = c[2:-2:1]
    return d


print(slice())


# 6. Добавьте в список два новых элемента и снова выведите его. +
def add_two_elements():
    global d
    d.extend(["3a", "3b"])
    return d


print(add_two_elements())


# 7. Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков. +
# !не использовать циклы for and while
def common_elements():
    global e
    global r
    global t1
    e = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    t1 = list(set(e) & set(r))
    return t1


print(common_elements())


# 8. Есть список: [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3] оставить в нем только уникальные значения. +
# !не использовать циклы
def unique_values():
    global t
    global y
    t = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
    y = set(t)
    y = list(y)
    return y


print(unique_values())
