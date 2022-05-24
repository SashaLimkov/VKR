from aiogram import Dispatcher
from aiogram import filters

from bot.handlers.user.doctor import doctor_registration
from bot.states import DoctorRegistration


def setup(dp: Dispatcher):
    dp.register_message_handler(doctor_registration.setup_doctor_command, filters.Command("setup_doctor"))
    dp.register_message_handler(doctor_registration.check_secret_key, state=DoctorRegistration.secret_key)
