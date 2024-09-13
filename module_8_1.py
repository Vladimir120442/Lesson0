def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (float, int)):
            result = a + b
            print('Ошибок нет')
            return f'{result:.3f}'
        if type(a) != type(b):
            result = a + b
            return result
        if isinstance(a, str) and isinstance(b, str):
            result = str(a) + ' ' + str(b)
            print('Ошибок нет')
            return result
    except TypeError as exc:
        print(f'Вот такая ошибка:  {exc}')
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('ПОДСТРОКА', 789.45))
print(add_everything_up('яблоко', 'тыква'))
print(add_everything_up(123.456, 7))
