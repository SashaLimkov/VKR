import asyncio
from typing import List

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


@sync_to_async
def select_all_doctors() -> List[Doctor]:
    doctors = Doctor.objects.all()
    return doctors


@sync_to_async
def select_doctor_by_id(doc_id) -> Doctor:
    return Doctor.objects.filter(id=doc_id)
