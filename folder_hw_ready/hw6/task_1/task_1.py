# +
# 1 Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного
# файла. Если чисел меньше 3 выводить ошибку
def func():
    """
    A file of integers containing at least four elements is given.
    Print the first, second, penultimate and last elements of this
    file. If the numbers are less than 3, output an error
    """
    with open("file_for_task_1.txt", "r") as ff:
        numbers = []
        for i in ff:
            for j in i.split():
                numbers.append(int(j))

        if len(numbers) < 3:
            print('Ошибка: чисел меньше 3')
        else:
            print(numbers[0], numbers[1], numbers[-2], numbers[-1])


func()