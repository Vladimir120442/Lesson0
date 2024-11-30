from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

api = '***'

bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Создание первичного меню с добавление кнопки 'Купить'
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button11 = KeyboardButton(text='Рассчитать')
button22 = KeyboardButton(text='Информация')
button33 = KeyboardButton(text='Купить')
kb.row(button11, button22)
kb.add(button33)

@dp.message_handler(commands=['start'])
async def start_cmd(message):
    await message.answer('👋 Привет! Я - бот, помогающий твоему здоровью.\n'
                         'Для расчета калорий нажми "Рассчитать".\n'
                         'Для получения информации - "Информация".\n'
                         'Для покупки товаров - "Купить"', reply_markup=kb)

# Вывод по кнопке "Информация" из первичного меню. Добавлена info о покупке
@dp.message_handler(text='Информация')
async def inf0_bot(message):
    await message.answer('Я - бот, помогающий твоему здоровью. '
                         'Я рассчитываю твою суточную норму калорий '
                         'по формуле Миффлина - Сан Жеора.\n'
                         'Я также помогу тебе купить продукты.', reply_markup=kb)

# Создание Inline-клавиатуры
inline_kb = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')
inline_kb.row(button1, button2)

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=inline_kb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формула Миффлина - Сан Жеора '
                              'для расчета суточной нормы калорий\n для мужчин:\n '
                              'Calories = 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5, \n'
                              'для женщин:\n'
                              'Calories = 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161',
                              reply_markup=inline_kb)
    await call.answer()

# Класс состояния (возраст, рост, вес)
class UserStates(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.callback_query_handler(text='calories')
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
    # Запись в переменную data ранее введенные состояния машины
    data = await state.get_data()

    # Расчет нормы калорий по формуле Миффлина-Сан Жеора для мужчин
    calories = int((10 * float(data['Вес'])) +
                   (6.25 * float(data['Рост'])) -
                   (5 * float(data['Возраст'])) + 5)

    await message.answer(f'Ваша норма калорий - {calories} ккал')
    await state.finish()

# Дополнение кода в соответствии с условиями задачи
# Создание Inline-клавиатуры. Создаем функцией; если клавиатура может потребоваться
# в других частях бота, достаточно будет вызвать только функцию
def get_inline_products():
    inline_kb_products = InlineKeyboardMarkup()
    button3 = InlineKeyboardButton(text='Продукт 1', callback_data='product_buying')
    button4 = InlineKeyboardButton(text='Продукт 2', callback_data='product_buying')
    button5 = InlineKeyboardButton(text='Продукт 3', callback_data='product_buying')
    button6 = InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')
    inline_kb_products.row(button3, button4, button5, button6)
    return inline_kb_products

# Создание ассортимента продуктов (кортежи)
products = [
        ('Картофель', '77 ккал в 100 г продукта', 2, 'files_products/prod_photo_1.png'),
        ('Сыр', '450 ккал в 100 г продукта', 3, 'files_products/prod_photo_2.png'),
        ('Мясо', '150 ккал в 100 г продукта', 4, 'files_products/prod_photo_3.png'),
        ('Брокколи', '31 ккал в 100 г продукта', 1, 'files_products/prod_photo_4.png')
    ]

# Обработка кнопки 'Купить' из первичного меню
@dp.message_handler(text='Купить')
async def get_buying_list(message):
    #Вывод информации о продуктах (распаковка кортежей циклом)
    for product in products:
        name, descr, number, photo = product
        await message.answer(f"Название: {name} | Описание: {descr} | Цена: {number * 100}")
        await message.answer_photo(photo=open(photo, 'rb'))
    await message.answer("Выберите продукт для покупки:", reply_markup=get_inline_products())

# Обработка Inline-кнопок
@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)