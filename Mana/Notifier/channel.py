import requests
from kavenegar import *
import os
from dotenv import load_dotenv, dotenv_values


load_dotenv('data.env')
data = dotenv_values('data.env')

APP_ID = os.environ.get('APP_ID')
AUTH_KEY = os.environ.get('AUTH_KEY')
push_url = os.environ.get('url')
API_KEY = os.environ.get('API_KEY')


class Channel:

    def send_push_notification(self, device_id):

        headers = {'Authorization': f'Token {AUTH_KEY}','Content-Type': 'application/json'}
        
        payload = {
            "app_ids": APP_ID,
            "data": {
                "title": 'Message',
                "content": 'Done!!'
            },
            "filters": {
                "device_id": [device_id]
            }
        }
       
        requests.post(push_url, json=payload, headers=headers)

    def send_sms(self, phone_number):


        try:
            api = KavenegarAPI(API_KEY)
            params = {
                'sender': '10008663',
                'receptor': phone_number,
                'message': 'sssss',
            } 
            api.sms_send(params)

        except Exception as exc:
            print(exc)
