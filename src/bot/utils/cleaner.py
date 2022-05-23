from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.config.loader import bot, user_data


async def delete_command_message(message: types.Message):
    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id
    )


async def delete_messages(user_id):
    message_id_list = user_data[user_id]["messages_to_delete"]
    for mes_id in message_id_list:
        try:
            await bot.delete_message(
                chat_id=user_id,
                message_id=mes_id
            )
        except Exception as e:
            print(e)
    user_data[user_id]["messages_to_delete"] = []
