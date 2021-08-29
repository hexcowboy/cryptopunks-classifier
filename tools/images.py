import os
from PIL import Image
from typing import List

# There are 10,000 punks
punks_count: range = range(10_000)

# Dimensions of one punk is 24x24
punks_sprite_width: int = 24
punks_sprite_height: int = 24

# Dimensions of spritesheet is 100x100
punks_spritesheet_width: range = range(100)
punks_spritesheet_height: range = range(100)

# Load the punk image as an object
punks_spritesheet: Image = Image.open("../punks.png")

# Individual punk sprites as images
punks_sprites: List = list(punks_count)

# Iterate over sprites and populate `punks_sprites`
for x in punks_spritesheet_width:
    for y in punks_spritesheet_height:
        # Exact pixel coordinates for the specific sprite
        left: int = x * punks_sprite_width
        upper: int = y * punks_sprite_height
        right: int = left + punks_sprite_width
        lower: int = upper + punks_sprite_height

        # Calculate the current index of the spritesheet
        index = (x * len(punks_spritesheet_width)) + y

        # Populate the sprite by cropping at the pixels from above
        punks_sprites[index] = punks_spritesheet.crop((left, upper, right, lower))

# Create the output directory
if not os.path.exists("../punks"):
    os.makedirs("../punks")

# Save punks to PNG files
for sprite_index in range(len(punks_sprites)):
    try:
        outpath = f"../punks/punk{sprite_index}.png"
        punks_sprites[sprite_index].save(outpath, "PNG")
        print(f"Saved Punk #{sprite_index} to {outpath}")
    except AttributeError:
        print(f"Error at punk index {sprite_index}.")
        exit(0)
