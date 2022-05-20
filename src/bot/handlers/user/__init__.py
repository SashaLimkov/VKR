from aiogram import Dispatcher
from aiogram import filters
from bot.handlers.user import cleaner, client
from bot.states import TelegramUserRegistration


def setup(dp: Dispatcher):
    dp.register_message_handler(client.start_command, filters.CommandStart)
    dp.register_callback_query_handler(client.reg_client, filters.Text("reg"))
    dp.register_message_handler(client.get_phone, state=TelegramUserRegistration.name)
    dp.register_message_handler(client.check_phone, state=TelegramUserRegistration.phone)
    dp.register_message_handler(client.check_email, state=TelegramUserRegistration.email)
    dp.register_message_handler(cleaner.clean_s)
