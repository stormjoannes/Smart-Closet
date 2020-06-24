import json
from Code.WeerAPI import *
from tkinter.messagebox import showinfo
from datetime import datetime
import random
from sys import exit
from tkinter import *

def SortedListSets(unsortedList, hitteNiveau, kortOfLangInf):
    allValues = []
    sortedList = []
    for x in unsortedList:
        kortLangSamenstelling = x[0][4] + "-" + x[1][4]
        kansKortLang = kortOfLangInf["temp"][hitteNiveau][kortLangSamenstelling]["yes"]
        kansKortLang = kansKortLang.split("/")
        kansKortLang = int(kansKortLang[0]) / int(kansKortLang[1])

        kansValueTop = kortOfLangInf["tops"][hitteNiveau][x[0][2]]["yes"]
        kansValueTop = kansValueTop.split("/")
        kansValueTop = int(kansValueTop[0]) / int(kansValueTop[1])

        # bottom = "".join(x[1][2])
        kansValueBottom = kortOfLangInf["bottoms"][hitteNiveau][x[1][2]]["yes"]
        kansValueBottom = kansValueBottom.split("/")
        kansValueBottom = int(kansValueBottom[0]) / int(kansValueBottom[1])

        kansSetje = kansKortLang * kansValueTop * kansValueBottom
        allValues.append(kansSetje)

    while len(allValues) != 0:
        for valueIndex in range(0, len(allValues)):
            MinValue = min(allValues)
            if allValues[valueIndex] == MinValue:
                # print("ja")
                # print(unsortedList)
                # print(allValues)
                sortedList.append(unsortedList[valueIndex])
                allValues.remove(allValues[valueIndex])
                unsortedList.remove(unsortedList[valueIndex])
                break
    return sortedList


def WeatherForPickClothes(func, userName, setGenScreen, rootGen):
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

    keuzeLangKort = random.choice(randomChoiceLijst)
    # print(keuzeLangKort)
    LengteMouwen = keuzeLangKort.split("-")[0]
    LengtePijpen = keuzeLangKort.split("-")[1]
    soortenTop = ["shirt", "hoodie", "hemdje", "trui", "vest", "crop top", "blazer", "jurk", "jumpsuit", "blousje"]
    soortenBottom = ["jeans", "legging", "chino", "joggingbroek", "jeans met gaten", "rokje", "high waste", "stoffen broek"]
    Tops = ChoiceTopBottom(userName, LengteMouwen, soortenTop, opportunity)
    Bottoms = ChoiceTopBottom(userName, LengtePijpen, soortenBottom, opportunity)
    if len(Tops) == 0 or len(Bottoms) == 0:
        errorMessage(setGenScreen, rootGen)
        exit(0)

    # print(Tops, "first")
    # print(Bottoms, "first")
    funcTops = getCommonClothingPieces(kortOfLangInf, hitteNiveau, Tops, "tops")
    Tops = funcTops[0]
    voorkomendeCategorieTop = funcTops[1]
    wearableTopBottomListTop = funcTops[2]
    funcBottoms = getCommonClothingPieces(kortOfLangInf, hitteNiveau, Bottoms, "bottoms")
    Bottoms = funcBottoms[0]
    voorkomendeCategorieBottom = funcBottoms[1]
    wearableTopBottomListBottom = funcBottoms[2]

    if len(Tops) == 0 or len(Bottoms) == 0:
        errorMessage(setGenScreen, rootGen)
        exit(0)
    # print(Tops, "second")
    # print(Bottoms, "second")
    unsortedSets = CollorChoice(userName, Tops, Bottoms, voorkomendeCategorieTop, wearableTopBottomListTop, voorkomendeCategorieBottom, wearableTopBottomListBottom, setGenScreen, rootGen)
    return SortedListSets(unsortedSets, hitteNiveau, kortOfLangInf)


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


def getCommonClothingPieces(kortOfLangInf, hitteNiveau, TopsBottoms, TopOrBottom):
    FiguratieLangKort = kortOfLangInf[TopOrBottom][hitteNiveau]
    # print(hitteNiveau)
    # print(TopsBottoms, 'list')

    wearableTopBottomList = []
    voorkomendeCategorie = []
    for x in FiguratieLangKort:
        kans = FiguratieLangKort[x]["yes"]
        kans = kans.split("/")[0]
        for i in range(0, int(kans)):
            wearableTopBottomList.append(x)
    # print(wearableTopBottomList)
    # print(TopsBottoms[0][2], "juahhhhhhhhhh")
    for kledingstuk in TopsBottoms:
        if kledingstuk[2] not in wearableTopBottomList:
            TopsBottoms.remove(kledingstuk)
        else:
            voorkomendeCategorie.append(kledingstuk[2])
    # keuzeLangKort = random.choice(wearableTopBottomList)
    # print(wearableTopBottomList, "filters")
    return TopsBottoms, voorkomendeCategorie, wearableTopBottomList

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


def errorMessage(setGenscreen, rootGen):
    bericht = "Helaas hebben we met deze beperkte kleding hoeveelheid geen setje kunnen vinden om aan te trekken."
    showinfo(title='Clothing error', message=bericht)
    rootGen.destroy()
    setGenscreen()


