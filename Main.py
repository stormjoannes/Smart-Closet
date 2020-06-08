from MatchingAppend import *
from WeerAPI import *

def config():
    bestaandeUser = input("Heb je al een account ja of nee: ")
    if bestaandeUser == 'ja':
        naamUser = input("Wat is je naam: ").lower()
        if checkIfExist(naamUser) == True:
            opties(naamUser)
        else:
            print('deze username is niet in gebruik')
            config()

    elif bestaandeUser == 'nee':
        print('maak een account aan')
        naamUser = input("Wat is je naam: ").lower()

        if checkIfExist(naamUser) == False:
            with open('Kledingkast.json', 'r+') as doc:
                allInf = json.load(doc)

            with open('Kledingkast.json', 'w') as document:
                allInf[naamUser] = []
                json.dump(allInf, document)
                document.close()
                doc.close()

            opties(naamUser)
        else:
            print('deze username is al in gebruik')
            config()

    else:
        config()

def checkIfExist(naamUser):
    with open('Kledingkast.json', 'r') as doc:
        allNames = json.load(doc)

    for i in allNames:
        if i == naamUser:
            return True
    return False


def opties(naamUser):
    print('\n')
    keuze = input("Wil je een kledingstuk toevoegen, verwijderen of uitkiezen: ").lower()
    if keuze == 'toevoegen':
        addClothes(naamUser)
        opties(naamUser)

    elif keuze == 'verwijderen':
        deleteClothes(naamUser)
        opties(naamUser)

    elif keuze == 'uitkiezen':
        weer = setValues()
        pickClothes(naamUser, weer[0], weer[1])
        opties(naamUser)

    else:
        print(f"'{keuze}' is geen geldige optie")
        opties(naamUser)


config()
# print(setValues())