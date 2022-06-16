from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.config.loader import user_data
from bot.data import list_data as ld
from bot.data import callback_data as cd

__all__ = [
    "test"
]


async def test():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="Не изменился", callback_data="client_reg"),
        InlineKeyboardButton(text="Пропал", callback_data="client_reg"),
    )
    keyboard.add(
        InlineKeyboardButton(text="Увеличился", callback_data="client_reg"),
        InlineKeyboardButton(text="Уменьшился", callback_data="client_reg"),
    )
    keyboard.add(InlineKeyboardButton(text="Предыдущий вопрос", callback_data="client_reg"))

    return keyboard
