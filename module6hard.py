import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = sides
        self.filled = False

    #геттер и сеттер цвета, проверки корректности цвета
    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return r, g, b
        else:
            print('Такого цвета не существует')

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    # геттер и сеттер сторон с созданием массива с единичными сторонами
    def __is_valid_sides(self, *sides):
        for i in sides:
            if isinstance(i, int) and i > 0 and len(sides) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print('Некорректное  количество  сторон')


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        if len(sides) == 1:  # проверка количества переданных сторон
            sides = [*sides] * self.sides_count
        else:
            self.sides = [1] * self.sides_count
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        square = math.pi * self.__radius ** 2
        return square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if len(sides) == 1:  # проверка количества переданных сторон
            sides = [*sides] * self.sides_count
        else:
            self.sides = [1] * self.sides_count
        super().__init__(color, *sides)

    # проверка треугольника на вырожденность и вычисление площади
    def get_square(self):
        sides = self.get_sides()
        if (sides[0] + sides[1] > sides[2]
            and sides[0] + sides[2] > sides[1]
            and sides[1] + sides[2] > sides[0]):
            p = sum(sides) / 2
            square = math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))
            return square
        else:
            pass


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:  # проверка количества переданных сторон
            sides = [*sides] * self.sides_count
        else:
            self.sides = [1] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        side_len = self.get_sides()[0]
        volume = side_len ** 3
        return volume


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
