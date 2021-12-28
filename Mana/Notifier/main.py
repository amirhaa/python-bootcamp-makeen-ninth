from users import Users
from channel import Channel


if __name__ == '__main__':

    answer = input('Do you wanna enter your info?[y/n]\n')
    if answer in ['y', 'Y']:
        name, email, phone_number, device_id = input('Please enter your name, email, phone number and your device id\n').split()
        user = Users(name, email, phone_number, device_id)
        user.save_info()


    answer = input('Do you wanna get your info?[y/n]\n')
    if answer in ['y', 'Y']:
        sth = input('Enter sth:\n')
        user = Users().get_info(sth)
        if user:
            obj = Users(user['name'], user['email'], user['phone number'], user['device id'])
            print(Users.show_info(obj))
        else:
            print('User does not exist')


    answer = input('Do you wanna send push notification?[y/n]\n')
    if answer in ['y', 'Y']:
        name = input('Who wanna send push notification?')
        user = Users().get_info(name)

        if user:
            device_id = user['device id']
            obj = Channel()
            obj.send_push_notification(device_id, 'somethiing')
        else:
            print('User does not exist')


    answer = input('Do you wanna send sms?')
    if answer in ['y', 'Y']:
        name = input('Who wanna send sms?')
        user = Users().get_info(name)

        if user:
            phone_number = user['phone number']
            obj = Channel()
            obj.send_sms(phone_number)
        else:
            print('User does not exist')


        

    
    
