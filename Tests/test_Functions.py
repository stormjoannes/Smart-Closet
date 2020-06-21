from Code.Functions import *
import string
import pytest


def test_config_sign_up():
        naamUser = "TestUserName"
        stad = "breda"
        land = "nl"
        StatusBefore = checkIfExist(naamUser)


        naamUser = "TestUserName"
        stad = "breda"
        land = "nl"
        configSignUp(naamUser, stad, land)
        StatusAfter = checkIfExist(naamUser)

        assert StatusBefore == False and StatusAfter == True




def test_check_if_exist():
    with open('../jsonFiles/Kledingkast.json', 'r') as doc:
        allInf = json.load(doc)

    for i in allInf:
        TestUsernameExist = i

    StatusUsernameExist = checkIfExist(TestUsernameExist)
    StatusUsernameNONExist = checkIfExist("TestUsernameNONExist")
    assert StatusUsernameExist == True and StatusUsernameNONExist == False


def test_backup_dump():
    pass


def test_refresh_gedragen():
    pass


def test_geg_wijzigen():
    pass


def test_delete_account():
    pass