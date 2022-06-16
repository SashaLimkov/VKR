from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.config.loader import user_data
from bot.data import callback_data as cd
from bot.services.db import doctor

__all__ = [
    "client_actions",
    "docs_list",
    "create_r_to_doc",
    "choose_datetime",
    "skip_test_or_no",
]

from usersupport.models import Doctor


async def client_actions():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="Выбрать врача", callback_data=cd.docs_list.new(
            action=1
        )),
    )
    return keyboard


async def docs_list():
    keyboard = InlineKeyboardMarkup(row_width=1)
    doctors: List[Doctor] = await doctor.select_all_doctors()
    for doc in doctors:
        keyboard.add(
            InlineKeyboardButton(text=f"{doc.profession} {doc.user.name}", callback_data=cd.chosen_doctor.new(
                action=1,
                doc_id=doc.id
            )),
        )
    keyboard.add(
        InlineKeyboardButton(text="Назад", callback_data="back_to_menu",
                             ))
    return keyboard


async def create_r_to_doc(callback_data: dict):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text=f"Записаться на прием", callback_data=cd.make_request.new(
            action=1,
            doc_id=callback_data["doc_id"],
            request=1
        )),
    )
    keyboard.add(
        InlineKeyboardButton(text="Назад", callback_data=cd.docs_list.new(
            action=1
        )),
    )
    return keyboard


async def choose_datetime(callback_data: dict, user_id):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(
            text="Выбрать дату",
            callback_data=cd.choose_datetime.new(
                action=callback_data["action"],
                doc_id=callback_data["doc_id"],
                request=callback_data["request"],
                datetime="d"
            )
        ),
        InlineKeyboardButton(
            text="Выбрать время",
            callback_data=cd.choose_datetime.new(
                action=callback_data["action"],
                doc_id=callback_data["doc_id"],
                request=callback_data["request"],
                datetime="t"
            )
        ))
    if "date" in user_data[user_id] and "time" in user_data[user_id]:
        keyboard.add(
            InlineKeyboardButton(
                text="Далее",
                callback_data=cd.next_step.new(
                    doc_id=callback_data["doc_id"],
                    date=user_data[user_id]["date"],
                    time=user_data[user_id]["time"]
                )
            ))
    keyboard.add(InlineKeyboardButton(
        text="Назад",
        callback_data=cd.chosen_doctor.new(
            action=callback_data["action"],
            doc_id=callback_data["doc_id"],
        )
    ))
    return keyboard


async def skip_test_or_no(callback_data):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(
            text="Пройти тест",
            callback_data="test"
        ),
        InlineKeyboardButton(
            text="Продолжить без теста",
            callback_data="skip"
        ))
    keyboard.add(InlineKeyboardButton(
        text="Назад",
        callback_data=cd.make_request.new(
            action=1,
            doc_id=callback_data["doc_id"],
            request=1,
        )
    ))
    return keyboard
