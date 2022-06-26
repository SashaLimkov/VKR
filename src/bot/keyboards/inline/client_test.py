from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.config.loader import user_data
from bot.data import list_data as ld
from bot.data import callback_data as cd

__all__ = [
    "start_test",
    "test_q",
    "second_stage"
]


async def start_test():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton(text="Начать тестирование", callback_data="answer_")
                 )
    keyboard.add(InlineKeyboardButton(text="Продолжить без теста", callback_data="skip"))
    return keyboard


async def second_stage():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton(text="Продалжить тестирование", callback_data="=")
                 )
    keyboard.add(InlineKeyboardButton(text="Продолжить без", callback_data="skip"))
    return keyboard


async def test_q():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="Да", callback_data="answer_+"),
        InlineKeyboardButton(text="Нет", callback_data="answer_-"),
    )
    return keyboard
