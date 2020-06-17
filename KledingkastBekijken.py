import json

with open('Kledingkast.json', 'r') as allVariables:
    allInfVariables = json.load(allVariables)
#
# def bekijken(naamUser):
#     differentVariables = []
#     for variable in allInfVariables[naamUser][2]:
#         differentVariables.append(variable)
#
#     print(getAllPossibleFilters(naamUser))
#     watBekijken = input("Waarop wil je filteren: ")
#
#     forSetVariables = []
#     for i in range(2, len(allInfVariables[naamUser])):
#         filterClothing = allInfVariables[naamUser][i][watBekijken]
#         forSetVariables.append(filterClothing)
#     forSetVariables = set(forSetVariables)
#     print(forSetVariables)
#
#     detailFilter = input(f"op welk(e) {watBekijken} wil je filteren: ")
#
#     for i in range(2, len(allInfVariables[naamUser])):
#        if detailFilter in allInfVariables[naamUser][i][watBekijken]:
#            print(allInfVariables[naamUser][i])

def getAllPossibleFilters(naamUser):
    differentVariables = []
    if len(allInfVariables[naamUser]) > 2:
        for variable in allInfVariables[naamUser][2]:
            differentVariables.append(variable)
        return differentVariables
    else:
        return []