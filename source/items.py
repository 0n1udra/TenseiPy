class Item:
    def __init__(self):
        self.name = ''
        self.item_type = ''
        self.amount = 0
        self.predator_add_amount = 1 # Amount to add when calling add()
        self.description = ''
        self.inventory_add_amount = 0
        self.description = ''

        self.game_object_type = 'item'

    def get_description(self):
        return self.description

    def acquired_msg(self):
        return f'<Acquired {self.predator_add_amount} {self.name}'
        # add function will append ' | Total : x'

    def update_info(self):
        self.info = f'''
    Name: {self.name}
    
    Usage:
        {self.usage}

    Appearance:
        {self.appearance}
    '''

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name.lower()


# ========== Materials ==========
class Hipokte_Grass(Item):
    def __init__(self):
        Item.__init__(self)
        self.name = 'Hipokte Grass'
        self.item_type = 'Material'
        self.predator_add_amount = 5
        self.amount = 0
        self.inventory_add_amount = 0.01
        self.usage = 'Mainly used for making healing potions.'
        self.description = 'Magicule infused grass, found in locations with high Magicule concentration'
        self.appearance = 'Looks like regular grass, but gives off small amounts of magic essence.'
        self.Data.update_info()


class Magic_Ore(Item):
    def __init__(self):
        Item.__init__(self)
        self.name = 'Magic Ore'
        self.item_type = 'Material'
        self.predator_add_amount = 5
        self.amount = 0
        self.inventory_add_amount = 0.1
        self.usage = 'Mainly used for making magic items and magic reinforced weapons and armor.'
        self.description = '''
        Magic ores form around high concentration of magic essence.
        Magic ore is the raw form of magic steel. Even in its unrefined form, magic ore is considered to be valuable.
        '''
        self.appearance = 'A very colorful ore. Almost like a glowing shimmering rainbow effect, while giving off some magic essence.'
        self.Data.update_info()
        
