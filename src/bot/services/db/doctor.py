from asgiref.sync import sync_to_async

from usersupport.models import Doctor


@sync_to_async
def select_doctor(user) -> Doctor:
    doctor = Doctor.objects.filter(user=user).first()
    return doctor


@sync_to_async
def add_doctor(user, education, experience, profession, photo_id, calendar_id):
    try:
        return Doctor(
            user=user, education=education, experience=experience, profession=profession, photo_id=photo_id,
            calendar_id=calendar_id
        ).save()
    except Exception as e:
        print(e)
        return select_doctor(user)
