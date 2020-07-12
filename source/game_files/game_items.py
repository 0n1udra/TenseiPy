class Item:
    def __init__(self):
        self.name = ''
        self.item_type = ''
        self.amount = 0
        self.amount_add = 1
        self.capacity_add = 0
        self.info = 'N/A'
        self.description = ''
        self.usage = ''
        self.appearance = ''
        self.game_object_type = 'item'

    def get_description(self):
        """
        Returns item description variable.

        Returns:
            Returns Item description.
        """

        return self.description

    def show_acquired_msg(self):
        """Print item's acquired message."""

        print(f'    <Acquired {self.amount_add}x [{self.name}].>\n')

    def update_info(self):
        """Updates item's info."""

        self.info = f'''
    Name: {self.name}
    
    Usage:
        {self.usage}

    Appearance:
        {self.appearance}
    '''

    def get_name(self):
        """
        Returns item's name variable.

        Returns:
            Returns item lower() item name
        """

        return self.name.lower()


# ========== Materials ==========
class Hipokte_Grass(Item):
    def __init__(self):
        Item.__init__(self)
        self.name = 'Hipokte Grass'
        self.item_type = 'Materials'
        self.amount = 0
        self.amount_add = 5
        self.capacity_add = 0.01
        self.usage = 'Mainly used for making healing potions.'
        self.description = 'Magicule infused grass, found in locations with high Magicule concentration'
        self.appearance = 'Looks like regular grass, but gives off small amounts of magic essence.'
        self.update_info()


class Magic_Ore(Item):
    def __init__(self):
        Item.__init__(self)
        self.name = 'Magic Ore'
        self.item_type = 'Materials'
        self.amount_add = 5
        self.amount = 0
        self.capacity_add = 0.1
        self.usage = 'Mainly used for making magic items and magic reinforced weapons and armor.'
        self.description = '''
        Magic ores form around high concentration of magic essence.
        Magic ore is the raw form of magic steel. Even in its unrefined form, magic ore is considered to be valuable.
        '''
        self.appearance = 'A very colorful ore. Almost like a glowing shimmering rainbow effect, while giving off some magic essence.'
        self.update_info()
