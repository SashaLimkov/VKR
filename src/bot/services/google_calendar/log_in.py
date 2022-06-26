from bot.services.google_calendar.Google import create_service
from bot.config.config import API_NAME, API_VERSION, SCOPES


def connect_to_calendar():
    print("создание календаря")
    return create_service(API_NAME, API_VERSION, SCOPES)


