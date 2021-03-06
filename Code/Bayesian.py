import json
from Code.WeerAPI import *
from tkinter.messagebox import showinfo
from datetime import datetime
import random
from sys import exit
from tkinter import *

def SortedListSets(unsortedList, hitteNiveau, kortOfLangInf):
    """
    Dit is het laatste stadium waar de mogelijke setjes in de lijst word aangepast.
    Hier worden namelijk de setjes van best naar slecht nog eens gesorteerd door middel van een formule.
    """

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
            MaxValue = max(allValues)
            if allValues[valueIndex] == MaxValue:
                sortedList.append(unsortedList[valueIndex])
                allValues.remove(allValues[valueIndex])
                unsortedList.remove(unsortedList[valueIndex])
                break
    return sortedList


def WeatherForPickClothes(opportunity, userName):
    """
    Hier kijk ik welke gelegenheid de persoon heeft uitgekozen en wat de de gevoelstemperatuur
    is door middel van een berekening van de windsnelheid en de temperatuur. Ook bepaal ik hier door middel van een
    kansberekening wat de configuratie wordt van lange of korte mouwen en lange of korte broekpijpen.
    """

    global loopIndex

    with open('../jsonFiles/Kledingkast.json', 'r+') as Data:
        placeInfo = json.load(Data)

    # Hier ga ik door middel van een formule de gevoelstemperatuur berekenen en op basis daarvan kijk ik in welke range de gevoelstemperatuur valt.
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

    # Hier kies ik door middel van een kansberekening wat de configuratie van de lengte van de mouwen en broeks pijpen word.
    randomChoiceLijst = []
    for x in FiguratieLangKort:
        kans = FiguratieLangKort[x]["yes"]
        kans = kans.split("/")[0]
        for i in range(0, int(kans)):
            randomChoiceLijst.append(x)
    keuzeLangKort = random.choice(randomChoiceLijst)
    LengteMouwen = keuzeLangKort.split("-")[0]
    LengtePijpen = keuzeLangKort.split("-")[1]

    # Hier zet ik alle soorten categorieën die kunnen voorkomen.
    soortenTop = ["shirt", "hoodie", "hemdje", "trui", "vest", "crop top", "blazer", "jurk", "jumpsuit", "blousje"]
    soortenBottom = ["jeans", "legging", "chino", "joggingbroek", "jeans met gaten", "rokje", "high waste", "stoffen broek"]

    # Hier kijk ik of er uberhaupt genoeg tops of bottoms in de digitale kledingkast staan om een setje uit te kiezen.
    Tops = ChoiceTopBottom(userName, LengteMouwen, soortenTop, opportunity)
    Bottoms = ChoiceTopBottom(userName, LengtePijpen, soortenBottom, opportunity)
    if len(Tops) == 0 or len(Bottoms) == 0:
        errorMessage()
        exit(0)

    # Hier roep ik alle functies aan met de waardes die ik onder andere weer van functies krijg.
    funcTops = getCommonClothingPieces(kortOfLangInf, hitteNiveau, Tops, "tops")
    Tops = funcTops[0]
    voorkomendeCategorieTop = funcTops[1]
    wearableTopBottomListTop = funcTops[2]
    funcBottoms = getCommonClothingPieces(kortOfLangInf, hitteNiveau, Bottoms, "bottoms")
    Bottoms = funcBottoms[0]
    voorkomendeCategorieBottom = funcBottoms[1]
    wearableTopBottomListBottom = funcBottoms[2]

    if len(Tops) == 0 or len(Bottoms) == 0:
        errorMessage()
        exit(0)
    unsortedSets = CollorChoice(userName, Tops, Bottoms, voorkomendeCategorieTop, wearableTopBottomListTop, voorkomendeCategorieBottom, wearableTopBottomListBottom)
    return SortedListSets(unsortedSets, hitteNiveau, kortOfLangInf)


def ChoiceTopBottom(userName, langKort, TopOfBroek, gelegenheid, path='../jsonFiles/Kledingkast.json'):
    """
    In deze functie kies ik als eerst de mogelijke setjes uit door middel van of bijvoorbeeld het shirt
    lange of korte mouwen heeft, bij een broek geld dit voor de broeks pijpen.
    """
    mogelijkeTopBottom = []
    with open(path, 'r+') as Data:
        clothesData = json.load(Data)

    # De kledingstukken die kloppen met de gegevens treshholds worden gereturned als mogelijkeTops of Bottoms.
    for x in range(2, len(clothesData[userName])):
        if clothesData[userName][x]["langKort"] == langKort and clothesData[userName][x]["categorie"] in TopOfBroek and \
                                                                clothesData[userName][x]["gelegenheid"] == gelegenheid:
            tempList = [clothesData[userName][x]["naam"], clothesData[userName][x]["kleur"],
                        clothesData[userName][x]["categorie"], clothesData[userName][x]["merk"],
                        clothesData[userName][x]["langKort"]]
            mogelijkeTopBottom.append(tempList)
    return mogelijkeTopBottom


