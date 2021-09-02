import json
import os
from rich import print


SLOTS: dict = {
    "SIZE": ("LARGE", "PETITE"),
    "SPECIES": ("ALIEN", "APE", "HUMAN", "ZOMBIE"),
    "FACE": (
        "MOLE",
        "ROSY_CHEEKS",
        "SPOTS",
        "VAMPIRE_HAIR",
    ),
    "NECK": (
        "CHOKER",
        "GOLD_CHAIN",
        "SILVER_CHAIN",
    ),
    "FACIAL_HAIR": (
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
    ),
    "NOSE": ("CLOWN_NOSE",),
    "EAR": ("EARRING",),
    "HEAD": (
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
    ),
    "MOUTH": (
        "BLACK_LIPSTICK",
        "BUCK_TEETH",
        "FROWN",
        "HOT_LIPSTICK",
        "MEDICAL_MASK",
        "PURPLE_LIPSTICK",
        "SMILE",
    ),
    "EYES": (
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
        "THREE_D_GLASSES",
        "VR",
        "WELDING_GOGGLES",
    ),
    "SMOKE": (
        "CIGARETTE",
        "PIPE",
        "VAPE",
    ),
}

ATTRIBUTES: list = sorted([attribute for attribute in SLOTS])


def normalize_attribute(attribute: str) -> str:
    return attribute.upper().replace(" ", "_").replace("-", "_").replace("3", "THREE_")


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


def generate_solidity_files(json_file_path: str, species: list, attributes: list):
    crypto_punk_traits_sol = """\
//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CryptoPunkTraits {{
    enum Slot {{
{slots}
    }}

    enum Trait {{
        // Default value
        NULL,

{traits}
    }}

    /**
     * @dev Get the slot of a trait by querying for the trait.
     * eg. traitToSlot(Trait.VAPE)
     */
    mapping(Trait => Slot) public traitToSlot;

    constructor() {{
{trait_to_slot}
    }}
}}
    """

    crypto_punk_sol = """\
//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import './CryptoPunkTraits.sol';

contract CryptoPunk {{
    // The structure of a CryptoPunk
    struct CryptoPunk {{
{slots}
    }}

    // A list of all original CryptoPunks and their traits
    CryptoPunk[10000] punks;

    constructor() {{
{original_punks}
    }}
}}
    """

    attributes_string: str = ""
    slots_string_enum: str = ""
    slots_string_struct: str = ""
    trait_to_slot_string: str = ""
    for slot in sorted(SLOTS):
        slots_string_enum += f"        {slot},\n"
        slots_string_struct += f"        CryptoPunkTraits.Trait {slot};\n"

        attributes_string += f"\n        // {slot.capitalize()}\n"
        for attribute in SLOTS[slot]:
            attributes_string += f"        {attribute},\n"

        for trait in SLOTS[slot]:
            trait_to_slot_string += (
                f"        traitToSlot[Trait.{trait}] = Slot.{slot};\n"
            )

    original_punks_string: str = ""
    with open(json_file_path) as json_file:
        punks = json.load(json_file)
        for punk_id in punks:
            punk = punks[punk_id]
            original_punks_string += f"        punks[{punk_id}] = CryptoPunk(\n"

            attributes = """\
            CryptoPunkTraits.Trait.EAR,
            CryptoPunkTraits.Trait.EYES,
            CryptoPunkTraits.Trait.FACE,
            CryptoPunkTraits.Trait.FACIAL_HAIR,
            CryptoPunkTraits.Trait.HEAD,
            CryptoPunkTraits.Trait.MOUTH,
            CryptoPunkTraits.Trait.NECK,
            CryptoPunkTraits.Trait.NOSE,
            CryptoPunkTraits.Trait.SIZE,
            CryptoPunkTraits.Trait.SMOKE,
            CryptoPunkTraits.Trait.SPECIES
        """

            if punk["species"] in ["Male", "Ape", "Zombie", "Alien"]:
                attributes = attributes.replace("SIZE", "LARGE")
                if punk["species"] == "Male":
                    attributes = attributes.replace("SPECIES", "HUMAN")
                else:
                    attributes = attributes.replace("SPECIES", punk["species"].upper())
            else:
                attributes = attributes.replace("SIZE", "PETITE")
                attributes = attributes.replace("SPECIES", "HUMAN")

            for slot in sorted(ATTRIBUTES):
                for attribute in punk["attributes"] + [""]:
                    attribute = (
                        attribute.upper()
                        .replace(" ", "_")
                        .replace("-", "_")
                        .replace("3", "THREE_")
                    )

                    if attribute not in SLOTS[slot]:
                        attributes = attributes.replace(slot, "NULL")
                    else:
                        attributes = attributes.replace(slot, attribute)
                        break

            original_punks_string += f"{attributes});\n"

    crypto_punk_traits_sol = crypto_punk_traits_sol.format(
        slots=slots_string_enum[:-2],
        traits=attributes_string[1:-2],
        original_punks="original_punks_string",
        trait_to_slot=trait_to_slot_string[:-1],
    )

    crypto_punk_sol = crypto_punk_sol.format(
        slots=slots_string_struct[:-1], original_punks=original_punks_string[:-1]
    )

    # Create the output directory
    if not os.path.exists("contracts"):
        os.makedirs("contracts")

    with open("contracts/CryptoPunkTraits.sol", "w") as file:
        file.write(crypto_punk_traits_sol)

    with open("contracts/CryptoPunk.sol", "w") as file:
        file.write(crypto_punk_sol)


if __name__ == "__main__":
    species, attributes = sift_traits("punks.json")
    generate_solidity_files("punks.json", species, attributes)
