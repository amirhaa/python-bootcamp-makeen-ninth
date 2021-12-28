import json


class Users:

    def __init__(self, name = '', email = '', phone_number = '', device_id = ''):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.device_id = device_id

    def show_info(self):
        return f'Name: {self.name}\nEmail: {self.email}\nPhone number: {self.phone_number}\nDevice id: {self.device_id}'
    
    def save_info(self):

        with open('users.json', 'r+') as json_file:
    
            data = {'users': []}
            if json.load(json_file) == '':

                json.dump(data, json_file)
                
            data = json.load(json_file)
            info = {'name': self.name, 'email': self.email, "phone number": self.phone_number, "device id": self.device_id}
            data['users'].append(info)
            json_file.seek(0)
            json.dump(data, json_file)
            info = {'name': self.name, 'email': self.email, "phone number": self.phone_number, "device id": self.device_id}
            

    def get_info(self, sth):
        
        with open('users.json') as json_file:

            data = json.load(json_file)
            for user in  data['users']:
                if sth in user.values():
                    return user
                

            


        

