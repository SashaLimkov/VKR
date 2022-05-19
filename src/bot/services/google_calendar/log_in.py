from pprint import pprint
from Google import create_service

CLIENT_SECRET_FIlE = "google_secret.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

service = create_service(CLIENT_SECRET_FIlE, API_NAME, API_VERSION, SCOPES)

pprint(dir(service))
