import json
from rich import print


SPECIES: list = ("ALIEN", "APE", "FEMALE", "MALE", "ZOMBIE")
SKIN_COLOR: list = ("LIGHTER", "LIGHT", "DARK", "DARKER")
FACE: list = (
    "MOLE",
    "ROSY_CHEEKS",
    "SPOTS",
    "VAMPIRE_HAIR",
)
NECK: list = (
    "CHOKER",
    "GOLD_CHAIN",
    "SILVER_CHAIN",
)
FACIAL_HAIR: list = (
    "BIG_BEARD",
    "CHINSTRAP",
    "FRONT_BEARD",
    "FRONT_BEARD_DARK",
    "GOAT",
    "HALF_SHAVED",
    "HANDLEBARS",
    "LUXURIOUS_BEARD",
    "MUSTACHE",
    "MUTTONCHOPS",
    "NORMAL_BEARD",
    "NORMAL_BEARD_BLACK",
    "SHADOW_BEARD",
)
NOSE: list = ("CLOWN_NOSE",)
EAR: list = ("EARRING",)
HEAD: list = (
    "BANDANA",
    "BEANIE",
    "BLONDE_BOB",
    "BLONDE_SHORT",
    "CAP",
    "CAP_FORWARD",
    "CLOWN_HAIR_GREEN",
    "COWBOY_HAT",
    "CRAZY_HAIR",
    "DARK_HAIR",
    "DO_RAG",
    "FEDORA",
    "FRUMPY_HAIR",
    "HEADBAND",
    "HOODIE",
    "KNITTED_CAP",
    "MESSY_HAIR",
    "MOHAWK",
    "MOHAWK_DARK",
    "MOHAWK_THIN",
    "ORANGE_SIDE",
    "PEAK_SPIKE",
    "PIGTAILS",
    "PILOT_HELMET",
    "PINK_WITH_HAT",
    "POLICE_CAP",
    "PURPLE_HAIR",
    "RED_MOHAWK",
    "SHAVED_HEAD",
    "STRAIGHT_HAIR",
    "STRAIGHT_HAIR_BLONDE",
    "STRAIGHT_HAIR_DARK",
    "STRINGY_HAIR",
    "TASSLE_HAT",
    "TIARA",
    "TOP_HAT",
    "WILD_BLONDE",
    "WILD_HAIR",
    "WILD_WHITE_HAIR",
)
MOUTH: list = (
    "BLACK_LIPSTICK",
    "BUCK_TEETH",
    "FROWN",
    "HOT_LIPSTICK",
    "MEDICAL_MASK",
    "PURPLE_LIPSTICK",
    "SMILE",
)
EYES: list = (
    "3D_GLASSES",
    "BIG_SHADES",
    "BLUE_EYE_SHADOW",
    "CLASSIC_SHADES",
    "CLOWN_EYES_BLUE",
    "CLOWN_EYES_GREEN",
    "EYE_MASK",
    "EYE_PATCH",
    "GREEN_EYE_SHADOW",
    "HORNED_RIM_GLASSES",
    "NERD_GLASSES",
    "PURPLE_EYE_SHADOW",
    "REGULAR_SHADES",
    "SMALL_SHADES",
    "VR",
    "WELDING_GOGGLES",
)
SMOKE: list = (
    "DEFAULT",
    "CIGARETTE",
    "PIPE",
    "VAPE",
)
ATTRIBUTES: list = sorted(
    FACE + NECK + FACIAL_HAIR + NOSE + EAR + HEAD + MOUTH + EYES + SMOKE
)


# Returns all species and attributes by iterating all punks and removing duplicates
def sift_traits(json_file_path: str):
    species: list = list()
    attributes: list = list()

    with open(json_file_path) as json_file:
        punks = json.load(json_file)
        for punk in punks:
            punk = punks[punk]

            if punk["species"] not in species:
                species.append(punk["species"])

            for attribute in enumerate(punk["attributes"]):
                if attribute[1] not in attributes:
                    attributes.append(punk["attributes"][attribute[0]])

    return species, attributes


def generate_solidity_file(json_file_path: str, species: list, attributes: list):
    solidity_file = """\
//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";

contract CryptoPunkItems is ERC1155, IERC721Receiver {{
    enum Slot {{
        SIZE,
        SPECIES,
        SKIN,
        FACE,
        NECK,
        FACIAL_HAIR,
        NOSE,
        EAR,
        HEAD,
        MOUTH,
        EYES,
        SMOKE
    }}

    struct CryptoPunkItem {{
        Slot slot;
    }}

    // The starting index of new items
    {index}

    // Maps the index to the Item
    mapping(uint256 => CryptoPunkItem) idToItem;

    // Original species
{species}

    // Original attributes
{attributes}
}}
    """

    index: int = 0

    species_string: str = ""
    for species in SPECIES:
        species_string = (
            species_string + f"    uint256 public constant {species} = {index};\n"
        )
        index += 1

    attributes_string: str = ""
    for attribute in ATTRIBUTES:
        attributes_string = (
            attributes_string + f"    uint256 public constant {attribute} = {index};\n"
        )
        index += 1

    index_string = f"uint256 public index = {index};"

    solidity_file = solidity_file.format(
        species=species_string[:-1],
        attributes=attributes_string[:-1],
        index=index_string,
    )
    print(solidity_file)


def generate_python_file(species: list, attributes: list):
    python_file = """\
species: list =  (
{species}
)

attributes: list = (
{attributes}
)
    """

    species = sorted(species)
    species_string = ""
    for species in species:
        species_string = species_string + f'    "{species.upper()}",\n'

    attributes = sorted(attributes)
    attributes_string = ""
    for attribute in attributes:
        attribute_formatted = attribute.upper().replace(" ", "_").replace("-", "_")
        attributes_string = attributes_string + f'    "{attribute_formatted}",\n'

    python_file = python_file.format(
        species=species_string[:-2], attributes=attributes_string[:-2]
    )
    print(python_file)


if __name__ == "__main__":
    species, attributes = sift_traits("punks.json")
    generate_solidity_file("punks.json", species, attributes)
