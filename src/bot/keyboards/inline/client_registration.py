from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.config.loader import user_data

__all__ = [
    "reg_client",
    "setup_client",
    "gender"
]


async def reg_client():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="Заполнить анкету", callback_data="client_reg"),
    )
    return keyboard


async def setup_client(user_id):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="Гендер", callback_data="c_sex"),
        InlineKeyboardButton(text="Рост", callback_data="c_height"),
        InlineKeyboardButton(text="Вес", callback_data="c_weight"),
        InlineKeyboardButton(text="Возраст", callback_data="c_age"),
    )
    data = user_data[user_id]
    if "age" in data and "sex" in data and "height" in data and "weight" in data:
        keyboard.add(
            InlineKeyboardButton(
                text="Подтвердить данные",
                callback_data="c_submit"
            )
        )
    return keyboard


async def gender():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="Ж", callback_data="sex_g"),
        InlineKeyboardButton(text="М", callback_data="sex_m"),
    )
    return keyboard
