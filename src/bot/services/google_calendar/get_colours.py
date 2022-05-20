from pprint import pprint

from bot.services.google_calendar.log_in import connect_to_calendar


def get_colours():
    worker = connect_to_calendar()
    colours = worker.colors().get().execute()
    return {"calendar": colours["calendar"], "event": colours["event"]}


if __name__ == '__main__':
    pprint(get_colours())
