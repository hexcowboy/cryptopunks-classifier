//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

library CryptoPunkTraits {
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
        HALF_SHAVED,
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
     * eg. traitToSlot[Trait.VAPE]
     */
    function traitToSlot(uint256 traitId) external pure returns (uint8) {
        Slot[93] memory traitsToSlots = [
            Slot.EAR, // EARRING
            Slot.EYES, // BIG_SHADES
            Slot.EYES, // BLUE_EYE_SHADOW
            Slot.EYES, // CLASSIC_SHADES
            Slot.EYES, // CLOWN_EYES_BLUE
            Slot.EYES, // CLOWN_EYES_GREEN
            Slot.EYES, // EYE_MASK
            Slot.EYES, // EYE_PATCH
            Slot.EYES, // GREEN_EYE_SHADOW
            Slot.EYES, // HORNED_RIM_GLASSES
            Slot.EYES, // NERD_GLASSES
            Slot.EYES, // PURPLE_EYE_SHADOW
            Slot.EYES, // REGULAR_SHADES
            Slot.EYES, // SMALL_SHADES
            Slot.EYES, // THREE_D_GLASSES
            Slot.EYES, // VR
            Slot.EYES, // WELDING_GOGGLES
            Slot.FACE, // MOLE
            Slot.FACE, // ROSY_CHEEKS
            Slot.FACE, // SPOTS
            Slot.FACE, // VAMPIRE_HAIR
            Slot.FACIAL_HAIR, // BIG_BEARD
            Slot.FACIAL_HAIR, // CHINSTRAP
            Slot.FACIAL_HAIR, // FRONT_BEARD
            Slot.FACIAL_HAIR, // FRONT_BEARD_DARK
            Slot.FACIAL_HAIR, // GOAT
            Slot.FACIAL_HAIR, // HANDLEBARS
            Slot.FACIAL_HAIR, // LUXURIOUS_BEARD
            Slot.FACIAL_HAIR, // MUSTACHE
            Slot.FACIAL_HAIR, // MUTTONCHOPS
            Slot.FACIAL_HAIR, // NORMAL_BEARD
            Slot.FACIAL_HAIR, // NORMAL_BEARD_BLACK
            Slot.FACIAL_HAIR, // SHADOW_BEARD
            Slot.HEAD, // BANDANA
            Slot.HEAD, // BEANIE
            Slot.HEAD, // BLONDE_BOB
            Slot.HEAD, // BLONDE_SHORT
            Slot.HEAD, // CAP
            Slot.HEAD, // CAP_FORWARD
            Slot.HEAD, // CLOWN_HAIR_GREEN
            Slot.HEAD, // COWBOY_HAT
            Slot.HEAD, // CRAZY_HAIR
            Slot.HEAD, // DARK_HAIR
            Slot.HEAD, // DO_RAG
            Slot.HEAD, // FEDORA
            Slot.HEAD, // FRUMPY_HAIR
            Slot.HEAD, // HALF_SHAVED
            Slot.HEAD, // HEADBAND
            Slot.HEAD, // HOODIE
            Slot.HEAD, // KNITTED_CAP
            Slot.HEAD, // MESSY_HAIR
            Slot.HEAD, // MOHAWK
            Slot.HEAD, // MOHAWK_DARK
            Slot.HEAD, // MOHAWK_THIN
            Slot.HEAD, // ORANGE_SIDE
            Slot.HEAD, // PEAK_SPIKE
            Slot.HEAD, // PIGTAILS
            Slot.HEAD, // PILOT_HELMET
            Slot.HEAD, // PINK_WITH_HAT
            Slot.HEAD, // POLICE_CAP
            Slot.HEAD, // PURPLE_HAIR
            Slot.HEAD, // RED_MOHAWK
            Slot.HEAD, // SHAVED_HEAD
            Slot.HEAD, // STRAIGHT_HAIR
            Slot.HEAD, // STRAIGHT_HAIR_BLONDE
            Slot.HEAD, // STRAIGHT_HAIR_DARK
            Slot.HEAD, // STRINGY_HAIR
            Slot.HEAD, // TASSLE_HAT
            Slot.HEAD, // TIARA
            Slot.HEAD, // TOP_HAT
            Slot.HEAD, // WILD_BLONDE
            Slot.HEAD, // WILD_HAIR
            Slot.HEAD, // WILD_WHITE_HAIR
            Slot.MOUTH, // BLACK_LIPSTICK
            Slot.MOUTH, // BUCK_TEETH
            Slot.MOUTH, // FROWN
            Slot.MOUTH, // HOT_LIPSTICK
            Slot.MOUTH, // MEDICAL_MASK
            Slot.MOUTH, // PURPLE_LIPSTICK
            Slot.MOUTH, // SMILE
            Slot.NECK, // CHOKER
            Slot.NECK, // GOLD_CHAIN
            Slot.NECK, // SILVER_CHAIN
            Slot.NOSE, // CLOWN_NOSE
            Slot.SIZE, // LARGE
            Slot.SIZE, // PETITE
            Slot.SMOKE, // CIGARETTE
            Slot.SMOKE, // PIPE
            Slot.SMOKE, // VAPE
            Slot.SPECIES, // ALIEN
            Slot.SPECIES, // APE
            Slot.SPECIES, // HUMAN
            Slot.SPECIES // ZOMBIE
        ];
        return uint8(traitsToSlots[traitId]);
    }
}
    