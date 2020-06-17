from AutomatischSetje import *
from WeerAPI import *
from AddOrDelete import *
import random
import json
from KledingkastBekijken import *

def configSignUp(naamUser, stad, land):
    with open('Kledingkast.json', 'r') as doc:
        allInf = json.load(doc)
        allInf[naamUser] = [
            {"gegevens": [{"locatie": {"stad": stad, "land": land}}, {"overigeGeg": {"betweenWear": 1}}]},
            {"gedragen": []}]

    with open('Kledingkast.json', 'w') as document:
        json.dump(allInf, document)


def checkIfExist(naamUser):
    with open('Kledingkast.json', 'r') as doc:
        allNames = json.load(doc)

    for i in allNames:
        if i == naamUser:
            return True
    return False

def backupDump():
    with open('Kledingkast.json', 'r') as forBackup:
        ForbackupDATA = json.load(forBackup)

    with open('BackupKledingkast.json', 'w') as frRefresh:
        json.dump(ForbackupDATA, frRefresh)
        frRefresh.close()


def refreshGedragen(naamUser):
    with open('Kledingkast.json', 'r+') as forRefresh:
        dataRefresh = json.load(forRefresh)

    for x in dataRefresh[naamUser][1]["gedragen"]:
        deltaTime = getTimeDifference(x)

        tussenPeriodeKleren = dataRefresh[naamUser][0]["gegevens"][1]["overigeGeg"]["betweenWear"]
        if deltaTime > tussenPeriodeKleren:
            with open('Kledingkast.json', 'w') as frRefresh:
                dataRefresh[naamUser][1]["gedragen"].remove(x)
                json.dump(dataRefresh, frRefresh)
                frRefresh.close()


def gegWijzigen(naamUser, tussenWearWijzig, stadWijzig, landWijzig, wijzigUsername):
    with open('Kledingkast.json', 'r+') as vrWijzig:
        allWijzig = json.load(vrWijzig)

    with open('Kledingkast.json', 'w') as vrWijzigWrite:
        tempValueUser = allWijzig[naamUser]
        allWijzig.pop(naamUser)
        allWijzig[wijzigUsername] = tempValueUser
        allWijzig[wijzigUsername][0]["gegevens"][0]["locatie"]["stad"] = stadWijzig
        allWijzig[wijzigUsername][0]["gegevens"][0]["locatie"]["land"] = landWijzig
        allWijzig[wijzigUsername][0]["gegevens"][1]["overigeGeg"]["betweenWear"] = int(tussenWearWijzig)

        json.dump(allWijzig, vrWijzigWrite)
        vrWijzigWrite.close()

    backupDump()
    return wijzigUsername

def deleteAccount(Login, userName, Globroot, rootDeleteAccount):
    with open('Kledingkast.json', 'r') as ALLaccounts:
        deleteAccountData = json.load(ALLaccounts)
        deleteAccountData.pop(userName)

    with open('Kledingkast.json', 'w') as deleteACC:
        json.dump(deleteAccountData, deleteACC)
    backupDump()
    Globroot.destroy()
    rootDeleteAccount.destroy()
    Login()