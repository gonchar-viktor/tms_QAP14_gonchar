# +++
# 1. Присвойте двум переменным любые числовые значения. +
a = 10
b = 20

# 2. Составьте четыре сложных логических выражения с помощью оператора and, два из +
# которых должны давать истину, а два других - ложь.

print(a ** 2 and b == 20)
print(b < 21 and a > 1)
print(a == b and b == 10)
print(a != 10 and b != 20)

# 3. Аналогично выполните п. 2, но уже используя оператор or. +
print(a >= 15 or b > 15)
print(a == 10 or b == 10)
print(a >= b + 5 or b < 19)
print(a == b ** 2 or b != 20)

# 4. Попробуйте использовать в сложных логических выражениях работу с переменными строкового типа +
print("hello" >= "14" or "1" >= "world")
print("hello" != 11111 and a < b)
print("11" <= "1" or "1" == "11")
print("11" == 11 or "world" == 11)



