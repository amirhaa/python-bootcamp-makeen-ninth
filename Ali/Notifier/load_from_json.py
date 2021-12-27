from tools import *
from MakeUser import User

def load_json(user_phone_number, jfile_name):
    jsn = dict(read_from_json(jfile_name))

    i = 0
    while True:
        if i == len(jsn['users']):
            print('couln\'t find the user!')
            return None

        if jsn['users'][i]['phone_number'] == user_phone_number:
            print('user found!!!')
            return jsn['users'][i]['name'], jsn['users'][i]['email'], jsn['users'][i]['phone_number'], jsn['users'][i]['device_id']

        i += 1



phone_num = input('Enter the phone number of the user to check if he/she exists : ')
user_info = load_json(phone_num, 'users.json')
if not user_info:
    exit()
print(user_info)
u2 = User(*user_info)
print(type(u2))
print(u2.name)
