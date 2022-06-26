from aiogram import types

from bot.config.loader import bot, user_data
from bot.data.list_data import TEST
from bot.keyboards import inline as ik


async def start_test(call: types.CallbackQuery):
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="Тест состоит из двух этапов.\n"
             "1) 11 вопросов на выявление основной пораженной системы"
             "2) неограниченное количество вопросов на выявления предполагаемого заболевания.",
        reply_markup=await ik.start_test()
    )


async def test_q(call: types.CallbackQuery):
    answer = call.data.replace("answer_", "")
    if "answers" not in user_data[call.message.chat.id]:
        user_data[call.message.chat.id].update({"answers": ""})
    user_data[call.message.chat.id]["answers"] += answer
    print(user_data[call.message.chat.id]["answers"])
    if len(user_data[call.message.chat.id]["answers"]) == len(TEST):
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Первый этап теста пройден. Начинаем второй этап?",
            reply_markup= await ik.second_stage()
        )
    else:
        await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=TEST[len(user_data[call.message.chat.id]["answers"])],
            reply_markup=await ik.test_q()
        )
