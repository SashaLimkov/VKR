from aiogram import Dispatcher

from bot.handlers.user import cleaner


def setup(dp: Dispatcher):
    dp.register_message_handler(cleaner.clean_s)
