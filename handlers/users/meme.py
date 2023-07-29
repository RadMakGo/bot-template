from aiogram import types
from aiogram.dispatcher.filters import Command
import random
from loader import dp
memes = ['What did the horse say after it tripped? : Help! I’ve fallen and I can’t giddyup!',
         'Where do polar bears keep their money? : In a snowbank.']
@dp.message_handler(Command('meme'))
async def meme_cmd(message:types.Message):
    await message.answer(random.choice(memes))