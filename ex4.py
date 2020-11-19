import json
path = 'acdc.json'
with open(path, 'r') as f:
    data = json.loads(f.read())
    for i in data['album']['tracks']['track']:
        if i["duration"] > '0':
            print(i["duration"])