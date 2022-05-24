from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.config import config
from bot.data import text_data as td
from bot.config.loader import bot, user_data
from bot.states import DoctorRegistration
from bot.utils import cleaner
from usersupport.models import TelegramUser
from bot.services.db import user
from bot.keyboards import inline as ik
from bot.keyboards import reply as rk


async def setup_doctor_command(message: types.Message):
    await cleaner.delete_command_message(message=message)
    sent_message = await bot.send_message(
        chat_id=message.from_user.id,
        text=td.DOCTOR_REG.format(name=message.from_user.first_name),
        reply_markup=rk.cancel
    )
    await DoctorRegistration.secret_key.set()
    mes_to_del = [sent_message.message_id, message.message_id]
    user_data[message.from_user.id] = {"messages_to_delete": mes_to_del}


async def check_secret_key(message: types.Message, state: FSMContext):
    secret_key = message.text
    user_id = message.from_user.id
    user_data[message.from_user.id]["messages_to_delete"].append(message.message_id)
    if secret_key == config.DOCTOR_SECRET_KEY:
        telegram_user: TelegramUser = await user.select_user(user_id=user_id)
        await bot.send_message(
            chat_id=user_id,
            text=td.DOCTOR_REG.format(
                name=telegram_user.name,
                education="",
                experience="",
                profession=""
            ),
            reply_markup=await ik.setup_doctor(state=state)
        )
        await state.finish()
        await cleaner.delete_messages(user_id=user_id)
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
