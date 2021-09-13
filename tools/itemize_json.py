import json

from ids import ITEMS
from rich import print
from traits import normalize_attribute

IPFS_URL: str = (
    "https://ipfs.io/ipfs/QmdLmvgeVk1hEkmHaikacWC5zNVvR99gGvPYMQmdWDFef9/{id}.gif"
)

# {
#   "description": "Friendly OpenSea Creature that enjoys long swims in the ocean.",
#   "external_url": "https://openseacreatures.io/3",
#   "image": "https://storage.googleapis.com/opensea-prod.appspot.com/puffs/3.png",
#   "name": "Dave Starbelly",
#   "attributes": [ ... ],
# }


def denormalize_attribute(item: str) -> str:
    return (
        item.replace("THREE_", "3")
        .replace("_", " ")
        .title()
        .replace("Vr", "VR")
        .replace("Do-Rag", "Do-rag")
    )


for item_id, item in enumerate(ITEMS):
    metadata: dict = dict()
    metadata["name"] = denormalize_attribute(item)
    metadata["image"] = IPFS_URL.format(id=item)
    with open(f"metadata/{item_id}.json", "w+") as file:
        json.dump(metadata, file)
    print(metadata)
