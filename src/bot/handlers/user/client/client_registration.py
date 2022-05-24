from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.config.loader import bot, user_data
from bot.data import text_data as td
from bot.services.db import telegram_user, client
from bot.keyboards import inline as ik
from bot.states import ClientRegistration
from bot.utils import cleaner
from bot.utils.medical_utils import get_ims
from usersupport.models import TelegramUser


async def start_client(call: types.CallbackQuery, state: FSMContext):
    # await bot.delete_message(
    #     chat_id=call.message.chat.id,
    #     message_id=call.message.message_id
    # )
    await get_panel(call.message, state=state)


async def start_register_client(call: types.CallbackQuery):
    callback = call.data.replace("c_", "")
    if callback == "sex":
        sent_message = await bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=td.GET_GENDER,
            reply_markup=await ik.gender()
        )
        user_data[call.message.chat.id]["messages_to_delete"].append(sent_message.message_id)
    elif callback == "height":
        sent_message = await bot.send_message(
            chat_id=call.message.chat.id,
            text=td.GET_HEIGHT
        )
        await ClientRegistration.height.set()
        user_data[call.message.chat.id]["messages_to_delete"].append(sent_message.message_id)

    elif callback == "weight":
        sent_message = await bot.send_message(
            chat_id=call.message.chat.id,
            text=td.GET_WEIGHT
        )
        await ClientRegistration.weight.set()
        user_data[call.message.chat.id]["messages_to_delete"].append(sent_message.message_id)

    elif callback == "age":
        sent_message = await bot.send_message(
            chat_id=call.message.chat.id,
            text=td.GET_AGE
        )
        await ClientRegistration.age.set()
        user_data[call.message.chat.id]["messages_to_delete"].append(sent_message.message_id)

    else:
        await confirm_data(call)


async def get_sex(call: types.CallbackQuery, state: FSMContext):
    user_data[call.message.chat.id]["messages_to_delete"].append(call.message.message_id)
    sex_data = call.data.replace("sex_", "")
    sex = "М" if sex_data == "m" else "Ж"
    user_data[call.message.chat.id].update({"sex": sex})
    await get_panel(call.message, state)


async def get_height(message: types.Message, state: FSMContext):
    user_data[message.chat.id]["messages_to_delete"].append(message.message_id)
    height = message.text
    user_data[message.chat.id].update({"height": height})
    await get_panel(message=message, state=state)


async def get_weight(message: types.Message, state: FSMContext):
    user_data[message.chat.id]["messages_to_delete"].append(message.message_id)
    weight = message.text
    user_data[message.chat.id].update({"weight": weight})
    await get_panel(message=message, state=state)


async def get_age(message: types.Message, state: FSMContext):
    user_data[message.chat.id]["messages_to_delete"].append(message.message_id)
    age = message.text
    user_data[message.chat.id].update({"age": age})
    await get_panel(message=message, state=state)


async def get_panel(message: types.Message, state: FSMContext):
    user_id = message.chat.id
    tg_user: TelegramUser = await telegram_user.select_user(user_id=user_id)
    await cleaner.delete_messages(user_id=user_id)
    try:
        sent_message = await bot.edit_message_text(
            chat_id=user_id,
            message_id=message.message_id,
            text=td.CLIENT_REG_MENU.format(
                name=tg_user.name,
                gender=user_data[user_id]["sex"] if "sex" in user_data[user_id] else "",
                height=user_data[user_id]["height"] if "height" in user_data[user_id] else "",
                weight=user_data[user_id]["weight"] if "weight" in user_data[user_id] else "",
                age=user_data[user_id]["age"] if "age" in user_data[user_id] else "",
            ),
            reply_markup=await ik.setup_client(user_id=user_id)
        )
        user_data[user_id]["messages_to_delete"].append(sent_message.message_id)
        await state.finish()
    except:
        sent_message = await bot.send_message(
            chat_id=user_id,
            text=td.CLIENT_REG_MENU.format(
                name=tg_user.name,
                gender=user_data[user_id]["sex"] if "sex" in user_data[user_id] else "",
                height=user_data[user_id]["height"] if "height" in user_data[user_id] else "",
                weight=user_data[user_id]["weight"] if "weight" in user_data[user_id] else "",
                age=user_data[user_id]["age"] if "age" in user_data[user_id] else "",
            ),
            reply_markup=await ik.setup_client(user_id=user_id)
        )
        user_data[user_id]["messages_to_delete"].append(sent_message.message_id)
        await state.finish()


async def confirm_data(call: types.CallbackQuery):
    user_id = call.message.chat.id
    tg_user: TelegramUser = await telegram_user.select_user(user_id=user_id)
    gender = user_data[user_id]["sex"]
    height = user_data[user_id]["height"]
    weight = user_data[user_id]["weight"]
    age = user_data[user_id]["age"]
    ims = await get_ims(height=height, weight=weight)
    await client.add_client(user=tg_user, gender=gender, height=height, weight=weight, age=age, ims=ims)
    await cleaner.delete_messages(user_id=user_id)
    await client_act_menu(call=call)


async def client_act_menu(call: types.CallbackQuery):
    user_id = call.message.chat.id
    tg_user: TelegramUser = await telegram_user.select_user(user_id=user_id)
    try:
        await bot.edit_message_text(
            chat_id=user_id,
            message_id=call.message.message_id,
            text=td.CLIENT_PROFILE.format(name=tg_user.name),
            reply_markup=await ik.client_actions()
        )
    except:
        await bot.send_message(
            chat_id=user_id,
            text=td.CLIENT_PROFILE.format(name=tg_user.name),
            reply_markup=await ik.client_actions())
