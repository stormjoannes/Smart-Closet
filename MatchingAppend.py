import json
from WeerAPI import *

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
        dataDelete = json.load(allKleding)

    with open('Kledingkast.json', 'w') as ALL:
        nameDelete = input('Naam van je kledingstuk: ').lower()
        longShortDelete = input('Lengte van je broeks pijpen of mouwen: lang of kort: ').lower()
        opportunityDelete = input('Category van je kledingstuk: Sport, Feestje of dagelijks leven: ').lower()
        colorDelete = input('Kleur van je kledingstuk: ').lower()
        brandDelete = input('Merk van je kledingstuk: ').lower()
        categoryDelete = input('Category van kledingstuk: ').lower()

        checkIfDone = False

        for i in range(1, len(dataDelete[personName])):
        # for i in dataDelete[personName]:
            if dataDelete[personName][i]['naam'] == nameDelete and dataDelete[personName][i]['langKort'] == longShortDelete and dataDelete[personName][i]['gelegenheid'] == opportunityDelete and dataDelete[personName][i]['kleur'] == colorDelete and dataDelete[personName][i]['merk'] == brandDelete and dataDelete[personName][i]['categorie'] == categoryDelete:
                dataDelete[personName].remove(dataDelete[personName][i])
                checkIfDone = True
                break

        if checkIfDone == False:
            print("dit kledingstuk bestaat niet en kan dus niet verwijderd worden")
        else:
            print(f'kledingstuk {nameDelete} is verwijderd')
        json.dump(dataDelete, ALL)
        ALL.close()



def pickClothes(personName, currentTemp, weersSituatie):
    with open('Kledingkast.json', 'r') as allKleding:
        dataSearch = json.load(allKleding)

    print(personName)
    print(currentTemp)
    print(weersSituatie)