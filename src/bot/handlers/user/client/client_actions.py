import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hlink

from bot.keyboards import inline as ik
from bot.config.loader import bot, user_data
from bot.services.db import doctor, telegram_user, client
from bot.services.google_calendar.events import create_google_event
from bot.states import ClientRequest
from bot.utils.user_menu import get_info_from_user_data
from usersupport.models import Doctor, TelegramUser, Client
from bot.data import text_data as td


async def doctors_list(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
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
    await state.finish()


async def doctor_profile(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    m = await bot.send_message(call.message.chat.id, ".")
    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )
    doc_id = callback_data["doc_id"]
    doc: Doctor = await doctor.select_doctor_by_id(doc_id)
    doc = doc[0]
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


async def choose_datetime(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    user_id = call.message.chat.id
    await bot.delete_message(
        chat_id=user_id,
        message_id=call.message.message_id,
    )
    if "hour" in user_data[user_id] and "min" in user_data[user_id]:
        user_data[user_id]["time"] = f"{user_data[user_id]['hour']}-{user_data[user_id]['min']}"
        await ClientRequest.waiting_for_answer.set()
    await bot.send_message(
        chat_id=user_id,
        text=td.CHOSEN_DATETIME.format(
            date=await get_info_from_user_data(user_id=user_id, key="date"),
            time=await get_info_from_user_data(user_id=user_id, key="time")
        ),
        reply_markup=await ik.choose_datetime(callback_data, user_id)
    )
    # await ClientRequest.additional.set()
    # user_data[call.message.chat.id].update({
    #     "doc_id": callback_data["doc_id"]
    # })


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


async def choose_date(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="Выберите дату",
        reply_markup=await ik.get_calendar_keyboard(callback_data)
    )


async def choose_hour(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    user_id = call.message.chat.id
    await bot.edit_message_text(
        chat_id=user_id,
        message_id=call.message.message_id,
        text="Выберите час приема",
        reply_markup=await ik.get_hours(callback_data)
    )


async def choose_min(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    user_id = call.message.chat.id
    await bot.edit_message_text(
        chat_id=user_id,
        message_id=call.message.message_id,
        text="Выберите минуты приема",
        reply_markup=await ik.get_min(callback_data)
    )


async def choose_time(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    user_id = call.message.chat.id
    await bot.edit_message_text(
        chat_id=user_id,
        message_id=call.message.message_id,
        text=td.CHOSEN_HOUR_MIN.format(
            hour=await get_info_from_user_data(user_id=user_id, key="hour"),
            min=await get_info_from_user_data(user_id=user_id, key="min")
        ),
        reply_markup=await ik.get_hour_min(callback_data)
    )


async def save_date(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    user_id = call.message.chat.id
    user_data[user_id]["date"] = callback_data["date"]
    await bot.edit_message_text(
        chat_id=user_id,
        message_id=call.message.message_id,
        text=td.CHOSEN_DATETIME.format(
            date=await get_info_from_user_data(user_id=user_id, key="date"),
            time=await get_info_from_user_data(user_id=user_id, key="time")
        ),
        reply_markup=await ik.choose_datetime(callback_data, user_id)
    )


async def save_time(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    user_id = call.message.chat.id
    user_data[user_id]["time"] = callback_data["time"]
    await bot.edit_message_text(
        chat_id=user_id,
        message_id=call.message.message_id,
        text=td.CHOSEN_DATETIME.format(
            date=await get_info_from_user_data(user_id=user_id, key="date"),
            time=await get_info_from_user_data(user_id=user_id, key="time")
        ),
        reply_markup=await ik.choose_datetime(callback_data, user_id)
    )


async def save_hour(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    user_id = call.message.chat.id
    user_data[user_id]["hour"] = callback_data["hour"]
    await bot.edit_message_text(
        chat_id=user_id,
        message_id=call.message.message_id,
        text=td.CHOSEN_HOUR_MIN.format(
            hour=await get_info_from_user_data(user_id=user_id, key="hour"),
            min=await get_info_from_user_data(user_id=user_id, key="min")
        ),
        reply_markup=await ik.get_hour_min(callback_data)
    )


async def save_min(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    user_id = call.message.chat.id
    user_data[user_id]["min"] = callback_data["minute"]
    await bot.edit_message_text(
        chat_id=user_id,
        message_id=call.message.message_id,
        text=td.CHOSEN_HOUR_MIN.format(
            hour=await get_info_from_user_data(user_id=user_id, key="hour"),
            min=await get_info_from_user_data(user_id=user_id, key="min")
        ),
        reply_markup=await ik.get_hour_min(callback_data)
    )


async def skip_test_or_no(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    user_id = call.message.chat.id
    doc: Doctor = await doctor.select_doctor_by_id(callback_data["doc_id"])
    doc = doc[0]
    await state.update_data(
        cd=callback_data
    )
    await bot.edit_message_text(
        chat_id=user_id,
        message_id=call.message.message_id,
        text=td.SKIP_TEST_OR_NOT.format(
            doc=doc.user.name,
            date=callback_data["date"],
            time=callback_data["time"]
        ),
        reply_markup=await ik.skip_test_or_no(callback_data)
    )



