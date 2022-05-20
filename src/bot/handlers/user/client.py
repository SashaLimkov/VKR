from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.config.loader import bot
from bot.keyboards import inline as ik
from bot.data import text_data as td
from bot.states import TelegramUserRegistration
from bot.services import db
from bot.utils.validators import is_phone_number_valid, is_email_valid

__all__ = [
    "start_command", "reg_client", "get_phone", "check_phone", "check_email"
]


async def start_command(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=td.CLIENT_REG,
        reply_markup=await ik.get_reg_menu()
    )


async def reg_client(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text=td.GET_NAME,
    )
    await TelegramUserRegistration.name.set()


async def get_phone(message: types.Message, state: FSMContext):
    await state.update_data(user_name=message.text)
    await bot.send_message(chat_id=message.chat.id, text=td.GET_PHONE)
    await TelegramUserRegistration.phone.set()


async def check_phone(message: types.Message, state: FSMContext):
    if await is_phone_number_valid(message.text):
        await state.update_data(phone=message.text)
        await bot.send_message(chat_id=message.chat.id, text=td.GET_EMAIL)
        await TelegramUserRegistration.email.set()
    else:
        await bot.send_message(chat_id=message.chat.id, text=td.GET_CORRECT_PHONE)


async def check_email(message: types.Message, state: FSMContext):
    if await is_email_valid(message.text):
        await bot.send_message(chat_id=message.chat.id, text=td.GET_READY)
        data = await state.get_data()
        name, phone, email = data.get("user_name"), data.get("phone"), message.text
        await db.add_user(
            user_id=message.chat.id,
            name=name,
            role=None,
            phone=phone,
            email=email
        )
    else:
        await bot.send_message(chat_id=message.chat.id, text=td.GET_CORRECT_EMAIL)
