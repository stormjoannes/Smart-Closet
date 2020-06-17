from tkinter import *
import json
from tkinter.messagebox import showinfo

with open('Kledingkast.json', 'r') as allVariables:
    allInfVariables = json.load(allVariables)

def getAllPossibleFilters(naamUser):
    differentVariables = []
    if len(allInfVariables[naamUser]) > 2:
        for variable in allInfVariables[naamUser][2]:
            differentVariables.append(variable)
        return differentVariables
    else:
        return []

def allClothes(rootChoose, naam):
    global userName
    global AllClothes
    userName = naam

    allClothingString = ''

    for indexAll in range(2, len(allInfVariables[userName])):
        allClothingString += str(allInfVariables[userName][indexAll]) + '\n'

    AllClothes = Label(rootChoose, text=f'{allClothingString}: ', background="gray")
    AllClothes.grid(row=2, column=0)

def toDeleteFilter(rootChoose):
    try:
        AllClothesDetailFiltered.destroy()
        chooseFilterLabel.destroy()
        chooseDetailFilterEntry.destroy()
        chooseFilterButton.destroy()
    except:
        bericht = 'No filter applied!'
        showinfo(title='Filter Error', message=bericht)
    allClothes(rootChoose, userName)

def getDetailFilters(watBekijken, detailFilter, rootChoose):
    global AllClothesDetailFiltered

    allFilteredClothingString = ''
    for indexAllFiltered in range(2, len(allInfVariables[userName])):
        if detailFilter in allInfVariables[userName][indexAllFiltered][watBekijken]:
            allFilteredClothingString += str(allInfVariables[userName][indexAllFiltered]) + '\n'

    if len(allFilteredClothingString) > 0:
        AllClothes.destroy()
        AllClothesDetailFiltered = Label(rootChoose, text=f'{allFilteredClothingString}: ', background="gray")
        AllClothesDetailFiltered.grid(row=indexAllFiltered, column=0)
    else:
        bericht = "Helaas zijn er 0 resultaten met deze filter"
        showinfo(title='Filter error', message=bericht)

def forDetailFilter(Combobox, rootChoose):
    global chooseFilterLabel
    global chooseDetailFilterEntry
    global chooseFilterButton

    chooseFilterLabel = Label(rootChoose, text=f'Op welke {Combobox} wil je filteren: ', background="gray")
    chooseFilterLabel.grid(row=1, sticky=W)

    chooseDetailFilterEntry = Entry(rootChoose)
    chooseDetailFilterEntry.grid(row=1, column=0)

    chooseFilterButton = Button(rootChoose, text='SUBMIT', command=lambda:getDetailFilters(Combobox, chooseDetailFilterEntry.get(), rootChoose))
    chooseFilterButton.grid(row=1, column=1)