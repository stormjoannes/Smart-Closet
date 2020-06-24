import json
from Code.WeerAPI import *
from tkinter.messagebox import showinfo
import random

def WeatherForPickClothes(func, userName):
    "'Hier kijk ik welke gelegenheid de persoon heeft uitgekozen en wat de de gevoelstemperatuur is door middel van een berekening van de windsnelheid en de temperatuur.'"
    global loopIndex
    if func == 'dagelijks':
        opportunity = 'dagelijks leven'
    elif func == 'sport':
        opportunity = 'sport'
    elif func == 'feest':
        opportunity = 'feestje'

    with open('../jsonFiles/Kledingkast.json', 'r+') as Data:
        placeInfo = json.load(Data)

    stad = placeInfo[userName][0]["gegevens"][0]["locatie"]["stad"]
    land = placeInfo[userName][0]["gegevens"][0]["locatie"]["land"]
    huidigeWeer = setValuesWeer(stad, land)
    gevoelsTemp = huidigeWeer[0]
    windSnelheid = huidigeWeer[2]
    if windSnelheid >= 5:
        gevoelsTemp = 13.12 + 0.6215 * gevoelsTemp - 11.37 * windSnelheid ** 0.16 + 0.3965 * gevoelsTemp * windSnelheid ** 0.16

    if gevoelsTemp < 12:
        hitteNiveau = "cold"
    elif gevoelsTemp >= 12 and gevoelsTemp < 23:
        hitteNiveau = "mild"
    else:
        hitteNiveau = "hot"

    with open('../jsonFiles/Datastructuur.json', 'r') as HeatlevelInf:
        kortOfLangInf = json.load(HeatlevelInf)

    FiguratieLangKort = kortOfLangInf["temp"][hitteNiveau]
    # print(hitteNiveau)

    randomChoiceLijst = []
    for x in FiguratieLangKort:
        kans = FiguratieLangKort[x]["yes"]
        kans = kans.split("/")[0]
        for i in range(0, int(kans)):
            randomChoiceLijst.append(x)
    # print(randomChoiceLijst)
    keuzeLangKort = random.choice(randomChoiceLijst)
    # print(FiguratieLangKort)
    # print(keuzeLangKort)
    LengteMouwen = keuzeLangKort.split("-")[0]
    LengtePijpen = keuzeLangKort.split("-")[1]
    soortenTop = ["shirt", "hoodie", "hemdje", "trui", "vest", "crop top", "blazer", "jurk", "jumpsuit", "blousje"]
    soortenBottom = ["jeans", "legging", "chino", "joggingbroek", "jeans met gaten", "rokje", "high waste", "stoffen broek"]
    # print(LengteMouwen, "!!!!!!!!!!!!!!!")
    # print(LengtePijpen, "!!!!!!!!!!!!!!!")
    Tops = ChoiceTopBottom(userName, LengteMouwen, soortenTop, opportunity)
    Bottoms = ChoiceTopBottom(userName, LengtePijpen, soortenBottom, opportunity)
    # print(Tops)
    # print(Bottoms)
    CollorChoice(userName, Tops, Bottoms)

def ChoiceTopBottom(userName, langKort, TopOfBroek, gelegenheid):
    mogelijkeTopBottom = []
    with open('../jsonFiles/Kledingkast.json', 'r+') as Data:
        clothesData = json.load(Data)

    for x in range(2, len(clothesData[userName])):
        # print(clothesData[userName][x], "stuk")
        # print(TopOfBroek, "lijstttttt")
        # print(clothesData[userName][x]["langKort"], "database")
        # print(langKort, "langkort")
        # print('\n')
        if clothesData[userName][x]["langKort"] == langKort and clothesData[userName][x]["categorie"] in TopOfBroek and clothesData[userName][x]["gelegenheid"] == gelegenheid:
            tempList = [clothesData[userName][x]["naam"], clothesData[userName][x]["kleur"],
                        clothesData[userName][x]["categorie"], clothesData[userName][x]["merk"],
                        clothesData[userName][x]["langKort"]]
            mogelijkeTopBottom.append(tempList)
    return mogelijkeTopBottom

def CollorChoice(userName, Tops, Bottoms):
    if len(Tops) == 0 or len(Bottoms) == 0:
        errorMessage()
    mogelijkSetjes = []
    for shirt in Tops:
        for bottom in Bottoms:
            collorTop = shirt[1]
            collorBottom = bottom[1]
            with open('../jsonFiles/Datastructuur.json', 'r') as ColorCombInf:
                collorCombinationsInfo = json.load(ColorCombInf)

            try:
                collorStatus = getCollorStatus(collorCombinationsInfo, collorTop, collorBottom)
            except:
                if "-" in collorTop and "-" in collorBottom:
                    collorTop = collorTop.split("-")
                    collorBottom = collorBottom.split("-")

                    splitStatusTop = []
                    splitStatusTop.append(getCollorStatus(collorCombinationsInfo, collorTop[0], collorBottom[0]))
                    splitStatusTop.append(getCollorStatus(collorCombinationsInfo, collorTop[0], collorBottom[1]))
                    splitStatusTop.append(getCollorStatus(collorCombinationsInfo, collorTop[1], collorBottom[0]))
                    splitStatusTop.append(getCollorStatus(collorCombinationsInfo, collorTop[1], collorBottom[1]))
                    collorStatus = random.choice(splitStatusTop)

                elif "-" in collorTop:
                    collorTop = collorTop.split("-")
                    splitStatusTop = []
                    splitStatusTop.append(getCollorStatus(collorCombinationsInfo, collorTop[0], collorBottom))
                    splitStatusTop.append(getCollorStatus(collorCombinationsInfo, collorTop[0], collorBottom))
                    collorStatus = random.choice(splitStatusTop)

                elif "-" in collorBottom:
                    collorBottom = collorBottom.split("-")
                    splitStatusBottom = []
                    splitStatusBottom.append(getCollorStatus(collorCombinationsInfo, collorTop, collorBottom[0]))
                    splitStatusBottom.append(getCollorStatus(collorCombinationsInfo, collorTop, collorBottom[1]))
                    collorStatus = random.choice(splitStatusBottom)

            if collorStatus == "ja":
                tempList = []
                if shirt[2] == "jumpsuit" or shirt[2] == "jurk":
                    tempList.append(shirt)
                else:
                    tempList.append(shirt)
                    tempList.append(bottom)

                statusGedragen = checkGedragen(userName, tempList)
                if statusGedragen == False:
                    mogelijkSetjes.append(tempList)
    if len(mogelijkSetjes) == 0:
        errorMessage()
    for y in mogelijkSetjes:
        print(y)

def getCollorStatus(collorCombinationsInfo, collorTop, collorBottom):
    try:
        collorStatus = collorCombinationsInfo["collor"][collorTop][collorBottom]
    except:
        collorStatus = collorCombinationsInfo["collor"][collorBottom][collorTop]

    return collorStatus

def checkGedragen(userName, setje):
    with open('../jsonFiles/Kledingkast.json', 'r') as Wear:
        WearInf = json.load(Wear)

    for x in WearInf[userName][1]["gedragen"]:
        tempComparrisenList = []
        tempComparrisenList.append(x[0])
        tempComparrisenList.append(x[1])
        if tempComparrisenList == setje:
            return True
    return False


def errorMessage():
    bericht = "Helaas hebben we met deze beperkte kleding hoeveelheid geen setje kunnen vinden om aan te trekken."
    showinfo(title='Clothing error', message=bericht)

WeatherForPickClothes("dagelijks", "admin")