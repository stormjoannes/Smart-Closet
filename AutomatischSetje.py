import json
from datetime import datetime


def pickClothes(naamUser, currentTemp, weersSituatie, keuzeGelegenheid):
    WarmNaarKoudTopDagelijks = {1: ["trui", "vest", "sweater"], 2: ["shirt"], 3: ["topje", "naveltrui", "shirt"]}
    WarmNaarKoudBottomDagelijks = {1: ["jeans", "joggingsbroek"], 2: ["chino", "jeans met gaten", "jeans"],
                                   3: ["rokje", "broekje"]}

    WarmNaarKoudTopSport = {1: ["trui"], 2: ["shirt"], 3: ["sport bh"]}
    WarmNaarKoudBottomSport = {1: ["joggingbroek"], 2: ["leggings"],
                               3: ["sport broekje"]}

    WarmNaarKoudTopFeestje = {1: ["sweater"], 2: ["shirt"], 3: ["shirt", "jurkje"]}
    WarmNaarKoudBottomFeestje = {1: ["jeans"], 2: ["chino", "jeans met gaten"],
                                 3: ["rokje", "broekje"]}

    if keuzeGelegenheid == "dagelijks leven":
        return opportunitySet(WarmNaarKoudTopDagelijks, WarmNaarKoudBottomDagelijks, naamUser, currentTemp, "dagelijks leven")

    elif keuzeGelegenheid == "sport":
        return opportunitySet(WarmNaarKoudTopSport, WarmNaarKoudBottomSport, naamUser, currentTemp, "sport")

    elif keuzeGelegenheid == "feestje":
        return opportunitySet(WarmNaarKoudTopFeestje, WarmNaarKoudBottomFeestje, naamUser, currentTemp, "feestje")



def opportunitySet(WarmNaarKoudTop, WarmNaarKoudBottom, naamUser, currentTemp, gelegenheid):
    if currentTemp < 15:
        LangOfKortTop = "lang"
        LangOfKortBottom = "lang"

        tresholdTopIndex = 1
        tresholdBottomIndex = 1

    elif currentTemp >= 15 and currentTemp < 20:
        LangOfKortTop = "lang"
        LangOfKortBottom = "lang"

        tresholdTopIndex = len(WarmNaarKoudTop) - 1
        tresholdBottomIndex = len(WarmNaarKoudBottom) - 1

    elif currentTemp >= 20 and currentTemp < 23:
        LangOfKortTop = "kort"
        LangOfKortBottom = "lang"

        tresholdTopIndex = len(WarmNaarKoudTop)
        tresholdBottomIndex = len(WarmNaarKoudBottom) - 1

    elif currentTemp >= 23:
        LangOfKortTop = "kort"
        LangOfKortBottom = "kort"

        tresholdTopIndex = len(WarmNaarKoudTop)
        tresholdBottomIndex = len(WarmNaarKoudBottom)



    mogelijkeTops = searchTopBottom(LangOfKortTop, tresholdTopIndex, WarmNaarKoudTop, naamUser, gelegenheid)
    mogelijkeBottoms = searchTopBottom(LangOfKortBottom, tresholdBottomIndex, WarmNaarKoudBottom, naamUser, gelegenheid)


    return mogelijkeTops, mogelijkeBottoms



def searchTopBottom(LangOfKortTopBottom, tresholdTopBottomIndex, WarmNaarKoudTopBottom, naamUser, gelegenheid):
    with open('Kledingkast.json', 'r') as allKleding:
        dataSearch = json.load(allKleding)

    possibleTopBottom = []
    tresholdTopBottomIndex -= 1

    while len(possibleTopBottom) == 0 and tresholdTopBottomIndex < 3:
        tresholdTopBottomIndex += 1
        for x in range(2, len(dataSearch[naamUser])):
            if dataSearch[naamUser][x]["categorie"] in WarmNaarKoudTopBottom[tresholdTopBottomIndex] and dataSearch[naamUser][x]["langKort"] == LangOfKortTopBottom and dataSearch[naamUser][x]["gelegenheid"] == gelegenheid:
                tempList = [dataSearch[naamUser][x]["naam"], dataSearch[naamUser][x]["kleur"],
                            dataSearch[naamUser][x]["categorie"], dataSearch[naamUser][x]["merk"],
                            dataSearch[naamUser][x]["langKort"]]
                possibleTopBottom.append(tempList)
    return possibleTopBottom

def getTimeDifference(x):
    date_format = "%Y-%m-%d"
    today = datetime.today()

    previousDay = datetime.strptime(x[2], date_format)

    diff = abs((today - previousDay).days)
    return diff
