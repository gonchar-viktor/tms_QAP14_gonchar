class Employee:
    working_years = 0

    def __init__(self, years, salary):
        self.years = years
        self.salary = salary

    def experience(self):
        self.years += 1

    def allowance(self):
        self.salary




class Person:
    species = 'Homo sapiens'

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    @staticmethod
    def speak(text):
        print(f'{text}')

    def print_name(self):
        print(self.name)
    def grown_up(self):
        self.age += 1

    def change_weight(self, kg):
        self.weight = kg

    def info(self):
        print(f'{self.name}: age = {self.age}, '
              f'weight = {self.weight}')

    @classmethod
    def print_species(cls):
        print(cls.species)


person1 = Person('Adam', 0, 3)
person1.print_species()
person1.print_name()
person1.grown_up()
person1.grown_up()
person1.grown_up()
person1.grown_up()
person1.grown_up()
#
person1.change_weight(35)

person1.speak('Hello')
person1.info()

