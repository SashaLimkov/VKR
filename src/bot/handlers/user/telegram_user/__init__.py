from aiogram import Dispatcher
from aiogram import filters

from bot.data import callback_data as cd
from bot.handlers.user.telegram_user import telegram_user
from bot.states import TelegramUserRegistration


def setup(dp: Dispatcher):
    dp.register_message_handler(telegram_user.start_command, filters.CommandStart())
    dp.register_callback_query_handler(telegram_user.reg_client, filters.Text("reg"),
                                       state=TelegramUserRegistration.registration)
    dp.register_callback_query_handler(telegram_user.handle_reg_menu, cd.reg_tg_user.filter(),
                                       state=TelegramUserRegistration.registration)
    dp.register_message_handler(telegram_user.get_name, state=TelegramUserRegistration.name)
    dp.register_message_handler(telegram_user.check_phone, state=TelegramUserRegistration.phone)
    dp.register_message_handler(telegram_user.check_email, state=TelegramUserRegistration.email)
