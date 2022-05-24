from aiogram import Dispatcher
from bot.handlers.user import cleaner,telegram_user


def setup(dp: Dispatcher):
    telegram_user.setup(dp)
    dp.register_message_handler(cleaner.clean_s)
