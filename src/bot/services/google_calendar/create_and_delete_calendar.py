from pprint import pprint
from Google import create_service

CLIENT_SECRET_FIlE = "client_secret.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

service = create_service(CLIENT_SECRET_FIlE, API_NAME, API_VERSION, SCOPES)
"""
Create calendar
"""


def create_calendar(worker, calendar_name):
    request_body = {
        "summary": f"{calendar_name}"
    }

    response = worker.calendars().insert(body=request_body).execute()
    return response


"""
Delete calendar by id
"""
# service.calendars().delete(calendarId = "9ps3d5gk3q4u7n1geevivt4500@group.calendar.google.com").execute()
"""
Get calendars list
"""
# ids_ = []
# page_token = None
# while True:
#     calendar_list = service.calendarList().list(pageToken=page_token).execute()
#     for calendar_list_entry in calendar_list["items"]:
#         ids_.append(calendar_list_entry["id"])
#     page_token = calendar_list.get("nextPageToken")
#     if not page_token:
#         break
# for calendar_id in ids_:
#     print(calendar_id)
if __name__ == '__main__':
    pprint(create_calendar(worker=service, calendar_name="Хирург"))
