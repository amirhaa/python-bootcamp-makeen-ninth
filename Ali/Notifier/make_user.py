import json

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
        User.append_to_json(data, json_file)


    def display_info(self):
        print(f'{self.name}\n{self.email}\n{self.phone_num}\n{self.device_id}')


    @staticmethod
    def append_to_json(data_dict, file_name):

        with open(file_name, 'r') as jfile:
            current_json = dict(json.load(jfile))

        current_json['users'].append(data_dict)

        json_object = json.dumps(current_json, indent = 4)
        
        with open(file_name, 'w') as jfile:
            jfile.write(json_object)
