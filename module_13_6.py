from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


api = '7827008035:AAHswPvdhgDahRmGtUE4NQFNBUIMbw9cw5k'

bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

#Создание первичного меню
kb = ReplyKeyboardMarkup(resize_keyboard = True)
button1 = KeyboardButton(text = 'Рассчитать')
button2 = KeyboardButton(text = 'Информация')
kb.add(button1)
kb.add(button2)
@dp.message_handler(commands=['start'])
async def start_cmd(message):
    await message.answer('Привет! Я - бот, помогающий твоему здоровью.                                 '
                         'Для расчета калорий нажми "Рассчитать", '
                         'для получения информации - "Информация"', reply_markup = kb)
#Вывод по кнопке "Информация" из первичного меню
@dp.message_handler(text = 'Информация')
async def inf0_bot(message):
    await message.answer('Я - бот, помогающий твоему здоровью.'
                         'Я рассчитываю твою суточную норму калорий '
                         'по формуле Миффлина - Сан Жеора', reply_markup = kb)

#Создание инлайн-клавиатуры
kb1 = InlineKeyboardMarkup()
button3 = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data = 'calories')
button4 = InlineKeyboardButton(text = 'Формулы расчета', callback_data = 'formulas')
kb1.add(button3)
kb1.add(button4)
@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup = kb1)

@dp.callback_query_handler(text = 'formylas')
async def get_formulas(call):
    await call.message.answer('Формула Миффлина - Сан Жеора '
                         'для расчета суточной нормы калорий для мужчин: '
                         'Calories = 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5)',
                          reply_markup = kb1)
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

    await message.answer(f'Твоя суточная норма - {calories} ккал')

    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
