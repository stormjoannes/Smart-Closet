import json
from tkinter.messagebox import showinfo

def addClothes(personName, nameAdd, longShortAdd, opportunityAdd, colorAdd, brandAdd, categoryAdd):
    with open('Kledingkast.json', 'r') as allKleding:
        data = json.load(allKleding)

    with open('Kledingkast.json', 'w') as ALL:
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
    with open('Kledingkast.json', 'r') as allKleding:
        dataDelete = json.load(allKleding)

    with open('Kledingkast.json', 'w') as ALL:
        checkIfDone = False
        for i in range(2, len(dataDelete[personName])):
            # print(dataDelete[personName][i], "1")
            # print(personName, nameDelete, longShortDelete, opportunityDelete, colorDelete, brandDelete, categoryDelete, "2")
            if dataDelete[personName][i]['naam'] == nameDelete and dataDelete[personName][i]['langKort'] == longShortDelete and dataDelete[personName][i]['gelegenheid'] == opportunityDelete and dataDelete[personName][i]['kleur'] == colorDelete and dataDelete[personName][i]['merk'] == brandDelete and dataDelete[personName][i]['categorie'] == categoryDelete:
                dataDelete[personName].remove(dataDelete[personName][i])
                checkIfDone = True
                break

        json.dump(dataDelete, ALL)
        ALL.close()
        return checkIfDone

def toAddClothing(userName, naam, langkort, gelegenheid, kleur, merk, categorie, toHub):
    addClothes(userName, str(naam), str(langkort),
               str(gelegenheid), str(kleur), str(merk),
               str(categorie))
    toHub()

def toDeleteClothing(userName, naam, langkort, gelegenheid, kleur, merk, categorie, toHub):
    print(userName, str(naam), str(langkort),
               str(gelegenheid), str(kleur), str(merk),
               str(categorie))
    statusDelete = deleteClothes(userName, str(naam), str(langkort),
               str(gelegenheid), str(kleur), str(merk),
               str(categorie))

    if statusDelete == False:
        bericht = f'kledingstuk {str(naam)} bestaat niet en kan dus ook niet verwijderd worden!'
        showinfo(title='Delete Error', message=bericht)
    else:
        toHub()