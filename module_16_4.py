from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List, Annotated

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
async def add_user(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
    age: Annotated[int, Path(ge=1, le=120, description="Enter age")]  # валидация с использованием Annotated
):
    new_id = (users[-1].id + 1) if users else 1                       # определение new_id для добавления
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

# PUT-запрос для обновления пользователя (по id)
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
    user_id: Annotated[int, Path(ge=1, le=1000, description="Enter User ID")],
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
    age: Annotated[int, Path(ge=1, le=120, description="Enter age")]): # валидация с использованием Annotated
    for user in users:                                                 # обновление пользователя, если он есть в списке
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail='User was not found')  # если пользователя нет

# DELETE-запрос для удаления пользователя (по id)
@app.delete('/user/{user_id}', response_model=User)
async def delete_user(
    user_id: Annotated[int, Path(ge=1, le=1000, description="Enter User ID")]  # валидация с использованием Annotated
):
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail='User was not found')

# Запуск приложения:
# uvicorn module_16_4:app --reload