def CollorChoice(userName, Tops, Bottoms, voorkomendeCategorieTop, wearableTopBottomListTop, voorkomendeCategorieBottom, wearableTopBottomListBottom, setGenscreen, rootGen):
    if len(Tops) == 0 or len(Bottoms) == 0:
        errorMessage(setGenscreen, rootGen)
        exit(0)

    mogelijkSetjes = []

    while len(Tops) != 0 and len(Bottoms) != 0:
        randTopCat = None
        randBottomCat = None
        while randTopCat not in voorkomendeCategorieTop:
            randTopCat = random.choice(wearableTopBottomListTop)

        while randBottomCat not in voorkomendeCategorieBottom:
            randBottomCat = random.choice(wearableTopBottomListBottom)

        wearableTopBottomListTop.remove(randTopCat)
        wearableTopBottomListBottom.remove(randBottomCat)
        for shirt in Tops:
            # print(shirt, "shirt")
            if shirt[2] == randTopCat:
                Tops.remove(shirt)
                for bottom in Bottoms:
                    if bottom[2] == randBottomCat:
                        # print(bottom, "bottom")
                        Bottoms.remove(bottom)
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
                            # print(tempList)

                            statusGedragen = checkGedragen(userName, tempList)
                            if statusGedragen == False:
                                mogelijkSetjes.append(tempList)
    # print("\n")
    # for y in mogelijkSetjes:
    #     print(y)
    return mogelijkSetjes


def frame(func, userName, setGenScreen, showMenu, rootGen):
    global SetsList
    loopIndex = -1
    SetsList = WeatherForPickClothes(func, userName, setGenScreen, rootGen)
    if len(SetsList) == 0:
        errorMessage(setGenScreen, rootGen)

    clothingloop(func, userName, loopIndex, setGenScreen, showMenu, rootGen)


def clothingloop(func, userName, loopIndex, setGenScreen, showMenu, rootGen):
    loopIndex += 1
    sideScreen(SetsList[loopIndex][0], SetsList[loopIndex][1], func, loopIndex, setGenScreen, showMenu, userName, rootGen)


def sideScreen(top, bottom, func, loopindex, setGenScreen, showMenu, userName, rootGen):
    if loopindex == 0:
        rootGen.destroy()
    global rootWear
    global Globroot

    rootWear = Tk()
    rootWear.title("Wear clothes")
    Globroot = rootWear

    showMenu(rootWear)

    GenTopLabel = Label(rootWear, text=f'Top: {top}', background="gray")
    GenTopLabel.grid(row=5)

    GenBottomLabel = Label(rootWear, text=f'Bottom: {bottom}', background="gray")
    GenBottomLabel.grid(row=6)

    genTitleLabel = Label(rootWear, text='Ga je dit setje dragen:', background="gray")
    genTitleLabel.grid(row=9)

    genYesButton = Button(rootWear, text='Ja',
                          command=lambda: autoGen("ja", top, bottom, userName, loopindex, func, setGenScreen, showMenu, rootGen))
    genYesButton.grid(row=11, sticky=W)

    genNoButton = Button(rootWear, text='Nee',
                         command=lambda: autoGen("nee", top, bottom, userName, loopindex, func, setGenScreen, showMenu, rootGen))
    genNoButton.grid(row=11, sticky=E)

    genBackButton = Button(rootWear, text='Back', command=lambda: backButton(setGenScreen, rootWear))
    genBackButton.grid(row=12)

    rootWear.mainloop()


def autoGen(aantrekken, top, bottom, userName, loopIndex, func, setGenScreen, showMenu, rootGen):
    "'Hier zorg ik er voor dat als iemand besluit het voorgelegde kleding setje aan te doen dat dat word geregistreerd in het json bestand.'"
    if aantrekken == "ja":
        rootWear.destroy()
        with open('../jsonFiles/Kledingkast.json', 'r') as alldata:
            allinformatie = json.load(alldata)
        with open('../jsonFiles/Kledingkast.json', 'w') as ALL:
            today = datetime.today().strftime("%Y-%m-%d")
            formatVoorAppend = [top, bottom, str(today)]
            allinformatie[userName][1]["gedragen"].append(formatVoorAppend)
            json.dump(allinformatie, ALL)
            ALL.close()
            backtoGenScreen(setGenScreen, rootGen)

    else:
        if loopIndex + 1 == len(SetsList):
            bericht = "Helaas hebben we geen setjes meer om te laten zien."
            showinfo(title='Clothing error', message=bericht)
            backButton(setGenScreen, rootWear)
        else:
            rootWear.destroy()
            clothingloop(func, userName, loopIndex, setGenScreen, showMenu, rootGen)

def backtoGenScreen(setGenScreen, rootGen):
    setGenScreen()

def backButton(setGenScreen, rootWear):
    rootWear.destroy()
    setGenScreen()

def getTimeDifference(x):
    "'In deze functie zoek ik naar het verschil in tijd tussen de meegegeven datum en de datum van nu(tijd in dagen).'"
    date_format = "%Y-%m-%d"
    today = datetime.today()

    previousDay = datetime.strptime(x[2], date_format)

    diff = abs((today - previousDay).days)
    return diff

# print(WeatherForPickClothes("dagelijks", "admin"))
# print(getCommonClothingPieces())