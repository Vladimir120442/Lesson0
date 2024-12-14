from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Создание класса User
class User(BaseModel):
    id: int
    username: str
    age: int

# Создание пустого списка пользователей
users: List[User] = []

# GET-запрос для возвращения списка пользователей
@app.get('/users', response_model=List[User])
async def get_users():
    return users

# POST-запрос для добавления пользователя
@app.post('/user/{username}/{age}', response_model=User)
async def add_user(username: str, age: int):
    new_id = (users[-1].id + 1) if users else 1 # определение new_id для добавления
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

# PUT-запрос для обновления пользователя (по id)
@app.put('/user/{user_id}', response_model=User)
async def update_user(user_id: int, username: str, age: int):
    for user in users:               # обновление пользователя, если он есть в списке
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail='User was not found') # если пользователя нет

# DELETE-запрос для удаления пользователя (по id)
@app.delete('/user/{user_id}', response_model=User)
async def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail='User was not found')

# Запуск приложения:
# uvicorn module_16_4:app --reload