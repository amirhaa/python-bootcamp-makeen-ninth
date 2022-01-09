import os
import json


class User:

    _db_name = 'db.json'

    def __init__(self, username, email, phone_number, device_id):
        self._username = username
        self._email = email
        self._phone_number = phone_number
        self._device_id = device_id

    def __open_file(self):
        if not os.path.exists(self._db_name):
            with open(self._db_name, 'w+') as f:
                json.dump([], f)

    def save(self):
        self.__open_file()

        user = {
            'username': self._username,
            'email': self._email,
            'pn': self._phone_number,
            'device_id': self._device_id
        }

        with open(self._db_name, 'r+') as f:
            try:
                d = json.load(f)
            except:
                d = []
            finally:
                d = [user, *d]

                f.truncate(0)
                f.seek(0)

                json.dump(d, f)
                

    @property
    def username(self):
        return self._username

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def device_id(self):
        return self._device_id

    @classmethod
    def load_from_json(cls, sth):
        with open(cls._db_name, 'r') as f:
            try:
                users = json.load(f)

                for user in users:
                    if sth in user.values():
                        return user

            except Exception as exc:
                print(f"Cannot load from json, exc: {exc}")

    @classmethod
    def get_user(cls, sth):
        user_dict = cls.load_from_json(sth)

        if not user_dict:
            raise Exception(f"could not find any user with {sth}")

        return cls(
            username=user_dict.get('username', ''),
            email=user_dict.get('email', ''),
            phone_number=user_dict.get('pn', ''),
            device_id=user_dict.get('device_id', '') 
        )

    def __str__(self):
        return f"User[username={self._username}]"

    def __repr__(self):
        return self.__str__()