class Car:
    def __init__(self, model: str, vin_number: int, numbers: str):
        self.model = model

        if self.__is_valid_vin(vin_number):     #вызов __is_valid_vin и __is_valid_numbers
            self.__vin_number = vin_number      #для корректного создания атрибутов класса
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int):
            pass
        else:
            raise IncorrectVinNumber('Некорректный тип vin номера')
        if 1000000 <= vin_number <= 9999999:
            pass
        else:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):        #вариант проверки на корректность через оператор not
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if not len(numbers) == 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

try:
    third = Car('Model3', 2020202, 14)
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

try:
    third = Car('Model3', 'vin_number', 'р737ум')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')