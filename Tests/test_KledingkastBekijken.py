from Code.KledingkastBekijken import *
import pytest

def test_get_all_possible_filters():
    returnList = getAllPossibleFilters("admin")
    expectedList = ["naam", "langKort", "gelegenheid", "kleur", "merk", "categorie"]
    assert returnList == expectedList


def test_all_clothes():
    rootChoose = Tk()
    naam = "admin"
    returnValue = allClothes(rootChoose, naam, path="../jsonFiles/TESTKledingkast.json")
    testUitkomstValue = "Een grijse trui met lange mouwen van het merk: abercrombie "
    assert len(returnValue) == len(testUitkomstValue)