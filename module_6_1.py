class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible is True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
            return self.fed
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
            return self.alive


class Plant:
    edible = False  # Несъедобное растение

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)


class Predator(Animal):

    def __init__(self, name):
        super().__init__(name)


class Flower(Plant):
    edible = False  # Несъедобный цветок


class Fruit(Plant):
    edible = True  # Съедобный фрукт


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)  # Хищник не стал есть несъедобную пищу и умер от голода
print(a2.fed)  # Млекопитающее сытое после еды
