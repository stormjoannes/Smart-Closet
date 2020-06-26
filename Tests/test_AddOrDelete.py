from Code.AddOrDelete import *
import pytest


def test_add_clothes():
    userName = "admin"
    naam = "test kledingstuk"
    langKort = "kort"
    gelegenheid = "dagelijks leven"
    kleur = "rood"
    merk = "levi's"
    categorie = "shirt"

    addClothes(userName, naam, langKort, gelegenheid, kleur, merk, categorie)

    with open('../jsonFiles/Kledingkast.json', 'r') as allKleding:
        data = json.load(allKleding)

    for i in range(2, len(data[userName])):
        if data[userName][i]["naam"] == naam and data[userName][i]["langKort"] == langKort and \
                data[userName][i]["gelegenheid"] == gelegenheid and data[userName][i]["kleur"] == kleur and \
                data[userName][i]["merk"] == merk and data[userName][i]["categorie"] == categorie:
            uitkomst = data[userName][i]

    expectedVal = {'naam': naam, 'langKort': langKort, 'gelegenheid': gelegenheid, 'kleur': kleur, 'merk': merk, 'categorie': categorie}

    assert expectedVal == uitkomst

def test_delete_clothes():
    userName = "admin"
    naam = "test kledingstuk"
    langKort = "kort"
    gelegenheid = "dagelijks leven"
    kleur = "rood"
    merk = "levi's"
    categorie = "shirt"
    deleteClothes(userName, naam, langKort, gelegenheid, kleur, merk, categorie)

    with open('../jsonFiles/Kledingkast.json', 'r') as allKleding:
        data = json.load(allKleding)

    x = None

    for i in range(2, len(data[userName])):
        if data[userName][i]["naam"] == naam and data[userName][i]["langKort"] == langKort and \
                data[userName][i]["gelegenheid"] == gelegenheid and data[userName][i]["kleur"] == kleur and \
                data[userName][i]["merk"] == merk and data[userName][i]["categorie"] == categorie:
            x = data[userName][i]

    assert x == None
