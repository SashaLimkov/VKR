from asgiref.sync import sync_to_async

from usersupport.models import RegWorker


@sync_to_async
def add_rworker(user, chanel_chat_id):
    try:
        return RegWorker(
            user=user, chanel_chat_id=chanel_chat_id
        ).save()
    except Exception as e:
        print(e)


@sync_to_async
def update_chanel_id(user, chanel_id):
    try:
        return RegWorker.objects.filter(user=user).update(chanel_id=chanel_id)
    except Exception as e:
        print(e)


@sync_to_async
def get_rworker(user):
    try:
        return RegWorker.objects.filter(user=user).first()
    except Exception as e:
        print(e)


@sync_to_async
def get_all_rworker():
    try:
        return RegWorker.objects.filter().all()
    except Exception as e:
        print(e)
