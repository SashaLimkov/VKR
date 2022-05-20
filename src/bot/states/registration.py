from aiogram.dispatcher.filters.state import StatesGroup, State


class TelegramUserRegistration(StatesGroup):
    name = State()
    phone = State()
    email = State()
