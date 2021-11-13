from character_object.object import Base
from character_object.inventory import Inventory
from game_files.output import gprint

class Shops(Base, Inventory):
    def __init__(self):
        self.inventory = {'Item': {}, 'Material': {}, 'Consumable': {}, 'Mob': {}, 'Weapon': {}, 'Misc': {}}
        self.services = []
        self.balance = 50


    def store_page(self):
        print()

    def item_info(self, item):
        print()

    def buy(self, item, amount):
        pass

    def sell(self, item, amount):
        pass


