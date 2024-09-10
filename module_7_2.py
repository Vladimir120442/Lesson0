import io
from pprint import pprint


def custom_write(file_name, strings):
    # словарь: ключ - номер строки, байт; значение - содержание строки
    strings_positions = {}
    # начальный номер строки
    number_str = 1
    # заполнение словаря
    name_f = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        number_byte = name_f.tell()
        name_f.write(i + '\n')
        strings_positions[(number_str, number_byte)] = i
        number_str += 1
    name_f.close()
    return strings_positions


# Пример использования функции.
strings = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', strings)
for elem in result.items():
    print(elem)

test_txt = open('test.txt', 'r', encoding='utf-8')
test_txt = test_txt.read()
print("\n\nВывод на печать "
      "файла test.txt после запуска:")
print(test_txt)