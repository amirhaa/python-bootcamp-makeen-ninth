import os
from kavenegar import *
from dotenv import load_dotenv

load_dotenv('Kaveh_Negar.env')
API_KEY = os.getenv('API_KEY')
SENDER_NUMBER = os.getenv('SENDER_NUMBER')


def send_sms():
    with open('../user_credentials.json') as f:
        tmp = json.load(f)
    newest_user = tmp['users'][0]

    try:
        api = KavenegarAPI('7138447037326E374954624958754C7A776D782F4C76435A765251316D533453306151553131732B7A4A633D')
        params = {'receptor': newest_user['pn'],
                  'message': f"name: {newest_user['name']}\n email: {newest_user['email']}"}
        response = api.sms_send(params)
        print(response)
    except Exception as e:
        print(e)
