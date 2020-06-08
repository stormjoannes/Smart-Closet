from WeerAPI import *
from MatchingAppend import *

def opties():
    keuze = input("Wil je een kledingstuk toevoegen, verwijderen of uitkiezen: ").lower()
    if keuze == 'toevoegen':
        addClothes()
        opties()

    elif keuze == 'verwijderen':
        deleteClothes()
        opties()

    elif keuze == 'uitkiezen':
        pickClothes()
        opties()

    else:
        print(f"'{keuze}' is geen geldige optie")
        opties()


opties()
print(setValues())
