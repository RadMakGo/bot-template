from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(row_width=3,resize_keyboard=True, keyboard=[
    [KeyboardButton(text='профиль')],
    [KeyboardButton(text='рандомное число')],
    [KeyboardButton(text='картинка')]

])