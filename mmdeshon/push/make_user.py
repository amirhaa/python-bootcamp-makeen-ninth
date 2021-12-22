import qrcode
import random
import re


class CreateUserQr:

    user_id = ''
    user_name = ''
    name = ''

    @classmethod
    def create_user(cls):
        pattern = '^[A-Z][a-z]+\\s[A-Z][a-z]+$'
        cls.name = input("What's your name? \n")
        while True:
            if re.search(pattern, cls.name):
                cls.user_name = cls.name.lower().replace(' ', '.')
                cls.user_id = random.randint(1000, 9999)
                return cls.name, cls.user_name, cls.user_id

            else:
                print('please Enter your name in the below foramt:\n[Amir Aleahmad]')
                cls.name = input("What's your name? \n")

    @classmethod
    def create_qr(cls):
        user_detail = CreateUserQr.create_user()
        image = qrcode.make(f"Name is: '{user_detail[0]}'\nUsername is '{user_detail[1]}'\nUserID is '{user_detail[2]}'")
        type(image)
        image.save(f"{user_detail[2]}.jpeg")
        return user_detail


if __name__ == '__main__':
    print('hiii')
