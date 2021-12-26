import os
import requests
from dotenv import load_dotenv
import json

load_dotenv('pushe.env')

AUTH_KEY = os.getenv('AUTH_KEY')
APP_ID = os.getenv('APP_ID')
NOTIFICATION_URL = os.getenv('NOTIFICATION_URL')


headers = {'Authorization': f'Token {AUTH_KEY}'}


def push_notification():
    with open('../user_credentials.json') as f:
        tmp = json.load(f)
    newest_user = tmp['users'][0]
    data = {
        'app_ids': APP_ID,
        'data': {
            'title': f'Qrcode for {newest_user["name"]}',
            'content': f"name: {newest_user['name']}\n email: {newest_user['email']}"
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
