from aiogram import types
from aiogram.dispatcher.filters import Command
import random
from loader import dp
answer = ['Yes','No','Ask again later',' Yes — definitely']
@dp.message_handler(Command('magic_8_ball'))
async def magic_8_ball_cmd(message:types.Message):
    await message.answer(random.choice(answer))
