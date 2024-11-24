import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Удаление таблицы Users, если она была создана
cursor.execute('DROP TABLE IF EXISTS Users')

# Созание новой таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
# Заполнение новой таблицы
for i in range(10):
   cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                  (f'User{i+1}', f'example{i+1}@gmail.com', i*10+10, 1000))
# Индексируем по email
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# Удаление каждой 3-й записи, начиная с 1-й
cursor.execute('DELETE FROM Users WHERE id % 3 = 1;')

# Выборка всех записей, где возраст не равен 60
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60;')
records = cursor.fetchall()

# Распаковка кортежей (построчно) и вывод результата
for j in records:
    username, email, age, balance = j
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')


connection.commit()
connection.close()