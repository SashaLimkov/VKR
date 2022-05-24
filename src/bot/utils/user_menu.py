from bot.config.loader import bot, user_data
from bot.services.db.doctor import select_doctor
from usersupport.models import TelegramUser
from bot.data import text_data as td
from bot.keyboards import inline as ik


async def send_user_menu(user: TelegramUser):
    doctor = await select_doctor(user=user)
    if doctor:
        sent_message = await bot.send_photo(
            chat_id=user.user_id,
            caption=td.DOCTOR_PROFILE.format(
                name=user.name,
                education=user_data[user.user_id]["education"],
                experience=user_data[user.user_id]["experience"],
                profession=user_data[user.user_id]["profession"],
            ),
            photo=user_data[user.user_id]["photo"],
            reply_markup=await ik.doctor_pp()
        )
        user_data[user.user_id]["messages_to_delete"].append(sent_message.message_id)
    else:
        sent_message = await bot.send_message(chat_id=user.user_id, text=td.GET_READY)
        user_data[user.user_id]["messages_to_delete"].append(sent_message.message_id)
