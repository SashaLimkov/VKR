from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.config.loader import user_data
from bot.data import list_data as ld
from bot.data import callback_data as cd

__all__ = [
    "accept"
]


async def accept(user_id):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="Подтвердить", callback_data=f"agree_{user_id}"),
        InlineKeyboardButton(text="Отклонить", callback_data="000"),
    )
    keyboard.add(
        InlineKeyboardButton(text="Редактировать", callback_data="000"),
    )
    return keyboard
