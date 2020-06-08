import json
from Main import config

with open('Kledingkast.json', 'r+') as allKleding:
    data = json.load(allKleding)

def addClothes():
    with open('Kledingkast.json', 'w') as allKleding:
        nameAdd = input('Naam van je kledingstuk: ').lower()
        longShortAdd = input('Lengte van je broeks pijpen of mouwen: lang of kort: ').lower()
        opportunityAdd = input('Category van je kledingstuk: Sport, Feestje of dagelijks leven: ').lower()
        colorAdd = input('Kleur van je kledingstuk: ').lower()
        brandAdd = input('Merk van je kledingstuk: ').lower()
        categoryAdd = input('Draag je dit kledingstuk alleen: ').lower()

        nieuweData = {"naam": nameAdd,
                      "langKort": longShortAdd,
                      "gelegenheid": opportunityAdd,
                      "kleur": colorAdd,
                      "merk": brandAdd,
                      "categorie": categoryAdd}

        data['kleding'].append(nieuweData)
        json.dump(data, allKleding)

def deleteClothes():
    with open('Kledingkast.json', 'w') as allKleding:
        nameDelete = input('Naam van je kledingstuk: ').lower()
        longShortDelete = input('Lengte van je broeks pijpen of mouwen: lang of kort: ').lower()
        opportunityDelete = input('Category van je kledingstuk: Sport, Feestje of dagelijks leven: ').lower()
        colorDelete = input('Kleur van je kledingstuk: ').lower()
        brandDelete = input('Merk van je kledingstuk: ').lower()
        categoryDelete = input('Draag je dit kledingstuk alleen: ').lower()


        for i in data['kleding']:
            if i['naam'] == nameDelete and i['langKort'] == longShortDelete and i['gelegenheid'] == opportunityDelete and i['kleur'] == colorDelete and i['merk'] == brandDelete and i['categorie'] == categoryDelete:
                data['kleding'].remove(i)
        json.dump(data, allKleding)



def pickClothes(currentTemp, weersSituatie):
    print('kiezen')