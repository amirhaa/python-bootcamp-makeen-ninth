from tools import *
from pprint import pprint

class User:
    def __init__(self, name, email, phone_number, device_id):
        self.name = name
        self.email = email
        self.phone_num = phone_number
        self.device_id = device_id

    def save(self):
        json_file = 'users.json'

        data = {
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_num,
            'device_id': self.device_id
        }
        
        append_to_json(data, json_file)


    # def display_info(self):
    #     print(f'{self.name}\n{self.email}\n{self.phone_num}\n{self.device_id}')



# # while True:
# name = input('Enter your name (or enter "exit" to leave): ')
# # if name.lower().rstrip() == 'exit':
# #     print('Bye-bye...')
# #     break
# email = input('Enter your email: ')
# phone_num = input('Enter your phone number: ')
# device_id = input('Enter your device id: ')
# # print('****************************************')

name = input('Enter your name (or enter "exit" to leave): ')
email = input('Enter your email: ')
phone_num = input('Enter your phone number: ')
device_id = input('Enter your device id: ')


u1 = User(name, email, phone_num, device_id)
u1.save()
