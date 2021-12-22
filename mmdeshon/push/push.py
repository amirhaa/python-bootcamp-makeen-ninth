import os
import requests
import json
from dotenv import load_dotenv, dotenv_values
from make_user import CreateUserQr

load_dotenv('variables.env')

app_id = os.environ.get('app_id')
authentication_key = os.environ.get('authentication_key')
upload_url = os.environ.get('upload_url')
notification_url = os.environ.get('notification_url')


class PostToWeb:
    user_details = CreateUserQr.create_qr()
    headers = {
        'Authorization': f'Token {authentication_key}',
        'Content-Type': 'application/json'
    }

    @classmethod
    def upload_qr(cls):
        headers = {'Authorization': f'Token {authentication_key}'}

        files = [('image', (f'{cls.user_details[2]}.jpeg', open(f'{cls.user_details[2]}.jpeg', 'rb'), 'image/jpeg'))]

        response = requests.post(upload_url, headers=headers, files=files)
        print(response.status_code)
        return response.json().get("url", "")


print(PostToWeb.upload_qr())

    payload = json.dumps({
        'app_ids': app_id,
        'data': {
            'title': f'QRcode for {user_details[0]}',
            'content': f'{result}'
        }
    })

    @classmethod
    def send_notification(cls):
        response = requests.post(notification_url, headers=cls.headers, data=cls.payload)
        print(response.status_code)
