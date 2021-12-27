import os
from dotenv import load_dotenv
from user_generator import CreateUser

load_dotenv('../device_id.env')
DEVICE_ID = os.getenv('DEVICE_ID')


def user_factory():

    user_input = ''
    while user_input not in ['y', 'Y', 'n', 'N']:
        user_input = input("Are you Going to Add a new user?[Y/n]\n")

    if user_input in ['y', 'Y']:
        name = input('What is your name?\n')
        email = input('What is your email address?\n')
        phone_number = input('What is your Phone Number?\n')
        user = CreateUser(name, email, phone_number, DEVICE_ID)
        user.save_to_json()
        print('____________')
        print(f'new user created for "{name}"')
        print('____________')
    else:
        print('____________')
        print('bye bye')
        print('____________')


if __name__ == '__main__':
    user_factory()
