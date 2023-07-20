#  +++ Словари

# 1. Создайте словарь, связав его с переменной school, и наполните его
# данными, которые бы отражали количество учащихся в десяти разных классах
# (например, 1а, 1б, 2б, 6а, 7в и т.д.).

def variable_school():
    """
    create a dictionary by associating it with the school variable, and fill
    it with data that would reflect the number of students in ten different
    classes
    """
    global school
    school = {"1a": 20, "2a": 21, "3a": 22, "4a": 23, "5a": 24, "1б": 25,
              "2б": 26, "3б": 27, "4б": 28, "5б": 29}
    return f"классы и количество учеников в них: {school}"


print(variable_school().replace(",", "\n").replace("{", "\n ").replace("}",
                                                                       "\n "))


# 2. Узнайте сколько человек в каком-нибудь классе.

def number_of_students():
    """
    find out how many people are in any class.
    :return: 2a class
    """
    a = school["2a"]
    return f"в классе 2а: {a} ученик"


print(number_of_students())
print()


# 3. Представьте, что в школе произошли изменения, внесите их в словарь:
# ◦ в трех классах изменилось количество учащихся;
# ◦ в школе появилось два новых класса;
# ◦ в школе расформировали один из классов.

def changes_in_the_school():
    """
    there have been changes in the school, add them to the dictionary:
    the number of students in three classes has changed;
    the school has two new classes;
    one of the classes was disbanded at the school.
    """
    school["1a"], school["2a"], school["3a"] = 19, 20, 21
    school["1в"], school["2в"] = 30, 31
    del school["5б"]
    return f"изменённые классы: {school}"


print(changes_in_the_school().replace(",", "\n").replace("{", "\n ").replace
      ("}", "\n "))

# 4. Выведите содержимое словаря на экран.

print(school)
