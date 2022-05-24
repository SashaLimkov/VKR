import os
import pickle
from datetime import datetime, date, time

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


def create_service(api_name, api_version, *scopes):
    CLIENT_SECRET_FILE = "bot\services\google_calendar\google_secret.json"
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]

    cred = None
    working_dir = os.getcwd()
    token_dir = 'token files'

    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'

    ### Check if token dir exists first, if not, create the folder
    if not os.path.exists(os.path.join(working_dir, token_dir)):
        os.mkdir(os.path.join(working_dir, token_dir))

    if os.path.exists(os.path.join(working_dir, token_dir, pickle_file)):
        with open(os.path.join(working_dir, token_dir, pickle_file), 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        with open(os.path.join(working_dir, token_dir, pickle_file), 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print(API_SERVICE_NAME, 'service created successfully')
        return service
    except Exception as e:
        print(e)
        print(f'Failed to create service instance for {API_SERVICE_NAME}')
        os.remove(os.path.join(working_dir, token_dir, pickle_file))
        return None


def convert_to_rfc_datetime(selected_date: tuple, selected_time: tuple):
    hour, minute = selected_time
    dt = f"{date(*selected_date)}T{time(hour, minute)}+03:00"
    print(dt)
    return dt


def convert_from_rfc(date_: str):
    date_dict = {}
    input_date = date_.split("T")
    date_ = date.fromisoformat(input_date[0])
    date_dict["year"] = date_.year
    date_dict["month"] = date_.month
    date_dict["day"] = date_.day
    date_dict["hour"] = int(input_date[1].split(":")[0])
    return date_dict


if __name__ == '__main__':
    print(convert_to_rfc_datetime((2022, 5, 20), (3, 50)))
