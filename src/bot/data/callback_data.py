from aiogram.utils.callback_data import CallbackData

reg = CallbackData("reg", "action")
docs_list = CallbackData("doctors_list", "action")
next_step = CallbackData("ns", "doc_id", "date", "time" )
chosen_doctor = CallbackData("chosen_doc", "action", "doc_id")
make_request = CallbackData("r_doc", "action", "doc_id", "request")
choose_datetime = CallbackData("r_doc", "action", "doc_id", "request", "datetime")
choose_date = CallbackData("r_doc", "action", "doc_id", "request", "datetime", "date")
choose_time = CallbackData("r_doc", "action", "doc_id", "request", "datetime", "time")
choose_hour = CallbackData("r_h", "action", "doc_id", "request", "datetime", "time", "hour")
choose_minute = CallbackData("r_m", "action", "doc_id", "request", "datetime", "time", "minute")
