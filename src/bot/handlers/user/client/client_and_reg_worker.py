from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hlink

from bot.config.loader import bot
from bot.data import text_data as td
from bot.keyboards import inline as ik

from bot.services.db import rworker, client, telegram_user, doctor
from bot.utils.docx_creator import get_docx
from usersupport.models import RegWorker, Client, TelegramUser, Doctor


async def skip_test(call: types.CallbackQuery, state: FSMContext):
    await call.answer(text="Происходит процесс записи, пожалуйста подождите 5 секунд", show_alert=True, cache_time=7)
    data = await state.get_data()
    cd = data.get("cd")
    user: TelegramUser = await telegram_user.select_user(user_id=call.message.chat.id)
    doc = await doctor.select_doctor_by_id(cd["doc_id"])
    doc: Doctor = doc[0]
    tg_client: Client = await client.select_client(user=user)
    rwokers = await rworker.get_all_rworker()
    rw: RegWorker = rwokers[0]
    text = td.TEXT_TO_RW.format(
        fio=user.name,
        phone=user.phone,
        email=user.email,
        doc=doc.profession + " " + doc.user.name,
        date=cd["date"],
        time=cd["time"],
        timetable=hlink("распиание", doc.calendar_id)
    )
    await bot.send_document(
        chat_id=rw.chanel_id,
        caption=text,
        document=get_docx(tg_client),
        reply_markup=await ik.test()
    )
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="В ближайшее время с вами свяжутся, ожидайте"
    )
