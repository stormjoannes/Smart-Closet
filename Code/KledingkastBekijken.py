from tkinter import *
import json
from tkinter.messagebox import showinfo


def getAllPossibleFilters(naamUser):
    """Deze functie pakt alle mogelijke categorieën waar je op kunt filterren, bijvoorbeeld: merk en kleur"""
    with open('../jsonFiles/Kledingkast.json', 'r') as allVariables:
        allInfVariables = json.load(allVariables)

    differentVariables = []
    if len(allInfVariables[naamUser]) > 2:
        for variable in allInfVariables[naamUser][2]:
            differentVariables.append(variable)
        return differentVariables
    else:
        return []


def allClothes(rootChoose, naam, path='../jsonFiles/Kledingkast.json'):
    """Deze functie zorgt dat als je op kleding uitkiezen klikt je gelijk al je kleding onder elkaar ziet staan."""
    global allInfVariables

    with open(path, 'r') as allVariables:
        allInfVariables = json.load(allVariables)
    global userName
    global AllClothes
    userName = naam

    allClothingString = ""

    for indexAll in range(2, len(allInfVariables[userName])):
        soortenTop = ["shirt", "hoodie", "hemdje", "trui", "vest", "crop top", "blazer", "jurk", "jumpsuit", "blousje"]
        soortenBottom = ["jeans", "legging", "chino", "joggingbroek", "jeans met gaten", "rokje", "high waste", "stoffen broek"]

        #Format voor makkelijk leesbaar kledingstuk.
        if allInfVariables[userName][indexAll]['categorie'] in soortenTop:
            leesbareTop = f"Een {allInfVariables[userName][indexAll]['kleur']}e {allInfVariables[userName][indexAll]['categorie']} met {allInfVariables[userName][indexAll]['langKort']}e mouwen van het merk: {allInfVariables[userName][indexAll]['merk']}"
            allClothingString += leesbareTop + '\n'

        elif allInfVariables[userName][indexAll] in soortenBottom:
            leesbareBottom = f"een {allInfVariables[userName][indexAll]['kleur']}e {allInfVariables[userName][indexAll]['categorie']} met {allInfVariables[userName][indexAll]['langKort']} broeks pijpen van het merk: {allInfVariables[userName][indexAll]['merk']}"
            allClothingString += leesbareBottom + '\n'
        else:
            continue

    AllClothes = Label(rootChoose, text=f'{allClothingString}: ', background="#c6def1")
    AllClothes.grid(row=2, column=0)

    return allClothingString


def toDeleteFilter(rootChoose, chooseFilterLabel, chooseFilterButton, chooseDeleteFilterButton):
    """Deze functie verwijdert de huidige filter als je die hebt toegepast."""
    try:
        #verwijder gefilterde kleding en delete filter button.
        chooseDeleteFilterButton.destroy()
        AllClothesDetailFiltered.destroy()
        chooseFilterLabel.destroy()
        chooseDetailFilterEntry.destroy()
        chooseFilterButton.destroy()
    except:
        bericht = 'No filter applied!'
        showinfo(title='Filter Error', message=bericht)
    allClothes(rootChoose, userName)


def getDetailFilters(watBekijken, detailFilter, rootChoose):
    """Deze functie past de hele filter toe, bijvoorbeeld: op kleur met de naam oranje of op merk met de naam abercrombie."""
    global AllClothesDetailFiltered

    allFilteredClothingString = ''
    for indexAllFiltered in range(2, len(allInfVariables[userName])):
        if detailFilter in allInfVariables[userName][indexAllFiltered][watBekijken]:
            soortenTop = ["shirt", "hoodie", "hemdje", "trui", "vest", "crop top", "blazer", "jurk", "jumpsuit", "blousje"]
            soortenBottom = ["jeans", "legging", "chino", "joggingbroek", "jeans met gaten", "rokje", "high waste", "stoffen broek"]

            # Format voor makkelijk leesbaar kledingstuk.
            if allInfVariables[userName][indexAllFiltered]['categorie'] in soortenTop:
                leesbareTop = f"Een {allInfVariables[userName][indexAllFiltered]['kleur']}e {allInfVariables[userName][indexAllFiltered]['categorie']} met {allInfVariables[userName][indexAllFiltered]['langKort']}e mouwen van het merk: {allInfVariables[userName][indexAllFiltered]['merk']}"
                allFilteredClothingString += leesbareTop + '\n'

            elif allInfVariables[userName][indexAllFiltered]['categorie'] in soortenBottom:
                leesbareBottom = f"Een {allInfVariables[userName][indexAllFiltered]['kleur']}e {allInfVariables[userName][indexAllFiltered]['categorie']} met {allInfVariables[userName][indexAllFiltered]['langKort']} broeks pijpen van het merk: {allInfVariables[userName][indexAllFiltered]['merk']}"
                allFilteredClothingString += leesbareBottom + '\n'
            else:
                continue

    #error voor als er geen kleren zijn bij de gekozen filter.
    if len(allFilteredClothingString) > 0:
        AllClothes.destroy()
        AllClothesDetailFiltered = Label(rootChoose, text=f'{allFilteredClothingString}: ', background="#c6def1")
        AllClothesDetailFiltered.grid(row=indexAllFiltered, column=0)
    else:
        bericht = "Helaas zijn er 0 resultaten met deze filter"
        showinfo(title='Filter error', message=bericht)


def forDetailFilter(Combobox, rootChoose):
    """Deze functie zorgt ervoor dat er een nieuwe regel met entry in je beeld komt zodra je de categorie filter hebt gekozen."""
    global chooseDetailFilterEntry

    chooseFilterLabel = Label(rootChoose, text=f'Welke {Combobox}: ', background="#c6def1")
    chooseFilterLabel.grid(row=1, sticky=W)

    chooseDetailFilterEntry = Entry(rootChoose)
    chooseDetailFilterEntry.grid(row=1, column=0)

    chooseFilterButton = Button(rootChoose, text='SUBMIT', command=lambda:getDetailFilters(Combobox, chooseDetailFilterEntry.get(), rootChoose))
    chooseFilterButton.grid(row=1, column=1)

    chooseDeleteFilterButton = Button(rootChoose, text='Delete Filter', command=lambda: toDeleteFilter(rootChoose, chooseFilterLabel, chooseFilterButton, chooseDeleteFilterButton))
    chooseDeleteFilterButton.grid(row=100, sticky=E)