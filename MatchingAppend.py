import json

with open('Kledingkast.json', 'r+') as allKleding:
    data = json.load(allKleding)

def addClothes():
    with open('Kledingkast.json', 'w') as allKleding:

    name = input('Naam van je kledingstuk: ').lower()
    longShort = input('Lengte van je broeks pijpen of mouwen: lang of kort: ').lower()
    category = input('Category van je kledingstuk: Sport, Feestje of dagelijks leven: ').lower()
    color = input('Kleur van je kledingstuk: ').lower()

    nieuweData = {"naam": name,
                  "langKort": longShort,
                  "gelegenheid": category,
                  "kleur": color}

    data['kleding'].append(nieuweData)
    allKleding.write(data)
    allKleding.close()



def pickClothes():
    for i in data['kleding']:
        print(i)

addClothes()
# pickClothes()