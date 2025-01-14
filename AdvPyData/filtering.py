import json

def filterEvens(x):
    if x % 2 == 0:
        return False
    return True

def filterUppers(x):
    if x.isupper():
        return False
    return True

nums = [1, 28, 13, 344, 345, 676, 677, 2, 8]
chars = 'asddasASDsfOSFmS'

odds = list(filter(filterEvens, nums))
lowers = list(filter(filterUppers, chars))

"""print(odds)
print(lowers)"""

with open('all_month.json', 'r', encoding='utf-8') as datafile:
    data = json.load(datafile)

def notAQuake(q):
    if q['properties']['type'] == 'earthquake':
        return False
    return True

events = list(filter(notAQuake, data['features']))
print(f"Total events: {len(events)}")
for i in range(0, 10):
    print(events[i]['properties']['type'])

print("merge test")