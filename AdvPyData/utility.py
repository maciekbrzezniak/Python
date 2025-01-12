import json

values = [0, 1, 2, 3, 4, 5]

"""print(any(values))

print(all(values))

print(sum(values))"""

with open('all_month.json', 'r', encoding='utf-8') as datafile:
    data = json.load(datafile)

print(any(quake["properties"]["felt"] is not None and quake["properties"]["felt"] > 25000
          for quake in data["features"]))

print(sum(1 for quake in data["features"] if quake["properties"]["felt"]
        is not None and quake["properties"]["felt"] >= 500))

print(sum(1 for quake in data["features"] if quake["properties"]["mag"]
          is not None and quake["properties"]["mag"] >= 6))