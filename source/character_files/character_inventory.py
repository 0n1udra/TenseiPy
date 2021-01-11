class Inventory:
    def inventory_generator(self, output=False):
        """
        Yields all items in character's inventory (Currently only Rimuru).

        Args:
            output: Yields a friendly string for printing in game purposes.

        Usage:
            .inventory_generator(output=True)
        """

        # Generator responsible for getting printout data when using show_attribute.
        for item_type, items in self.inventory.items():

            # Yields item type if formatting for output to player.
            if output and items:
                yield f'[{item_type}]'

            for item_name, item_object in items.items():
                if output:
                    item_text = f'    {item_object.inventory_capacity_add * item_object.quantity:.1f}% - {self.inventory[item_type][item_name].quantity}x {item_object.name}'
                    if item_object.status:
                        yield item_text + f' ({item_object.status})'
                    else:
                        yield item_text
                else:
                    yield item_object

    def show_inventory(self, *args):
        """
        Prints out inventory items, corresponding category, and capacity.

        Usage:
            .show('gobta')

            > inv
        """

        print('\n-----Inventory-----')
        print(f'Capacity: {self.inventory_capacity:.1f}%\n')
        for i in self.inventory_generator(output=True): print(i)
        print()

    def add_inventory(self, item, amount=1):
        """
        Adds item to character (currently only Rimuru) inventory.

        Args:
            item: Item to add to inventory.
            amount: Amount of specified item to add to inventory. If not specified, will use item's .add_amount value.

        Usage:
            .add_inventory('hipokte grass')
        """

        # Adds new item to inventory if not already exists.
        item_object = self.check_acquired(item)

        if not item_object:
            try:
                if item.name:
                    item_object = item
                    self.inventory[item_object.item_type][item_object.name] = item_object
            except:
                if item_object := self.get_object(item, new=True):
                    self.inventory[item_object.item_type][item_object.name] = item_object
                    print(f'\n    << Analysis on [{item_object.name}] Complete. >>')
                else:
                    return False

        # Adds to total inventory capacity %.
        self.inventory_capacity += item_object.inventory_capacity_add * item_object.quantity_add
        # Adds to quantity variable residing in item's object which is saved in character's inventory dict.
        self.inventory[item_object.item_type][item_object.name].quantity += amount * item_object.quantity_add

        print(f'\n    < Acquired: {amount * item_object.quantity_add}x [{item_object.name}] >\n')

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

        item.quantity -= amount
        if item.quantity < 0:
            del self.inventory[item.item_type]

        print(f"\n    < Removed: {amount}x [{item.name}] >\n")

    def craft_item(self, item):
        """
        Craft item if have necessary material.

        Use 'craft' command in game to craft items. It will ask how many you want to make.
        Will check if user has needed ingredients to craft item.

        Args:
            item: Item to craft.

        Usage:
            > craft full potion
        """

        item = self.get_object(item, new=True)
        if item is None: return

        # Shows recipe.
        recipe = ''
        print(f"Recipe for {item.quantity_add}x:")
        for ingredient, amount in item.recipe.items():
            recipe += F"{amount}x {ingredient}, "
        print(f"{recipe[:-2]}")  # [:-2] cuts off last comma and space
        print(f"\nInputting 1 will create {item.quantity_add}. 0 will cancel crafting.")

        # Asks for how much to make. note that some items are crafted in batches.
        try:
            craft_amount = int(input(f"> "))
        except ValueError:
            print("\n    < Error, need integer input. >\n")
            return False

        # Checks if have enough ingredients.
        for ingredient_name, ingredient_amount in item.recipe.items():
            if ingredient := self.check_acquired(ingredient_name):
                if ingredient.quantity > ingredient_amount * craft_amount:
                    continue
            else:
                print("\n    < Missing Ingredient(s) >")
                return False

        # Use up ingredients then add to inventory
        for ingredient_name, ingredient_amount in item.recipe.items():
            self.remove_inventory(ingredient_name, ingredient_amount * craft_amount)
        self.add_inventory(item, craft_amount)
        print()
