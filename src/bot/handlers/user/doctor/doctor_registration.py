from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.config import config
from bot.data import text_data as td
from bot.config.loader import bot
from bot.states import DoctorRegistration


async def setup_doctor_command(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=td.DOCTOR_REG.format(name=message.from_user.first_name)
    )
    await DoctorRegistration.secret_key.set()

# async def check_secret_key(message: types.Message):
#     secret_key = message.text
#     if secret_key == config.DOCTOR_SECRET_KEY:
#         await bot.send_message(
#             chat_id=message.from_user.id
#         )
