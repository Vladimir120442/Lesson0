class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self, new_floor):
        # print(f'Здравствуйте, Вы в {self.name}, введите номер нужного Вам этажа')
        # new_floor = int(input())
        if 1 < new_floor > self.numbers_of_floors:
            print('Такого этажа не существует')
        else:
            print(*list(range(1, new_floor + 1)), sep='\n')

    def __str__(self):
        return (f'Название: {self.name}, количество этажей: {self.numbers_of_floors}')

    def __len__(self):
        return self.numbers_of_floors

    def __check__(self, other):
        other = other.numbers_of_floors
        if not isinstance(other, int) and not isinstance(other, House):
            print('Переменная не относится ни к типу "int", ни к классу "House"')

    def __eq__(self, other):
        self.__check__(other)
        return self.numbers_of_floors == other.numbers_of_floors

    def __lt__(self, other):
        self.__check__(other)
        return self.numbers_of_floors < other.numbers_of_floors

    def __le__(self, other):
        self.__check__(other)
        return self.numbers_of_floors <= other.numbers_of_floors

    def __gt__(self, other):
        self.__check__(other)
        return self.numbers_of_floors > other.numbers_of_floors

    def __ge__(self, other):
        self.__check__(other)
        return not self.__eq__(other)

    def __add__(self, value):
        if not isinstance(value, int):
            print('Переменная не относится к типу "int"')
        self.numbers_of_floors = self.numbers_of_floors + value
        return self

    def __radd__(self, value):
        if not isinstance(value, int):
            print('Переменная не относится к типу "int"')
        return self.__add__(value)

    def __iadd__(self, value):
        if not isinstance(value, int):
            print('Переменная не относится к типу "int"')
        return self.__add__(value)


#  h1 = House('ЖК "Три пальмы"', 5)
#  h2 = House('ЖК "Рублевка"', 3)

h1 = House('ЖК "Эльбрус"', 10)
h2 = House('ЖК "Акация"', 20)

# h1.go_to(3)
# h2.go_to(2)
print(h1)
print(h2)
# print(len(h1))
# print(len(h2))
print(h1 == h2)
h1 = h1 + 10
print(h1)
print(h1 == h2)
h1 += 10
print(h1)
h2 = 10 + h2
print(h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 <= h2)
print(h1 != h2)
