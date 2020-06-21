import json

with open('../jsonFiles/Kledingkast.json', 'r') as doc:
    allInf = json.load(doc)

for i in allInf:
    print(i)
