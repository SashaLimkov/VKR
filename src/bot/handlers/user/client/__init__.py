from aiogram import Dispatcher
from aiogram import filters

from bot.handlers.user.client import client_registration, client_actions, client_test, client_and_reg_worker
from bot.states import ClientRegistration, ClientRequest
from bot.data import callback_data as cd


def setup(dp: Dispatcher):
    dp.register_callback_query_handler(client_registration.start_client, filters.Text("client_reg"))
    dp.register_message_handler(client_test.send_test, filters.Command("test"))
    dp.register_callback_query_handler(client_registration.start_register_client, cd.reg.filter(),
                                       state=ClientRegistration.registration)
    dp.register_callback_query_handler(client_registration.get_sex, filters.Text(startswith="sex_"),
                                       state=ClientRegistration.registration)
    dp.register_message_handler(client_registration.get_height, state=ClientRegistration.height)
    dp.register_message_handler(client_registration.get_weight, state=ClientRegistration.weight)
    dp.register_message_handler(client_registration.get_age, state=ClientRegistration.age)
    dp.register_callback_query_handler(client_actions.doctors_list, cd.docs_list.filter(), state="*")
    dp.register_callback_query_handler(client_registration.client_act_menu, filters.Text("back_to_menu"), state="*")
    dp.register_callback_query_handler(client_actions.doctor_profile, cd.chosen_doctor.filter(), state="*")
    dp.register_callback_query_handler(client_actions.choose_datetime, cd.make_request.filter(), state="*")
    dp.register_callback_query_handler(client_actions.choose_date, cd.choose_datetime.filter(datetime="d"), state="*")
    dp.register_callback_query_handler(client_actions.choose_time, cd.choose_datetime.filter(datetime="t"), state="*")
    dp.register_callback_query_handler(client_actions.choose_hour, cd.choose_time.filter(time="h"), state="*")
    dp.register_callback_query_handler(client_actions.choose_min, cd.choose_time.filter(time="m"), state="*")
    dp.register_callback_query_handler(client_actions.save_min, cd.choose_minute.filter(), state="*")
    dp.register_callback_query_handler(client_actions.save_hour, cd.choose_hour.filter(), state="*")
    dp.register_callback_query_handler(client_actions.save_date, cd.choose_date.filter(), state="*")
    dp.register_callback_query_handler(client_actions.save_date, cd.choose_time.filter(), state="*")
    dp.register_callback_query_handler(client_actions.skip_test_or_no,
                                       cd.next_step.filter(),
                                       state=ClientRequest.waiting_for_answer)
    dp.register_callback_query_handler(client_and_reg_worker.skip_test,
                                       filters.Text("skip"),
                                       state=ClientRequest.waiting_for_answer)
    # dp.register_message_handler(client_actions.get_client_addition, state=ClientRequest.additional)
