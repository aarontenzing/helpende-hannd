import json


def write(data,filename = 'data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
