import datetime
import time
from pprint import pprint

from bot.services.google_calendar.Google import convert_to_rfc_datetime
from bot.services.google_calendar.log_in import connect_to_calendar


def create_google_event(user_name: str, prediction: str, date_time: dict, doctor, user_email):
    calendar_id = "95onhp8luapfusk2ip1o3iksbk@group.calendar.google.com"  # doctor.calendar_id  #
    email = "magl.galimov@gmail.com"  # doctor.email  #
    worker = connect_to_calendar()

    event = {
        'summary': user_name,
        'description': prediction,
        'start': {
            'dateTime': convert_to_rfc_datetime(selected_date=date_time["selected_date"],
                                                selected_time=date_time["start_time"]),
            'timeZone': 'Europe/Moscow',
        },
        'end': {
            'dateTime': convert_to_rfc_datetime(selected_date=date_time["selected_date"],
                                                selected_time=date_time["end_time"]),
            'timeZone': 'Europe/Moscow',
        },
        'attendees': [
            {'email': email},
            {'email': user_email},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'email', 'minutes': 4},
                {'method': 'popup', 'minutes': 1},
            ],
        },
    }
    event = worker.events().insert(calendarId=calendar_id,
                                   body=event).execute()
    print(f'Event created {user_name}: {event.get("htmlLink")}')
    return event.get("htmlLink")


def get_events(calendar_id: str):
    worker = connect_to_calendar()
    page_token = None
    all_events = {}
    today = datetime.date.today()
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    while True:
        events = worker.events().list(
            calendarId=calendar_id,
            timeMin=convert_to_rfc_datetime(
                selected_date=(today.year, today.month, today.day),
                selected_time=tuple([int(i) for i in current_time.split(":")])),
            pageToken=page_token).execute()
        for index, event in enumerate(events['items']):
            all_events.update(
                {index + 1: {
                    "start": event["start"]["dateTime"],
                    "end": event["end"]["dateTime"],
                }
                }
            )
        page_token = events.get('nextPageToken')
        if not page_token:
            break
    return all_events


if __name__ == '__main__':
    t = {
        "selected_date": (2022, 5, 20),
        "start_time": (9, 15),
        "end_time": (9, 30)
    }
    create_google_event("Мансур", "Полноcтью здоров", t, "", "example@gmail.com")
    time.sleep(10)
    print(get_events("95onhp8luapfusk2ip1o3iksbk@group.calendar.google.com"))
# def get_google_events(nickname):
#     days = datetime.today()
#     days += timedelta(days=1)
#     end_day = days + timedelta(days=14)
#
#     CLIENT_SECRET_FIlE = "services/google_calendar/client_secret.json"
#     API_NAME = "calendar"
#     API_VERSION = "v3"
#     SCOPES = ["https://www.googleapis.com/auth/calendar"]
#
#     service = Create_Service(CLIENT_SECRET_FIlE, API_NAME, API_VERSION, SCOPES)
#     events = service.events().list(
#         calendarId='3q8efa1o9v3l1miscagp04tnbs@group.calendar.google.com',
#         timeMin=convert_to_RFC_datetime(days.year, days.month, days.day, 0, 0),
#         timeMax=convert_to_RFC_datetime(end_day.year, end_day.month, end_day.day, 0, 0)
#     ).execute()
#     list_to_return = []
#     for item in events["items"]:
#         if item["summary"] == nickname:
#             list_to_return.append([nickname, convert_from_RFC(item["start"]["dateTime"]),
#                                    convert_from_RFC(item["end"]["dateTime"])])
#
#     return list_to_return