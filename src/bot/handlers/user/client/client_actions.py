import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hlink

from bot.keyboards import inline as ik
from bot.config.loader import bot, user_data
from bot.services.db import doctor, telegram_user, client
from bot.services.google_calendar.events import create_google_event
from bot.states import ClientRequest
from usersupport.models import Doctor, TelegramUser, Client
from bot.data import text_data as td


async def doctors_list(call: types.CallbackQuery, callback_data: dict):
    try:
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Список врачей",
            reply_markup=await ik.docs_list()
        )
    except:
        await bot.delete_message(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id
        )
        await bot.send_message(
            chat_id=call.message.chat.id,
            text="Список врачей",
            reply_markup=await ik.docs_list()
        )


async def doctor_profile(call: types.CallbackQuery, callback_data: dict):
    m = await bot.send_message(call.message.chat.id, ".")
    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )
    doc_id = callback_data["doc_id"]
    doc_user = await telegram_user.select_user(user_id=doc_id)
    doc: Doctor = await doctor.select_doctor(user=doc_user)
    await bot.send_photo(
        chat_id=call.message.chat.id,
        caption=td.DOCTOR_PROFILE.format(
            name=doc.user.name,
            education=doc.education,
            profession=doc.profession,
            experience=doc.experience
        ),
        photo=doc.photo_id,
        reply_markup=await ik.create_r_to_doc(callback_data=callback_data)
    )
    await bot.delete_message(call.message.chat.id, m.message_id)


async def create_r(call: types.CallbackQuery, callback_data: dict):
    await bot.send_message(
        call.message.chat.id,
        "Ведите свои жалобы"
    )
    await ClientRequest.additional.set()
    user_data[call.message.chat.id].update({
        "doc_id": callback_data["doc_id"]
    })


async def get_client_addition(message: types.Message, state: FSMContext):
    client_usr: TelegramUser = await telegram_user.select_user(user_id=message.chat.id)
    doc_usr = await telegram_user.select_user(user_id=user_data[message.chat.id]["doc_id"])
    cli: Client = await client.select_client(user=client_usr)
    doc: Doctor = await doctor.select_doctor(user=doc_usr)
    addition = message.text
    segodnya = datetime.date.today()
    now = datetime.datetime.now() + datetime.timedelta(minutes=6)
    five_m = now + datetime.timedelta(minutes=15)
    t = {
        "selected_date": (segodnya.year, segodnya.month, segodnya.day),
        "start_time": (now.hour, now.minute),
        "end_time": (five_m.hour, five_m.minute)
    }
    res = create_google_event(
        prediction=f"{cli.ims}\nпредварительный диагноз не поставлен",
        doctor=doc,
        client=cli,
        date_time=t
    )
    await bot.send_message(
        message.chat.id,
        text=hlink("Ссылка на запись", res)
    )
    await state.finish()
