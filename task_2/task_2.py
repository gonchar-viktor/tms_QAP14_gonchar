# +
# 2 Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить
# пустым.

with open("numbers_for_task_2.txt", "r") as was:
    aa = []
    bb = []
    b = list(map(int, was.readline().split()))
    for p in b:
        if p % 2:
            aa.append(p)
            with open("odd_numbers.txt", "w+") as f1:
                f1.writelines(str(aa))
                # odd_numbers - нечётные
        else:
            bb.append(p)
            with open("even_numbers.txt", "w+") as f2:
                f2.writelines(str(bb))
                # even_numbers - чётные

pass

