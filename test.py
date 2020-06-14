
import json
with open('Kledingkast.json', 'r+') as vrWijzig:
    allWijzig = json.load(vrWijzig)

# with open('Kledingkast.json', 'w') as vrWijzigWrite:
print(allWijzig['storm joannes'][0]["gegevens"][0]["locatie"]["stad"])
# print(allWijzig['storm joannes'][0])

