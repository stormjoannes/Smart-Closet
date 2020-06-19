from AutomatischSetje import *
from WeerAPI import *
from AddOrDelete import *
import random
import json
from KledingkastBekijken import *

def configSignUp(naamUser, stad, land):
    "'Hier zet ik de ingevulde gegevens van de signup in het json bestand.'"
    with open('Kledingkast.json', 'r') as doc:
        allInf = json.load(doc)
        allInf[naamUser] = [
            {"gegevens": [{"locatie": {"stad": stad, "land": land}}, {"overigeGeg": {"betweenWear": 1}}]},
            {"gedragen": []}]

    with open('Kledingkast.json', 'w') as document:
        json.dump(allInf, document)


def checkIfExist(naamUser):
    "'Deze functie gebruik ik om de controleren of een ingevulde username bestaat of niet.'"
    with open('Kledingkast.json', 'r') as doc:
        allNames = json.load(doc)

    for i in allNames:
        if i == naamUser:
            return True
    return False

def backupDump():
    "'Deze functie gebruik ik om de recente gegevens steeds worden gekopieerd naar een backup 'server'.'"
    with open('Kledingkast.json', 'r') as forBackup:
        ForbackupDATA = json.load(forBackup)

    with open('BackupKledingkast.json', 'w') as frRefresh:
        json.dump(ForbackupDATA, frRefresh)
        frRefresh.close()


def refreshGedragen(naamUser):
    "'Deze functie zorgt ervoor dat er gedragen kleding word verwijderd zodra die buiten de range valt van hoe lang iemand zijn setjes niet achter elkaar wilt dragen (tussenWear).'"
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
    "'In deze functie worden de ingevulde veranderde persoonlijke gegevens in het json bestand gezet.'"
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
    "'In deze functie word je account verwijderd uit de bestanden.'"
    with open('Kledingkast.json', 'r') as ALLaccounts:
        deleteAccountData = json.load(ALLaccounts)
        deleteAccountData.pop(userName)

    with open('Kledingkast.json', 'w') as deleteACC:
        json.dump(deleteAccountData, deleteACC)
    backupDump()
    Globroot.destroy()
    rootDeleteAccount.destroy()
    Login()