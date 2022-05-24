from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.config import config
from bot.config.loader import bot, user_data
from bot.data import text_data as td
from bot.keyboards import inline as ik
from bot.keyboards import reply as rk
from bot.services.db import telegram_user, doctor
from bot.services.google_calendar.calendars import create_calendar
from bot.states import DoctorRegistration
from bot.utils import cleaner
from usersupport.models import TelegramUser


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
        await get_panel(message=message, state=state)
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


async def handle_info(call: types.CallbackQuery):
    callback = call.data.replace("doc_", "")
    if callback == "edu":
        sent_message = await bot.send_message(
            chat_id=call.message.chat.id,
            text=td.GET_EDUCATION
        )
        await DoctorRegistration.education.set()

    elif callback == "exp":
        sent_message = await bot.send_message(
            chat_id=call.message.chat.id,
            text=td.GET_EXPERIENCE
        )
        await DoctorRegistration.experience.set()
    elif callback == "prof":
        sent_message = await bot.send_message(
            chat_id=call.message.chat.id,
            text=td.GET_PROFESSION
        )
        await DoctorRegistration.profession.set()
    else:
        sent_message = await bot.send_message(
            chat_id=call.message.chat.id,
            text=td.GET_PHOTO
        )
        await DoctorRegistration.photo.set()
    user_data[call.message.chat.id]["messages_to_delete"].append(sent_message.message_id)


async def get_education(message: types.Message, state: FSMContext):
    user_data[message.chat.id]["messages_to_delete"].append(message.message_id)
    education = message.text
    user_data[message.chat.id].update({"education": education})
    await get_panel(message=message, state=state)


async def get_experience(message: types.Message, state: FSMContext):
    user_data[message.chat.id]["messages_to_delete"].append(message.message_id)
    experience = message.text
    user_data[message.chat.id].update({"experience": experience})
    await get_panel(message=message, state=state)


async def get_profession(message: types.Message, state: FSMContext):
    user_data[message.chat.id]["messages_to_delete"].append(message.message_id)
    profession = message.text
    user_data[message.chat.id].update({"profession": profession})
    await get_panel(message=message, state=state)


async def get_photo(message: types.Message, state: FSMContext):
    user_data[message.chat.id]["messages_to_delete"].append(message.message_id)
    photo = message.photo[-1].file_id
    user_data[message.chat.id].update({"photo": photo})
    await add_doc_to_database(user_id=message.chat.id, state=state)


async def add_doc_to_database(user_id, state: FSMContext):
    tg_user: TelegramUser = await telegram_user.select_user(user_id=user_id)
    calendar = create_calendar(f"{user_data[user_id]['profession']} {tg_user.name}")
    await doctor.add_doctor(
        user=tg_user,
        education=user_data[user_id]["education"],
        experience=user_data[user_id]["experience"],
        profession=user_data[user_id]["profession"],
        photo_id=user_data[user_id]["photo"],
        calendar_id=calendar["id"]
    )
    await cleaner.delete_messages(user_id=user_id)
    tg_user: TelegramUser = await telegram_user.select_user(user_id=user_id)
    sent_message = await bot.send_photo(
        chat_id=user_id,
        caption=td.DOCTOR_PROFILE.format(
            name=tg_user.name,
            education=user_data[user_id]["education"],
            experience=user_data[user_id]["experience"],
            profession=user_data[user_id]["profession"],
        ),
        photo=user_data[user_id]["photo"],
        reply_markup=await ik.doctor_pp()
    )
    user_data[user_id]["messages_to_delete"].append(sent_message.message_id)
    await state.finish()


async def get_panel(message: types.Message, state: FSMContext):
    user_id = message.chat.id
    await cleaner.delete_messages(user_id=user_id)
    tg_user: TelegramUser = await telegram_user.select_user(user_id=user_id)
    sent_message = await bot.send_message(
        chat_id=user_id,
        text=td.DOCTOR_REG_MENU.format(
            name=tg_user.name,
            education=user_data[user_id]["education"] if "education" in user_data[user_id] else "",
            experience=user_data[user_id]["experience"] if "experience" in user_data[user_id] else "",
            profession=user_data[user_id]["profession"] if "profession" in user_data[user_id] else "",
        ),
        reply_markup=await ik.setup_doctor(user_id=user_id)
    )
    user_data[user_id]["messages_to_delete"].append(sent_message.message_id)
    await state.finish()
