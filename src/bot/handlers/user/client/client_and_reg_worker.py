from time import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hlink

from bot.config.loader import bot, user_data
from bot.data import text_data as td
from bot.keyboards import inline as ik

from bot.services.db import rworker, client, telegram_user, doctor, user_request
from bot.services.fuzzy_test.main import get_fuzzy_ill_system
from bot.utils.docx_creator import get_docx
from bot.utils.medical_utils import get_recomendations
from usersupport.models import RegWorker, Client, TelegramUser, Doctor, UserRequest


async def skip_test(call: types.CallbackQuery, state: FSMContext):
    await call.answer(text="Происходит процесс записи, пожалуйста подождите 5 секунд", show_alert=True, cache_time=7)
    data = await state.get_data()
    cd = data.get("cd")
    print(user_data)
    user_data[call.message.chat.id]["cd"] = cd
    user: TelegramUser = await telegram_user.select_user(user_id=call.message.chat.id)
    doc = await doctor.select_doctor_by_id(cd["doc_id"])
    doc: Doctor = doc[0]
    tg_client: Client = await client.select_client(user=user)
    rwokers = await rworker.get_all_rworker()
    rw: RegWorker = rwokers[0]
    if "answers" in user_data[call.message.chat.id]:
        answers = user_data[call.message.chat.id]["answers"]
        user_answers = {
            "temp": answers[0],
            "skin_t": answers[1],
            "lymph": answers[2],
            "weakness": answers[3],
            "edema": answers[4],
            "nausea": answers[5],
            "stiffness": answers[6],
            "noj": answers[7],
            "back_pain": answers[8],
            "mus_pain": answers[9],
            "cancer": answers[10],
        }
        res = get_fuzzy_ill_system(user_answers)
        recomendations = get_recomendations(res)
        await client.update_prediction(user=user, recomendations=recomendations)
        sleep(1)
    file_name = get_docx(tg_client)
    document = open(f'{file_name}', mode='rb')
    date = cd["date"]
    time = cd["time"]
    r: UserRequest = await user_request.add_request(client=tg_client, date=date, time=time, doc_id=doc.id,
                                                    file_name=file_name)
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
        document=document,
        reply_markup=await ik.accept(r_id=r.id)
    )
    document.close()
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="В ближайшее время с вами свяжутся, ожидайте"
    )
