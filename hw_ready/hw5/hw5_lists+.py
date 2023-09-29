# +++ Списки

# 1. Создайте два любых списка и свяжите их с переменными.

def two_spis():
    """
    Create any two lists and associate them with variables.
    """
    global a
    global b
    a = ["1a", "1b", "1c", "1d"]
    b = ["2a", "2b", "2c", "2d"]
    return f"1 список: {a}\n2 список: {b}"


print(two_spis())


# 2. Извлеките из первого списка второй элемент.

def izvl():
    """
    Extract the second item from the first list.
    """
    aa = (a[1])
    return f"второй элемент первого списка: {aa}"


print(izvl())


# 3. Измените во втором списке последний элемент. Выведите список на экран.

def new_last_element():
    """
    Change the last item in the second list. Display the list on the screen.
    """
    global b
    b[-1] = "3d"
    return f"изменил последний элемент во 2 списке: {b}"


print(new_last_element())


# 4. Соедините оба списка в один, присвоив результат новой переменной.
# Выведите получившийся список на экран.

def summ_spiskov():
    """
    Combine both lists into one by assigning the result to a new variable.
    Display the resulting list on the screen
    """
    global c
    c = a + b
    return f"объединённые списки: {c}"


print(summ_spiskov())


# 5. "Снимите" срез из соединенного списка так, чтобы туда попали некоторые
# части обоих первых списков. Срез свяжите с очередной новой переменной.
# Выведите значение этой переменной.

def slice():
    """
    "Remove" the slice from the connected list so that some parts of both first
    lists get there. Link the slice to the next new variable. Print the value
    of this variable.
    """
    global d
    d = c[2:-2:1]
    return f"срез обоих списков: {d}"


print(slice())


# 6. Добавьте в список два новых элемента и снова выведите его.
def add_two_elements():
    """
    Add two new items to the list and output it again.
    """
    global d
    d.extend(["3a", "3b"])
    return f"добавил 2 новых элемента: {d}"


print(add_two_elements())


# 7. Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# Нужно вернуть список, который состоит из элементов, общих для этих двух
# списков. !не использовать циклы for and while

def common_elements():
    """
    You need to return a list that consists of elements common to these two
     lists, without using for and while loops.
    """
    e = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    t1 = list(set(e) & set(r))
    return f"общие элементы: {t1}"


print(common_elements())


# 8. Есть список: [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3] оставить в нем
# только уникальные значения. !не использовать циклы
def unique_values():
    """
    leave only unique values in the list, without using loops
    """
    t = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
    y = set(t)
    y = list(y)
    return f"уникальные значения: {y}"


print(unique_values())
