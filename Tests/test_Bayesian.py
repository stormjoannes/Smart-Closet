from Code.Functions import *
import pytest

def test_Choice_Top_Bottom():
    userName = "TestChoiceTopBottom"
    stad = "utrecht"
    land = "nl"
    configSignUp(userName, stad, land)
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

    uitkomst = CollorChoice(userName, [['kort test shirt', 'wit', 'shirt', 'h&m', 'kort']], [['kort test jeans', 'zwart', 'jeans', 'zara', 'kort']],
                            ['shirt'], ['shirt'], ['jeans'], ['jeans'])
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

    expectedList = [[['kort test shirt', 'wit', 'shirt', 'h&m', 'kort'], ['kort test jeans', 'zwart', 'jeans', 'zara', 'kort']],
                    [['lang test shirt', 'wit', 'shirt', 'h&m', 'lang'], ['lang test jeans', 'zwart', 'jeans', 'zara', 'lang']]]

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
    with open('../jsonFiles/Datastructuur.json', 'r') as HeatlevelInf:
        kortOfLangInf = json.load(HeatlevelInf)

    AllBottoms = [['zwarte jeans', 'zwart', 'jeans', 'scotch en soda', 'lang'], ['blauwe jeans', 'blauw', 'jeans', 'h&m', 'kort'],
                  ['witte jeans', 'wit', 'jeans', 'scotch en soda', 'lang']]
    voorkomendeCategorie = ["jeans", "jeans", "jeans"]
    wearableTopBottomList = ['jeans', 'jeans', 'jeans', 'jeans', 'legging', 'jeans met gaten', 'rokje', 'high waste', 'stoffen broek']
    uitkomst = getCommonClothingPieces(kortOfLangInf, "hot", AllBottoms, "bottoms")

    assert 3 == len(uitkomst[0]) and voorkomendeCategorie == uitkomst[1] and wearableTopBottomList == uitkomst[2]

def test_get_Time_Difference():
    firstTime = [[], [], "2020-06-22"]
    date_formatToday = "%Y-%m-%d"
    today = datetime.strptime("2020-06-25", date_formatToday)
    timeDifference = getTimeDifference(firstTime, today)

    assert "3" == str(timeDifference)