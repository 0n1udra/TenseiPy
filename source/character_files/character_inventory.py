class Inventory:
    def inventory_generator(self, character=None, output=False):
        """
        Yields all items in character's inventory (Currently only Rimuru).

        Args:
            character: Character to yield inventory items from.
            output: Yields a friendly string for printing in game purposes.

        Usage:
            .inventory_generator(output=True)
        """

        if not character: character = self

        # Generator responsible for getting printout data when using show_attribute.
        for item_type, items in character.inventory.items():
            if output and items:
                # If output=True yields out item_type to printout.
                yield f'[{item_type}]'

            for item_name, item_object in items.items():
                if output:
                    yield f'    {self.inventory[item_type][item_name].quantity}x {item_object.name}'
                else: yield item_object

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
            print(i)
        print()

    def add_inventory(self, item, amount=None, print_analysis_message=False):
        """
        Adds item to character (currently only Rimuru) inventory.

        Args:
            item: Item to add to inventory.
            amount: Amount of specified item to add to inventory. If not specified, will use item's .add_amount value.
            print_analysis_message: Prints analysis complete message.

        Usage:
            .add_inventory('hipokte grass')
        """

        item = self.get_object(item, new=True)

        # Adds new item to inventory if not already exists.
        if not self.check_acquired(item):
            self.inventory[item.item_type][item.name] = item
            print_analysis_message = True

        # Uses item's amount_add to add items in batches.
        if amount:
            self.inventory[item.item_type][item.name].quantity += amount * item.quantity_add
            print(f'    < Acquired {amount * item.quantity_add}x [{item.name}]. >\n')
        else:
            self.inventory[item.item_type][item.name].quantity += item.quantity_add
            item.show_acquired_msg()

        self.inventory_capacity += item.inventory_capacity_add

        if print_analysis_message:
            print(f'    << Analysis on [{item.name}] successful. >>\n')

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

    def craft_item(self, item, craft_amount=1):
        """
        Craft item if have necessary material.

        Use 'craft' command in game to craft items. It will ask how many you want to make.
        Will check if user has needed ingredients to craft item.

        Args:
            item: Item to craft.
            craft_amount: How many to craft.

        Usage:
            > craft full potion
        """

        item = self.get_object(item, new=True)
        if not item: return

        recipe = ''
        for ingredient, amount in item.recipe.items():
            recipe += F"{amount}x {ingredient}, "
        print(f"{item.quantity_add}x {item.name}: {recipe[:-2]}")

        # Asks for how much to make. note that some items are crafted in batches.
        try:
            craft_amount = int(input("Amount (0 to cancel) > "))
        except ValueError:
            print("    < Error, need integer input. >")
            return

        if not craft_amount: return

        for ingredient_name, ingredient_amount in item.recipe.items():
            if self.check_acquired(ingredient_name, ingredient_amount * craft_amount):
                print("    < Not enough materials to craft item. >")
                return

        # Use ingredients to make the item.
        for ingredient_name, ingredient_amount in item.recipe.items():
            self.remove_inventory(ingredient_name, ingredient_amount * craft_amount)

        self.add_inventory(item, craft_amount)
