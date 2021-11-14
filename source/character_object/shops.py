from character_object.object import Base
from character_object.inventory import Inventory
from game_files.output import gprint

class Shop(Base, Inventory):
    name = ''
    description = ''
    initialized = False
    game_object_type = 'shop'

    def __init__(self):
        self.inventory = {'Item': {}, 'Material': {}, 'Consumable': {}, 'Mob': {}, 'Weapon': {}, 'Misc': {}}
        self.services = []
        self.balance = 50


    def store_page(self):
        self.show_inventory()

    def item_info(self, item):
        print(self.info_page)

    def buy(self, item, amount):
        pass

    def sell(self, item, amount):
        pass


