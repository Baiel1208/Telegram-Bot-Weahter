from aiogram import Bot, Dispatcher, types, executor
import random

bot = Bot("6264543307:AAF6wZgO9AnTs239BJ52Z_K_GJRjgtLbF-U")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.answer("Я загадал число от 1 до 3, отгадай: ")


@dp.message_handler(text=['1', '2', '3'])
async def play(message:types.Message):
    num = random.randint(1, 3)
    if int(message.text) == num:
        await message.reply('Вы угадали!')
    else:
        await message.reply(f'Неправильно. Число было {num}.')


executor.start_polling(dp)