from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
cancel.add(
    KeyboardButton(text="Отмена")
)
