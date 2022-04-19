# from usersupport.models import TelegramUser
from asgiref.sync import sync_to_async


# @sync_to_async
# def select_user(user_id) -> TelegramUser:
#     user = TelegramUser.objects.filter(user_id=user_id).first()
#     return user
#
#
# @sync_to_async
# def add_user(user_id, name, role, phone_number):
#     try:
#         return TelegramUser(
#             user_id=int(user_id), name=name, user_role=role, phone=phone_number
#         ).save()
#     except Exception:
#         return select_user(int(user_id))
