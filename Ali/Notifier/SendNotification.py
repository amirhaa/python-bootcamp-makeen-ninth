from MakeUser import *
from load_from_json import load_json
import requests
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv('data.env')

class Notification:
    data = dotenv_values('data.env')
    APP_ID = os.environ.get('APP_ID')
    AUTH_KEY = os.environ.get('AUTH_KEY')
    PUSH_URL = os.environ.get('PUSH_URL')
    headers = {'Authorization': f'Token {AUTH_KEY}'}

    def __init__(self):
        pass

    def push(self, arg1, arg2):
        data = {
            'app_ids': Notification.APP_ID,
            'data': {
                'title': arg1,
                'content': arg2
            }
        }
        requests.post(Notification.PUSH_URL, json=data, headers=Notification.headers)


class send_sms(Notification):
    pass

class send_email(Notification):
    pass

class push_notification(Notification):
    def __init__(self, user):
        super().__init__()
        self.user = user


phone_num = input('Enter the phone number of the user to check if he/she exists : ')
user_info = load_json(phone_num, 'users.json')
if not user_info:
    exit()
print(user_info)
u2 = User(*user_info)


notif = push_notification(u2)
notif.push(u2.name, u2.phone_num)
