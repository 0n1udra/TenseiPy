from game_objects.object import Base
from game_objects.inventory import Inventory
from game_files.output import gprint

class Vendor(Base, Inventory):
    name = ''
    balance = 50
    services = []
    description = ''
    initialized = False
    object_type = 'shop'
    starting_state = []

    def __init__(self, *args):
        self.inventory = {'Item': {}, 'Material': {}, 'Consumable': {}, 'Mob': {}, 'Weapon': {}, 'Misc': {}}

    def vendor_info(self):
        self.show_inventory()

    def item_info(self, item):
        print(self.info_page)

    def item_buy(self, item, amount):
        pass

    def item_sell(self, item, amount):
        pass


