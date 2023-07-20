# +++ Подзадание "Строки 2 и 4" реализовать через возврат нескольких значений
# 2
def slice_str():
    """
    Assign an arbitrary string 10-15 characters long to a variable and extract
    the following slices from it:
    ● The first eight characters
    ● four characters from the center of the string
    ● symbols with indexes that are multiples of three
    ● Flip the line
    """
    global c, v1, v2, v3, v4
    c = "qwertyuiop[]"
    v1 = (c[0:8])
    v2 = (c[5:9])
    v3 = (c[3:12:3])
    v4 = (c[::-1])
    return f"{c}\n{v1}\n{v2}\n{v3}\n{v4}"


print(slice_str())

# 4
def tes_tring():
    """
    There is a line: test_tring = "Hello world!", you need to:
    ● print where the letter w is located
    ● number of letters l
    ● Check whether the string starts with the substring: “Hello”
    ● Check whether the string ends with a substring: “qwe”
    """
    global tring, t1, t2, t3, t4
    tring = "Hello world!"
    t1 = (tring.find("w"))
    t2 = (tring.count("l"))
    t3 = (tring.startswith("Hello"))
    t4 = (tring.endswith("qwe"))
    return f"{t1}\n{t2}\n{t3}\n{t4}"


print(tes_tring())