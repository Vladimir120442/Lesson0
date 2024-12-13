from fastapi import FastAPI

app = FastAPI()
# Маршрут к главной странице
@app.get('/')
async def read_root():
    return 'Главная страница'

# Маршрут к странице администратора
@app.get('/user/admin')
async def read_admin():
    return 'Вы вошли как администратор'

# Маршрут к странице пользователя (по id)
@app.get('/user/{user_id}')
async def read_user(user_id: int):
    return f'Вы вошли как пользователь № {user_id}'

# Маршрут к страницам пользователей
# с передачей данных о них в адресной строке
@app.get('/user')
async def read_user_info(username: str, age: int):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'

# user_id = 1050764
# username=Vladimir
# age=42
# 1. Запуск приложения:
#    uvicorn module_16_1:app --reload
# 2. Доступ к документации:
#    Swagger UI — http://127.0.0.1:8000/docs
# 3. Доступ по id —  http://127.0.0.1:8000/user/1050764
# 4. Доступ с передачей данных — http: //127.0.0.1:8000/user?username=Vladimir&age=42

