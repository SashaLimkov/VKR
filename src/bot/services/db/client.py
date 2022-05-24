from asgiref.sync import sync_to_async

from usersupport.models import Client


@sync_to_async
def select_client(user) -> Client:
    user = Client.objects.filter(user=user).first()
    return user


@sync_to_async
def add_client(user, gender, height, weight, age, ims):
    try:
        return Client(
            user=user, gender=gender, height=height, weight=weight, age=age, ims=ims
        ).save()
    except Exception as e:
        print(e)
        return select_client(user)
