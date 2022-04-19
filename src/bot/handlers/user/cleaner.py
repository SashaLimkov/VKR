from aiogram import types

from bot.config.loader import bot


async def clean_s(message: types.Message):
    await bot.delete_message(
        chat_id=message.from_user.id, message_id=message.message_id
    )
