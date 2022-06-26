from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.config.loader import bot, user_data
from bot.data import text_data as td
from bot.keyboards import inline as ik
from bot.services import db
from bot.services.google_calendar.calendars import get_calendars
from bot.states import TelegramUserRegistration
from bot.utils.cleaner import delete_user_message, delete_messages
from bot.utils.user_menu import send_user_menu, get_info_from_user_data
from bot.utils.validators import is_phone_number_valid, is_email_valid

__all__ = [
    "start_command", "reg_client", "check_phone", "check_email"
]

from usersupport.models import TelegramUser


async def start_command(message: types.Message):
    await delete_user_message(message=message)
    user_id = message.chat.id
    user: TelegramUser = await db.select_user(user_id=user_id)
    print(await get_calendars())
    if user_id not in user_data:
        user_data[user_id] = {}
    if user:
        await send_user_menu(user=user)
    else:
        mes = await bot.send_message(
            chat_id=user_id,
            text=td.CLIENT_REG.format(
                name=message.from_user.first_name
            ),
            reply_markup=await ik.get_reg()
        )
        await TelegramUserRegistration.registration.set()
        user_data[user_id].update({"last_bot_sent_message": mes.message_id})


async def reg_client(call: types.CallbackQuery):
    await get_panel(message=call.message)


async def handle_reg_menu(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    action = callback_data["action"]
    user_id = call.message.chat.id
    if action == "1":
        await bot.edit_message_text(
            chat_id=user_id,
            message_id=call.message.message_id,
            text=td.GET_NAME
        )
        await TelegramUserRegistration.name.set()
    elif action == "2":
        await bot.edit_message_text(
            chat_id=user_id,
            message_id=call.message.message_id,
            text=td.GET_PHONE
        )
        await TelegramUserRegistration.phone.set()
    elif action == "3":
        await bot.edit_message_text(
            chat_id=user_id,
            message_id=call.message.message_id,
            text=td.GET_EMAIL
        )
        await TelegramUserRegistration.email.set()
    else:
        await state.finish()
        user: TelegramUser = await db.add_user(
            user_id=user_id,
            name=await get_info_from_user_data(user_id, "fio"),
            phone=await get_info_from_user_data(user_id, "phone"),
            email=await get_info_from_user_data(user_id, "email"),
        )
        if not user:
            await call.answer(text=td.ALREADY_REG, show_alert=True)
            await bot.edit_message_text(
                text='.',
                chat_id=user_id,
                message_id=call.message.message_id,
            )
            await get_panel(message=call.message)
        else:
            await bot.edit_message_text(
                chat_id=user_id,
                message_id=user_data[user_id]["last_bot_sent_message"],
                text=td.GET_READY,
                reply_markup=await ik.reg_client()
            )


async def get_name(message: types.Message):
    user_id = message.chat.id
    user_data[user_id].update({
        "fio": message.text
    })
    await delete_user_message(message=message)
    await get_panel(message=message)


async def check_phone(message: types.Message):
    user_id = message.chat.id
    await delete_user_message(message=message)
    if await is_phone_number_valid(message.text):
        user_data[user_id].update({
            "phone": message.text
        })
        await get_panel(message)
    else:
        await bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=user_data[user_id]["last_bot_sent_message"],
            text=td.GET_CORRECT_PHONE
        )
        # need to add cancel btn


async def check_email(message: types.Message):
    user_id = message.chat.id
    await delete_user_message(message)
    if await is_email_valid(message.text):
        user_data[user_id].update({
            "email": message.text
        })
        await get_panel(message)
    else:
        await bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=user_data[user_id]["last_bot_sent_message"],
            text=td.GET_CORRECT_EMAIL
        )


async def get_panel(message):
    await TelegramUserRegistration.registration.set()
    user_id = message.chat.id
    await bot.edit_message_text(
        chat_id=user_id,
        message_id=user_data[user_id]["last_bot_sent_message"],
        text=td.T_USER_REG_MENU.format(
            name=message.chat.first_name,
            fio=await get_info_from_user_data(user_id, "fio"),
            phone=await get_info_from_user_data(user_id, "phone"),
            email=await get_info_from_user_data(user_id, "email"),
        ),
        reply_markup=await ik.get_reg_menu(user_id=user_id)
    )
