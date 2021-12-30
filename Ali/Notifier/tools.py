import json
import re


def validate_email(email):   
    
    email_pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    while True:
        if(re.match(email_pattern, email)):   
            break   
        else:   
            email = input('invalid email! please try again : ')

    return email


def validate_phonenumber(phone_number):   
    
    pn_pattern = '^09[0-9]{9}$'
    while True:
        if(re.match(pn_pattern, phone_number)):   
            break   
        else:   
            phone_number = input('invalid phone number! please try again : ')

    return phone_number


def load_from_json(user_phone_number, jfile_name):

    with open(jfile_name, 'r') as f:
        jsn = dict(json.load(f))

    i = 0
    while True:
        
        if i == len(jsn['users']):
            print('couln\'t find the user!')
            return None

        if jsn['users'][i]['phone_number'] == user_phone_number:
            return jsn['users'][i]['name'], jsn['users'][i]['email'], jsn['users'][i]['phone_number'], jsn['users'][i]['device_id']

        i += 1