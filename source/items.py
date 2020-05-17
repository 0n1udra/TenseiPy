class Item:
    def __init__(self):
        self.name = ''
        self.itemType = ''
        self.description = ''

    def ItemDescription(self):
        return(self.description)

    def AcquiredMsg(self):
        return(self.acquiredMsg)

    def __str__(self):
        return(self.name)


# ========== Materials ==========
class Hipokte_Grass(Item):
    def __init__(self):
        Item.__init__(self)
        self.name = 'Hipokte Grass'
        self.itemType = 'Material'

        self.info = "\tMagicule infused grass, found in locations with high Magicule concentration"
        self.acquiredMsg = '<Hipotke Grass acquired>'
