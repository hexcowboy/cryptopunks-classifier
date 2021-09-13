from rich import print
import json

SLOTS: dict = {
    "SIZE": ("LARGE", "PETITE"),
    "SPECIES": ("ALIEN", "APE", "HUMAN", "ZOMBIE"),
    "FACE": (
        "NONE",
        "MOLE",
        "ROSY_CHEEKS",
        "SPOTS",
        "VAMPIRE_HAIR",
    ),
    "NECK": (
        "NONE",
        "CHOKER",
        "GOLD_CHAIN",
        "SILVER_CHAIN",
    ),
    "FACIAL_HAIR": (
        "NONE",
        "BIG_BEARD",
        "CHINSTRAP",
        "FRONT_BEARD",
        "FRONT_BEARD_DARK",
        "GOAT",
        "HANDLEBARS",
        "LUXURIOUS_BEARD",
        "MUSTACHE",
        "MUTTONCHOPS",
        "NORMAL_BEARD",
        "NORMAL_BEARD_BLACK",
        "SHADOW_BEARD",
    ),
    "NOSE": ("CLOWN_NOSE", "NONE"),
    "EAR": ("EARRING", "NONE"),
    "HEAD": (
        "NONE",
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
        "HALF_SHAVED",
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
        "NONE",
        "BLACK_LIPSTICK",
        "BUCK_TEETH",
        "FROWN",
        "HOT_LIPSTICK",
        "MEDICAL_MASK",
        "PURPLE_LIPSTICK",
        "SMILE",
    ),
    "EYES": (
        "NONE",
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
        "NONE",
        "CIGARETTE",
        "PIPE",
        "VAPE",
    ),
}

count = 0

# for species in SLOTS["SPECIES"]:
#     for size in SLOTS["SIZE"]:
#         for face in SLOTS["FACE"]:
#             for neck in SLOTS["NECK"]:
#                 for fhair in SLOTS["FACIAL_HAIR"]:
#                     for nose in SLOTS["NOSE"]:
#                         for ear in SLOTS["EAR"]:
#                             for head in SLOTS["HEAD"]:
#                                 for mouth in SLOTS["MOUTH"]:
#                                     for eyes in SLOTS["EYES"]:
#                                         for smoke in SLOTS["SMOKE"]:
#                                             count += 1

items = 0

with open("./punks.json") as file:
    punks = json.load(file)
    for punk in punks:
        # add 1 for species
        items += 1
        for attribute in punks[punk]["attributes"]:
            items += 1

print(f"There are {count} possible combinations")
print(f"There are potentially {items} items")
