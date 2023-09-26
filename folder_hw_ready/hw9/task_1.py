# +
# Придумать класс и методы к нему, использовать:
# - инкапсуляцию
# - полиморфизм
# - наследование
# -----------------------------------------------------------------------------
# 0. создать минимум два класса. Один класс будет родитель и несколько
# наследников
# 1. реализовать конструкторы для инициализации
# 2. реализовать вывод данных в основном и дополнительном классе
# 3. реализовать полиморфизм (перегрузка и переопределение)
# 4. реализовать инкапсуляцию методов и свойств
# -----------------------------------------------------------------------------
class Parent:
    def __init__(self, name, age, work, city):
        self.name = name
        self.age = age
        self.work = work
        self.city = city
        self.__secret = "\n*** Hi, tell me about yourself! ***\n"
        print(self.__secret)

    def bye(self, bye):
        if bye is True:
            print("method overrides")
        else:
            print("method overrides")


class Worker(Parent):
    def __init__(self, name, age, work, experience, employee_position,
                 salary, city, life_plans=None):
        super().__init__(name, age, work, city)
        self.experience = experience
        self.employee_position = employee_position
        self.salary = salary
        self.life_plans = life_plans

        print(
            f"Hi, my name is {name}.\nI`m {age}, and i am work as a {work}.\n"
            f"I have {experience} of experience and i am a"
            f" {employee_position}\nMy salary is {salary} Br\n"
            f"I live in {city}")

        if life_plans is not None:
            print(f"I plan to - {life_plans}.")

    def bye(self, bye):
        if bye is True:
            print("I hope that's enough, goodbye!\n")
        else:
            print("What else can I tell you?")


class Student(Parent):
    def __init__(self, name, age, work, course, place_of_study, city,
                 life_plans=None):
        super().__init__(name, age, work, city)
        self.course = course
        self.place_of_study = place_of_study
        self.life_plans = life_plans
        print(f"Hi, my name is {name}.\nI'm {age} and I am a {work}.\nI'm in"
              f" the {course} year at {place_of_study}\n"
              f"I live in {city}.")

        if life_plans is not None:
            print(f"I plan to - {life_plans}.")

    def bye(self, bye):
        if bye is True:
            print("I hope that's enough, goodbye!\n")
        else:
            print("What else can I tell you?")


a = Worker("Vasya", 21, "cook", "6 year", "chef", 2000, "Minsk")
a.bye(True)
b = Student("Zhenya", 18, "student", "2nd", "'MGY'", "Brest", "finish my "
                                                              "studies with a "
                                                              "red diploma "
                                                              "and move to "
                                                              "another city")
b.bye(False)
