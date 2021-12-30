from tools import validate_phonenumber, validate_email
import requests
import os
from dotenv import load_dotenv, dotenv_values
from kavenegar import *


load_dotenv('data.env')
data = dotenv_values('data.env')
APP_ID = os.environ.get('APP_ID')
AUTH_KEY = os.environ.get('AUTH_KEY')
PUSH_URL = os.environ.get('PUSH_URL')
KAVENEGAR_API_KEY = os.environ.get('KAVENEGAR_API_KEY')
headers = {'Authorization': f'Token {AUTH_KEY}'}


class Notification:
    
    def __init__(self, user):
        self.phone_number = user.phone_num
        self.email = user.email


    def send_sms(self, message):
        receptor = validate_phonenumber(self.phone_number)
        api = KavenegarAPI(KAVENEGAR_API_KEY)
        params = {
            'receptor' : receptor,
            'message' : message
        }   
        try:
            response = api.sms_send(params)
        except Exception as exc:
            print('some problem occured while sending the sms!')


    def send_email(self, message):
        receptor = validate_email(self.email)
        pass


    def push_notification(self, title, content):
        data = {
            'app_ids': APP_ID,
            'data': {
                'title': title,
                'content': content
            }
        }
        requests.post(PUSH_URL, json=data, headers=headers)
