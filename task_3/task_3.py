# +
# 3 Дан файл вещественных чисел. Заменить в нем все элементы на их
# квадраты.

with open("float_numbers.txt", "r") as f:
    b = list(map(float, f.readline().split()))


def float_to_int():
    global c
    c = []
    d = 0
    for i in b:
        d = i ** 2
        d = round(d, 2)
        c.append(d)
    return c


float_to_int()

c = str(c)
c = c.replace("[", "")
c = c.replace("]", "")
c = c.replace(",", "")
print(c)
with open("float_numbers.txt", "w") as file:
    file.write(str(c))

float_to_int()

# ввожу значения 1.1 2.2 3.3 4.4 5.5
# получаю значания 1.21 4.84 10.89 19.36 30.25
