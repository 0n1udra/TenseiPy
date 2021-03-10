class Inventory:
    def inventory_generator(self, output=False):
        """
        Yields all items in character's inventory.

        Args:
            output bool(False): Yields a friendly string for printing in game purposes.

        Usage:
            .inventory_generator(output=True)
        """

        # Generator is also responsible for getting printout data when using show_attribute.
        for item_type, items in self.inventory.items():

            # Yields item type if formatting for output to player.
            if output and items:
                yield f'[{item_type}]'

            for item_name, item_object in items.items():
                if output:
                    item_text = f'    {item_object.inventory_capacity_add * item_object.quantity:.1f}% - {self.inventory[item_type][item_name].quantity}x {item_object.name}'
                    if item_object.status:  # if has a custom status set.
                        yield item_text + f' ({item_object.status})'
                    else:
                        yield item_text  # Text to be shown for gameplay.
                else:
                    yield item_object  # Object to be used by code.

    def update_inventory_capacity(self):
        """Updates inventory_capacity variable by going through all items in inventory and adding them up."""

        total = 0
        for item in self.inventory_generator():
            total += item.quantity * item.inventory_capacity_add
        self.inventory_capacity = total

        return total

    def show_inventory(self, *args):
        """
        Prints out inventory items, corresponding category, and capacity.

        Usage:
            .show_inventory('gobta')

            > inv
        """

        print('----- Inventory -----')
        print(f'Capacity: {self.inventory_capacity:.1f}%\n')
        for i in self.inventory_generator(output=True):
            print(i)

    def add_inventory(self, item_object, amount=1, show_acquired_msg=True, show_analysis_msg=None):
        """
        Adds item to character (currently only Rimuru) inventory.

        Args:
            item_object str, obj: Item to add to inventory.
            amount int(None): Amount of specified item to add to inventory. If not specified, will use item's .add_amount value.
            show_msg bool(True): Hide acquired and/or analyzed message.
            show_analysis_msg bool(None): Show/Hide analyzed message.
            bot_newline bool(True): Print newline at end.

        Usage:
            .add_inventory('hipokte grass')
        """

        # Check if passed in a string to find corresponding object or a game object iteself.
        if type(item_object) is str: item_object = self.get_object(item_object, new=True)

        if not item_object: return False  # Does not have game object to add to inventory.

        if self.check_acquired(item_object):
            self.inventory[item_object.item_type][item_object.name].quantity += amount * item_object.quantity_add
        else:
            if not item_object.initialized:
                item_object = item_object()
            self.inventory[item_object.item_type][item_object.name] = item_object
            self.inventory[item_object.item_type][item_object.name].quantity += amount * item_object.quantity_add
            if show_analysis_msg is None:
                show_analysis_msg = True

        self.update_inventory_capacity()

        if show_acquired_msg:
            print(f'    < Acquired: {amount * item_object.quantity_add}x [{item_object.name}] >')
        if show_analysis_msg:
            print(f'    << Analysis on [{item_object.name}] Complete. >>')

    def remove_inventory(self, item, amount=1):
        """
        Remove item from inventory (Currently only Rimuru).

        Args:
            item str: Item to remove from inventory.
            amount int(1): How many to remove from inventory. -1 to remove all.

        Usage:
            .remove_inventory('hipokte grass')
            .remove_inventory('magic ore', 5)
            .remove_inventory('water' -1)
        """

        item = self.get_object(item)
        if not item: return

        if item.quantity <= 0 or amount <= 0:
            del self.inventory[item.item_type][item.name]
            print(f"    < Removed Item: [{item.name}] >")
        else:
            item.quantity -= amount
            print(f"    < Removed: {amount}x [{item.name}] >")

        self.update_inventory_capacity()

    def craft_item(self, args):
        """
        Craft item if have necessary material.

        Use 'craft' command in game to craft items. It will ask how many you want to make.
        Will check if user has needed ingredients to craft item.

        Args:
            arg str: Item to craft and amount.

        Usage:
            > craft full potion
            > craft full potion 10
        """

        # Gets craft amount and item name from passed in input.
        try:
            craft_amount = int(args.split(' ')[-1])
            item = ' '.join((args.split(' ')[:-1]))
        except:
            craft_amount = None
            item = args

        item = self.get_object(item, new=True)
        if item is None: return

        # You can craft an item with specific amount with 'craft full potion 2', or 'craft full potion' then specify amount.
        if craft_amount is None:
            # Shows recipe.
            recipe = ''
            print(f"    Recipe for {item.quantity_add}x {item.name}:")
            for ingredient, amount in item.recipe.items():
                recipe += F"        {amount}x {ingredient}, "
            # [:-2] will cuts off last comma and space.
            print(f"{recipe[:-2]}\n    Inputting 1 will craft {item.quantity_add}. 0 will cancel crafting.\n")

            # Asks for how much to make. note that some items are crafted in batches.
            try:
                craft_amount = int(input("Craft > "))
                print()
            except ValueError:
                print("\n    < Error: need integer input >")
                return False

        # Checks if have all the ingredients.
        for ingredient_name, ingredient_amount in item.recipe.items():
            if self.check_acquired(ingredient_name, ingredient_amount * craft_amount):
                continue

            print("    < Missing Ingredient(s) >")
            return False

        # Use up ingredients then add to inventory
        for ingredient_name, ingredient_amount in item.recipe.items():
            self.remove_inventory(ingredient_name, ingredient_amount * craft_amount)

        print()
        self.add_inventory(item, craft_amount)
