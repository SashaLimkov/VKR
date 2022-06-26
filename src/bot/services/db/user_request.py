from asgiref.sync import sync_to_async

from usersupport.models import UserRequest


@sync_to_async
def add_request(client, file_name, date, time, doc_id):
    try:
        r = UserRequest(client=client, file_name=file_name, date=date, time=time, doc_id=doc_id)
        r.save()
        return r
    except Exception as e:
        print(e)


@sync_to_async
def get_request(r_id):
    return UserRequest.objects.filter(pk=r_id).first()
