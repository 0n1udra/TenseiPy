def ssprint(Msg):
    print(f'    {Msg}\n')


class Inventory:
    def __init__(self):
        self.inventory_capacity = 0
        self.inventory_add_capacity = 0
        self.inventory = {
            'Items': {},
            'Material': {},
            'Potions': {},
            'Misc': {}
        }

    def inventory_generator(self, output=False):
        """
        Yields all items in character's inventory (Currently only Rimuru).

        Args:
            output: Yields a friendly string for printing in game purposes.

        Usage:
            .inventory_generator(output=True)
        """
        for item_type, items in self.inventory.items():
            if output and items:
                yield f'{item_type}:'  # If output=True prints out item_type also

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
        print(f'Capacity: {self.inventory_capacity:.2f}%\n')
        for i in self.inventory_generator(output=True):
            print(i)  # Prints out inventory items

    def add_inventory(self, item):
        """
        Adds item to character (currently only Rimuru) inventory.

        Args:
            item: Item to add to inventory.

        Usage:
            .add_inventory('hipokte grass')
        """

        item = self.get_object(item, new=True)

        if self.check_mob_has(item):
            self.inventory[item.item_type][item.name].amount += item.inventory_add_capacity
            self.inventory_capacity += item.inventory_add_capacity
            item.show_acquired_msg()
        else:
            self.inventory[item.item_type][item.name] = item
            self.inventory[item.item_type][item.name].amount += item.inventory_add_capacity
            ssprint(f'<<Analysis on {item.name} successful.>>')

            self.inventory_capacity += item.inventory_add_capacity

    def remove_inventory(self, item):
        """
        Remove item from inventory (Currently only Rimuru).

        Args:
            item: Item to remove from inventory.

        Usage:
            .remove('hipokte grass')
        """

        try:
            self.inventory[item.item_type].remove(item)
        except:
            ssprint('<Failed removing item from inventory.>')
