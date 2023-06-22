#  1.2 Определить переменные всех типов и выведете их на экран +
print(type(int(1)))
print(type(float(1.22)))
print(type(str("hi")))
print(type(list([1, 2, "gfg"])))
dd = {"1А": 1, "2Б": 2}
print(type(dict(dd)))
q1 = {"hi", "word"}
print(type(set(q1)))
print(type(tuple("111")))
ww = True
print(type(bool(ww)))

#  1.3 Найти значение выражений +
x1 = (17/(2*3))+2
x2 = 2+(17/(2*3))
x3 = 19%4+(15/(2*3))
x4 = (15+6)-(10*4)
x5 = (17/2)%(2*(3**3))
print(x1, x2, x3, x4, x5)
#  --------
x6 = 17/2*3+2
print(x6)

#  1.4 Создать три переменные, содержащие возраст трех ближайших соседей, найти сумму и вывести ее на экран. +
# Создать еще одну переменную равную среднему арифметическому возрасту, и вывести это значение на экран.  +
per1 = 22
per2 = 21
per3 = 20
print(per1 + per2 + per3)
per4 = (per1 + per2 + per3)/3
print(per4)

# Привести к целому типу -1.6, 2.99 +
a = (int(-1.6))
print(a)
b = (int(2.99))
print(b)

#  Заменить символ “#” на символ “/” в строке 'www.my_site.com#about' +
c = "www.my_site.com#about"
new_c = c.replace("#", "/", 1)
print(new_c)

#  Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’ +
print("stroka" + "ing")
#  or
rr = "stroka"
tt = "ing"
print(rr+tt)

#  В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou" +
s1 = "Ivanou Ivan"
s2 = s1.split()
print(" ".join(s2[::-1]))  # Ivan Ivanou
# or
s3 = ["Ivanou", "Ivan"]
s3.reverse()
print(" ".join(s3))  # Ivan Ivanou

#  Напишите программу, которая удаляет пробел в начале, в конце строки
s = "       hello world       "
print(s.strip())

#  Создайте словарь, связав его с переменной school, и наполните его данными которые бы отражали количество учащихся +
#  в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
school = {"1a": 20, "2a": 21, "3a": 22, "4a": 23, "5a": 24, "1б": 25, "2б": 26, "3б": 27, "4б": 28, "5б": 29}
for class_, students_ in school.items():
    print(class_.upper(), "=", students_)

#  Создайте список и извлеките из него списка второй элемент. +
spisok = ["element1", "element2", "element3"]
print(spisok[1])

#  Вывести входит ли строка1 в строку2 (пример: employ и employment)
stroka1 = "employ"
stroka2 = "employment"
print(stroka1 in stroka2)

#  Вывести нужные символы +
x = "My name is Agent Smith"
print(x[1])  # y
print(x[3:16:3])  # nesgt



