# 1. Сторонняя библиотека requests (на примере Яндекс-карт)

from requests import get
from PIL import Image

# Запрос к Яндекс.Карт посредством Static API (бесплатная версия)
#ll (latitude and longitude): координаты центра карты (долгота, широта)
#spn (span): масштаб карты (горизонт. и вертик. диапазоны)
#l (layer): слой карты (map - обычная, sat - спутниковая, skl - схема)
response = get('https://static-maps.yandex.ru/1.x/?'
               'll=30.313139,59.940783&'
               'spn=0.0075,0.0021&'
               'l=map')

#Создание файла с расширением .png и запись ответа с сервера в файл
with open('map.png', 'wb') as file:
    file.write(response.content)
# Вывод карты
map = Image.open('map.png')
map.show()


# 2. Сторонняя библиотека pandas (на примере журнала успеваемости учеников)

import pandas as pd

# Необходимо:
#             1. Определить средний балл каждого ученика
#             2. Определить наилучшего ученика
#             3. Определить средний балл группы

# Создание непосредственно в коде журнала успеваемости (таблица sql)
data = {
    'id_ученика': [1, 2, 3, 1, 2, 3, 1, 2, 3],
    'Имя_ученика': ['Иван', 'Мария', 'Петр', 'Иван', 'Мария',
                    'Петр', 'Иван', 'Мария', 'Петр'],
    'Оценка': [4, 5, 3, 5, 4, 4, 3, 5, 4]}

# Создание DataFrame - двумерной таблицы, основной структуры данных в библиотеке
grades_df = pd.DataFrame(data)

# Определение среднего балла каждого ученика
average_grades = grades_df.groupby(['id_ученика', 'Имя_ученика'])['Оценка'].mean().reset_index()
average_grades.rename(columns={'Оценка': 'Средний балл'}, inplace=True)

# Определение наилучшего ученика
best_student = average_grades.loc[average_grades['Средний балл'].idxmax()]

# Определение среднего балла группы и печать результата
group_average = average_grades['Средний балл'].mean()

print(f'Средний балл учеников:')
print(round(average_grades,2))
print('Наилучший ученик:')
print(f'{best_student['Имя_ученика']}, средний балл: {best_student['Средний балл']:.2f}')
print(f'Средний балл всей группы: {group_average:.2f}')


# 3. Библиотека numpy (на примере матриц)
# с библиотекой matplotlib для визуализации результата

import numpy as np
import matplotlib.pyplot as plt

# Есть 2 склада, в которых находятся по три вида товаров - 1, 2, 3.
# Есть данные по количеству товара на складах на начало и конец года, а также его стоимость
# Необходимо:
#       1. Определить и напечатать общий остаток товара каждого вида
#       2. Определить  и напечатать выручку от проданного товара
#       3. Вывести выручку по каждому товару в виде гистограммы

# Создание матрицы товара на складах: строки - склады, столбцы - товар
# Количество товара на начало года
product_start = np.array([[50, 30, 20],
                          [40, 20, 60]])
# Количество товара на конец года
product_end = np.array([[15, 20, 5],
                        [25, 10, 50]])

# Матрица стоимости товара
price = np.array([140, 210, 150])

# Определение количества проданного товара (разница строк матриц)
sale_from_warehouse1 = product_start[0] - product_end[0]
sale_from_warehouse2 = product_start[1] - product_end[1]

# Определение выручки от продаж с каждого склада (перемножение матриц)
money_from_warehouse1 = sale_from_warehouse1 * price
money_from_warehouse2 = sale_from_warehouse2 * price

# Определение суммарной выручки
total_money = sale_from_warehouse1 + sale_from_warehouse2

# Печать остатка товара
remains_warehouse1 = product_end[0]
remains_warehouse2 = product_end[1]
print("\nОстаток товара на складах:")
for i in range(len(price)):
    total_remains = remains_warehouse1[i] + remains_warehouse2[i]
    print(f"Товар {i + 1}: {total_remains} единиц")

# Печать выручки
print("Выручка от продаж:")
for i, j in enumerate(total_money):
    print(f"Товар {i + 1}: {j} у.е.")

# Построение гистограммы выручки (легенда, оси, характеристики элементов)
plt.figure(figsize=(6, 6))
product = np.arange(len(price))
bar_width = 0.3

plt.bar(product, total_money, width=bar_width, color= ['red', 'blue', 'forestgreen'])
plt.xlabel('Товары')
plt.ylabel('Выручка (у.е.)')
plt.title('Выручка от продаж')
plt.xticks(product, [f'Товар {i + 1}' for i in product])
plt.grid(axis='y')
# Вывод гистограммы
plt.show()
