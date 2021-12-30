import make_user
from tools import load_from_json
from send_notification import Notification

if __name__ == '__main__':
    print('Welcome to Notifier :)')


while True:
    name = input('Enter the user\'s name (or enter "exit" to leave): ')
    if name.lower().rstrip() == 'exit':
        break
    email = input('Enter the user\'s email: ').lower().rstrip()
    phone_num = input('Enter the user\'s phone number: ').rstrip()
    device_id = input('Enter the user\'s device id: ').rstrip()

    user = make_user.User(name, email, phone_num, device_id)
    user.save()
    print('****************************************')


pn = input('\nEnter the phone number of the user to check if he/she exists : ').rstrip()
while True:    
    user_info = load_from_json(pn, 'users.json')
    if user_info:
        user2 = make_user.User(*user_info)
        print(f'sending message to {user2.name}...')
        break
    else:
        pn = input('the user your\'re looking for doesn\'t exist! please try again : ').rstrip()


notif = Notification(user2)
notif.send_sms('پیامک آزمایشی - مکین')
notif.push_notification('Hello;', 'how do doing\'?')

print('\nmessage sent.\nbye...\n')
