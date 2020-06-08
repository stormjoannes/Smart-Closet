from WeerAPI import *
from MatchingAppend import *

def opties():
    keuze = input("Wil je een kledingstuk toevoegen, verwijderen of uitkiezen: ").lower()
    if keuze == 'toevoegen':
        addClothes()

    elif keuze == 'verwijderen':
        deleteClothes()

    elif keuze == 'uitkiezen':
        pickClothes()

    else:
        print("optie is geen geldige optie")
        opties()


opties()
# print(setValues())
