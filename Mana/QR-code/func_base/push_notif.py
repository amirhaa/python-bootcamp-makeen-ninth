from qr_generate import *
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv('data.env')


data = dotenv_values('data.env')

APP_ID = os.environ.get('APP_ID')
AUTH_KEY = os.environ.get('AUTH_KEY')
push_url = os.environ.get('push_url')
upload_url = os.environ.get('upload_url')

headers = {'Authorization': f'Token {AUTH_KEY}'}

name, user_name, user_id = set_info()

qr_generator(name, user_name, user_id)

notification(APP_ID, user_name, push_url, headers, upload_url)



