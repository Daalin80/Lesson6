import json
import datetime
path = 'acdc.json'
with open(path, 'r') as f:
    data = json.loads(f.read())
    s = 0
    for i in data['album']['tracks']['track']:
        if i["duration"] > '0':
            s += int(i["duration"])
print("Общая длительность всех треков в секундах:", (s))
print("или:", str(datetime.timedelta(seconds=2499)))