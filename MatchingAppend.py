import json
import random
from datetime import datetime


def pickClothes(personName, currentTemp, weersSituatie):
    # scheelt het 1 maand doe je, de dag - maanden dat het scheelt n . Nieuwe data min die waarde heb je hoeveel dagen het scheelt met een variatie van 1 dag per bij de helft van de maanden

    WarmNaarKoudTopDagelijks = {1: ["trui", "vest"], 2: ["shirt"], 3: ["topje", "naveltrui", "shirt"]}
    WarmNaarKoudBottomDagelijks = {1: ["jeans", "joggingsbroek"], 2: ["chino", "jeans met gaten", "jeans"],
                                   3: ["rokje", "broekje"]}

    WarmNaarKoudTopSport = {1: ["trui", "vest"], 2: ["shirt"], 3: ["topje", "naveltrui", "shirt"]}
    WarmNaarKoudBottomSport = {1: ["jeans", "joggingsbroek"], 2: ["chino", "jeans met gaten", "jeans"],
                               3: ["rokje", "broekje"]}

    WarmNaarKoudTopFeestje = {1: ["trui", "vest"], 2: ["shirt"], 3: ["topje", "naveltrui", "shirt"]}
    WarmNaarKoudBottomFeestje = {1: ["jeans", "joggingsbroek"], 2: ["chino", "jeans met gaten", "jeans"],
                                 3: ["rokje", "broekje"]}

    keuzeGelegenheid = input('Wil je iets voor het sporten, dagelijks leven of een feestje: ').lower()

    if keuzeGelegenheid == "dagelijks leven":
        opportunitySet(WarmNaarKoudTopDagelijks, WarmNaarKoudBottomDagelijks, personName, currentTemp, weersSituatie)

    elif keuzeGelegenheid == "sporten":
        opportunitySet(WarmNaarKoudTopSport, WarmNaarKoudBottomSport, personName, currentTemp, weersSituatie)

    elif keuzeGelegenheid == "feestje":
        opportunitySet(WarmNaarKoudTopFeestje, WarmNaarKoudBottomFeestje, personName, currentTemp, weersSituatie)

    else:
        print('De gekozen gelgenheid is niet in gebruik!')
        pickClothes(personName, currentTemp, weersSituatie)


def opportunitySet(WarmNaarKoudTop, WarmNaarKoudBottom, personName, currentTemp, weersSituatie):
    if currentTemp < 15:
        LangOfKortTop = "lang"
        LangOfKortBottom = "lang"

        tresholdTop = 1
        tresholdBottom = 1

    elif currentTemp >= 15 and currentTemp < 20:
        LangOfKortTop = "lang"
        LangOfKortBottom = "lang"

        tresholdTop = len(WarmNaarKoudTop) - 1
        tresholdBottom = len(WarmNaarKoudBottom) - 1

    elif currentTemp >= 20 and currentTemp < 23:
        LangOfKortTop = "kort"
        LangOfKortBottom = "Lang"

        tresholdTop = len(WarmNaarKoudTop)
        tresholdBottom = len(WarmNaarKoudBottom) - 1

    elif currentTemp >= 23:
        LangOfKortTop = "kort"
        LangOfKortBottom = "kort"

        tresholdTop = len(WarmNaarKoudTop)
        tresholdBottom = len(WarmNaarKoudBottom)

    mogelijkeTops = searchTopBottom(LangOfKortTop, tresholdTop, WarmNaarKoudTop, personName)
    top = random.choice(mogelijkeTops)

    if top[2] != "jurkje":
        mogelijkeBottoms = searchTopBottom(LangOfKortBottom, tresholdBottom, WarmNaarKoudBottom, personName)
        bottom = random.choice(mogelijkeBottoms)

    aangetrokken = False

    while aangetrokken == False:
        with open('Kledingkast.json', 'r+') as inf:
            data = json.load(inf)

        top = random.choice(mogelijkeTops)

        if top[2] != "jurkje":
            bottom = random.choice(mogelijkeBottoms)
            while bottom[1] == top[1] and len(bottom) > 1:
                bottom = random.choice(mogelijkeBottoms)
        else:
            bottom == None

        status = 'positive'

        for index in data[personName][1]["gedragen"]:
            if top in index and bottom in index:
                status = 'negative'
                if len(mogelijkeTops) <= 1 and len(mogelijkeBottoms) <= 1:
                    print("Helaas hebben we met deze beperkte kleding hoeveelheid geen setje kunnen vinden om aan te trekken.")
                    status = 'execute'

        if status != 'negative':
            if len(mogelijkeBottoms) > 1 and len(mogelijkeTops) > 1 and status != 'execute':
                print(top)
                print(bottom)
                aantrekken = input("ga je dit setje aantrekken ja of nee: ").lower()
                if aantrekken == "ja":
                    aangetrokken = True

                    with open('Kledingkast.json', 'w') as ALL:
                        today = datetime.today().strftime("%Y-%m-%d")

                        formatVoorAppend = [top, bottom, str(today)]
                        data[personName][1]["gedragen"].append(formatVoorAppend)

                        print(formatVoorAppend)
                        json.dump(data, ALL)
                        ALL.close()

                else:
                    print('we zoeken een nieuw setje voor je!')
                    mogelijkeTops.remove(top)
                    mogelijkeBottoms.remove(bottom)
            else:
                print(
                    "Helaas hebben we met deze beperkte kleding hoeveelheid geen setje kunnen vinden om aan te trekken.")
                aangetrokken = True


def searchTopBottom(LangOfKortTopBottom, tresholdTopBottom, WarmNaarKoudTopBottom, personName):
    with open('Kledingkast.json', 'r') as allKleding:
        dataSearch = json.load(allKleding)

    possibleTop = []
    for x in range(2, len(dataSearch[personName])):
        if dataSearch[personName][x]["categorie"] in WarmNaarKoudTopBottom[tresholdTopBottom] and dataSearch[personName][x]["langKort"] == LangOfKortTopBottom:
            tempList = [dataSearch[personName][x]["naam"], dataSearch[personName][x]["kleur"],
                        dataSearch[personName][x]["categorie"], dataSearch[personName][x]["merk"],
                        dataSearch[personName][x]["langKort"]]
            possibleTop.append(tempList)
    return possibleTop

def getTimeDifference(x):
    date_format = "%Y-%m-%d"
    today = datetime.today()

    previousDay = datetime.strptime(x[2], date_format)

    diff = abs((today - previousDay).days)
    return diff
