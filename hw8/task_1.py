# +
# 1. Написать обычную функцию для факториала, генератор и
# рекурсию. Сравнить их время работы

import requests

import time

# 1.1 decorator (я дополнительно добавил декоратор)
start = time.time()


def decorator(a):
    """
    decorator execution time
    """

    def f(h=100):
        h = h ** 100
        a()

    return f


@decorator
def fetch_webpage():
    requests.get('https://github.com/gonchar-viktor')


fetch_webpage()
end = time.time()
c = end - start
print(f"[*] Время выполнения декоратора: {c:.10f} секунд.")

# 1.2 factorial

start = time.time()


def factorial(h=100):
    h = h ** 100
    number = 1000
    factorial = 1
    while number > 1:
        factorial = factorial * number
        number -= 1
    return factorial


factorial()
end = time.time()
c = end - start

print(f'[*] Время выполнения факториала: {c:.10f} секунд.')

# 1.3 generator

start = time.time()


def time_generator(gen, h=100):
    """
    generator execution time
    """
    h = h ** 100
    list(gen)
    return gen


def generator():
    mylist = range(300000)
    for i in mylist:
        yield i * i


n = time_generator(generator())
end = time.time()
c = end - start
print(f'[*] Время выполнения генератора: {c:.10f} секунд.')

# 1.4 recursion

start = time.time()


def sum_recursion(n, h=100):
    """
    recursion execution time
    """
    h = h ** 100
    if n == 0:
        return 1
    else:
        return n * sum_recursion(n - 1)


sum_recursion(900)
end = time.time()
c = end - start
print(f'[*] Время выполнения рекурсии:   {c:.10f} секунд.')
