# +
# 3 Дан файл вещественных чисел. Заменить в нем все элементы на их
# квадраты.
def func3():
    """
    A file of real numbers is given. Replace all the elements in it with their
    squares.
    """
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

        print(c)
        c = str(c)
        c = c.replace("[", "")
        c = c.replace("]", "")
        c = c.replace(",", "")

        print(c)
        with open("float_numbers.txt", "w") as file:
            file.write(str(c))

    # ввожу значения 1.1 2.2 3.3 4.4 5.5
    # получаю значения 1.21 4.84 10.89 19.36 30.25
    float_to_int()


func3()
