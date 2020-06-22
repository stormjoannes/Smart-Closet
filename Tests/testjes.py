import json
from Code.Functions import *

username = "TestRefreshGedragen"
stad = "utrecht"
land = "nl"

configSignUp(username, stad, land)

gedragenSetje = [["h&m shirt wit", "wit", "shirt", "h&m", "kort"],
                 ["grijze jeans", "grijze", "jeans", "denham", "lang"], "2020-06-10"]

with open('../jsonFiles/BackupKledingkast.json', 'r') as doc:
    allInf = json.load(doc)

with open('../jsonFiles/BackupKledingkast.json', 'w') as docWrite:
    allInf[username][1]["gedragen"].append(gedragenSetje)
    json.dump(allInf, docWrite)

refreshGedragen(username)

with open('../jsonFiles/BackupKledingkast.json', 'r') as doc:
    allInf = json.load(doc)

    lengteGedragenList = allInf[username][1]["gedragen"]

deleteAccount(username)