def getCommonClothingPieces(kortOfLangInf, hitteNiveau, TopsBottoms, TopOrBottom):
    """
    Hier houd ik alleen de kledingstukken over die bij die temperatuur ook gedragen worden.
    """

    FiguratieLangKort = kortOfLangInf[TopOrBottom][hitteNiveau]

    # Hier kijk ik wat de kans is dat een kleding categorie bij een temperatuur gedragen word.
    wearableTopBottomList = []
    voorkomendeCategorie = []
    for x in FiguratieLangKort:
        kans = FiguratieLangKort[x]["yes"]
        kans = kans.split("/")[0]
        for i in range(0, int(kans)):
            wearableTopBottomList.append(x)

    # Hier verwijder ik een kledingstuk dat geen kans heeft om gedragen te worden.
    for kledingstuk in TopsBottoms:
        if kledingstuk[2] not in wearableTopBottomList:
            TopsBottoms.remove(kledingstuk)
        else:
            voorkomendeCategorie.append(kledingstuk[2])
    return TopsBottoms, voorkomendeCategorie, wearableTopBottomList

def getCollorStatus(collorCombinationsInfo, collorTop, collorBottom):
    """
    Hier worden de kleurensetjes geprobeerd of ze kunnen of niet. Dit is een try except
    omdat ik niet elke kleur dubbel heb staan in de datastructuur omdat dat overbodig was.
    """

    try:
        collorStatus = collorCombinationsInfo["collor"][collorTop][collorBottom]
    except:
        collorStatus = collorCombinationsInfo["collor"][collorBottom][collorTop]

    return collorStatus

def checkGedragen(userName, setje, path = '../jsonFiles/Kledingkast.json'):
    """
    Hier word er gekeken of het automatisch uitgekozen setje al eens in gedragen in de periode dat je
    setje niet achter elkaar mag dragen(deze word gekozen door de gebruiker).
    """

    with open(path, 'r') as Wear:
        WearInf = json.load(Wear)

    for x in WearInf[userName][1]["gedragen"]:
        # In deze list formatteer ik het gedragen setje vanuit de database om hem te vergelijken.
        tempComparrisenList = []
        tempComparrisenList.append(x[0])
        tempComparrisenList.append(x[1])
        if tempComparrisenList == setje:
            return True
    return False


def errorMessage():
    """
    Hier word alleen de pop-up errormessage aangemaakt en het categorie keuzescherm gerefreshed.
    """

    bericht = "Helaas hebben we met deze beperkte kleding hoeveelheid geen setje kunnen vinden om aan te trekken."
    showinfo(title='Clothing error', message=bericht)
    rootGen.destroy()
    setGenScreen()


def CollorChoice(userName, Tops, Bottoms, voorkomendeCategorieTop, wearableTopBottomListTop, voorkomendeCategorieBottom, wearableTopBottomListBottom):
    """
    Hier word de kleurenkeuze gecontroleerd en worden de kledingstukken op basis van kans een beetje gesorteerd van goed setje naar een minder goed setje.
    """

    if len(Tops) == 0 or len(Bottoms) == 0:
        errorMessage()
        exit(0)

    mogelijkSetjes = []

    while len(Tops) != 0 and len(Bottoms) != 0:
        randTopCat = None
        randBottomCat = None
        # Hier kies ik een random categorie die mogelijk zijn bij het weer
        while randTopCat not in voorkomendeCategorieTop:
            randTopCat = random.choice(wearableTopBottomListTop)

        while randBottomCat not in voorkomendeCategorieBottom:
            randBottomCat = random.choice(wearableTopBottomListBottom)

        wearableTopBottomListTop.remove(randTopCat)
        wearableTopBottomListBottom.remove(randBottomCat)
        for shirt in Tops:
            # shirt[2] is de categorie van het schirt
            if shirt[2] == randTopCat:
                Tops.remove(shirt)
                for bottom in Bottoms:
                    if bottom[2] == randBottomCat:
                        Bottoms.remove(bottom)
                        collorTop = shirt[1]
                        collorBottom = bottom[1]
                        with open('../jsonFiles/Datastructuur.json', 'r') as ColorCombInf:
                            collorCombinationsInfo = json.load(ColorCombInf)
                        try:
                            collorStatus = getCollorStatus(collorCombinationsInfo, collorTop, collorBottom)
                        except:
                            # Kledingstukken die 2 kleuren hebben worden met de goede kansen alsnog verwerkt.
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

                        # Als de kleurencombinatie mogelijk is word het setje doorgelaten.
                        if collorStatus == "ja":
                            tempList = []
                            # Zolang het geen jumpsuit of jurk is word ook de bottom meegerekend in het setje.
                            if shirt[2] == "jumpsuit" or shirt[2] == "jurk":
                                tempList.append(shirt)
                            else:
                                tempList.append(shirt)
                                tempList.append(bottom)

                            statusGedragen = checkGedragen(userName, tempList)
                            if statusGedragen == False:
                                mogelijkSetjes.append(tempList)

    return mogelijkSetjes


