import qrcode
import requests
import re
from random import randint
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv('data.env')


class Notification:

    data = dotenv_values('data.env')
    APP_ID = os.environ.get('APP_ID')
    AUTH_KEY = os.environ.get('AUTH_KEY')
    push_url = os.environ.get('push_url')
    upload_url = os.environ.get('upload_url')
    headers = {'Authorization': f'Token {AUTH_KEY}'}

    pattern = '^[A-Z][a-z]+\s[A-Z][a-z]+$'
    
    def fill_info(self):
        name = input('Enter your name: ')

        if re.match(Notification.pattern, name):
            self.name = name
            self.username = self.name.replace(' ', '.').lower()
            self.user_id = randint(1000, 9999)
            self.filename = self.username + '.jpeg'
        else:
            print('invalid name format! Enter your name like the following pattern :\nEx: Ali Hosseinzadeh\n')
            self.fill_info()

    
    def make_qrcode(self):
        img = qrcode.make(f'name: {self.name}\nusername: {self.username}\nid: {self.user_id}')
        img.save(f'{self.filename}')
        


    def upload_qr(self):
        files = [('image', (f'{self.filename}', open(f'{self.filename}','rb'),'image/jpeg'))]
        
        response = requests.post(Notification.upload_url, headers=Notification.headers, files=files)
        return response.json().get("url", "")


    def push_notification(self):
        qr = self.upload_qr()
        data = {
            'app_ids': Notification.APP_ID,
            'data': {
                'title': 'QR code: ',
                'content': qr
            }
        }
        requests.post(Notification.push_url, json=data, headers=Notification.headers)



obj = Notification()            # first we create an object of the Notification class
obj.fill_info()                 # then we pass the needed information
obj.make_qrcode()               # we generate the QRcode next
obj.upload_qr()                 # this line converts the QRcode to link
obj.push_notification()         # and finally this line weill send a notification to all the website users
