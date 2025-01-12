import json

values = [1, 2, 3, 4, 5]
string = ['one', 'two', 'three', 'four', 'five']

"""print(f"The minimum value is {min(values)}")
print(f"The maximum value is {max(values)}")

print(f"The minimum value is {min(string)}")
print(f"The maximum value is {max(string)}")

print(f"The minimum value is {min(string, key=len)}")
print(f"The maximum value is {max(string, key=len)}")"""

with open('all_month.json', 'r', encoding='utf-8') as datafile:
    data = json.load(datafile)

print(data['metadata']['title'])
print(len(data['features']))

def gatmag(dataitem):
    magnitude = dataitem['properties']['mag']
    if (magnitude is None):
        magnitude = 0
    return float(magnitude)

print(min(data['features'], key=gatmag))
print(max(data['features'], key=gatmag))