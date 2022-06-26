from aiogram import Dispatcher, types
from aiogram import filters

from bot.handlers.user.doctor import doctor_registration
from bot.states import DoctorRegistration


def setup(dp: Dispatcher):
    dp.register_message_handler(doctor_registration.setup_doctor_command, filters.Command("setup_doctor"))
    dp.register_message_handler(doctor_registration.check_secret_key, state=DoctorRegistration.secret_key)
    dp.register_callback_query_handler(doctor_registration.handle_info, filters.Text(startswith="doc_"))
    dp.register_message_handler(doctor_registration.get_education, state=DoctorRegistration.education)
    dp.register_message_handler(doctor_registration.get_experience, state=DoctorRegistration.experience)
    dp.register_message_handler(doctor_registration.get_profession, state=DoctorRegistration.profession)
    dp.register_message_handler(doctor_registration.get_photo, content_types=types.ContentTypes.PHOTO,
                                state=DoctorRegistration.photo)
