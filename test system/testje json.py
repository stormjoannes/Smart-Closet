import json

def WeatherForPickClothes():
    stad = [userName][0]["gegevens"][0]["locatie"]["stad"]
    land = [userName][0]["gegevens"][0]["locatie"]["land"]
    huidigeWeer = setValuesWeer(stad, land)
    gevoelsTemp = huidigeWeer[0]
    windSnelheid = huidigeWeer[2]
    if windSnelheid >= 5:
        gevoelsTemp = 13.12 + 0.6215 * gevoelsTemp - 11.37 * windSnelheid ** 0.16 + 0.3965 * gevoelsTemp * windSnelheid ** 0.16
    print(gevoelsTemp)
    # pickClothes(userName, gevoelsTemp, huidigeWeer[1])