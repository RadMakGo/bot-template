from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("meme", "отправить рандомную шутку"),
            types.BotCommand("magic_8_ball", "совет от магического шара"),
            types.BotCommand("time", "показывает время в Москве и в Лос-Анджелесе и Лондоне"),
            types.BotCommand("info", "показывает информацию про ваш аккаунт"),
            types.BotCommand("meme_photos","показывает очень смешную картинку")
        ]
    )