def frame(func, userName, setGenScreenfor, showMenu, rootGenfor):
    """
    Dit is het beginframe dat word aangeroepen vanuit de interface, vanuit hier komt de berekening
    terug om vervolgens het proces van setjes laten zien te beginnen.
    """

    global setGenScreen
    global rootGen
    global SetsList

    setGenScreen = setGenScreenfor
    rootGen = rootGenfor
    loopIndex = -1
    SetsList = WeatherForPickClothes(func, userName)
    # Setslist is de helemaal gesorteerde list van mogelijke kledingstukken van best naar worst.
    if len(SetsList) == 0:
        errorMessage()

    clothingloop(func, userName, loopIndex, showMenu)


def clothingloop(func, userName, loopIndex, showMenu):
    """
    Deze functie word steeds aangeroepen zodra een gebruiker nee zegt op het voorgelegde kledingsetje.
    """

    loopIndex += 1
    sideScreen(SetsList[loopIndex][0], SetsList[loopIndex][1], func, loopIndex, showMenu, userName)


def sideScreen(top, bottom, func, loopindex, showMenu, userName):
    """
    Hier word het keuze scherm aangemaakt om je voorgelegde kledingsetje te laten zien.
    """

    if loopindex == 0:
        rootGen.destroy()
    global rootWear
    global Globroot

    rootWear = Tk()
    rootWear.title("Wear clothes")
    Globroot = rootWear

    showMenu(rootWear)

    # Hier formatteer ik een goed leesbare zin van het kledingstuk.
    leesbareTop = f"Een {top[1]} {top[2]} met {top[4]}e mouwen van het merk: {top[3]}"
    leesbareBottom = f"een{bottom[1]} {bottom[2]} met {bottom[4]} broeks pijpen van het merk: {bottom[3]}"

    GenTopLabel = Label(rootWear, text=f'{leesbareTop}', background="#c6def1")
    GenTopLabel.grid(row=5)

    GenBottomLabel = Label(rootWear, text=f'en {leesbareBottom}.', background="#c6def1")
    GenBottomLabel.grid(row=6)

    genTitleLabel = Label(rootWear, text='Ga je dit setje dragen:', background="#c6def1")
    genTitleLabel.grid(row=9)

    genYesButton = Button(rootWear, text='Ja',
                          command=lambda: autoGen("ja", top, bottom, userName, loopindex, func, showMenu))
    genYesButton.grid(row=11, sticky=W)

    genNoButton = Button(rootWear, text='Nee',
                         command=lambda: autoGen("nee", top, bottom, userName, loopindex, func, showMenu))
    genNoButton.grid(row=11, sticky=E)

    genBackButton = Button(rootWear, text='Back', command=lambda: backButton())
    genBackButton.grid(row=12)

    rootWear.mainloop()


def autoGen(aantrekken, top, bottom, userName, loopIndex, func, showMenu):
    """
    Hier zorg ik er voor dat als iemand besluit het voorgelegde kleding setje aan te
    doen dat dat word geregistreerd in het json bestand.
    """

    if aantrekken == "ja":
        rootWear.destroy()
        with open('../jsonFiles/Kledingkast.json', 'r') as alldata:
            allinformatie = json.load(alldata)
        with open('../jsonFiles/Kledingkast.json', 'w') as ALL:
            # De datum word meegegeven wanner het gedragen is.
            today = datetime.today().strftime("%Y-%m-%d")
            formatVoorAppend = [top, bottom, str(today)]
            allinformatie[userName][1]["gedragen"].append(formatVoorAppend)
            json.dump(allinformatie, ALL)
            ALL.close()
            backtoGenScreen()

    else:
        if loopIndex + 1 == len(SetsList):
            bericht = "Helaas hebben we geen setjes meer om te laten zien."
            showinfo(title='Clothing error', message=bericht)
            backButton()
        else:
            rootWear.destroy()
            clothingloop(func, userName, loopIndex, showMenu)

def backtoGenScreen():
    """
    Deze functie heb ik gebruikt om alleen terug te gaan naar het categorie keuze scherm.
    """

    setGenScreen()

def backButton():
    """
    Deze functie word gebruikt om het keuzescherm af te sluiten en terug te gaan naar het categorie keuze scherm.
    """

    rootWear.destroy()
    setGenScreen()

def getTimeDifference(x, today = datetime.today()):
    """
    In deze functie zoek ik naar het verschil in tijd tussen de meegegeven datum en de datum van nu(tijd in dagen).
    """

    date_format = "%Y-%m-%d"

    previousDay = datetime.strptime(x[2], date_format)

    diff = abs((today - previousDay).days)
    return diff