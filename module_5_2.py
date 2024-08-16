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


h1 = House('ЖК "Три пальмы"', 5)
h2 = House('ЖК "Рублевка"', 3)

h1 = House('ЖК "Эльбрус"', 10)
h2 = House('ЖК "Акация"', 20)

#h1.go_to(3)
#h2.go_to(2)
print(h1)
print(h2)
print(len(h1))
print(len(h2))
