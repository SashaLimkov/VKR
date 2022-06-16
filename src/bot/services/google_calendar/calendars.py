from pprint import pprint

from bot.services.google_calendar.log_in import connect_to_calendar


def create_calendar(calendar_name: str):
    worker = connect_to_calendar()
    request_body = {
        "summary": f"{calendar_name}",
        "timeZone": "Europe/Moscow"
    }
    response = worker.calendars().insert(body=request_body).execute()
    return response


def delete_calendar(calendar_id: str):
    worker = connect_to_calendar()
    return worker.calendars().delete(calendarId=calendar_id).execute()


async def get_calendars():
    worker = connect_to_calendar()
    current_calendars = {}
    page_token = None
    while True:
        calendar_list = worker.calendarList().list(pageToken=page_token).execute()
        for index, calendar_list_entry in enumerate(calendar_list["items"]):
            current_calendars.update(
                {index: {
                    "calendar_name": calendar_list_entry["summary"],
                    "calendar_id": calendar_list_entry["id"]
                }}
            )
        page_token = calendar_list.get("nextPageToken")
        if not page_token:
            break
    current_calendars.pop(0)
    return current_calendars

#
if __name__ == '__main__':
    # print(create_calendar(calendar_name="Хирург"))
    # print(create_calendar(calendar_name="Терапевт"))
    pprint(get_calendars())
    # print(delete_calendar(worker=service, calendar_id="me0ea2ia1po7t83vmscm09jek8@group.calendar.google.com"))
