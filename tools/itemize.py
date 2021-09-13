import json
from rich import print

from traits import normalize_attribute
from ids import ITEMS

items: list = list()

with open("punks.json") as file:
    punks = json.load(file)

for punk in punks:
    punk_id = int(punk)
    items.append(list())

    if punks[punk]["species"] in ["Male", "Female"]:
        item_name = normalize_attribute("Human")
        item = ITEMS.index(item_name)
        items[punk_id].append(item)
    else:
        item_name = normalize_attribute(punks[punk]["species"])
        item = ITEMS.index(item_name)
        items[punk_id].append(item)

    for attribute in punks[punk]["attributes"]:
        item_name = normalize_attribute(attribute)
        item = ITEMS.index(item_name)
        items[punk_id].append(item)


with open("punk_database.json", "w+") as file:
    json.dump(items, file)
