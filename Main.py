from MatchingAppend import *
from WeerAPI import *
from AddOrDelete import *
from datetime import datetime

def config():
    bestaandeUser = input("Heb je al een account ja of nee: ").lower().strip()
    if bestaandeUser == 'ja':
        naamUser = input("Wat is je naam: ").lower()
        if checkIfExist(naamUser) == True:
            with open('Kledingkast.json', 'r+') as doc:
                getWeatherCoords = json.load(doc)
            opties(naamUser, getWeatherCoords["storm joannes"][0]["stad"], getWeatherCoords["storm joannes"][0]["land"])
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
                stad = input('In welke stad staat je kledingkast: ').lower()
                land = input('In welk Land staat je kledingkast (afkorting van land): ').lower()
                allInf[naamUser] = [{"stad": stad, "land": land}, {"gedragen": []}]
                json.dump(allInf, document)
                document.close()
                doc.close()

            opties(naamUser, stad, land)
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


def opties(naamUser, stad, land):

    refreshGedragen(naamUser)

    print('\n')
    keuze = input("Wil je een kledingstuk toevoegen, verwijderen of uitkiezen: ").lower()
    if keuze == 'toevoegen':
        addClothes(naamUser)
        opties(naamUser, stad, land)

    elif keuze == 'verwijderen':
        deleteClothes(naamUser)
        opties(naamUser, stad, land)

    elif keuze == 'uitkiezen':
        huidigeWeer = setValuesWeer(stad, land)
        pickClothes(naamUser, huidigeWeer[0], huidigeWeer[1])
        opties(naamUser, stad, land)

    else:
        print(f"'{keuze}' is geen geldige optie")
        opties(naamUser, stad, land)

def refreshGedragen(naamUser):
    with open('Kledingkast.json', 'r+') as forRefresh:
        dataRefresh = json.load(forRefresh)

    date_format = "%Y-%m-%d"
    today = datetime.today().strftime("%Y-%m-%d")

    for x in dataRefresh[naamUser][1]["gedragen"]:
        previousDay = datetime.strptime(x[2], date_format).strftime("%Y-%m-%d")
        diff = abs(today - previousDay)
        print(diff)
        if str(diff) > str(1):
            with open('Kledingkast.json', 'w') as frRefresh:
                dataRefresh[naamUser][1]["gedragen"].remove(x)
                json.dump(dataRefresh, frRefresh)
                frRefresh.close()

config()
# print(setValuesWeer())