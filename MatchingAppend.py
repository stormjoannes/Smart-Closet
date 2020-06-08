import json

def addClothes(personName):
    with open('Kledingkast.json', 'r+') as allKleding:
        data = json.load(allKleding)

    with open('Kledingkast.json', 'w') as ALL:
        nameAdd = input('Naam van je kledingstuk: ').lower()
        longShortAdd = input('Lengte van je broeks pijpen of mouwen: lang of kort: ').lower()
        opportunityAdd = input('Category van je kledingstuk: Sport, Feestje of dagelijks leven: ').lower()
        colorAdd = input('Kleur van je kledingstuk: ').lower()
        brandAdd = input('Merk van je kledingstuk: ').lower()
        categoryAdd = input('Category van kledingstuk: ').lower()

        nieuweData = {"naam": nameAdd,
                      "langKort": longShortAdd,
                      "gelegenheid": opportunityAdd,
                      "kleur": colorAdd,
                      "merk": brandAdd,
                      "categorie": categoryAdd}

        data[personName].append(nieuweData)
        json.dump(data, ALL)
        ALL.close()

def deleteClothes(personName):
    with open('Kledingkast.json', 'r+') as allKleding:
        data = json.load(allKleding)

    with open('Kledingkast.json', 'w') as ALL:
        nameDelete = input('Naam van je kledingstuk: ').lower()
        longShortDelete = input('Lengte van je broeks pijpen of mouwen: lang of kort: ').lower()
        opportunityDelete = input('Category van je kledingstuk: Sport, Feestje of dagelijks leven: ').lower()
        colorDelete = input('Kleur van je kledingstuk: ').lower()
        brandDelete = input('Merk van je kledingstuk: ').lower()
        categoryDelete = input('Category van kledingstuk: ').lower()


        for i in data[personName]:
            if i['naam'] == nameDelete and i['langKort'] == longShortDelete and i['gelegenheid'] == opportunityDelete and i['kleur'] == colorDelete and i['merk'] == brandDelete and i['categorie'] == categoryDelete:
                data[personName].remove(i)
                break
        json.dump(data, ALL)
        ALL.close()



def pickClothes(personName, currentTemp, weersSituatie):
    with open('Kledingkast.json', 'r+') as allKleding:
        data = json.load(allKleding)

    print('kiezen')