import re
import random
import qrcode
import requests
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv('data.env')

data = dotenv_values('data.env')

APP_ID = os.environ.get('APP_ID')
AUTH_KEY = os.environ.get('AUTH_KEY')
push_url = os.environ.get('push_url')
upload_url = os.environ.get('upload_url')

headers = {'Authorization': f'Token {AUTH_KEY}'}


class GenerateQR:

    def set_info():

        while True:
            name = input('Please enter your name [Mana Shams]')
            if re.match('^[A-Z][a-z]+\s[A-z][a-z]+$', name):
                user_id = random.randint(1000, 9999)
                user = name.split()
                return name, f'{user[0].lower()}.{user[1].lower()}', user_id
            else:
                print('Your input is invalid, try again')


    def qr_generator(name, user_name, user_id):
        img = qrcode.make(f'{name}\nid: {user_id}\nUser name: {user_name}')
        img.save(f'{user_name}.jpeg')

    
    def upload_qr(qr_name, upload_url, headers):

        files = [('image', (f'{qr_name}.jpeg', open(f'{qr_name}.jpeg','rb'),'image/jpeg'))]
        
        response = requests.post(upload_url, headers= headers, files= files)
        return response.json().get("url", "")


class PushNotifiction(GenerateQR):

    
    def notification(APP_ID, user_name, push_url, headers, upload_url):

        qr = GenerateQR.upload_qr(user_name, upload_url, headers)
        data = {
            'app_ids': APP_ID,
            'data': {
                'title': 'QR code: ',
                'content': qr
            }
        }

        requests.post(push_url, json= data, headers= headers)


name, user_name, user_id = GenerateQR.set_info()

GenerateQR.qr_generator(name, user_name, user_id)

PushNotifiction.notification(APP_ID, user_name, push_url, headers, upload_url)