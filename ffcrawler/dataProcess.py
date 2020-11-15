import json
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
    padding = max([len(x[0]) if condition(x[1]) else 0 for x in data])
    for row in data:
        if condition(row[1]):
            print(str(row[0]).ljust(padding + 1), end="")
            print(row[1])

data = json.load(open("result1885.json"))

ships = list()

to_strip = [
    "(The Dragon Prince)",
    "Lord",
    "Queen",
    "King"
]

for point in data:
    for x in point["relationships"]:
        x = strip(x, to_strip).replace("Tinker | Necklace Elf", "Ethari")
        x = normalize_ship(x)
        if "/" in x:
            ships.append(x)
print("\nLanguages:\n----------")
printRows(count(data, lambda x: x["language"], True))
print("\nShips:\n---------")
printRows(count(ships, sort = True), lambda x: x > 10)