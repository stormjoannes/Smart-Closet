from MatchingAppend import *
from WeerAPI import *
from AddOrDelete import *

def config():
    try:
        bestaandeUser = input("Heb je al een account ja of nee: ").lower().strip()
        if bestaandeUser == 'ja':
            naamUser = input("Wat is je naam: ").lower()
            if checkIfExist(naamUser) == True:
                with open('Kledingkast.json', 'r') as doc:
                    getWeatherCoords = json.load(doc)
                opties(naamUser, getWeatherCoords[naamUser][0]["gegevens"][0]["locatie"]["stad"], getWeatherCoords[naamUser][0]["gegevens"][0]["locatie"]["land"])
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
                    allInf[naamUser] = [{"gegevens": [{"locatie": {"stad": stad, "land": land}}, {"overigeGeg":  {"betweenWear": 1}}]}, {"gedragen": []}]

                    json.dump(allInf, document)
                    document.close()
                    doc.close()

                opties(naamUser, stad, land)
            else:
                print('deze username is al in gebruik')
                config()

        else:
            config()
    except:
        with open('BackupKledingkast.json', 'r') as forReset:
            resetData = json.load(forReset)

        with open('Kledingkast.json', 'w') as frReset:
            json.dump(resetData, frReset)
            frReset.close()

        print("er is iets mis gegaan, je word terug gebracht naar het beginscherm. probeer het zo opnieuw." + '\n')
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
    keuze = input("Wil je een kledingstuk toevoegen, verwijderen, uitkiezen of wil je gegevens wijzigen : ").lower()
    if keuze == 'toevoegen':
        addClothes(naamUser)

    elif keuze == 'verwijderen':
        deleteClothes(naamUser)

    elif keuze == 'uitkiezen':
        huidigeWeer = setValuesWeer(stad, land)
        pickClothes(naamUser, huidigeWeer[0], huidigeWeer[1])

    elif keuze == 'gegevens wijzigen':
        gegWijzigen(naamUser, stad, land)

    else:
        print(f"'{keuze}' is geen geldige optie")
        opties(naamUser, stad, land)

    with open('Kledingkast.json', 'r') as forBackup:
        backupDATA = json.load(forBackup)

    with open('BackupKledingkast.json', 'w') as frRefresh:
        json.dump(backupDATA, frRefresh)
        frRefresh.close()

    opties(naamUser, stad, land)

def refreshGedragen(naamUser):
    with open('Kledingkast.json', 'r+') as forRefresh:
        dataRefresh = json.load(forRefresh)

    for x in dataRefresh[naamUser][1]["gedragen"]:
        differ = getTimeDifference(x)

    tussenPeriodeKleren = dataRefresh[naamUser][0]["gegevens"][1]["overigeGeg"]["betweenWear"]

    if differ > tussenPeriodeKleren:
        with open('Kledingkast.json', 'w') as frRefresh:
            dataRefresh[naamUser][1]["gedragen"].remove(x)
            json.dump(dataRefresh, frRefresh)
            frRefresh.close()

def gegWijzigen(naamUser, stad, land):
    with open('Kledingkast.json', 'r+') as vrWijzig:
        allWijzig = json.load(vrWijzig)

    with open('Kledingkast.json', 'w') as vrWijzigWrite:
        wijzig = input("Wat wil je wijzigen? De locatie of het tussenwear getal: ").lower()

        if wijzig == "locatie":
            stadWijzig = input('In welke stad staat je kledingkast: ').lower()
            landWijzig = input('In welk Land staat je kledingkast (afkorting van land): ').lower()
            allWijzig[naamUser][0]["gegevens"][0]["locatie"]["stad"] = stadWijzig
            allWijzig[naamUser][0]["gegevens"][0]["locatie"]["land"] = landWijzig

        elif wijzig == "tussenwear":
           tussenWearWijzig = input('Hoeveel dagen wil je dat de tussenwear is: ').lower()
           allWijzig[naamUser][0]["gegevens"][1]["overigeGeg"]["betweenWear"] = int(tussenWearWijzig)

        else:
            print("geen geldige optie, je word terug gestuurd naar het mainscreen")

        json.dump(allWijzig, vrWijzigWrite)
        vrWijzigWrite.close()
        opties(naamUser, stad, land)


config()