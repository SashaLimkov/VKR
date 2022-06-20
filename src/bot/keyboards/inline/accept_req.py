from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.config.loader import user_data
from bot.data import list_data as ld
from bot.data import callback_data as cd

__all__ = [
    "accept"
]


async def accept(r_id):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="Подтвердить", callback_data=f"agree_{r_id}"),
        InlineKeyboardButton(text="Отклонить", callback_data=f"denied_{r_id}"),
    )
    keyboard.add(
        InlineKeyboardButton(text="Редактировать", callback_data=f"edit_{r_id}"),
    )
    return keyboard
