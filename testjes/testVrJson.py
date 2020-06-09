import json
try:
    with open('testjes.json', 'r') as forBackup:
        backupDATA = json.load(forBackup)
except:
    print("hoi")

