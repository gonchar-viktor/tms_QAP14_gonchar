# +
# 4 Даны два файла произвольного типа. Поменять местами их
# содержимое. Файлы должны быть бинарного типа

lst1 = 1, 2, 3, 4, 5  # в первый сперва записываются цифры
lst2 = "a", "b", "c", "d"  # во второй сперва записываются буквы

with open("file_bin_1.bin", "wb") as file1:
    for i in lst1:
        i = str(i)
        p = i.encode()
        file1.write(p)

pass

with open("file_bin_2.bin", "wb") as file2:
    for u in lst2:
        u = str(u)
        k = u.encode()
        file2.write(k)

pass

# чтобы проверить работу можно сделать всё, что ниже этой записи комментарием

with open("file_bin_1.bin", "rb") as rep_1:
    bb = rep_1.read()

with open("file_bin_2.bin", "rb") as rep_2:
    nn = rep_2.read()

with open("file_bin_1.bin", "wb") as rep_1:
    rep_1.write(nn)

with open("file_bin_2.bin", "wb") as rep_2:
    rep_2.write(bb)


