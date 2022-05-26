from aiogram import Dispatcher
from aiogram import filters

from bot.handlers.user.client import client_registration, client_actions
from bot.states import ClientRegistration, ClientRequest
from bot.data import callback_data as cd


def setup(dp: Dispatcher):
    dp.register_callback_query_handler(client_registration.start_client, filters.Text("client_reg"))
    dp.register_callback_query_handler(client_registration.start_register_client, cd.reg.filter(),
                                       state=ClientRegistration.registration)
    dp.register_callback_query_handler(client_registration.get_sex, filters.Text(startswith="sex_"),
                                       state=ClientRegistration.registration)
    dp.register_message_handler(client_registration.get_height, state=ClientRegistration.height)
    dp.register_message_handler(client_registration.get_weight, state=ClientRegistration.weight)
    dp.register_message_handler(client_registration.get_age, state=ClientRegistration.age)
    dp.register_callback_query_handler(client_actions.doctors_list, cd.docs_list.filter())
    dp.register_callback_query_handler(client_registration.client_act_menu, filters.Text("back_to_menu"))
    dp.register_callback_query_handler(client_actions.doctor_profile, cd.chosen_doctor.filter())
    dp.register_callback_query_handler(client_actions.create_r, cd.request_doc.filter())
    dp.register_message_handler(client_actions.get_client_addition, state=ClientRequest.additional)
