from Code.Functions import *
import string
import pytest


def test_config_sign_up():
        naamUser = "TestUserName"
        stad = "breda"
        land = "nl"
        StatusBefore = checkIfExist(naamUser)

        configSignUp(naamUser, stad, land)
        StatusAfter = checkIfExist(naamUser)
        deleteAccount(naamUser)

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
    username = "TestBackupDump"
    configSignUp(username, "utrecht", "nl")

    with open('../jsonFiles/BackupKledingkast.json', 'r') as doc:
        allInf = json.load(doc)

        TestBefore = False
        for i in allInf:
            if i == username:
                TestBefore = True

    backupDump()

    with open('../jsonFiles/BackupKledingkast.json', 'r') as doc:
        allInf = json.load(doc)

        TestAfter = False
        for i in allInf:
            if i == username:
                TestAfter = True

    deleteAccount(username)

    assert TestBefore == False and TestAfter == True



def test_refresh_gedragen():
    username = "TestRefreshGedragen"
    stad = "utrecht"
    land = "nl"

    configSignUp(username, stad, land)

    gedragenSetje = [["h&m shirt wit", "wit", "shirt", "h&m", "kort"],
                     ["grijze jeans", "grijze", "jeans", "denham", "lang"], "2020-06-10"]

    with open('../jsonFiles/Kledingkast.json', 'r') as doc:
        allInf = json.load(doc)

    with open('../jsonFiles/Kledingkast.json', 'w') as docWrite:
        allInf[username][1]["gedragen"].append(gedragenSetje)
        json.dump(allInf, docWrite)

    refreshGedragen(username)

    with open('../jsonFiles/Kledingkast.json', 'r') as doc:
        allInf = json.load(doc)

        lengteGedragenList = allInf[username][1]["gedragen"]

    deleteAccount(username)

    assert len(lengteGedragenList) == 0



def test_geg_wijzigen():
    naamUser = "TestGegevens"
    stad = "Utrecht"
    land = "nl"
    tussenWear = 1

    WijzigUserName = "TestGewijzigd"

    configSignUp(naamUser, stad, land)

    with open('../jsonFiles/Kledingkast.json', 'r') as doc:
        allInf = json.load(doc)

        TestBeforeName = False
        for i in allInf:
            if i == naamUser:
                TestBeforeName = True

        TestBeforeWijzigName = False
        for i in allInf:
            if i == WijzigUserName:
                TestBeforeWijzigName = True

    gegWijzigen(naamUser, tussenWear, stad, land, WijzigUserName) #Alleen de username word hier gewijzigd

    with open('../jsonFiles/Kledingkast.json', 'r') as doc:
        allInf = json.load(doc)

        TestAfterName = False
        for i in allInf:
            if i == naamUser:
                TestAfterName = True

        TestAfterWijzigName = False
        for i in allInf:
            if i == WijzigUserName:
                TestAfterWijzigName = True

    deleteAccount(WijzigUserName)

    assert TestBeforeName == True and TestBeforeWijzigName == False and TestAfterName == False and TestAfterWijzigName == True


def test_delete_account():
    naamUser = "TestDeleteAccount"
    stad = "breda"
    land = "nl"

    configSignUp(naamUser, stad, land)

    with open('../jsonFiles/Kledingkast.json', 'r') as doc:
        allInf = json.load(doc)

        TestBefore = False
        for i in allInf:
            if i == naamUser:
                TestBefore = True

    deleteAccount(naamUser)

    with open('../jsonFiles/Kledingkast.json', 'r') as doc:
        allInf = json.load(doc)

        TestAfter = False
        for i in allInf:
            if i == naamUser:
                TestAfter = True

    assert TestBefore == True and TestAfter == False