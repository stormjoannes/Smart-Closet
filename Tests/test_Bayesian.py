from time import strptime
from Code.AddOrDelete import *

from Code.Bayesian import *
from Code.Functions import *
from datetime import datetime
from tkinter import *
import pytest

def test_Choice_Top_Bottom():
    userName = "TestChoiceTopBottom"
    stad = "utrecht"
    land = "nl"
    configSignUp(userName, stad, land)
    # addClothes(userName, "korte test jeans", "kort", "dagelijks leven", "zwart", "zara", "jeans")
    addClothes(userName, "kort test shirt", "kort", "dagelijks leven", "wit", "h&m", "shirt")
    soortenTop = ["shirt", "hoodie", "hemdje", "trui", "vest", "crop top", "blazer", "jurk", "jumpsuit", "blousje"]

    expectedValue = [['kort test shirt', 'wit', 'shirt', 'h&m', 'kort']]

    uitkomst = ChoiceTopBottom(userName, "kort", soortenTop, "dagelijks leven")

    deleteAccount(userName)

    assert expectedValue == uitkomst


def test_Collor_Choice():
    userName = "TestCollorChoice"
    stad = "utrecht"
    land = "nl"
    configSignUp(userName, stad, land)

    addClothes(userName, "korte test jeans", "kort", "dagelijks leven", "zwart", "zara", "jeans")
    addClothes(userName, "kort test shirt", "kort", "dagelijks leven", "wit", "h&m", "shirt")
    soortenTop = ["shirt", "hoodie", "hemdje", "trui", "vest", "crop top", "blazer", "jurk", "jumpsuit", "blousje"]
    soortenBottom = ["jeans", "legging", "chino", "joggingbroek", "jeans met gaten", "rokje", "high waste", "stoffen broek"]

    uitkomst = CollorChoice(userName, [['kort test shirt', 'wit', 'shirt', 'h&m', 'kort']], [['kort test jeans', 'zwart', 'jeans', 'zara', 'kort']], ['shirt'], ['shirt'], ['jeans'], ['jeans'])
    expectedValue = [[['kort test shirt', 'wit', 'shirt', 'h&m', 'kort'], ['kort test jeans', 'zwart', 'jeans', 'zara', 'kort']]]

    deleteAccount(userName)

    assert uitkomst == expectedValue


def test_Sorted_List_Sets():
    hitteNiveau = "hot"
    with open('../jsonFiles/Datastructuur.json', 'r') as HeatlevelInf:
        kortOfLangInf = json.load(HeatlevelInf)
    unsortedList = []
    unsortedList.append([['lang test shirt', 'wit', 'shirt', 'h&m', 'lang'], ['lang test jeans', 'zwart', 'jeans', 'zara', 'lang']])
    unsortedList.append([['kort test shirt', 'wit', 'shirt', 'h&m', 'kort'], ['kort test jeans', 'zwart', 'jeans', 'zara', 'kort']])

    uitkomstList = SortedListSets(unsortedList, hitteNiveau, kortOfLangInf)

    expectedList = [[['kort test shirt', 'wit', 'shirt', 'h&m', 'kort'], ['kort test jeans', 'zwart', 'jeans', 'zara', 'kort']], [['lang test shirt', 'wit', 'shirt', 'h&m', 'lang'], ['lang test jeans', 'zwart', 'jeans', 'zara', 'lang']]]

    assert expectedList == uitkomstList


def test_check_Gedragen():
    userName = "admin"

    setje = [["kort test shirt", "wit", "shirt", "h&m", "kort"], ["kort test jeans", "zwart", "jeans", "zara", "kort"]]

    assert True == checkGedragen(userName, setje, path='../jsonFiles/TESTKledingkast.json')


def test_get_Collor_Status():
    with open('../jsonFiles/Datastructuur.json', 'r') as ColorCombInf:
        collorCombinationsInfo = json.load(ColorCombInf)

    expectedValue = "ja"

    assert expectedValue == getCollorStatus(collorCombinationsInfo, "wit", "blauw")

def test_get_Common_Clothing_Pieces():
    pass

# def test_get_Time_Difference():
#     pass
#     firstTime = "2020-06-22"
#     timeDifference = getTimeDifference(firstTime)
#
#     assert "2" == "2"