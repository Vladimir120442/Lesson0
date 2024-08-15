class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self, new_floor):
        print(f'Здравствуйте, Вы в {self.name}, введите номер нужного Вам этажа')
        new_floor = int(input())
        if 1 < new_floor > self.numbers_of_floors:
            print('Такого этажа не существует')
        else:
            print(*list(range(1, new_floor + 1)), sep='\n')


h1 = House('ЖК "Три пальмы"', 5)
h2 = House('ЖК "Рублевка"', 3)

h1.go_to(1)
h2.go_to(1)
