from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.config.loader import user_data
from bot.data import list_data as ld
from bot.data import callback_data as cd

__all__ = [
    "accept",
    "edit_datetime",
    "edit_date_keyboard",
    "edit_hour_min",
    "edit_hours",
    "edit_min"
]

from bot.utils.calendar_heler import get_date_list


async def accept(r_id):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="Подтвердить", callback_data=f"agree_{r_id}"),
        InlineKeyboardButton(text="Отклонить", callback_data=f"cancel_{r_id}"),
    )
    keyboard.add(
        InlineKeyboardButton(text="Редактировать", callback_data=f"edit_{r_id}"),
    )
    return keyboard


async def edit_datetime(user_id, r_id):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(
            text="Изменить дату",
            callback_data=cd.choose_datetime.new(
                action=1,
                doc_id=1,
                request=1,
                datetime="d"
            )
        ),
        InlineKeyboardButton(
            text="Изменить время",
            callback_data=cd.choose_datetime.new(
                action=1,
                doc_id=1,
                request=1,
                datetime="t"
            )
        ))
    if "date" in user_data[user_id] and "time" in user_data[user_id]:
        keyboard.add(
            InlineKeyboardButton(
                text="Сохранить",
                callback_data=f"saver_{r_id}"
            ))
    keyboard.add(InlineKeyboardButton(
        text="Назад",
        callback_data=f"edit_{r_id}"
    ))
    return keyboard


async def edit_date_keyboard(callback_data: dict, r_id):
    keyboard = InlineKeyboardMarkup(row_width=2)
    date_list: list = await get_date_list()
    for date in date_list:
        keyboard.insert(
            InlineKeyboardButton(
                text=date,
                callback_data=cd.choose_date.new(
                    action=callback_data["action"],
                    doc_id=callback_data["doc_id"],
                    request=callback_data["request"],
                    datetime=callback_data["datetime"],
                    date=date,
                )
            )
        )
    keyboard.add(
        InlineKeyboardButton(
            text="Назад",
            callback_data=f"edit_{r_id}"
        )
    )
    return keyboard


async def edit_hour_min(callback_data: dict, r_id):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(
            text="Час",
            callback_data=cd.choose_time.new(
                action=callback_data["action"],
                doc_id=callback_data["doc_id"],
                request=callback_data["request"],
                datetime=callback_data["datetime"],
                time="h"
            )
        ),
        InlineKeyboardButton(
            text="Минута",
            callback_data=cd.choose_time.new(
                action=callback_data["action"],
                doc_id=callback_data["doc_id"],
                request=callback_data["request"],
                datetime=callback_data["datetime"],
                time="m"
            )
        ),
        InlineKeyboardButton(
            text="Назад",
            callback_data=f"edit_{r_id}"
        ))
    return keyboard


async def edit_hours(callback_data):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for hour in range(8, 20):
        keyboard.insert(
            InlineKeyboardButton(
                text=str(hour),
                callback_data=cd.choose_hour.new(
                    action=callback_data["action"],
                    doc_id=callback_data["doc_id"],
                    request=callback_data["request"],
                    datetime=callback_data["datetime"],
                    time=callback_data["time"],
                    hour=hour,
                )
            )
        )
    keyboard.add(
        InlineKeyboardButton(
            text="Назад",
            callback_data=cd.choose_datetime.new(
                action=callback_data["action"],
                doc_id=callback_data["doc_id"],
                request=callback_data["request"],
                datetime=callback_data["datetime"],
            )
        )
    )
    return keyboard


async def edit_min(callback_data):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.insert(
        InlineKeyboardButton(
            text="00",
            callback_data=cd.choose_minute.new(
                action=callback_data["action"],
                doc_id=callback_data["doc_id"],
                request=callback_data["request"],
                datetime=callback_data["datetime"],
                time=callback_data["time"],
                minute="00",
            )
        )
    )
    for minute in range(15, 60, 15):
        keyboard.insert(
            InlineKeyboardButton(
                text=str(minute),
                callback_data=cd.choose_minute.new(
                    action=callback_data["action"],
                    doc_id=callback_data["doc_id"],
                    request=callback_data["request"],
                    datetime=callback_data["datetime"],
                    time=callback_data["time"],
                    minute=minute,
                )
            )
        )
    keyboard.add(
        InlineKeyboardButton(
            text="Назад",
            callback_data=cd.choose_datetime.new(
                action=callback_data["action"],
                doc_id=callback_data["doc_id"],
                request=callback_data["request"],
                datetime=callback_data["datetime"],
            )
        )
    )
    return keyboard
