class Item:
    def __init__(self):
        self.name = ''
        self.itemType = ''
        self.amount = 0
        self.addAmount = 1 # Amount to add when calling AddInventory()
        self.capacity = 0
        self.description = ''

    def ItemDescription(self):
        return(self.description)

    def AcquiredMsg(self):
        return(f'<Acquired {self.addAmount} {self.name}')
        # AddInventory function will append ' | Total : x'

    def __str__(self):
        return(self.name)


# ========== Materials ==========
class Hipokte_Grass(Item):
    def __init__(self):
        Item.__init__(self)
        self.name = 'Hipokte Grass'
        self.itemType = 'Material'
        self.addAmount = 5
        self.amount = 0
        self.capacity = 0.01
        self.info = """
    Description:
        Magicule infused grass, found in locations with high Magicule concentration.

    Usage:
        Mainly used for making healing potions.

"""



class Magic_Ore(Item):
    def __init__(self):
        Item.__init__(self)
        self.name = 'Magic Ore'
        self.itemType = 'Material'
        self.addAmount = 5
        self.amount = 0
        self.capacity = 0.1
        self.info = """
    Description:
        Magic ores form around high concentration of magic essence.
        Magic ore is the raw form of magic steel. Even in its unrefined form, magic ore is considered to be valuable.

    Usage:
        Mainly used for making magic items and magic reinforced weapons and armor.
    """
        
