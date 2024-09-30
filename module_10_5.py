import multiprocessing
from datetime import datetime

RED = "\033[31m"
RESET = "\033[0m"
GREEN = "\033[32m"
RESET = "\033[0m"


def read_info(name):  # Функция чтения файла и записи в список
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())


if __name__ == '__main__':
    # Список файлов из текущей директории
    file_names = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = datetime.now()
    for name in file_names:  # Линейное выполнение функции read_info
        read_info(name)
    end_time = datetime.now()
    print(f'{RED}Линейный вызов за {end_time - start_time} сек.{RESET}')

    # if __name__ == '__main__':
    # all_data =[]
    start_time = datetime.now()
    with multiprocessing.Pool() as pool:  # Многопроцессорное выполнение функции read_info
        pool.map(read_info, file_names)
    end_time = datetime.now()
    print(f'{GREEN}Многопроцессный вызов за {end_time - start_time} сек.{RESET}')
    