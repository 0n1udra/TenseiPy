class Item:
    def __init__(self):
        self.name = ''
        self.itemType = ''
        self.description = ''

    def description(self):
        return(self.description)

    def __str__(self):
        return(self.name)




class Grass_Item(Item):
    def __init__(self):
        Item.__init__(self)
        self.name = 'Magicule Grass'
        self.itemType = 'Material'

        self.description = "Magicule infused grass, found in Valdora's cave"
