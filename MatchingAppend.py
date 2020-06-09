import json
from WeerAPI import *
import random

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

        for i in range(2, len(dataDelete[personName])):
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
    #scheelt het 1 maand doe je, de dag - maanden dat het scheelt n . Nieuwe data min die waarde heb je hoeveel dagen het scheelt met een variatie van 1 dag per bij de helft van de maanden

    WarmNaarKoudTopDagelijks = {1: ["trui", "vest"], 2: ["shirt"], 3:["topje", "naveltrui", "shirt"]}
    WarmNaarKoudBottomDagelijks = {1: ["jeans", "joggingsbroek"], 2: ["chino", "jeans met gaten", "jeans"], 3:["rokje", "broekje"]}

    WarmNaarKoudTopSport = {1: ["trui", "vest"], 2: ["shirt"], 3:["topje", "naveltrui", "shirt"]}
    WarmNaarKoudBottomSport = {1: ["jeans", "joggingsbroek"], 2: ["chino", "jeans met gaten", "jeans"], 3:["rokje", "broekje"]}

    WarmNaarKoudTopFeestje = {1: ["trui", "vest"], 2: ["shirt"], 3:["topje", "naveltrui", "shirt"]}
    WarmNaarKoudBottomFeestje = {1: ["jeans", "joggingsbroek"], 2: ["chino", "jeans met gaten", "jeans"], 3:["rokje", "broekje"]}

    keuzeGelegenheid = input('Wil je iets voor het sporten, dagelijks leven of een feestje: ').lower()

    if keuzeGelegenheid == "dagelijks":
        opportunitySet(WarmNaarKoudTopDagelijks, WarmNaarKoudBottomDagelijks, personName, currentTemp, weersSituatie)

    elif keuzeGelegenheid == "sporten":
        opportunitySet(WarmNaarKoudTopSport, WarmNaarKoudBottomSport, personName, currentTemp, weersSituatie)

    elif keuzegelegenheid == "feestje":
        opportunitySet(WarmNaarKoudTopFeestje, WarmNaarKoudBottomFeestje, personName, currentTemp, weersSituatie)

    else:
        print('De gekozen gelgenheid is niet in gebruik!')
        pickClothes(personName, currentTemp, weersSituatie)

    print(personName)
    print(currentTemp)
    print(weersSituatie)

def opportunitySet(WarmNaarKoudTop, WarmNaarKoudBottom, personName, currentTemp, weersSituatie):

    # mogelijkeLangOfKort = ["lang", "kort"]
    # LangOfKortTop = random.choice(mogelijkeLangOfKort)
    # LangOfKortBottom = random.choice(mogelijkeLangOfKort)
    #
    # mogelijkeIndexTop = random.choice(WarmNaarKoudTop)
    # mogelijkeIndexBottom = random.choice(WarmNaarKoudBottom)

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

    mogelijkeTops = searchTop(LangOfKortTop, tresholdTop, WarmNaarKoudTop, personName)
    topje = random.choice(mogelijkeTops)
    print(topje)
    if topje[len(topje) - 1] != "jurkje":
        mogelijkeBottoms = searchBottom(LangOfKortBottom, tresholdBottom, WarmNaarKoudBottom, personName, topje[1])
        bottom = random.choice(mogelijkeBottoms)
        print(bottom)




def searchTop(LangOfKortTop, tresholdTop, WarmNaarKoudTop, personName):
    with open('Kledingkast.json', 'r') as allKleding:
        dataSearch = json.load(allKleding)

    possibleTop = []
    for x in range(2, len(dataSearch[personName])):
        if dataSearch[personName][x]["categorie"] in WarmNaarKoudTop[tresholdTop] and dataSearch[personName][x]["langKort"] == LangOfKortTop:
            tempList = [dataSearch[personName][x]["naam"], dataSearch[personName][x]["kleur"], dataSearch[personName][x]["categorie"]]
            possibleTop.append(tempList)
    return possibleTop



def searchBottom(LangOfKortBottom, tresholdBottom, WarmNaarKoudBottom, personName, kleurTopje):
    with open('Kledingkast.json', 'r') as allKleding:
        dataSearch = json.load(allKleding)

    possibleBottom = []
    for x in range(2, len(dataSearch[personName])):
        if dataSearch[personName][x]["categorie"] in WarmNaarKoudBottom[tresholdBottom] and dataSearch[personName][x]["langKort"] == LangOfKortBottom and dataSearch[personName][x]["langKort"] != kleurTopje:
            tempList = [dataSearch[personName][x]["naam"], dataSearch[personName][x]["kleur"], dataSearch[personName][x]["categorie"]]
            possibleBottom.append(tempList)

    if len(possibleBottom) == 0:
        for x in range(2, len(dataSearch[personName])):
            if dataSearch[personName][x]["categorie"] in WarmNaarKoudBottom[tresholdBottom] and \
                    dataSearch[personName][x]["langKort"] == LangOfKortBottom:
                tempList = [dataSearch[personName][x]["naam"], dataSearch[personName][x]["kleur"],
                            dataSearch[personName][x]["categorie"]]
                possibleBottom.append(tempList)
    return possibleBottom
