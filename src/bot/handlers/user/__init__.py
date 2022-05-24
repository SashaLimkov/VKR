from aiogram import Dispatcher
from bot.handlers.user import cleaner, telegram_user, doctor
from bot.states import TelegramUserRegistration


def setup(dp: Dispatcher):
    telegram_user.setup(dp)
    doctor.setup(dp)
    dp.register_message_handler(cleaner.clean_registration, state=TelegramUserRegistration.registration)
