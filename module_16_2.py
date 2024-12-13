from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
# Маршрут к главной странице
@app.get('/')
async def read_root():
    return 'Главная страница'

# Маршрут к странице администратора
@app.get('/user/admin')
async def read_admin():
    return 'Вы вошли как администратор'

# Маршрут к странице пользователя (по id) + ВАЛИДАЦИЯ (1 <= id <= 100)
@app.get('/user/{user_id}')
async def read_user(
    user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')]
):
    return f'Вы вошли как пользователь № {user_id}'

# Маршрут к страницам пользователей
# с передачей данных о них в адресной строке + ВАЛИДАЦИЯ
# (Username содержит от 5 до 20 символов, 18 <= age <= 120)
@app.get('/user')
async def read_user_info(
    username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
    age: Annotated[int, Path(ge=18, le=120, description='Enter age')]
):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'

# user_id = 55
# username=UrbanUser
# age=42
# 1. Запуск приложения:
#    uvicorn module_16_2:app --reload
# 2. Доступ к документации:
#    Swagger UI — http://127.0.0.1:8000/docs
# 3. Доступ по id —  http://127.0.0.1:8000/user/55
# 4. Доступ с передачей данных — http: //127.0.0.1:8000/user?username=UrbanUser&age=42

