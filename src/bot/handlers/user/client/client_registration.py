from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.config.loader import bot, user_data
from bot.data import text_data as td
from bot.services.db import telegram_user, client
from bot.keyboards import inline as ik
from bot.states import ClientRegistration
from bot.utils import cleaner
from bot.utils.cleaner import delete_user_message
from bot.utils.medical_utils import get_ims
from bot.utils.user_menu import get_info_from_user_data
from usersupport.models import TelegramUser


async def start_client(call: types.CallbackQuery):
    await get_panel(call.message)


async def start_register_client(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    action = callback_data["action"]
    user_id = call.message.chat.id
    if action == "1":
        await bot.edit_message_text(
            chat_id=user_id,
            message_id=user_data[user_id]["last_bot_sent_message"],
            text=td.GET_GENDER,
            reply_markup=await ik.gender()
        )
    elif action == "2":
        await bot.edit_message_text(
            chat_id=user_id,
            message_id=user_data[user_id]["last_bot_sent_message"],
            text=td.GET_HEIGHT
        )
        await ClientRegistration.height.set()

    elif action == "3":
        await bot.edit_message_text(
            chat_id=user_id,
            message_id=user_data[user_id]["last_bot_sent_message"],
            text=td.GET_WEIGHT
        )
        await ClientRegistration.weight.set()

    elif action == "4":
        await bot.edit_message_text(
            chat_id=user_id,
            message_id=user_data[user_id]["last_bot_sent_message"],
            text=td.GET_AGE
        )
        await ClientRegistration.age.set()
    else:
        await state.finish()
        await confirm_data(call)


async def get_sex(call: types.CallbackQuery):
    sex_data = call.data.replace("sex_", "")
    sex = "М" if sex_data == "m" else "Ж"
    user_data[call.message.chat.id].update({"sex": sex})
    await get_panel(call.message)


async def get_height(message: types.Message):
    height = message.text
    user_data[message.chat.id].update({"height": height})
    await delete_user_message(message=message)
    await get_panel(message=message)


async def get_weight(message: types.Message):
    weight = message.text
    user_data[message.chat.id].update({"weight": weight})
    await delete_user_message(message=message)
    await get_panel(message=message)


async def get_age(message: types.Message):
    age = message.text
    user_data[message.chat.id].update({"age": age})
    await delete_user_message(message=message)
    await get_panel(message=message)


async def get_panel(message: types.Message):
    user_id = message.chat.id
    tg_user: TelegramUser = await telegram_user.select_user(user_id=user_id)
    await bot.edit_message_text(
        chat_id=user_id,
        message_id=user_data[user_id]["last_bot_sent_message"],
        text=td.CLIENT_REG_MENU.format(
            name=tg_user.name,
            gender=await get_info_from_user_data(user_id=user_id, key="sex"),
            height=await get_info_from_user_data(user_id=user_id, key="height"),
            weight=await get_info_from_user_data(user_id=user_id, key="weight"),
            age=await get_info_from_user_data(user_id=user_id, key="age"),
        ),
        reply_markup=await ik.setup_client(user_id=user_id)
    )
    await ClientRegistration.registration.set()


async def confirm_data(call: types.CallbackQuery):
    user_id = call.message.chat.id
    tg_user: TelegramUser = await telegram_user.select_user(user_id=user_id)
    gender = await get_info_from_user_data(user_id=user_id, key="sex")
    height = await get_info_from_user_data(user_id=user_id, key="height")
    weight = await get_info_from_user_data(user_id=user_id, key="weight")
    age = await get_info_from_user_data(user_id=user_id, key="age")
    ims = await get_ims(height=height, weight=weight)
    await client.add_client(user=tg_user, gender=gender, height=height, weight=weight, age=age, ims=ims)
    await client_act_menu(call=call)


async def client_act_menu(call: types.CallbackQuery):
    user_id = call.message.chat.id
    tg_user: TelegramUser = await telegram_user.select_user(user_id=user_id)
    await bot.edit_message_text(
        chat_id=user_id,
        message_id=call.message.message_id,
        text=td.CLIENT_PROFILE.format(name=tg_user.name),
        reply_markup=await ik.client_actions()
    )
