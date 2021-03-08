from game_files.extra import format_info

class Item:
    def __init__(self):
        self.name = ''
        self.status = ''
        self.item_type = ''
        self.damage_type = ''
        self.damage_level = None
        self.quantity = 0
        self.quantity_add = 1
        self.inventory_capacity_add = 0.1
        self.info_page = 'N/A'
        self.description = ''
        self.usage = ''
        self.appearance = ''
        self.recipe = {}
        self.ingredient_for = []
        self.game_object_type = 'item'

    def get_description(self):
        """
        Returns item description variable.

        Returns:
            Returns Item description.
        """

        return self.description

    def update_info(self):
        """ Updates item's info. """

        self.info_page = f'    Name: [{self.name}] {"(" + self.status + ")" if self.status else ""}\n'

        info_dict = {'Item Type': self.item_type, 'Damage Type': self.damage_type, 'Damage Level': self.damage_level,
                     '*Description': self.description, '*Appearance': self.appearance, '*Usage': self.usage}
        for k, v in info_dict.items():
            if formatted_info := format_info(k, v):
                self.info_page += f"    {formatted_info}\n"

        if self.ingredient_for:
            self.info_page += "\n    Ingredient for:\n"

            for item in self.ingredient_for:
                self.info_page += f'        [{item}], '
            self.info_page = self.info_page[:-2] + '\n'

        if self.recipe:
            self.info_page += f'\n    Recipe:\n        Will craft {self.quantity_add} at a time.\n'

            for item, amount in self.recipe.items():
                self.info_page += f'        {amount}x [{item}]\n'

    def get_name(self):
        """
        Returns item's name variable.

        Returns:
            Returns item lower() item name
        """

        return self.name.lower()

    def __str__(self): return self.name.lower()


# ========== Materials ==========
class Water(Item):
    def __init__(self):
        Item.__init__(self)
        self.name = 'Water'
        self.item_type = 'Material'
        self.quantity_add = 100
        self.inventory_capacity_add = 0.01
        self.usage = 'Can be used in high pressure attacks.'
        self.description = '''It's wet, and it's clear, it is just water...'''
        self.appearance = 'Clear flowing liquid.'
        self.update_info()

class Hipokte_Grass(Item):
    def __init__(self):
        Item.__init__(self)
        self.name = 'Hipokte Grass'
        self.item_type = 'Material'
        self.quantity_add = 50
        self.inventory_capacity_add = 0.01
        self.usage = 'Mainly used for making healing potions.'
        self.description = 'Magicule infused grass, found in locations with high Magicule concentration'
        self.appearance = 'Looks like regular grass, but gives off small amounts of magic essence.'
        self.ingredient_for = ['Full Potion']
        self.update_info()

class Magic_Ore(Item):
    def __init__(self):
        Item.__init__(self)
        self.name = 'Magic Ore'
        self.item_type = 'Material'
        self.quantity_add = 25
        self.inventory_capacity_add = 0.1
        self.usage = 'Mainly used for making magic items and magic reinforced weapons and armor.'
        self.description = '''Magic ores form around high concentration of magic essence.
        Magic ore is the raw form of magic steel. Even in its unrefined form, magic ore is considered to be valuable.
        '''
        self.appearance = 'A very colorful ore. Almost like a glowing shimmering rainbow effect, while giving off some magic essence.'
        self.update_info()

class Full_Potion(Item):
    def __init__(self):
        Item.__init__(self)
        self.name = 'Full Potion'
        self.item_type = 'Consumable'
        self.quantity_add = 25
        self.inventory_capacity_add = 0.1
        self.usage = 'Heals major wounds even severed limbs and illnesses. However, can not resurrect.'
        self.description = '''Can heal subject to optimum condition, but cannot revive the dead.'''
        self.appearance = 'Blue potion in a glass bottle.'
        # One Hipokte Grass makes 10 potions.
        self.recipe = {'Hipokte Grass': 1}
        self.update_info()

# ========== Weapons ==========
class Magic_Sword(Item):
    def __init__(self):
        Item.__init__(self)
        self.name = "Magic Sword"
        self.item_type = 'Weapon'
        self.damage_type = 'Melee'
        self.damage_level = 6
        self.description = """If a huge amount of magic essence was included in the raw materials of a sword, apparently it would become a sword that grows. 
        Infusing magic into a sword, though you'd expect it to be a common technique, it's actually really difficult.
        """
        self.appearance = """Although they are usually made using a simple design, they are perfectly straight.
        It could be said that there are no unnecessary parts to them.
        It isn't meant for pure cutting, but still capable of slashing attacks.
        The goal of this design is to use this simplicity as a base to make it easier to realize an individual's respective ideal form.
        
        Another special characteristic of magic swords is that the blade will never rust or become chipped.
        The sword also has a life of its own.
        If it became completely broken or bent, then the magic essence would bleed out and dissipate all at once.
        """
        self.update_info()



