from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
from aiogram.utils import executor

api = '###################################'

bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

#Класс состояния (возраст, рост, вес)
class UserStates(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start_cmd(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью. '
                         'Набери /Calories для начала расчета')

@dp.message_handler(commands=['Calories'])
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserStates.age.set()

@dp.message_handler(state=UserStates.age)
async def set_growth(message, state):
   await state.update_data(Возраст=message.text)
   await message.answer("Введите свой рост:")
   await UserStates.next()

@dp.message_handler(state=UserStates.growth)
async def set_weight(message, state):
    await state.update_data(Рост=message.text)
    await message.answer("Введите свой вес:")
    await UserStates.next()

@dp.message_handler(state=UserStates.weight)
async def send_calories(message, state):
    await state.update_data(Вес=message.text)
    #Запись в переменную data ранее введенные состояния машины
    data = await state.get_data()

    # Расчет нормы калорий по упрощенной формуле Миффлина-Сан Жеора для мужчин
    calories = int((10 * float(data['Вес'])) +
                   (6.25 * float(data['Рост'])) -
                   (5 * float(data['Возраст'])) + 5)

    await message.answer(f"Ваша суточная норма калорий: {calories} ккал")

    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

