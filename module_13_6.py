from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from module_13_6_new import inline_kb

api = '###'

bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

#Создание инлайн-клавиатуры
inline_kb = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data = 'calories')
button2 = InlineKeyboardButton(text = 'Формулы расчета', callback_data = 'formulas')
inline_kb.row(button1, button2)

@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup = inline_kb)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('Формула Миффлина - Сан Жеора '
                         'для расчета суточной нормы калорий для мужчин: '
                         'Calories = 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5)',
                          reply_markup = inline_kb)
    await call.answer()

#Класс состояния (возраст, рост, вес)
class UserStates(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserStates.age.set()
    await call.answer()

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

    await message.answer(f'Ваша норма калорий - {calories} ккал')

    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
