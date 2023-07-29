from aiogram import types
from aiogram.dispatcher.filters import Text
import random
from loader import dp
@dp.message_handler(Text(equals='профиль'))
async def show_profile(message:types.Message):
    await message.answer('Ваш профиль:/n'
                         f'Имя пользователя: {message.from_user.username}/n'
                         f'Имя: {message.from_user.first_name}/n')

@dp.message_handler(Text(equals='рандомное число'))
async def random_number(message:types.Message):
    await message.answer(random.randint(0, 5000))
@dp.message_handler(Text(equals='картинка'))
async def picture(message:types.Message):
    url = 'https://mymodernmet.com/wp/wp-content/uploads/2022/10/meetissai-internet-cat-sculptures-1.jpg'
    await message.answer_photo(
        photo=url,
        caption='очень смешня картинка'

    )


