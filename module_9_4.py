# Составление lambda-функции
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = map(lambda x, y: x == y, first, second)
print(list(result))

# Замыкание
from pprint import pprint


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file_write:
            for elements in data_set:
                file_write.write(str(elements) + '\n')

    return write_everything


# Создание файла, запись в него data_set  и чтение
write = get_advanced_writer('example.txt')
write('Очередной запуск кода', 'Это строчка',
      ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
with open('example.txt', 'r', encoding='utf-8') as file_read:
    file_read = file_read.read()
pprint(file_read)

# Метод __call__
from random import choice


class MysticBall:
    def __init__(self, *words: str):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('РАСКИНУЛОСЬ', 'МОРЕ', 'ШИРОКО')
print(first_ball())
print(first_ball())
print(first_ball())
