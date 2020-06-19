import json
from datetime import datetime
from tkinter.messagebox import showinfo
from WeerAPI import *
import random
from tkinter import *

def pickClothes(naamUser, currentTemp, weersSituatie, keuzeGelegenheid):
    "'Hier zet ik de verschillende tresholds van wat warm en wat koud is bij welke gelegenheid.'"
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
    "'Hier zet ik door middel van hoe warm het is de combinatie van bijvoorbelde een kort shirt en een lange broek.'"
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
    "'In deze functie zoek ik naar de top of de bottom door middel van de of het lang of kort moet zijn en van de lijst waarin kledingstukken staan georden van warm naar koud.'"
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
    "'In deze functie zoek ik naar het verschil in tijd tussen de meegegeven datum en de datum van nu(tijd in dagen).'"
    date_format = "%Y-%m-%d"
    today = datetime.today()

    previousDay = datetime.strptime(x[2], date_format)

    diff = abs((today - previousDay).days)
    return diff


def WeatherForPickClothes(func, rootGen, userName, Homescreen, showMenu):
    "'Hier kijk ik welke gelegenheid de persoon heeft uitgekozen en wat de de gevoelstemperatuur is door middel van een berekening van de windsnelheid en de temperatuur.'"
    global loopIndex
    if func == 'dagelijks':
        opportunity = 'dagelijks leven'
    elif func == 'sport':
        opportunity = 'sport'
    elif func == 'feest':
        opportunity = 'feestje'

    with open('Kledingkast.json', 'r+') as Data:
        placeInfo = json.load(Data)

    stad = placeInfo[userName][0]["gegevens"][0]["locatie"]["stad"]
    land = placeInfo[userName][0]["gegevens"][0]["locatie"]["land"]
    huidigeWeer = setValuesWeer(stad, land)
    gevoelsTemp = huidigeWeer[0]
    windSnelheid = huidigeWeer[2]
    if windSnelheid >= 5:
        gevoelsTemp = 13.12 + 0.6215 * gevoelsTemp - 11.37 * windSnelheid ** 0.16 + 0.3965 * gevoelsTemp * windSnelheid ** 0.16
    RandomClothes = pickClothes(userName, gevoelsTemp, huidigeWeer[1], opportunity)
    loopIndex = 0
    recommendedClothes(RandomClothes[0], RandomClothes[1], loopIndex, rootGen, Homescreen, showMenu, userName)


def autoGen(mogelijkeTops, mogelijkeBottoms, aantrekken, top, bottom, data, loopIndex, rootGen, Homescreen, showMenu, userName):
    "'Hier zorg ik er voor dat als iemand besluit het voorgelegde kleding setje aan te doen dat dat word geregistreerd in het json bestand.'"
    rootWear.destroy()
    if aantrekken == "ja":

        with open('Kledingkast.json', 'w') as ALL:
            today = datetime.today().strftime("%Y-%m-%d")
            formatVoorAppend = [top, bottom, str(today)]
            data[userName][1]["gedragen"].append(formatVoorAppend)
            json.dump(data, ALL)
            ALL.close()
            rootGen.update()
            rootGen.destroy()
            Homescreen()

    else:
        mogelijkeTops.remove(top)
        mogelijkeBottoms.remove(bottom)
        recommendedClothes(mogelijkeTops, mogelijkeBottoms, loopIndex, rootGen, Homescreen, showMenu, userName)


def recommendedClothes(mogelijkeTop, mogelijkeBottom, loopIndex, rootGen, Homescreen, showMenu, userName):
    "'Hier zorg ik voor dat alle errors worden opgevangen bij bijvoorbeeld te weinig kleding om uit te kiezen.'"
    "'Ook zorg ik er hier voor dat de kleur niet het zelfde zal zijn of dat je bij een jurkje geen broek draagt.'"
    "'Als laatst worden hier nog de knoppen aangemaakt om bijvoorbeeld een nieuw setje uit te gaan berekenen in een andere functie.'"
    mogelijkeTops = mogelijkeTop
    mogelijkeBottoms = mogelijkeBottom

    with open('Kledingkast.json', 'r+') as inf:
        data = json.load(inf)

    loopIndex += 1

    if len(mogelijkeTops) != 0:
        top = random.choice(mogelijkeTops)

        if top[2] != 'jurkje':
            if len(mogelijkeBottoms) != 0:
                bottom = random.choice(mogelijkeBottoms)
                if bottom[1] == top[1]:
                    bottom.random.choice(mogelijkeBottoms)
            else:
                bottom = None
    else:
        top = None

    if top == None or top == None and bottom == None or top[2] != 'jurkje' and bottom == None:
        bericht = "Helaas hebben we met deze beperkte kleding hoeveelheid geen setje kunnen vinden om aan te trekken."
        showinfo(title='Clothing error', message=bericht)
        rootGen.update()
        rootGen.destroy()
        Homescreen()
    else:
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
                              command=lambda: autoGen(mogelijkeTops, mogelijkeBottoms, 'ja', top, bottom, data,
                                                      loopIndex, rootGen, Homescreen, showMenu, userName))
        genYesButton.grid(row=11, sticky=W)

        genNoButton = Button(rootWear, text='Nee',
                             command=lambda: autoGen(mogelijkeTops, mogelijkeBottoms, 'nee', top, bottom, data,
                                                     loopIndex, rootGen, Homescreen, showMenu, userName))
        genNoButton.grid(row=11, sticky=E)

        genBackButton = Button(rootWear, text='Back', command=exit)
        genBackButton.grid(row=12)

        rootWear.mainloop()
