import sqlite3

# Создание таблицы Products
def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    # Удаление таблицы Products, если она была создана
    #cursor.execute('DROP TABLE IF EXISTS Products')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products
                 (id INTEGER PRIMARY KEY, 
                 title TEXT NOT NULL, 
                 description TEXT NOT NULL, 
                 price INTEGER NOT NULL)''')
    cursor.execute('DELETE FROM Products')
    connection.commit()
    connection.close()

    # Функция SQL-запроса добавления данных в таблицу Products
    def add_product(_id, title, description, price):
        connection = sqlite3.connect('products.db')
        cursor = connection.cursor()
        # Обновление предыдущих записей командой INSERT OR REPLACE
        cursor.execute('INSERT OR REPLACE INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
                       (_id, title, description, price))
        connection.commit()
        connection.close()

    products = [
        (1, 'Картофель', '77 ккал в 100 г продукта', 2),
        (2, 'Сыр', '450 ккал в 100 г продукта', 3),
        (3, 'Мясо', '150 ккал в 100 г продукта', 4),
        (4, 'Брокколи', '31 ккал в 100 г продукта', 1)
    ]

    # Загрузка данных в таблицу Products циклом с распаковкой кортежей продуктов
    for product in products:
        add_product(*product)


#Функция возврата записей из таблицы Products
def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products

initiate_db()
get_all_products()