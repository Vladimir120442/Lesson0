from pprint import pprint
def introspection_info(obj):

    #Список значений для словаря
    obj_type = []
    obj_attributes = []
    obj_methods = []
    obj_module =[]

    # Определяем тип объекта - функция type() + встроенрый метод __name__
    obj_type = type(obj).__name__

    # Проверяем наличие атрибутов и их значений у 'obj',
    # а также является ли 'obj' вызываемым и каким методом.
    # Записываем значения в словарь
    for attr in dir(obj):
        if hasattr(obj, attr) and callable(getattr(obj, attr)):
            obj_methods.append(attr)
        else:
            obj_attributes.append(attr)

    # Определяем модуль объекта
    obj_module = obj.__module__

    # Записываем в словарь ключ: значение
    dict = {'type': obj_type,
        'attributes': obj_attributes,
        'methods': obj_methods,
        'module': obj_module}
    return dict

# В качестве примера используем класс 'House' из задания 'module_5_2.py'
class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self, new_floor):
        if 1 < new_floor > self.numbers_of_floors:
            print('Такого этажа не существует')
        else:
            print(*list(range(1, new_floor + 1)), sep='\n')

    def __str__(self):
        return (f'Название: {self.name}, количество этажей: {self.numbers_of_floors}')


h1 = House('ЖК "Три пальмы"', 5)
h2 = House('ЖК "Рублевка"', 3)
print(h1)
print(h2)

#Вывод на консоль:
h1_introspect = introspection_info(h1)
#h2_introspect = introspection_info(h1)
pprint(h1_introspect)
#pprint(h2_introspect)

