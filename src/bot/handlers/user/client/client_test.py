from aiogram import types

from bot.config.loader import bot
from bot.keyboards import inline as ik


async def send_test(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Изменился ли ваш аппетит?",
        reply_markup=await ik.test()
    )
