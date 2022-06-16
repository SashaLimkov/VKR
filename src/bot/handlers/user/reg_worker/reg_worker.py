from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.config import config
from bot.config.loader import bot, user_data
from bot.services.db import select_user
from bot.services.db.rworker import add_rworker, update_chanel_id, get_rworker
from bot.states import RWorkerRegistration
from bot.utils import cleaner
from bot.keyboards import reply as rk


async def setup_rworker_command(message: types.Message):
    await cleaner.delete_user_message(message=message)
    sent_message = await bot.send_message(
        chat_id=message.chat.id,
        text="Введите секретный ключ",
        reply_markup=rk.cancel
    )
    await RWorkerRegistration.secret_key.set()
    mes_to_del = [sent_message.message_id, message.message_id]
    user_data[message.from_user.id] = {"messages_to_delete": mes_to_del}


async def check_secret_key(message: types.Message, state: FSMContext):
    secret_key = message.text
    user_id = message.from_user.id
    user_data[message.from_user.id]["messages_to_delete"].append(message.message_id)
    if secret_key == config.RW_SECRET_KEY:
        await bot.send_message(
            chat_id=message.chat.id,
            text="Регистрация прошла успешно"
        )
        user = await select_user(message.from_user.id)
        await add_rworker(user=user, chanel_chat_id=message.chat.id)
        await state.finish()
    elif secret_key == "Отмена":
        await cleaner.delete_messages(user_id=user_id)
        sent_message = await bot.send_message(
            chat_id=user_id,
            text="Свяжитесь с администратором или напишите /start"
        )
        user_data[user_id]["messages_to_delete"].append(sent_message.message_id)
        await state.finish()
    else:
        sent_message = await bot.send_message(
            chat_id=user_id,
            text="Введенный не корректный ключ"
        )
        user_data[user_id]["messages_to_delete"].append(sent_message.message_id)


async def update_chanel(message: types.Message):
    user_id = message.from_user.id
    user = await select_user(user_id=user_id)
    rw = await get_rworker(user)
    if rw:
        chanel_id = message.reply_to_message.forward_from_chat.id
        await update_chanel_id(user=user, chanel_id=chanel_id)


async def all(message: types.Message):
    pass