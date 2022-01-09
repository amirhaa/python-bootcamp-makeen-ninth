import qrcode
import requests
import specifications

def qr_generator(name, user_name, person_id):
    img = qrcode.make(f'{name}\nid: {person_id}\nUser name: {user_name}')
    img.save(f'{user_name}.jpeg')


def upload_qr(qr_name, upload_url, headers):

    files = [('image', (f'{qr_name}.jpeg', open(f'{qr_name}.jpeg','rb'),'image/jpeg'))]
    
    response = requests.post(upload_url, headers= headers, files= files)
    return response.json().get("url", "")


def notification(APP_ID, user_name, push_url, headers, upload_url):

    qr =upload_qr(user_name, upload_url, headers)
    data = {
        'app_ids': APP_ID,
        'data': {
            'title': 'QR code: ',
            'content': qr
        }
    }

    requests.post(push_url, json= data, headers= headers)