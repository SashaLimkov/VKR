from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.config.loader import bot, user_data
from bot.data import text_data as td
from bot.keyboards import inline as ik
from bot.services import db
from bot.states import TelegramUserRegistration
from bot.utils.cleaner import delete_command_message, delete_messages
from bot.utils.user_menu import send_user_menu
from bot.utils.validators import is_phone_number_valid, is_email_valid

__all__ = [
    "start_command", "reg_client", "get_phone", "check_phone", "check_email"
]

from usersupport.models import TelegramUser


async def start_command(message: types.Message):
    await delete_command_message(message=message)
    user_id = message.chat.id
    user: TelegramUser = await db.select_user(user_id=user_id)
    if user:
        await delete_messages(user_id=user_id)
        await send_user_menu(user=user)
    else:
        sent_message = await bot.send_message(
            chat_id=user_id,
            text=td.CLIENT_REG.format(
                name=message.from_user.first_name
            ),
            reply_markup=await ik.get_reg_menu()
        )
        mes_to_del = [sent_message.message_id]
        user_data[message.from_user.id] = {"messages_to_delete": mes_to_del}
        await TelegramUserRegistration.registration.set()


async def reg_client(call: types.CallbackQuery):
    sent_message = await bot.send_message(
        chat_id=call.message.chat.id,
        text=td.GET_NAME,
    )
    user_data[call.message.chat.id]["messages_to_delete"].append(sent_message.message_id)
    await TelegramUserRegistration.name.set()


async def get_phone(message: types.Message, state: FSMContext):
    sent_message = await bot.send_message(chat_id=message.chat.id, text=td.GET_PHONE)
    user_data[message.chat.id]["messages_to_delete"] += [message.message_id, sent_message.message_id]
    await state.update_data(user_name=message.text)
    await TelegramUserRegistration.phone.set()


async def check_phone(message: types.Message, state: FSMContext):
    if await is_phone_number_valid(message.text):
        await state.update_data(phone=message.text)
        sent_message = await bot.send_message(chat_id=message.chat.id, text=td.GET_EMAIL)
        await TelegramUserRegistration.email.set()
    else:
        sent_message = await bot.send_message(chat_id=message.chat.id, text=td.GET_CORRECT_PHONE)
    user_data[message.chat.id]["messages_to_delete"] += [message.message_id, sent_message.message_id]


async def check_email(message: types.Message, state: FSMContext):
    user_data[message.chat.id]["messages_to_delete"].append(message.message_id)
    if await is_email_valid(message.text):
        sent_message = await bot.send_message(chat_id=message.chat.id, text=td.GET_READY)
        data = await state.get_data()
        name, phone, email = data.get("user_name"), data.get("phone"), message.text
        await db.add_user(
            user_id=message.chat.id,
            name=name,
            phone=phone,
            email=email
        )
        await state.finish()
        await delete_messages(user_id=message.from_user.id)
        user_data[message.chat.id]["messages_to_delete"].append(sent_message.message_id)
    else:
        sent_message = await bot.send_message(chat_id=message.chat.id, text=td.GET_CORRECT_EMAIL)
        user_data[message.chat.id]["messages_to_delete"].append(sent_message.message_id)
