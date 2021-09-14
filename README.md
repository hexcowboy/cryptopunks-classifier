# cryptopunks-classifier

Classify CryptoPunks based on their species and attributes.

This repository contains the following tools:

- `tools/api.py` creates a json file with every cryptopunk and its attributes and saves to `api.json`
- `tools/calulator.py` misspelled and counts the total amount of all CryptoPunk attributes
- `tools/ids.py` library of the IDs used for Loot for Punks
- `tools/images.py` takes the big CryptoPunk image [punks.png](./punks.png) and separately saves every punk to it's own file in `images/`
- `tools/itemize.py` takes every cryptopunk and puts the ID of its items (including species) into a json list [punk_database.json](./punk_database.json)
- `tools/itemize_json.py` takes every CryptoPunk and puts the `NORMALIZED_NAME` into separate json files in `metadata/`
- `tools/traits.py` gets all traits for every CryptoPunk and outputs them to solidity contracts in `contracts/` (not really used)
