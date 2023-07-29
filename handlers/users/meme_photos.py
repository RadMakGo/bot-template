from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
@dp.message_handler(Command('meme_photos'))
async def meme_photo(message:types.Message):
    url = 'https://mymodernmet.com/wp/wp-content/uploads/2022/10/meetissai-internet-cat-sculptures-1.jpg'
    await message.answer_photo(
        photo=url,
        caption='очень смешня картинка'

    )