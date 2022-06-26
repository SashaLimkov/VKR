import os

from googleapiclient.http import MediaFileUpload

from bot.services.google_calendar.Google import create_service


def connect_to_drive():
    print("создание drive")
    return create_service("drive", "v3", ['https://www.googleapis.com/auth/drive.file'])


def uploadFile(file_name):
    worker = connect_to_drive()
    file_metadata = {
        'name': f'Анкета {file_name}',
        'mimeType': '*/*'
    }
    media = MediaFileUpload(f'{file_name}',
                            mimetype='*/*',
                            resumable=True)

    file = worker.files().create(body=file_metadata, media_body=media, fields='id').execute()
    worker.permissions().create(body={"role": "reader", "type": "anyone"}, fileId=file.get('id')).execute()
    print('File ID: ' + file.get('id'))
    # os.remove(f'{file_name}')
    return f"https://drive.google.com/file/d/{file.get('id')}/view?usp=sharing"
