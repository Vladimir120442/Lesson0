def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    RED = '\033[91m'
    RESET = '\033[0m'
    for symbol in numbers:
        try:
            result += symbol
        except TypeError as exc:
            print(f'Символ {RED}{symbol}{RESET} некорректен для подсчета суммы, {exc}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    RED = '\033[91m'
    UNDERLINE = '\033[93m'  # '\033[4m'
    RESET = '\033[0m'
    try:
        result, incorrect_data = personal_sum(numbers)
        # average_sum = result
        correct_data = len(numbers) - incorrect_data  # количество чисел для подсчета среднего значения суммы
        return result / correct_data
    except ZeroDivisionError as exc:
        # print(f'Вот такая ошибка - деление на ноль:  {exc}')
        return 0
        return result / correct_data
    except TypeError as exc:
        print(f'{UNDERLINE}Тип данных не является коллекцией и некорректен для подсчета суммы{RESET}')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
