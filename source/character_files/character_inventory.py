class Inventory:
    def __init__(self):
        self.capacity = 0
        self.capacity_add = 0
        self.amount = 0
        self.amount_add = 1
        self.inventory = {
            'Items': {},
            'Materials': {},
            'Potions': {},
            'Misc': {}
        }

    def inventory_generator(self, character=None, output=False):
        """
        Yields all items in character's inventory (Currently only Rimuru).

        Args:
            output: Yields a friendly string for printing in game purposes.

        Usage:
            .inventory_generator(output=True)
        """

        if not character:
            character = self

        for item_type, items in character.inventory.items():
            if output and items:
                # If output=True prints out item_type also
                yield f'[{item_type}]'

            for item_name, item_object in items.items():
                if output:
                    yield f'\t{self.inventory[item_type][item_name].amount}x {item_object.name}'
                else:
                    yield item_object

    def show_inventory(self, character=None):
        """
        Prints out inventory items, corresponding category, and capacity.

        Args:
            character: Specify which character's inventory to show.

        Usage:
            .show('gobta')

            > inv
        """

        print('\n-----Inventory-----')
        print(f'Capacity: {self.capacity:.2f}%\n')
        for i in self.inventory_generator(output=True):
            print(i)
        print()

    def add_inventory(self, item):
        """
        Adds item to character (currently only Rimuru) inventory.

        Args:
            item: Item to add to inventory.

        Usage:
            .add_inventory('hipokte grass')
        """

        item = self.get_object(item, new=True)

        item.show_acquired_msg()

        if not self.check_acquired(item):
            self.inventory[item.item_type][item.name] = item
            print(f'    << Analysis on [{item.name}] successful. >>\n')

        self.inventory[item.item_type][item.name].amount += item.amount_add
        self.capacity += item.capacity_add

    def remove_inventory(self, item, amount=1):
        """
        Remove item from inventory (Currently only Rimuru).

        Args:
            item: Item to remove from inventory.
            amount: How many to remove from inventory.

        Usage:
            .remove('hipokte grass')
            .remove('magic ore', 5)
        """

        item = self.get_object(item)

        if item.amount <= 1:
            self.inventory[item.item_type].remove(item)
        else:
            item.amount -= amount

    def craft_item(self, item, amount):

        item = self.get_object(item, new=True)

        for ingredient_name, ingredient_amount in item.recipe.items():
            if self.check_acquired(ingredient_name, ingredient_amount * amount):
                





