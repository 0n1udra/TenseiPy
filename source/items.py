class Item:
    def __init__(self):
        self.name = ''
        self.itemType = ''
        self.amount = 0
        self.addAmount = 1 # Amount to add when calling add_inventory()
        self.description = ''
        self.capacityUse = 0
        self.description = ''

        self.objectType = 'item'

    def ItemDescription(self):
        return self.description

    def AcquiredMsg(self):
        return f'<Acquired {self.addAmount} {self.name}'
        # add_inventory function will append ' | Total : x'

    def UpdateInfo(self):
        self.info = f'''
    Name: {self.name}
    
    Usage:
        {self.usage}

    Appearance:
        {self.appearance}
    '''

    def __str__(self):
        return self.name

    def GetName(self):
        return self.name.lower()


# ========== Materials ==========
class Hipokte_Grass(Item):
    def __init__(self):
        Item.__init__(self)
        self.name = 'Hipokte Grass'
        self.itemType = 'Material'
        self.addAmount = 5
        self.amount = 0
        self.capacityUse = 0.01
        self.usage = 'Mainly used for making healing potions.'
        self.description = 'Magicule infused grass, found in locations with high Magicule concentration'
        self.appearance = 'Looks like regular grass, but gives off small amounts of magic essence.'
        self.UpdateInfo()


class Magic_Ore(Item):
    def __init__(self):
        Item.__init__(self)
        self.name = 'Magic Ore'
        self.itemType = 'Material'
        self.addAmount = 5
        self.amount = 0
        self.capacityUse = 0.1
        self.usage = 'Mainly used for making magic items and magic reinforced weapons and armor.'
        self.description = '''
        Magic ores form around high concentration of magic essence.
        Magic ore is the raw form of magic steel. Even in its unrefined form, magic ore is considered to be valuable.
        '''
        self.appearance = 'A very colorful ore. Almost like a glowing shimmering rainbow effect, while giving off some magic essence.'
        self.UpdateInfo()
        
