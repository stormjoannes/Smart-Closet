import json
from Code.WeerAPI import *
import random

with open('../jsonFiles/kledingkast.json', 'r+') as Data:
    placeInfo = json.load(Data)

userName = "admin"

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

FiguratieLangKort = kortOfLangInf["tops"][hitteNiveau]
# print(hitteNiveau)

randomChoiceLijst = []
for x in FiguratieLangKort:
    kans = FiguratieLangKort[x]["yes"]
    kans = kans.split("/")[0]
    for i in range(0, int(kans)):
        randomChoiceLijst.append(x)
# print(randomChoiceLijst)
keuzeLangKort = random.choice(randomChoiceLijst)
print(randomChoiceLijst)
print(keuzeLangKort)
print(randomChoiceLijst[4], "juahhhhhhhhhh")

