import sqlite3

# Создание таблицы Products
def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS Products') # Удаление таблицы Products, если она была создана
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products
                 (id INTEGER PRIMARY KEY, 
                 title TEXT NOT NULL, 
                 description TEXT NOT NULL, 
                 price INTEGER NOT NULL)''')

    # Функция добавления продуктов в таблицу Products
    def add_product(_id, title, description, price):
        cursor.execute('INSERT OR REPLACE INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
                       (_id, title, description, price))
    products = [
        (1, 'Картофель', '77 ккал в 100 г продукта', 2),
        (2, 'Сыр', '450 ккал в 100 г продукта', 3),
        (3, 'Мясо', '150 ккал в 100 г продукта', 4),
        (4, 'Брокколи', '31 ккал в 100 г продукта', 1)
    ]
    # Загрузка данных в таблицу Products циклом с распаковкой кортежей продуктов
    for product in products:
        add_product(*product)
    connection.commit()
    connection.close()

    #Создание таблицы Users
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS Users')# Удаление таблицы Users, если она была создана
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL DEFAULT 1000
        )
    ''')
    connection.commit()
    connection.close()

# Функция добавления пользователей в таблицу Users
def add_user(username, email, age):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    newuser = 'INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)'
    cursor.execute(newuser, (username, email, age, 1000))
    connection.commit()
    connection.close()

# Функция проверки существования пользователя
def is_included(username):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM Users WHERE username = ?', (username,))
    check = cursor.fetchone()
    connection.close()
    return check[0] > 0

# Функция возврата записей из таблицы Products
def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products

# Инициализация базы данных
initiate_db()
# Добавление пользователей по умолчанию (в соответствии с примером в задании)
add_user('newuser', 'user@gmail.com', 33)
add_user('seconduser', 'ex1@gmail.com', 22)
