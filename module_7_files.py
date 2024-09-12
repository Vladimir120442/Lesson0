import os
import time


print('Текущая директория: ', os.getcwd())
directory = "."
# обход всех дисков, директорий на пути к directory и файлам в ней
for root, dirs, files in os.walk('.'):
    for i in files:
        # формирование полного пути к файлам (объединение пути в одно имя)
        path_file = os.path.join(root, i)

        # получение и отображение времени
        # последней модификации файла в читаемом формате
        time_file = os.path.getmtime(path_file)
        time_format = time.strftime("%d.%m.%Y %H:%M", time.localtime(time_file))

        # получение размера файла
        filesize = os.path.getsize(path_file)

        # определение родительской директории файла
        parent_dir = os.path.dirname(path_file)

        # вывод результата
        print(f'Обнаружен файл: {i}, '
              f'Путь: {path_file}, '
              f'Размер: {filesize} байт, '
              f'Время изменения: {time_format}, '
              f'Родительская директория: {parent_dir}')

