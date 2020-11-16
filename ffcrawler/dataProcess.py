import json, re, random
from chord import Chord
from pprint import pprint

def normalize_ship(text):
    people = list()
    for person in text.split("/"):
        person = person.strip().lower()
        if "original character" in person or "oc" in person \
            or "original male character" in person or "original female character" in person:
            person = "OC"
        people.append(person)
    res = str()
    for person in sorted(people):
        res += person.title() + "/"
    return res[0:-1]
    

def strip(text, to_strip):
    text = text.strip()
    for x in to_strip:
        text = text.replace(x, "")
    return text

def count(data, func = lambda x: x, sort = False):
    res = dict()
    for point in data:
        res[func(point)] = 1 + res.get(func(point), 0)
    if not sort:
        return res
    else:
        return sorted(res.items(), key= lambda x: x[1], reverse = True)

def printRows(data, condition = lambda x: True):
    i = 1
    padding = max([len(x[0]) if condition(x[1]) else 0 for x in data])
    for row in data:
        if condition(row[1]):
            print("{}.".format(i), end = "\t")
            i += 1
            print(str(row[0]).ljust(padding + 1), end="")
            print(row[1])

data = json.load(open("result.json"))

ships = list()

to_strip = [
    "Lord",
    "Queen",
    "King"
]


for point in data:
    for x in point["relationships"]:
        x = re.sub("\(.+\)", "", x)
        x = strip(x, to_strip).replace("Tinker | Necklace Elf", "Ethari").replace("You", "Reader")
        x = normalize_ship(x)
        if "/" in x:
            ships.append(x)

print("Of {} fanfics scraped:".format(len(data)))
print("\nLanguages:\n----------")
printRows(count(data, lambda x: x["language"], True))
print("\nShips:\n---------")
printRows(count(ships, sort = True), lambda x: x > 5)
shipsCount = count(ships, sort = True)

# Create matrix

characters = list()
for pair in ships:
    characters += pair.split("/")

characters = count(characters)
names = list()
for name, occur in characters.items():
    if occur > 20:
        names.append(name)

random.shuffle(names)

matrix = list()

while True:
    matrix = list()
    redo = False
    for name1 in names:
        row = list()
        for name2 in names:
            x = 0
            for ship in shipsCount:
                if name1 != name2 and \
                    name1.lower() in ship[0].lower() and name2.lower() in ship[0].lower():
                    x += ship[1]
            if x > 20:
                row.append(x)
            else:
                row.append(0)
        if max(row) < 5:
            names.remove(name1)
            print("Discarding", name1)
            redo = True
            break
        matrix.append(row)
    if not redo:
        break

Chord(matrix, names, title="Most popular Dragon Prince ships on AO3", noun="fics mention this ship", width=2200, wrap_labels=True, margin=30, credit="u/hakiergrzonzo").to_html()
