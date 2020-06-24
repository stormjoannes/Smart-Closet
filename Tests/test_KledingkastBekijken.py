from Code.KledingkastBekijken import *
from Code.AddOrDelete import *
import pathlib
import tkinter
import pytest

def test_get_all_possible_filters():
    returnList = getAllPossibleFilters("admin")
    expectedList = ["naam", "langKort", "gelegenheid", "kleur", "merk", "categorie"]
    assert returnList == expectedList


def test_all_clothes():
    rootChoose = Tk()
    naam = "admin"
    returnValue = allClothes(rootChoose, naam, path="../jsonFiles/TESTKledingkast.json")
    testUitkomstValue = "{'naam': 'chino broek', 'langKort': 'lang', 'gelegenheid': 'dagelijks leven', 'kleur': 'zwart', 'merk': 'h&m', 'categorie': 'broek'} \n{'naam': 'abecrombie trui', 'langKort': 'lang', 'gelegenheid': 'dagelijks leven', 'kleur': 'grijs', 'merk': 'abercrombie', 'categorie': 'trui'}"
    assert len(returnValue) == len(testUitkomstValue)