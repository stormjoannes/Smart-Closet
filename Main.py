from MatchingAppend import *
from WeerAPI import *

def config():
    bestaandeUser = input("Heb je al een account ja of nee: ")
    if bestaandeUser == 'ja':
        naamUser = input("Wat is je naam: ").lower()
    elif bestaandeUser == 'nee':
        print('maak een account aan')
        naamUser = input("Wat is je naam: ").lower()

        with open('Kledingkast.json', 'r+') as doc:
            allInf = json.load(doc)

        with open('Kledingkast.json', 'w') as document:
            allInf[naamUser] = []
            json.dump(allInf, document)

    else:
        config()

def opties():
    keuze = input("Wil je een kledingstuk toevoegen, verwijderen of uitkiezen: ").lower()
    if keuze == 'toevoegen':
        addClothes()
        opties()

    elif keuze == 'verwijderen':
        deleteClothes()
        opties()

    elif keuze == 'uitkiezen':
        pickClothes()
        opties()

    else:
        print(f"'{keuze}' is geen geldige optie")
        opties()


# opties()
print(setValues())
