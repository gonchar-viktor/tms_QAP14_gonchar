# +
# 1 Создать lambda функцию, которая принимает на вход
# имя и выводит его в формате “Hello, {name}”

a = lambda name: f"Hello {name}"
print(a("Viktor"))

# 2 Создать lambda функцию, которая принимает на вход
# список имен и выводит их в формате “Hello, {name}” в
# другой список

spisok = ["Viktor", "Elena", "Venya", "Alex"]
m = list(map(lambda x: f'Hello {x}', spisok))
print("spisok:", m)
