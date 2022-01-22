import os
from dotenv import load_dotenv, dotenv_values
from kavenegar import *
import re

load_dotenv('send_sms/modules/api.env')
data = dotenv_values('api.env')
Kavenegar_API = os.environ.get('Kavenegar_API')

class make_sms():
    api = KavenegarAPI(Kavenegar_API)
    def __init__(self, phone_number, message):
        self.phone_number = phone_number
        self.message = message
        self.params = {
            'receptor' : self.phone_number,
            'message' : self.message
        }

    def send(self):
        try:
            response = make_sms.api.sms_send(self.params)
        except Exception as exc:
            print('problem to sending the message!', exc)
