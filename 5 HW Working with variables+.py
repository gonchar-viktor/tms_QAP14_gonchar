# +++ Работа с переменными

# 1. Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No". +
var_int = 10
var_float = 8.4
var_str = "No"
print(var_int, var_float, var_str)


# 2. Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза, +
# результат свяжите с переменной big_int
big_int = 0
def new_big_int():
    global big_int
    big_int = var_int * 3.5
    return big_int


print(new_big_int())

# 3 Измените значение, хранимое в переменной var_float, уменьшив его на единицу, +
# результат свяжите с той же переменнои
def new_var_float():
    global var_float
    var_float -= 1
    return var_float


print(new_var_float())

# 4. Разделите var_int на var_float, а затем big_int на var_float. Результат данных выражений не привязывайте ни +
# к каким переменным.
def del_int_float():
    a = var_int / var_float
    b = big_int / var_float
    return a, b

print(del_int_float())

# 5. Измените значение переменной var_str на "NoNoYesYesYes". При формировании +
# нового значения используйте операции конкатенации (+) и повторения строки (*).

def new_var_str():
    global var_str
    var_str = var_str * 2 + "Yes" * 3
    return var_str


print(new_var_str())

# 6. Выведите значения всех переменных. +
