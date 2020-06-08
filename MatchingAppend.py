import json

with open('Kledingkast.json', 'r+') as allKleding:
    data = json.load(allKleding)

def addClothes():
    with open('Kledingkast.json', 'w') as allKleding:
        name = input('Naam van je kledingstuk: ').lower()
        longShort = input('Lengte van je broeks pijpen of mouwen: lang of kort: ').lower()
        opportunity = input('Category van je kledingstuk: Sport, Feestje of dagelijks leven: ').lower()
        color = input('Kleur van je kledingstuk: ').lower()
        brand = input('Merk van je kledingstuk: ').lower()
        category = input('Draag je dit kledingstuk alleen: ').lower()

        nieuweData = {"naam": name,
                      "langKort": longShort,
                      "gelegenheid": opportunity,
                      "kleur": color,
                      "merk": brand,
                      "categorie": category}

        data['kleding'].append(nieuweData)
        json.dump(data, allKleding)

def deleteClothes():
    with open('Kledingkast.json', 'w') as allKleding:
        name = input('Naam van je kledingstuk: ').lower()
        longShort = input('Lengte van je broeks pijpen of mouwen: lang of kort: ').lower()
        opportunity = input('Category van je kledingstuk: Sport, Feestje of dagelijks leven: ').lower()
        color = input('Kleur van je kledingstuk: ').lower()
        brand = input('Merk van je kledingstuk: ').lower()
        category = input('Draag je dit kledingstuk alleen: ').lower()


        for i in data['kleding']:
            if i['naam'] == name and i['langKort'] == longShort and i['gelegenheid'] == opportunity and i['kleur'] == color and i['merk'] == brand and i['categorie'] == category:
                data['kleding'].remove(i)
        json.dump(data, allKleding)



def pickClothes():
    for i in data['kleding']:
        print(i)