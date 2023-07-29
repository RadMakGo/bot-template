from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
@dp.message_handler(Command('info'))
async def info_cmd(message:types.Message):
    await message.answer(f'<i> your account id - {message.from_user.id}</i>')
    await message.answer(f'<b> your account name - {message.from_user.first_name}</b>')
    await message.answer(f'<i> your account last name - {message.from_user.last_name}</i>')
    await message.answer(f'<b> your account username - {message.from_user.username}</b>')
    await message.answer(f'<a href = "https://clck.ru/3vyXS"> ХИХИХА</a>')