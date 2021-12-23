import os
import requests
from dotenv import load_dotenv

load_dotenv('variables.env')

AUTH_KEY = os.getenv('AUTH_KEY')
APP_ID = os.getenv('APP_ID')
UPLOAD_URL = os.getenv('UPLOAD_URL')
NOTIFICATION_URL = os.getenv('NOTIFICATION_URL')

qrcode_link = ''

headers = {'Authorization': f'Token {AUTH_KEY}'}


def upload_qr(image_name):

    files = [('image', (f'{image_name}.jpeg', open(f'{image_name}.jpeg', 'rb'), 'image/jpeg'))]

    print('---------------------------')
    print('Uploading Qrcode ...')
    try:
        response = requests.post(UPLOAD_URL, headers=headers, files=files)
        print('Status Code:', response.status_code)
        global qrcode_link
        qrcode_link = response.json().get("url", "")
    except Exception as exc:
        print(f'"{exc}" raised!!!!')
    print('---------------------------')


def send_notification(name):
    data = {
        'app_ids': APP_ID,
        'data': {
            'title': f'Qrcode for {name}',
            'content': f'{qrcode_link}'
        }
    }
    print('---------------------------')
    print('Sending Notification ...')
    try:
        response = requests.post(NOTIFICATION_URL, headers=headers, json=data)
        print('Status Code:', response.status_code)
    except Exception as exc:
        print(f'"{exc}" raised!!!!')
    print('---------------------------')
