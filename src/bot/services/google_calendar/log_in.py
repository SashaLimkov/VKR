from Google import create_service
from bot.config.config import CLIENT_SECRET_FIlE, API_NAME, API_VERSION, SCOPES


def connect_to_calendar():
    return create_service(CLIENT_SECRET_FIlE, API_NAME, API_VERSION, SCOPES)

