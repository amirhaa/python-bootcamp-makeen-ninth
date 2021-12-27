import json


def read_from_json(file_name):

    with open(file_name, 'r') as openfile:
        json_object = json.load(openfile)

    return dict(json_object)
    
            

def append_to_json(data_dict, file_name):
    
    current_json = dict(read_from_json(file_name))
    current_json['users'].append(data_dict)

    json_object = json.dumps(current_json, indent = 4)
    
    with open(file_name, 'w') as jfile:
        jfile.write(json_object)
