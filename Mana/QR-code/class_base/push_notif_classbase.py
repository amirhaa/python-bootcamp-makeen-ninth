from qr_classbase import GenerateQR , PushNotifiction
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv('data.env')


data = dotenv_values('data.env')

APP_ID = os.environ.get('APP_ID')
AUTH_KEY = os.environ.get('AUTH_KEY')
push_url = os.environ.get('push_url')
upload_url = os.environ.get('upload_url')

headers = {'Authorization': f'Token {AUTH_KEY}'}

p1 = GenerateQR()
print(p1)

name, user_name, user_id = GenerateQR.set_info()

GenerateQR.qr_generator(name, user_name, user_id)

PushNotifiction.notification(APP_ID, user_name, push_url, headers, upload_url)
