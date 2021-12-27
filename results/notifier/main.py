import config
from users import User
from notification import Notification

if __name__ == "__main__":

    user_dict = {
        "username": "mmdeshon",
        "email": "mmdeshon@chmail.ir",
        "phone_number": "09190149233",
        "device_id": "5ej19744zxjl9n3e53db02231bdd4b9399e1ba885673d8a1"
    }

    user = User(
        username=user_dict.get('username', ''),
        email=user_dict.get('email', ''),
        phone_number=user_dict.get('phone_number', ''),
        device_id=user_dict.get('device_id', '')
    )

    user.save()

    u = User.get_user('mmdeshon')    

    notification = Notification(
        user=u, 
        app_id=config.APP_ID, 
        auth_token=config.AUTH_TOKEN
    )

    notification.send(title="Hello", content="Are you doing well?")