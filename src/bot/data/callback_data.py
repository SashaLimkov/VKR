from aiogram.utils.callback_data import CallbackData

reg = CallbackData("reg", "action")
docs_list = CallbackData("doctors_list", "action")
chosen_doctor = CallbackData("chosen_doc", "action", "doc_id")
request_doc = CallbackData("r_doc", "action", "doc_id", "request")
