from bot.config.loader import bot, user_data
from bot.services.db.client import select_client
from bot.services.db.doctor import select_doctor
from usersupport.models import TelegramUser
from bot.data import text_data as td
from bot.keyboards import inline as ik


async def send_user_menu(user: TelegramUser):
    doctor = await select_doctor(user=user)
    client = await select_client(user=user)
    if doctor:
        sent_message = await bot.send_photo(
            chat_id=user.user_id,
            caption=td.DOCTOR_PROFILE.format(
                name=user.name,
                education=doctor.education,
                experience=doctor.experience,
                profession=doctor.profession,
            ),
            photo=doctor.photo_id,
            reply_markup=await ik.doctor_pp()
        )
        user_data[user.user_id]["messages_to_delete"].append(sent_message.message_id)
    elif client:
        sent_message = await bot.send_message(
            chat_id=client.user.user_id,
            # message_id=call.message.message_id,
            text=td.CLIENT_PROFILE.format(name=client.user.name),
            reply_markup=await ik.client_actions()
        )
        user_data[user.user_id]["messages_to_delete"].append(sent_message.message_id)

    else:
        sent_message = await bot.send_message(
            chat_id=user.user_id,
            text=td.GET_READY,
            reply_markup=await ik.reg_client()
        )
        user_data[user.user_id]["messages_to_delete"].append(sent_message.message_id)
