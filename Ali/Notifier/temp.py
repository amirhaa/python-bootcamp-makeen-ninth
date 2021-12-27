import json
from tools import *

dikt = {
            "name": "Aliiiii",
            "email": "ali@gmail.commmm",
            "phone_number": "765433333",
            "device_id": "asdug4uh43aaaa"

}
    # users.append(dikt)
jfile = 'jfile.json'

# with open(jfile, 'r+') as jf:
#     text = jf.read()
#     json_info = json.loads(jf)
# print(text)
# print('-------------')
# print(json_info)

print(read_from_json(jfile))
print(type(read_from_json(jfile)))
print('--------------------\n')
append_to_json(dikt, jfile)
print(read_from_json(jfile))