# -------------- T E L E G R A M  B O T --------------

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ' '
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

# Перехват сообщений, указанных в text
# @dp.message_handler (text = ['urban','hello'])
# async def bot_message(message):
#     print('Слушаю вас внимательно')

# Выполнение команд
@dp.message_handler (commands = ['start'])
async def start(message):
#    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

# Перехват всех сообщений
@dp.message_handler()
async def all_messages(message):
#    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)