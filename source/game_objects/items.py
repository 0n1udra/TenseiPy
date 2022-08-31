from base_objects.item import Item

# ========== Materials ==========
class Water(Item):
    name = 'Water'
    item_type = 'Material'
    quantity_add = 100
    inv_capacity_add = 0.01
    usage = 'Can be used in high pressure attacks.'
    description = '''It's wet, and it's clear, it is just water...'''
    appearance = "Clear flowing liquid, oh, and it's wet too!"

class Hipokte_Grass(Item):
    name = 'Hipokte Grass'
    item_type = 'Material'
    quantity_add = 50
    inv_capacity_add = 0.01
    usage = 'Mainly used for making healing potions.'
    description = 'Magicule infused grass, found in locations with high Magicule concentration'
    appearance = 'Looks like regular grass, but gives off small amounts of magic essence.'
    ingredient_for = ['Full Potion']

class Magic_Ore(Item):
    name = 'Magic Ore'
    item_type = 'Material'
    quantity_add = 25
    inv_capacity_add = 0.1
    usage = 'Mainly used for making magic items and magic reinforced weapons and armor.'
    description = '''Magic ores form around high concentration of magic essence.
        Magic ore is the raw form of magic steel. Even in its unrefined form, magic ore is considered to be valuable.'''
    appearance = 'A very colorful ore. Almost like a glowing shimmering rainbow effect, while giving off some magic essence.'

class Full_Potion(Item):
    name = 'Full Potion'
    item_type = 'Consumable'
    quantity_add = 25
    inv_capacity_add = 0.1
    usage = 'Heals major wounds even severed limbs and illnesses. However, can not resurrect.'
    description = '''Can heal subject to optimum condition, but cannot revive the dead.'''
    appearance = 'Blue potion in a glass bottle.'
    # One Hipokte Grass makes 10 potions.
    recipe = {'Hipokte Grass': 1}


# ========== Weapons ==========
class Magic_Sword(Item):
    name = "Magic Sword"
    item_type = 'Weapon'
    damage_type = 'Melee'
    damage_level = 6
    description = """If a huge amount of magic essence was included in the raw materials of a sword, apparently it would become a sword that grows. 
        Infusing magic into a sword, though you'd expect it to be a common technique, it's actually really difficult."""
    appearance = """Although they are usually made using a simple design, they are perfectly straight.
        It could be said that there are no unnecessary parts to them.
        It isn't meant for pure cutting, but still capable of slashing attacks.
        The goal of this design is to use this simplicity as a base to make it easier to realize an individual's respective ideal form.
        
        Another special characteristic of magic swords is that the blade will never rust or become chipped.
        The sword also has a life of its own.
        If it became completely broken or bent, then the magic essence would bleed out and dissipate all at once."""
