from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.data import list_data as ld
from bot.data import callback_data as cd

__all__ = [
    "get_reg",
    "get_reg_menu"
]

from bot.config.loader import user_data


async def get_reg():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="Зарегестрироваться", callback_data="reg")
    )
    return keyboard


async def get_reg_menu(user_id):
    keyboard = InlineKeyboardMarkup(row_width=1)
    for index, text in enumerate(ld.REG_TG_USER):
        keyboard.add(InlineKeyboardButton(
            text=text,
            callback_data=cd.reg.new(
                action=index + 1
            )
        ))
    data = user_data[user_id]
    if "fio" in data and "phone" in data and "email" in data:
        keyboard.add(
            InlineKeyboardButton(
                text="Подтвердить данные",
                callback_data=cd.reg.new(
                    action="submit"
                )
            )
        )
    return keyboard
