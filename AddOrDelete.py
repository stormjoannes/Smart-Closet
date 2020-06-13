import json

def addClothes(personName, nameAdd, longShortAdd, opportunityAdd, colorAdd, brandAdd, categoryAdd):
    # print("add")
    # print(personName)
    with open('Kledingkast.json', 'r+') as allKleding:
        data = json.load(allKleding)

    with open('Kledingkast.json', 'w') as ALL:
        # nameAdd = input('Naam van je kledingstuk: ').lower()
        # longShortAdd = input('Lengte van je broeks pijpen of mouwen: lang of kort: ').lower()
        # opportunityAdd = input('Category van je kledingstuk: Sport, Feestje of dagelijks leven: ').lower()
        # colorAdd = input('Kleur van je kledingstuk: ').lower()
        # brandAdd = input('Merk van je kledingstuk: ').lower()
        # categoryAdd = input('Category van kledingstuk: ').lower()

        nieuweData = {"naam": nameAdd,
                      "langKort": longShortAdd,
                      "gelegenheid": opportunityAdd,
                      "kleur": colorAdd,
                      "merk": brandAdd,
                      "categorie": categoryAdd}

        data[personName].append(nieuweData)
        json.dump(data, ALL)
        ALL.close()

def deleteClothes(personName, nameDelete, longShortDelete, opportunityDelete, colorDelete, brandDelete, categoryDelete):
    with open('Kledingkast.json', 'r+') as allKleding:
        dataDelete = json.load(allKleding)

    print("Alle verwijderbare kleding:")
    for allCl in range(2, len(dataDelete[personName])):
        print(dataDelete[personName][allCl])

    with open('Kledingkast.json', 'w') as ALL:
        # nameDelete = input('Naam van je kledingstuk: ').lower()
        # longShortDelete = input('Lengte van je broeks pijpen of mouwen: lang of kort: ').lower()
        # opportunityDelete = input('Category van je kledingstuk: Sport, Feestje of dagelijks leven: ').lower()
        # colorDelete = input('Kleur van je kledingstuk: ').lower()
        # brandDelete = input('Merk van je kledingstuk: ').lower()
        # categoryDelete = input('Category van kledingstuk: ').lower()

        checkIfDone = False

        for i in range(2, len(dataDelete[personName])):
            if dataDelete[personName][i]['naam'] == nameDelete and dataDelete[personName][i]['langKort'] == longShortDelete and dataDelete[personName][i]['gelegenheid'] == opportunityDelete and dataDelete[personName][i]['kleur'] == colorDelete and dataDelete[personName][i]['merk'] == brandDelete and dataDelete[personName][i]['categorie'] == categoryDelete:
                dataDelete[personName].remove(dataDelete[personName][i])
                checkIfDone = True
                break

        json.dump(dataDelete, ALL)
        ALL.close()
        return checkIfDone