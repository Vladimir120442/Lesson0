from fastapi import FastAPI, Path
from typing import Annotated, Dict

app = FastAPI()

# Создание словаря users
users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}

# GET запрос для возвращения словаря (все пользователи)
# с использованием параметра response_model для корректного возвращения словаря
@app.get('/users', response_model=Dict[str, str])
async def get_users():
    return users

# POST запрос для добавления пользователя
@app.post('/user/{username}/{age}')
async def add_user(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
    age: Annotated[int, Path(ge=1, le=120, description="Enter age")]): # валидация
    new_id = str(max(map(int, users.keys()), default=0) + 1) # определение new_id для добавления
    users[new_id] = f'Имя: {username}, возраст: {age}'
    return f'User {new_id} is registered'

# PUT запрос для обновления пользователя (по id)
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
    user_id: Annotated[int, Path(ge=1, le=1000, description="Enter User ID")],
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
    age: Annotated[int, Path(ge=1, le=120, description="Enter age")]): # валидация
    id_search = str(user_id)
    if id_search in users:
        users[id_search] = f'Имя: {username}, возраст: {age}'
        return f"User {user_id} has been updated"

# DELETE запрос для удаления пользователя (по id)
@app.delete('/user/{user_id}')
async def delete_user(
    user_id: Annotated[int, Path(ge=1, le=1000, description="Enter User ID")]): # валидация
    id_search = str(user_id)
    if id_search in users:
        del users[id_search]
        return f"User {user_id} has been deleted"

# Запуск приложения:
# uvicorn module_16_3:app --reload


