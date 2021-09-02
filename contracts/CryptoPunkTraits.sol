//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CryptoPunkTraits {
    enum Slot {
        EAR,
        EYES,
        FACE,
        FACIAL_HAIR,
        HEAD,
        MOUTH,
        NECK,
        NOSE,
        SIZE,
        SMOKE,
        SPECIES
    }

    enum Trait {
        // Default value
        NULL,

        // Ear
        EARRING,

        // Eyes
        BIG_SHADES,
        BLUE_EYE_SHADOW,
        CLASSIC_SHADES,
        CLOWN_EYES_BLUE,
        CLOWN_EYES_GREEN,
        EYE_MASK,
        EYE_PATCH,
        GREEN_EYE_SHADOW,
        HORNED_RIM_GLASSES,
        NERD_GLASSES,
        PURPLE_EYE_SHADOW,
        REGULAR_SHADES,
        SMALL_SHADES,
        THREE_D_GLASSES,
        VR,
        WELDING_GOGGLES,

        // Face
        MOLE,
        ROSY_CHEEKS,
        SPOTS,
        VAMPIRE_HAIR,

        // Facial_hair
        BIG_BEARD,
        CHINSTRAP,
        FRONT_BEARD,
        FRONT_BEARD_DARK,
        GOAT,
        HALF_SHAVED,
        HANDLEBARS,
        LUXURIOUS_BEARD,
        MUSTACHE,
        MUTTONCHOPS,
        NORMAL_BEARD,
        NORMAL_BEARD_BLACK,
        SHADOW_BEARD,

        // Head
        BANDANA,
        BEANIE,
        BLONDE_BOB,
        BLONDE_SHORT,
        CAP,
        CAP_FORWARD,
        CLOWN_HAIR_GREEN,
        COWBOY_HAT,
        CRAZY_HAIR,
        DARK_HAIR,
        DO_RAG,
        FEDORA,
        FRUMPY_HAIR,
        HEADBAND,
        HOODIE,
        KNITTED_CAP,
        MESSY_HAIR,
        MOHAWK,
        MOHAWK_DARK,
        MOHAWK_THIN,
        ORANGE_SIDE,
        PEAK_SPIKE,
        PIGTAILS,
        PILOT_HELMET,
        PINK_WITH_HAT,
        POLICE_CAP,
        PURPLE_HAIR,
        RED_MOHAWK,
        SHAVED_HEAD,
        STRAIGHT_HAIR,
        STRAIGHT_HAIR_BLONDE,
        STRAIGHT_HAIR_DARK,
        STRINGY_HAIR,
        TASSLE_HAT,
        TIARA,
        TOP_HAT,
        WILD_BLONDE,
        WILD_HAIR,
        WILD_WHITE_HAIR,

        // Mouth
        BLACK_LIPSTICK,
        BUCK_TEETH,
        FROWN,
        HOT_LIPSTICK,
        MEDICAL_MASK,
        PURPLE_LIPSTICK,
        SMILE,

        // Neck
        CHOKER,
        GOLD_CHAIN,
        SILVER_CHAIN,

        // Nose
        CLOWN_NOSE,

        // Size
        LARGE,
        PETITE,

        // Smoke
        CIGARETTE,
        PIPE,
        VAPE,

        // Species
        ALIEN,
        APE,
        HUMAN,
        ZOMBIE
    }

    /**
     * @dev Get the slot of a trait by querying for the trait.
     * eg. traitToSlot(Trait.VAPE)
     */
    mapping(Trait => Slot) public traitToSlot;

    constructor() {
        traitToSlot[Trait.EARRING] = Slot.EAR;
        traitToSlot[Trait.BIG_SHADES] = Slot.EYES;
        traitToSlot[Trait.BLUE_EYE_SHADOW] = Slot.EYES;
        traitToSlot[Trait.CLASSIC_SHADES] = Slot.EYES;
        traitToSlot[Trait.CLOWN_EYES_BLUE] = Slot.EYES;
        traitToSlot[Trait.CLOWN_EYES_GREEN] = Slot.EYES;
        traitToSlot[Trait.EYE_MASK] = Slot.EYES;
        traitToSlot[Trait.EYE_PATCH] = Slot.EYES;
        traitToSlot[Trait.GREEN_EYE_SHADOW] = Slot.EYES;
        traitToSlot[Trait.HORNED_RIM_GLASSES] = Slot.EYES;
        traitToSlot[Trait.NERD_GLASSES] = Slot.EYES;
        traitToSlot[Trait.PURPLE_EYE_SHADOW] = Slot.EYES;
        traitToSlot[Trait.REGULAR_SHADES] = Slot.EYES;
        traitToSlot[Trait.SMALL_SHADES] = Slot.EYES;
        traitToSlot[Trait.THREE_D_GLASSES] = Slot.EYES;
        traitToSlot[Trait.VR] = Slot.EYES;
        traitToSlot[Trait.WELDING_GOGGLES] = Slot.EYES;
        traitToSlot[Trait.MOLE] = Slot.FACE;
        traitToSlot[Trait.ROSY_CHEEKS] = Slot.FACE;
        traitToSlot[Trait.SPOTS] = Slot.FACE;
        traitToSlot[Trait.VAMPIRE_HAIR] = Slot.FACE;
        traitToSlot[Trait.BIG_BEARD] = Slot.FACIAL_HAIR;
        traitToSlot[Trait.CHINSTRAP] = Slot.FACIAL_HAIR;
        traitToSlot[Trait.FRONT_BEARD] = Slot.FACIAL_HAIR;
        traitToSlot[Trait.FRONT_BEARD_DARK] = Slot.FACIAL_HAIR;
        traitToSlot[Trait.GOAT] = Slot.FACIAL_HAIR;
        traitToSlot[Trait.HALF_SHAVED] = Slot.FACIAL_HAIR;
        traitToSlot[Trait.HANDLEBARS] = Slot.FACIAL_HAIR;
        traitToSlot[Trait.LUXURIOUS_BEARD] = Slot.FACIAL_HAIR;
        traitToSlot[Trait.MUSTACHE] = Slot.FACIAL_HAIR;
        traitToSlot[Trait.MUTTONCHOPS] = Slot.FACIAL_HAIR;
        traitToSlot[Trait.NORMAL_BEARD] = Slot.FACIAL_HAIR;
        traitToSlot[Trait.NORMAL_BEARD_BLACK] = Slot.FACIAL_HAIR;
        traitToSlot[Trait.SHADOW_BEARD] = Slot.FACIAL_HAIR;
        traitToSlot[Trait.BANDANA] = Slot.HEAD;
        traitToSlot[Trait.BEANIE] = Slot.HEAD;
        traitToSlot[Trait.BLONDE_BOB] = Slot.HEAD;
        traitToSlot[Trait.BLONDE_SHORT] = Slot.HEAD;
        traitToSlot[Trait.CAP] = Slot.HEAD;
        traitToSlot[Trait.CAP_FORWARD] = Slot.HEAD;
        traitToSlot[Trait.CLOWN_HAIR_GREEN] = Slot.HEAD;
        traitToSlot[Trait.COWBOY_HAT] = Slot.HEAD;
        traitToSlot[Trait.CRAZY_HAIR] = Slot.HEAD;
        traitToSlot[Trait.DARK_HAIR] = Slot.HEAD;
        traitToSlot[Trait.DO_RAG] = Slot.HEAD;
        traitToSlot[Trait.FEDORA] = Slot.HEAD;
        traitToSlot[Trait.FRUMPY_HAIR] = Slot.HEAD;
        traitToSlot[Trait.HEADBAND] = Slot.HEAD;
        traitToSlot[Trait.HOODIE] = Slot.HEAD;
        traitToSlot[Trait.KNITTED_CAP] = Slot.HEAD;
        traitToSlot[Trait.MESSY_HAIR] = Slot.HEAD;
        traitToSlot[Trait.MOHAWK] = Slot.HEAD;
        traitToSlot[Trait.MOHAWK_DARK] = Slot.HEAD;
        traitToSlot[Trait.MOHAWK_THIN] = Slot.HEAD;
        traitToSlot[Trait.ORANGE_SIDE] = Slot.HEAD;
        traitToSlot[Trait.PEAK_SPIKE] = Slot.HEAD;
        traitToSlot[Trait.PIGTAILS] = Slot.HEAD;
        traitToSlot[Trait.PILOT_HELMET] = Slot.HEAD;
        traitToSlot[Trait.PINK_WITH_HAT] = Slot.HEAD;
        traitToSlot[Trait.POLICE_CAP] = Slot.HEAD;
        traitToSlot[Trait.PURPLE_HAIR] = Slot.HEAD;
        traitToSlot[Trait.RED_MOHAWK] = Slot.HEAD;
        traitToSlot[Trait.SHAVED_HEAD] = Slot.HEAD;
        traitToSlot[Trait.STRAIGHT_HAIR] = Slot.HEAD;
        traitToSlot[Trait.STRAIGHT_HAIR_BLONDE] = Slot.HEAD;
        traitToSlot[Trait.STRAIGHT_HAIR_DARK] = Slot.HEAD;
        traitToSlot[Trait.STRINGY_HAIR] = Slot.HEAD;
        traitToSlot[Trait.TASSLE_HAT] = Slot.HEAD;
        traitToSlot[Trait.TIARA] = Slot.HEAD;
        traitToSlot[Trait.TOP_HAT] = Slot.HEAD;
        traitToSlot[Trait.WILD_BLONDE] = Slot.HEAD;
        traitToSlot[Trait.WILD_HAIR] = Slot.HEAD;
        traitToSlot[Trait.WILD_WHITE_HAIR] = Slot.HEAD;
        traitToSlot[Trait.BLACK_LIPSTICK] = Slot.MOUTH;
        traitToSlot[Trait.BUCK_TEETH] = Slot.MOUTH;
        traitToSlot[Trait.FROWN] = Slot.MOUTH;
        traitToSlot[Trait.HOT_LIPSTICK] = Slot.MOUTH;
        traitToSlot[Trait.MEDICAL_MASK] = Slot.MOUTH;
        traitToSlot[Trait.PURPLE_LIPSTICK] = Slot.MOUTH;
        traitToSlot[Trait.SMILE] = Slot.MOUTH;
        traitToSlot[Trait.CHOKER] = Slot.NECK;
        traitToSlot[Trait.GOLD_CHAIN] = Slot.NECK;
        traitToSlot[Trait.SILVER_CHAIN] = Slot.NECK;
        traitToSlot[Trait.CLOWN_NOSE] = Slot.NOSE;
        traitToSlot[Trait.LARGE] = Slot.SIZE;
        traitToSlot[Trait.PETITE] = Slot.SIZE;
        traitToSlot[Trait.CIGARETTE] = Slot.SMOKE;
        traitToSlot[Trait.PIPE] = Slot.SMOKE;
        traitToSlot[Trait.VAPE] = Slot.SMOKE;
        traitToSlot[Trait.ALIEN] = Slot.SPECIES;
        traitToSlot[Trait.APE] = Slot.SPECIES;
        traitToSlot[Trait.HUMAN] = Slot.SPECIES;
        traitToSlot[Trait.ZOMBIE] = Slot.SPECIES;
    }
}
    