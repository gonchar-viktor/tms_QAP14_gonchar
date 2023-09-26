# +++ Работа с переменными

# 1. Переменной var_int присвойте значение 10, var_float - значение 8.4,
# var_str - "No".
def variables():
    """
    Assign the var_int variable the value 10, var_float - the value 8.4,
    var_str - "No".
    """
    global var_int, var_float, var_str
    var_int = 10
    var_float = 8.4
    var_str = "No"
    return f"{var_int}, {var_float}, {var_str}"


print(variables())


# 2. Измените значение, хранимое в переменной var_int, увеличив его в 3.5
# раза, результат свяжите с переменной big_int
def new_big_int():
    """
    Change the value stored in the var_int variable by increasing it 3.5 times,
     associate the result with the big_int variable
    """
    global big_int
    big_int = var_int * 3.5
    return big_int


print(new_big_int())


# 3 Измените значение, хранимое в переменной var_float, уменьшив его на
# единицу, результат свяжите с той же переменной
def new_var_float():
    """
    Change the value stored in the var_float variable by reducing it by one,
    associate the result with the same variable
    """
    global var_float
    var_float -= 1
    return var_float


print(new_var_float())


# 4. Разделите var_int на var_float, а затем big_int на var_float. Результат
# данных выражений не привязывайте ни к каким переменным.
def del_int_float():
    """
    Divide var_int by var_float, and then big_int by var_float. Do not bind the
     result of these expressions to any variables.
    """
    return f"{var_int / var_float}, {big_int / var_float}"


print(del_int_float())


# 5. Измените значение переменной var_str на "NoNoYesYesYes". При формировании
# нового значения используйте операции конкатенации + и повторения строки *

def new_var_str():
    """
    Change the value of the var_str variable to "NoNoYesYesYes". When forming a
    new value, use the operations of concatenation + and repetition of the
    string *
    """
    global var_str
    var_str = var_str * 2 + "Yes" * 3
    return var_str


print(new_var_str())
# 6. Выведите значения всех переменных.
print()

print(f"var_int:   {var_int}\nuntitled:  {var_int / var_float},"
      f"{big_int / var_float}\nvar_float: {var_float}\nvar_str:   {var_str}")
