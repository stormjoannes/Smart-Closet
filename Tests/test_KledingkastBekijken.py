from Code.KledingkastBekijken import *
import tkinter
import pytest

def test_get_all_possible_filters():
    returnList = getAllPossibleFilters("admin")
    expectedList = ["naam", "langKort", "gelegenheid", "kleur", "merk", "categorie"]
    assert returnList == expectedList


def test_all_clothes():
    rootChoose = Tk()
    naam = "admin"
    returnValue = allClothes(rootChoose, naam)
    assert returnValue != None