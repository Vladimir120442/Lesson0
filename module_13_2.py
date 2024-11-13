import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

# Ввод токена
api = '####################################'

# Создание экземпляров бота и диспетчера
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())

# Функция обработки команды /start
@dp.message(Command('start'))
async def start(message: types.Message):
    print('Привет! Я бот, помогающий твоему здоровью.')

# Функция обработки сообщений
@dp.message()
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')

# Запуск бота
async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    asyncio.run(main())

