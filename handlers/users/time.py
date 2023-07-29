from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from datetime import datetime
import pytz
moscow_tz = pytz.timezone('Europe/Moscow')
Los_Angeles_tz = pytz.timezone('America/Los_Angeles')
London_tz = pytz.timezone('Europe/London')
time = {'Moscow':datetime.now(tz=moscow_tz) ,'Los Angels': datetime.now(tz=Los_Angeles_tz),'London': datetime.now(tz=London_tz)}

@dp.message_handler(Command('time'))
async def time_cmd(message:types.Message):
    await message.answer(f'''Moscow - {time['Moscow']}
Los Angels - {time['Los Angels']}
London - {time['London']}''')