import qrcode
import random
import re
from qrcode_uploader import upload_qr, send_notification


class CreateUserQr:
    pattern = '^[A-Z][a-z]+\\s[A-Z][a-z]+$'

    def __init__(self, pattern=pattern):

        self.name = input("What's your name? \n")
        while True:
            if re.match(pattern, self.name):
                self.user_name = self.name.lower().replace(' ', '.')
                self.user_id = random.randint(1000, 9999)
                break
            print('please Enter your name in the below format:\n[Amir Aleahmad]')
            self.name = input("What's your name? \n")

    def get_info(self):
        return self.name, self.user_name, self.user_id

    def create_qr(self):
        img = qrcode.make(f"Name: '{self.name}'\nUsername: '{self.user_name}'\nUserID: '{self.user_id}'")
        img.save(f"{self.user_id}.jpeg")


if __name__ == '__main__':
    user1 = CreateUserQr()
    user1.create_qr()
    upload_qr(image_name=user1.user_id)
    send_notification(name=user1.name)
