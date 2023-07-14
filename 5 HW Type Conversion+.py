# +++ Преобразование типов
# 1. Перевести строку в массив : "Robin Singh" => ["Robin", "Singh"] , +
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]


def str_robin(a):
    return a.split()


print(str_robin("Robin Singh"))


def str_love(b):
    return b.split()


print(str_love("I love arrays they are my favorite"))

# 2. Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus +
# # Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”


def spisok_m():
    spisok = ["Ivan", "Ivanou"]
    str1 = "Minsk"
    str2 = "Belarus"
    return f"Привет, " + " ".join(spisok) + "! " + "Добро пожаловать в " + str1 + " " + str2


print(spisok_m())

# 3. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него +
# строку => "I love arrays they are my favorite"


def spisok_in_str():
    w = ["I", "love", "arrays", "they", "are", "my", "favorite"]
    e = " ".join(w)
    return e


print(spisok_in_str())

# 4. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6 +
def new_pos():
    r = [1, 2, 3, 4, 5, "indx6", 7, 8, 9, 10]
    r.insert(2, "new3pos")
    del r[6]
    return r


print(new_pos())

# 5. Есть 2 словаря +
# a = { 'a': 1, 'b': 2, 'c': 3}
# b = { 'c': 3, 'd': 4,'e': 5}
# Необходимо их объединить по ключам, а значения ключей поместить в список, если у
# одного словаря есть ключ "а", а у другого нет, то поставить значение None на
# соответствующую позицию(1-я позиция для 1-ого словаря, вторая для 2-ого)
# ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}


def dict_():
    aa = {'a': 1, 'b': 2, 'c': 3}
    bb = {'c': 3, 'd': 4, 'e': 5}

    ab = {}
    for i in set(aa.keys()) | set(bb.keys()):
        ab[i] = [aa.get(i), bb.get(i)]
    return ab


print(dict_())

# *1) Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару, +
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число


def mass():
    y = [1, 5, 2, 9, 2, 9, 1]
    for u in y:
        if y.count(u) < 2:
            return u


print(mass())