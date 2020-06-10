import json

def bekijken(naamUser):
    with open('Kledingkast.json', 'r') as allVariables:
        allInfVariables = json.load(allVariables)

    differentVariables = []
    for variable in allInfVariables[naamUser][2]:
        differentVariables.append(variable)

    print(differentVariables)
    watBekijken = input("Waarop wil je filteren: ")

    for i in range(2, len(allInfVariables[naamUser])):
        filterClothing = allInfVariables[naamUser][i][watBekijken]
        print(filterClothing)

    detailFilter = input(f"op welk(e) {watBekijken} wil je filteren: ")

    for i in range(2, len(allInfVariables[naamUser])):
       if detailFilter in allInfVariables[naamUser][i][watBekijken]:
           print(allInfVariables[naamUser][i])