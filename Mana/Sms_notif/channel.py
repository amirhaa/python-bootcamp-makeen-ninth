import requests
from kavenegar import *



class Channel:

    def send_push_notification(self, device_id):

        AUTH_KEY = '4979bff4c2a77b2f4dfe1943a4af56239e687a48'
        APP_ID = '5ej19744zxjl9n3e'

        url = 'https://api.pushe.co/v2/messaging/web-rapid/'

        headers = {'Authorization': f'Token {AUTH_KEY}','Content-Type': 'application/json'}
        

        data = {'app_id': APP_ID,'data': {'title': 'Message:','content': 'Done!!!'},'device_id': [device_id]}
       
        requests.post(url, data=data, headers=headers)

    def send_sms(self, phone_number):

        API_KEY = '5131662F3033556F567A557168316754794D67527A6D394E517946586C6776724A6779676E66524E584C593D'

        try:
            api = KavenegarAPI(API_KEY)
            params = {
                'sender': '10008663',
                'receptor': phone_number,
                'message': 'sssss',
            } 
            api.sms_send(params)

        except APIException as e: 
            print(e)
        except HTTPException as e: 
            print(e)
