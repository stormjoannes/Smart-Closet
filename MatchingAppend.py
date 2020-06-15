import json
import random
from datetime import datetime


def pickClothes(naamUser, currentTemp, weersSituatie, keuzeGelegenheid):
    # scheelt het 1 maand doe je, de dag - maanden dat het scheelt n . Nieuwe data min die waarde heb je hoeveel dagen het scheelt met een variatie van 1 dag per bij de helft van de maanden

    WarmNaarKoudTopDagelijks = {1: ["trui", "vest", "sweater"], 2: ["shirt"], 3: ["topje", "naveltrui", "shirt"]}
    WarmNaarKoudBottomDagelijks = {1: ["jeans", "joggingsbroek"], 2: ["chino", "jeans met gaten", "jeans"],
                                   3: ["rokje", "broekje"]}

    WarmNaarKoudTopSport = {1: ["trui"], 2: ["shirt"], 3: ["sport bh"]}
    WarmNaarKoudBottomSport = {1: ["joggingbroek"], 2: ["leggings"],
                               3: ["sport broekje"]}

    WarmNaarKoudTopFeestje = {1: ["sweater"], 2: ["shirt"], 3: ["shirt", "jurkje"]}
    WarmNaarKoudBottomFeestje = {1: ["jeans"], 2: ["chino", "jeans met gaten"],
                                 3: ["rokje", "broekje"]}

    # keuzeGelegenheid = input('Wil je iets voor het sporten, dagelijks leven of een feestje: ').lower()

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
    # if len(mogelijkeTops) != 0:
    #     top = random.choice(mogelijkeTops)
    # else:
    #     top = None
    #
    # if top[2] != "jurkje":
    mogelijkeBottoms = searchTopBottom(LangOfKortBottom, tresholdBottomIndex, WarmNaarKoudBottom, naamUser, gelegenheid)
    #     if len(mogelijkeBottoms) != 0:
    #         bottom = random.choice(mogelijkeBottoms)
    #     else:
    #         bottom = None

    return mogelijkeTops, mogelijkeBottoms

    #
    # aangetrokken = False
    # indexEndlessLoop = 0
    #
    # while aangetrokken == False:
    #     indexEndlessLoop += 1
    #
    #     with open('Kledingkast.json', 'r+') as inf:
    #         data = json.load(inf)
    #
    #     top = random.choice(mogelijkeTops)
    #
    #     if top[2] != "jurkje":
    #         bottom = random.choice(mogelijkeBottoms)
    #         while bottom[1] == top[1] and len(bottom) > 1:
    #             bottom = random.choice(mogelijkeBottoms)
    #     else:
    #         bottom == None
    #
    #     status = 'positive'
    #
    #     for index in data[naamUser][1]["gedragen"]:
    #         if top in index and bottom in index:
    #             status = 'negative'
    #             if len(mogelijkeTops) <= 1 and len(mogelijkeBottoms) <= 1:
    #                 print("Helaas hebben we met deze beperkte kleding hoeveelheid geen setje kunnen vinden om aan te trekken.")
    #                 status = 'execute'
    #
    #     if status != 'negative':
    #         if len(mogelijkeBottoms) > 1 and len(mogelijkeTops) > 1 and status != 'execute':
    #             print(top)
    #             print(bottom)
    #             aantrekken = input("ga je dit setje aantrekken ja of nee: ").lower()
    #             if aantrekken == "ja":
    #                 aangetrokken = True
    #
    #                 with open('Kledingkast.json', 'w') as ALL:
    #                     today = datetime.today().strftime("%Y-%m-%d")
    #
    #                     formatVoorAppend = [top, bottom, str(today)]
    #                     data[naamUser][1]["gedragen"].append(formatVoorAppend)
    #
    #                     print(formatVoorAppend)
    #                     json.dump(data, ALL)
    #                     ALL.close()
    #
    #             else:
    #                 print('we zoeken een nieuw setje voor je!')
    #                 mogelijkeTops.remove(top)
    #                 mogelijkeBottoms.remove(bottom)
    #
    #     if len(mogelijkeBottoms) < 1 and len(mogelijkeTops) < 1 and status == 'execute' or indexEndlessLoop > 9999:
    #         print(
    #             "Helaas hebben we met deze beperkte kleding hoeveelheid geen setje kunnen vinden om aan te trekken.")
    #         aangetrokken = True


def searchTopBottom(LangOfKortTopBottom, tresholdTopBottomIndex, WarmNaarKoudTopBottom, naamUser, gelegenheid):
    with open('Kledingkast.json', 'r') as allKleding:
        dataSearch = json.load(allKleding)

    possibleTopBottom = []
    tresholdTopBottomIndex -= 1

    while len(possibleTopBottom) == 0 and tresholdTopBottomIndex < 3:
        tresholdTopBottomIndex += 1
        # print(WarmNaarKoudTopBottom[tresholdTopBottomIndex], LangOfKortTopBottom, gelegenheid, "!!!!!!!!!")
        for x in range(2, len(dataSearch[naamUser])):
            # print(dataSearch[naamUser][x]["categorie"], dataSearch[naamUser][x]["langKort"], dataSearch[naamUser][x]["gelegenheid"], '?????????????????????')
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
