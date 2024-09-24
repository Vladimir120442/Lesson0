import time
from threading import Thread
from datetime import datetime

RED = "\033[31m"
RESET = "\033[0m"
GREEN = "\033[32m"
RESET = "\033[0m"


# Создание функции для записи в file_name (example*.txt)
def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file_write:
        for i in range(1, word_count + 1):
            file_write.write(f'Какое-то слово № {i} + \n')
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")
    return write_words


# Взятие текущего времени для замера старта функции
start_time = datetime.now()

# Запуск функции с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени для замера завершения работы функции
end_time = datetime.now()
# Время работы функции
rez_time = (end_time - start_time).total_seconds()
print(f'{RED}Функция сработала 4 раза за {rez_time:.2F} сек.{RESET}')

# Создание потоков с аргументами из задачи
flow_1 = Thread(target=write_words, args=(10, 'example5.txt'))
flow_2 = Thread(target=write_words, args=(30, 'example6.txt'))
flow_3 = Thread(target=write_words, args=(200, 'example7.txt'))
flow_4 = Thread(target=write_words, args=(100, 'example8.txt'))
# Запуск и завершение потоков с подсчетом времени их работы
start_time = datetime.now()

flow_1.start()
flow_2.start()
flow_3.start()
flow_4.start()

flow_1.join()
flow_2.join()
flow_3.join()
flow_4.join()

end_time = datetime.now()
rez_time = (end_time - start_time).total_seconds()
print(f'{GREEN}Время работы функции в четырех потоках - {rez_time:.2F} сек.{RESET}')
