import json

with open('../Kledingkast.json', 'r') as doc:
    getWeatherCoords = json.load(doc)
x = getWeatherCoords["storm joannes"][0]["gegevens"][0]
print(x)

