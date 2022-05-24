from usersupport.models import TelegramUser
from asgiref.sync import sync_to_async


@sync_to_async
def select_user(user_id) -> TelegramUser:
    user = TelegramUser.objects.filter(user_id=user_id).first()
    return user


@sync_to_async
def add_user(user_id, name, phone, email):
    try:
        TelegramUser(
            user_id=user_id, name=name, phone=phone, email=email).save()
        return True
    except Exception as e:
        print(e)
        return False


@sync_to_async
def update_role(user_id, role):
    return TelegramUser.objects.filter(user_id=user_id).update(role="Врач")
