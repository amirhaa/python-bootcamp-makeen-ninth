import re
import random
import qrcode
import requests

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


def notification(APP_ID, file_name, push_url, headers, upload_url):

    qr =upload_qr(file_name, upload_url, headers)
    
    data = {
        'app_ids': APP_ID,
        'data': {
            'title': 'QR code: ',
            'content': qr
        }
    }

    requests.post(push_url, json= data, headers= headers)


    
