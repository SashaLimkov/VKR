from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

__all__ = [
    "setup_doctor",
]


async def setup_doctor(state: FSMContext):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="Образование", callback_data="doc_edu"),
        InlineKeyboardButton(text="Стаж", callback_data="doc_exp"),
        InlineKeyboardButton(text="Должность", callback_data="doc_prof"),
    )
    data = dict(await state.get_data())
    if "edu" in data and "exp" in data and "prof" in data:
        keyboard.add(
            InlineKeyboardButton(
                text="Подтвердить данные",
                callback_data="doc_submit"
            )
        )
    return keyboard
