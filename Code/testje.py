import json

with open('../jsonFiles/Datastructuur.json', 'r+') as Data:
    placeInfo = json.load(Data)

print(placeInfo["temp"]["hot"]["kort-kort"]["yes"])