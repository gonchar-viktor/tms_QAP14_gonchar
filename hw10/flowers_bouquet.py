#
# Цветочница.
#
# Определить иерархию и создать несколько цветов. Собрать букет с
# использованием аксессуаров с определением его стоимости.
#
# Определить время его увядания по среднему времени жизни всех цветов в букете.
#
# Позволить сортировку цветов стоимости.
#
# Узнать, есть ли цветок в букете.

class Flower:
    def __init__(self, name_flower, cost_flower, flower_withering_time):
        # название, цена, время жизни
        self.name_flower = name_flower
        self.cost_flower = cost_flower
        self.flower_withering_time = flower_withering_time

    def name(self):
        return self.name_flower

    def cost(self):
        return self.cost_flower

    def time(self):
        return self.flower_withering_time


class Chamomile(Flower):  # Ромашка
    def __init__(self):
        super().__init__("Chamomile", 3, 120)


class Rose(Flower):  # Роза
    def __init__(self):
        super().__init__("Rose", 5, 96)


class Tulip(Flower):  # Тюльпан
    def __init__(self):
        super().__init__("Tulip", 4, 72)


print()
cham = Chamomile()
ros = Rose()
tul = Tulip()

# Сбор букета с определением стоимости
bouquet = [cham, ros, ros, tul, tul, tul]
the_cost_of_the_bouquet = sum(i.cost() for i in bouquet)
print("The cost of the bouquet:", the_cost_of_the_bouquet, "Br")

# Определение времени увядания букета

time = sum(i.time() for i in bouquet) / len(bouquet)
print("Average wilting time:", time, "hours")

# Сортировка цветов по стоимости

sorted_bouquet = sorted(bouquet, key=lambda i: i.cost(), reverse=True)
print("Sorting colors by cost in descending order", [i.name_flower for i in
                                                     sorted_bouquet])

# Проверка, есть ли цветок в букете

flower_name1 = "Chamomile"
flower_name2 = "Windows 10"
flower_name3 = "Tulip"
print()
check = any(i.name() == flower_name1 for i in bouquet)
print(f"Flower \"{flower_name1}\" there is in the bouquet: {check}")
check = any(i.name() == flower_name2 for i in bouquet)
print(f"Flower \"{flower_name2}\" there is in the bouquet: {check}")
check = any(i.name() == flower_name3 for i in bouquet)
print(f"Flower \"{flower_name3}\" there is in the bouquet: {check}")
print()
print("Roses in a bouquet:", bouquet.count(ros), "pieces")
print("Chamomiles in a bouquet:", bouquet.count(tul), "pieces")
print("Tulips in a bouquet:", bouquet.count(cham), "pieces")
