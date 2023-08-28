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
    def __init__(self, core="core"):
        self.core = core
        super().__init__("Chamomile", 3, 120)

    def chamomile_core(self):
        return f"Chamomile has a pronounced and large {self.core}."


class Rose(Flower):  # Роза
    def __init__(self, thorns="thorns"):
        self.thorns = thorns
        super().__init__("Rose", 5, 96)

    def rose_thorns(self):
        return f"A rose differs from other flowers in that it " \
               f"has{self.thorns}."


class Tulip(Flower):  # Тюльпан
    def __init__(self, pollen="pollen"):
        self.pollen = pollen
        super().__init__("Tulip", 4, 72)

    def tulip_pollen(self):
        return f"There is a lot of {self.pollen} in a tulip."


print()
cham = Chamomile()
ros = Rose()
tul = Tulip()


# Сбор букета с определением стоимости
def bouquet_flower():
    global bouquet
    bouquet = [cham, ros, ros, tul, tul, tul]
    cost_accessories = 3  # аксессуар ленточка
    the_cost_of_the_bouquet = sum(i.cost() for i in bouquet)
    print("The cost of the bouquet:", the_cost_of_the_bouquet +
          cost_accessories, "Br")
    print(f"The cost of the ribbon for flowers: {cost_accessories} Br")


bouquet_flower()


# Определение времени увядания букета
def time_flower():
    time = sum(i.time() for i in bouquet) / len(bouquet)
    print("Average wilting time:", time, "hours")


time_flower()


# Сортировка цветов по стоимости
def sort():
    sorted_bouquet = sorted(bouquet, key=lambda i: i.cost(), reverse=True)
    print("Sorting colors by cost in descending order", [i.name_flower for i in
                                                         sorted_bouquet], "\n")


sort()


# Проверка, есть ли цветок в букете
def check_flowers(flower):
    """
    Checks if there is a flower in the bouquet
    """
    check = any(i.name() == flower for i in bouquet)
    print(f"Flower\" {flower}\" there is in the bouquet: {check}")


check_flowers("Chamomile")
check_flowers("Windows 10")
check_flowers("Tulip")
print()


def number_flowers(flower, variable):
    """
    Learns the number of specific flowers in a bouquet
    """
    print(f"{flower} in a bouquet: {bouquet.count(variable)} pieces.")


number_flowers("Chamomiles", cham)
number_flowers("Roses", ros)
number_flowers("Tulips", tul)
print()


def features():
    print("\tFeatures of flowers:")
    print(cham.chamomile_core())
    print(ros.rose_thorns())
    print(tul.tulip_pollen())


features()
