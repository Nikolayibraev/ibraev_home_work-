from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = '  '  # Замените на ваш токен
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()                # состояния
    weight = State()
    gender = State()



@dp.message_handler (text = ['Calories'])


async def set_gender (message):
    await message.answer ('Введите ваш пол')
    await UserState.gender.set()                        # ожидание ввода пользователя

@dp.message_handler (state = UserState.gender)
async def set_age (message, state):
    await state.update_data(gender = message.text)
    await message.answer ('Укажите ваш взраст')
    await UserState.age.set()


@dp.message_handler (state = UserState.age)
async def set_growth (message, state):
    await state.update_data(age = int(message.text))
    await message.answer ('Введите ваш рост')
    await UserState.growth.set()

@dp.message_handler (state = UserState.growth)
async def weight (message, state):
    await state.update_data(growth = int(message.text))
    await message.answer ('Введите ваш вес')
    await UserState.weight.set()


@dp.message_handler (state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = int(message.text))
    data = await state.get_data ()

    gender = data['gender']
    weight = data['weight']
    growth = data['growth']       #данные из состояния
    age = data['age']

    if gender == 'мужчина':
        answ = 10 * weight + 6.25 * growth - 5 * age + 5
    else:
        answ = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f'Ваша норма калорий: {answ} ккал в день.')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)