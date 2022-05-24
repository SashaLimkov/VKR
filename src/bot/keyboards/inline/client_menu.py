from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.data import callback_data as cd
from bot.services.db import doctor

__all__ = [
    "client_actions",
    "docs_list",
    "create_r_to_doc",
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
                doc_id=doc.user.user_id
            )),
        )
    keyboard.add(
        InlineKeyboardButton(text="Назад", callback_data="back_to_menu",
    ))
    return keyboard


async def create_r_to_doc(callback_data: dict):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text=f"Записаться на прием", callback_data=cd.request_doc.new(
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
