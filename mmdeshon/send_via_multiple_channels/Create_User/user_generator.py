import os
import json


class CreateUser:
    def __init__(self, user_name, user_email, user_phone_number, user_device_id):
        self.user_credentials = {
            "users": [{
                "name": user_name,
                "email": user_email,
                "pn": user_phone_number,
                "device_id": user_device_id
            }]
        }

    def save_to_json(self):
        jsonfile = '../user_credentials.json'
        data = self.user_credentials
        if os.path.exists(jsonfile):
            with open(jsonfile) as f:
                data = json.load(f)
            data['users'].insert(0, (data['users'][0]))

        with open(jsonfile, 'w') as f:
            json.dump(data, f)
