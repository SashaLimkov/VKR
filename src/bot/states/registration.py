from aiogram.dispatcher.filters.state import StatesGroup, State


class TelegramUserRegistration(StatesGroup):
    registration = State()
    name = State()
    phone = State()
    email = State()


class DoctorRegistration(StatesGroup):
    registration = State()
    secret_key = State()
    education = State()
    experience = State()
    profession = State()
    photo = State()


class ClientRegistration(StatesGroup):
    registration = State()
    gender = State()
    height = State()
    weight = State()
    age = State()


class RWorkerRegistration(StatesGroup):
    registration = State()
    secret_key = State()
