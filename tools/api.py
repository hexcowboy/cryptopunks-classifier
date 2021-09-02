import json
from rich import print

from traits import ATTRIBUTES, SLOTS, normalize_attribute


def create_api_data(punk_json: dict):
    """Create API data from the original CryptoPunk scrape"""
    punk_json = json.load(punk_json)
    punk_api_data = dict()

    for slot in SLOTS:
        for punk_id in punk_json:
            punk = punk_json[punk_id]

            # Initialize the punk entry
            if punk_id not in punk_api_data:
                punk_api_data[punk_id] = dict()

            if slot == "SPECIES":
                if punk["species"] in ("Male", "Female"):
                    punk_api_data[punk_id][slot] = "HUMAN"
                    punk_api_data[punk_id]["SIZE"] = normalize_attribute(
                        "Large" if punk["species"] == "Male" else "Petite"
                    )
                else:
                    punk_api_data[punk_id][slot] = normalize_attribute(punk["species"])
                    punk_api_data[punk_id]["SIZE"] = "LARGE"
            else:
                punk_api_data[punk_id][slot] = "NULL"
                for attribute in punk["attributes"]:
                    attribute = normalize_attribute(attribute)
                    if attribute in SLOTS[slot]:
                        punk_api_data[punk_id][slot] = attribute

    with open("./api.json", "w") as api_file:
        json.dump(punk_api_data, api_file)


if __name__ == "__main__":
    with open("./punks.json") as punk_json:
        create_api_data(punk_json)
