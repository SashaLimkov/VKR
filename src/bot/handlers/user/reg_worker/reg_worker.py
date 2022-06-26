import datetime
import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hlink

from bot.config import config
from bot.config.loader import bot, user_data, dp
from bot.services.db import select_user, user_request, client, telegram_user, doctor
from bot.services.db.rworker import add_rworker, update_chanel_id, get_rworker
from bot.services.google_calendar.events import create_google_event
from bot.states import RWorkerRegistration
from bot.utils import cleaner
from bot.keyboards import reply as rk
from usersupport.models import UserRequest, TelegramUser, Doctor, Client
from bot.keyboards import inline as ik


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


async def accept(call: types.CallbackQuery):
    r_id = call.data.replace("agree_", "")
    await call.answer()
    r: UserRequest = await user_request.get_request(r_id)
    cli: Client = r.client
    doc: Doctor = await doctor.select_doctor_by_id(doc_id=r.doc_id)
    addition = ""
    day, month = r.date.split(".")
    hour, minute = r.time.split("-")
    segodnya = datetime.date.today()
    now = datetime.datetime.now() + datetime.timedelta(minutes=6)
    five_m = datetime.datetime(day=int(day), month=int(month), year=segodnya.year, hour=int(hour),
                               minute=int(minute)) + datetime.timedelta(minutes=15)
    t = {
        "selected_date": (segodnya.year, int(month), int(day)),
        "start_time": (int(hour), int(minute)),
        "end_time": (five_m.hour, five_m.minute)
    }
    res = create_google_event(
        prediction=f"{cli.ims}\nпредварительный диагноз не поставлен",
        doctor=doc,
        client=cli,
        date_time=t,
        file_name=r.file_name
    )
    await bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=None
    )
    await call.answer(
        text="Запись подтверждена"
    )
    await bot.send_message(
        chat_id=cli.user.user_id,
        text=hlink("Ссылка на запись", res)
    )


async def cancel(call: types.CallbackQuery):
    r_id = call.data.replace("cancel_", "")
    await call.answer()
    r: UserRequest = await user_request.get_request(r_id)
    cli: Client = r.client
    await bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=None
    )
    os.remove(r.file_name)
    await bot.send_message(
        chat_id=cli.user.user_id,
        text="Ваша запись отклонена"
    )


async def edit(call: types.CallbackQuery):
    r_id = call.data.replace("edit_", "")
    await call.answer()
    r: UserRequest = await user_request.get_request(r_id)
    cli: Client = r.client
    await bot.send_message(
        chat_id=call.message.chat.id,
        text=f"Для изменения записи перейдите в {hlink('админ панель', 'http://127.0.0.1:8000/admin/usersupport/userrequest/')}."
    )