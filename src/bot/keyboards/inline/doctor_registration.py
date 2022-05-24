from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

__all__ = [
    "setup_doctor",
    "doctor_pp",
]

from bot.config.loader import user_data


async def setup_doctor(user_id):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="Образование", callback_data="doc_edu"),
        InlineKeyboardButton(text="Стаж", callback_data="doc_exp"),
        InlineKeyboardButton(text="Должность", callback_data="doc_prof"),
    )
    data = user_data[user_id]
    if "education" in data and "experience" in data and "profession" in data:
        keyboard.add(
            InlineKeyboardButton(
                text="Подтвердить данные",
                callback_data="doc_submit"
            )
        )
    return keyboard


async def doctor_pp():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(
            text="Изменить расписание",
            callback_data="t"
        )
    )
    return keyboard
