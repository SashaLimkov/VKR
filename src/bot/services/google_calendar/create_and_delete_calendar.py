from pprint import pprint
from log_in import connect_to_calendar


def create_calendar(calendar_name: str):
    # need to add response to database
    worker = connect_to_calendar()
    request_body = {
        "summary": f"{calendar_name}"
    }
    response = worker.calendars().insert(body=request_body).execute()
    return response


def delete_calendar(calendar_id: str):
    worker = connect_to_calendar()
    return worker.calendars().delete(calendarId=calendar_id).execute()


def get_calendars():
    worker = connect_to_calendar()
    current_calendars = {}
    page_token = None
    while True:
        calendar_list = worker.calendarList().list(pageToken=page_token).execute()
        for calendar_list_entry in calendar_list["items"]:
            current_calendars.update(
                {
                    "calendar_name": calendar_list_entry["summary"],
                    "calendar_id": calendar_list_entry["id"]
                }
            )
        page_token = calendar_list.get("nextPageToken")
        if not page_token:
            break
    return current_calendars


if __name__ == '__main__':
    # pprint(create_calendar(worker=service, calendar_name="Хирург"))
    pprint(get_calendars())
    # pprint(delete_calendar(worker=service, calendar_id="me0ea2ia1po7t83vmscm09jek8@group.calendar.google.com"))
