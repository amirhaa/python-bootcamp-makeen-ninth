from specifications import specification
from createqrcode import *
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv('Personal Information.env')


data = dotenv_values('Personal Information.env')

APP_ID = os.environ.get('APP_ID')
AUTH_KEY = os.environ.get('AUTH_KEY')
push_url = os.environ.get('push_url')
upload_url = os.environ.get('upload_url')

headers = {'Authorization': f'Token {AUTH_KEY}'}

name, user_name, person_id = specification()

qr_generator(name, user_name, person_id)

notification(APP_ID, user_name, push_url, headers, upload_url)