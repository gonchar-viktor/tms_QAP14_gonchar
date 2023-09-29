# +
# Напишите декоратор, который проверял бы тип параметров
# функции, конвертировал их если надо и складывал:
# @typed(type=’str’)
# def add_two_symbols(a, b):
#  return a + b
# add_two_symbols("3", 5) -> "35"
# add_two_symbols(5, 5) -> 55
# add_two_symbols('a', 'b') -> 'ab’
# @typed(type=’int’)
# def add_three_symbols(a, b, с):
#  return a + b + с
# add_three_symbols(5, 6, 7) -> 18
# add_three_symbols("3", 5, 0) -> 8
# add_three_symbols(0.1, 0.2, 0.4) -> 0.7000000000000001

def typed(val):
    """
    The decorator checks the type of each argument and, if the type does not
    match, tries to convert it. If this is not possible, a TypeError
    exception is thrown.
    """
    def decorator(func):
        def inner(*args):
            lst = []
            for i, o in enumerate(args):
                i = i  # чтобы не ругался flake8
                if isinstance(o, val):
                    lst.append(o)
                else:
                    try:
                        c = val(o)
                        lst.append(c)
                    except TypeError:
                        raise
            return func(*lst)

        return inner

    return decorator


@typed(val=str)
def add_two_symbols(a, b):
    """
    :return: str(a + b) , type
    """
    return f"{a + b}\t\t\t\t\t\t{type(a + b)}"


v1 = add_two_symbols("3", 5)  # -> "35"
v2 = add_two_symbols(5, 5)  # -> 55
v3 = add_two_symbols('a', 'b')  # -> 'ab’

print(v1, " ")
print(v2, " ")
print(v3, " ", "\n")


@typed(val=int)
def add_three_symbols(a, b, c):
    """
    :return: int(a + b + c) , type
    """
    return f"{a + b + c}\t\t\t\t\t\t{type(a + b + c)}"


v4 = add_three_symbols(5, 6, 7)  # -> 18
v5 = add_three_symbols("3", 5, 0)  # -> 8

print(v4, " ")
print(v5, "  ", "\n")


@typed(val=float)
def add_three_symbols_float(a, b, c):
    """
    :return: float(a + b + c) , type
    """
    return f"{a + b + c}\t\t{type(a + b + c)}"


v6 = add_three_symbols_float(0.1, 0.2, 0.4)  # -> 0.7000000000000001

print(v6, "  ")