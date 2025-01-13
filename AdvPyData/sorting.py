import json

with open('all_month.json', 'r', encoding='utf-8') as datafile:
    data = json.load(datafile)

def gatmag(dataitem):
    magnitude = dataitem['properties']['mag']
    if (magnitude is None):
        magnitude = 0
    return float(magnitude)

data["features"].sort(key=gatmag, reverse=True)

for i in range(0,10):
    print(data["features"][i]["properties"]["place"])