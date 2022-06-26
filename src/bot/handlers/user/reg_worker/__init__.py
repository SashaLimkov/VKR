from aiogram import Dispatcher, types
from aiogram import filters

from bot.handlers.user.reg_worker import reg_worker
from bot.states import RWorkerRegistration


def setup(dp: Dispatcher):
    dp.register_message_handler(reg_worker.setup_rworker_command, filters.Command("rw_setup"))
    dp.register_message_handler(reg_worker.check_secret_key, state=RWorkerRegistration.secret_key)
    dp.register_message_handler(reg_worker.update_chanel, lambda message: message.reply_to_message)
    dp.register_callback_query_handler(reg_worker.accept, filters.Text(startswith="agree"))
    dp.register_callback_query_handler(reg_worker.edit, filters.Text(startswith="edit"))
    dp.register_callback_query_handler(reg_worker.cancel, filters.Text(startswith="cancel"))
