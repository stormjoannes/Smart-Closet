import json
from tkinter.messagebox import showinfo

def addClothes(personName, nameAdd, longShortAdd, opportunityAdd, colorAdd, brandAdd, categoryAdd, path='../jsonFiles/Kledingkast.json'):
    """Hier word het kledingstuk dat je hebt ingevuld toegevoegd aan de bestanden(je virtuele kledingkast)."""
    with open(path, 'r') as allKleding:
        data = json.load(allKleding)

    with open('../jsonFiles/Kledingkast.json', 'w') as ALL:
        #format van de data om het in het json bestand te zetten.
        nieuweData = {"naam": nameAdd,
                      "langKort": longShortAdd,
                      "gelegenheid": opportunityAdd,
                      "kleur": colorAdd,
                      "merk": brandAdd,
                      "categorie": categoryAdd}

        data[personName].append(nieuweData)
        json.dump(data, ALL)
        ALL.close()

def deleteClothes(personName, nameDelete, longShortDelete, opportunityDelete, colorDelete, brandDelete, categoryDelete):
    """Hier word het uitgekozen kledingstuk verwijderd uit de bestanden(je virtuele kledingkast)."""
    with open('../jsonFiles/Kledingkast.json', 'r') as allKleding:
        dataDelete = json.load(allKleding)

    with open('../jsonFiles/Kledingkast.json', 'w') as ALL:
        checkIfDone = False
        for i in range(2, len(dataDelete[personName])):
            #check of het ingevoerde kledingstk wel bestaat.
            if dataDelete[personName][i]['naam'] == nameDelete and dataDelete[personName][i]['langKort'] == longShortDelete and dataDelete[personName][i]['gelegenheid'] == opportunityDelete and dataDelete[personName][i]['kleur'] == colorDelete and dataDelete[personName][i]['merk'] == brandDelete and dataDelete[personName][i]['categorie'] == categoryDelete:
                dataDelete[personName].remove(dataDelete[personName][i])
                checkIfDone = True
                break

        if checkIfDone == False:
            bericht = f'kledingstuk {str(personName)} bestaat niet en kan dus ook niet verwijderd worden!'
            showinfo(title='Delete Error', message=bericht)
        else:
            json.dump(dataDelete, ALL)
            ALL.close()