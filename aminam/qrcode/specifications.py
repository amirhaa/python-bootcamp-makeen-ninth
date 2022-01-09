import re
import random


def specification():
    
    while True:
        name = input('enter your name Example(َAmin Vaezi)')
        if re.match('^[A-Z][a-z]+\s[A-z][a-z]+$', name):
            person_id = random.randint(1000, 9999)
            user = name.split()
            return name, f'{user[0].lower()}.{user[1].lower()}', person_id
        else:
            print('The name sent is incorrect, Try again')