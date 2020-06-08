import json

naamUser = 'fanne de bie'

with open('koekje.json', 'r+') as doc:
    allInf = json.load(doc)

with open('koekje.json', 'w') as document:
    nameAdd = input('Naam van je kledingstuk: ').lower()
    longShortAdd = input('Lengte van je broeks pijpen of mouwen: lang of kort: ').lower()
    opportunityAdd = input('Category van je kledingstuk: Sport, Feestje of dagelijks leven: ').lower()
    colorAdd = input('Kleur van je kledingstuk: ').lower()
    brandAdd = input('Merk van je kledingstuk: ').lower()
    categoryAdd = input('Category van kledingstuk: ').lower()

    nieuweData = {"naam": nameAdd,
                  "langKort": longShortAdd,
                  "gelegenheid": opportunityAdd,
                  "kleur": colorAdd,
                  "merk": brandAdd,
                  "categorie": categoryAdd}

    allInf[naamUser].append(nieuweData)
    json.dump(allInf, document)