from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

__all__ = [
    "get_reg_menu",
]


async def get_reg_menu():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="Зарегестрироваться", callback_data="reg")
    )
    return keyboard
