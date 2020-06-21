from Code.AddOrDelete import *
from Code.interface import toHub

def test_add_clothes():
    userName = "admin"
    naam = "test kledingstuk"
    langKort = "kort"
    gelegenheid = "dagelijks leven"
    kleur = "rood"
    merk = "levi's"
    categorie = "shirt"

    addClothes(userName, naam, langKort, gelegenheid, kleur, merk, categorie, toHub)

    with open('.../Smart-Closet/Kledingkast.json', 'r') as allKleding:
        data = json.load(allKleding)

    for i in data[userName]:
        if i["naam"] == naam and i["langKort"] == langKort and i["gelegenheid"] == gelegenheid and i["kleur"] == kleur and i["merk"] == merk and i["categorie"] == categorie:
            x = i

    uitkomst = [naam, langKort, gelegenheid, kleur, merk, categorie]

    assert x == uitkomst

# def test_delete_clothes():
#     self.fail()
