import json

with open('../Kledingkast.json', 'r+') as forRefresh:
    dataRefresh = json.load(forRefresh)

for x in dataRefresh['storm joannes'][1]["gedragen"]:
    print(x[2])