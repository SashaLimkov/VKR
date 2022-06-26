from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.utils.calendar_heler import get_date_list
from bot.data import callback_data as cd

__all__ = [
    "get_calendar_keyboard",
    "get_hour_min",
    "get_hours",
    "get_min"
]


async def get_calendar_keyboard(callback_data: dict):
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
            callback_data=cd.make_request.new(
                action=callback_data["action"],
                doc_id=callback_data["doc_id"],
                request=callback_data["request"]
            )
        )
    )
    return keyboard


async def get_hour_min(callback_data: dict):
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
            callback_data=cd.make_request.new(
                action=callback_data["action"],
                doc_id=callback_data["doc_id"],
                request=callback_data["request"],
            )
        ))
    return keyboard


async def get_hours(callback_data):
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


async def get_min(callback_data):
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
