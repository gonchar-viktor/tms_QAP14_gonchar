# +++  "Работа с переменными" объединить в одну функцию
def func():
    """
    1. Assign the var_int variable the value 10, var_float - the value 8.4,
    var_str - "No".

    2. Change the value stored in the var_int variable by increasing it 3.5
    times,associate the result with the big_int variable

    3 Change the value stored in the var_float variable by reducing it by one,
    associate the result with the same variable

    4. Divide var_int by var_float, and then big_int by var_float. Do not bind
    the result of these expressions to any variables.

    5. Change the value of the variable var_str to "NoNoYesYesYes". When
    forming a new value, use concatenation (+) and string repetition (*)
    operations.

    6. Output the values of all variables.
    """
    var_int = 10
    var_float = 8.4
    var_str = "No"
    big_int = var_int * 3.5
    var_float -= 1
    var_str = var_str * 2 + "Yes" * 3
    return f"{var_int}\n{big_int}\n{var_float}\n{var_int / var_float}\
 {big_int / var_float}\n{var_str}"


print(func())
