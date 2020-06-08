import json

naamUser = 'fanne de bie'

with open('koekje.json', 'r+') as doc:
    allInf = json.load(doc)

with open('koekje.json', 'w') as document:
    allInf[naamUser] = []
    json.dump(allInf, document)