class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Plant:
    edible = False #Несъедобный цветок
    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def eat(self, food):
        if food.edible is True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
            return self.fed
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
            return self.alive


class Predator(Animal):
    def eat(self, food):
        if food.edible is True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
            return self.fed
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
            return self.alive


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

print(a1.alive)  # До еды живой
print(a2.fed)  # До еды голодный
a1.eat(p1)
a2.eat(p2)
print(a1.alive)  # Хищник после еды неживой
print(a2.fed)  # Млекопитающее после еды сытое
