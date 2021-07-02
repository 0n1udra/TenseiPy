from game_files.output import gprint, print_header, parse_input

class Inventory:
    def inventory_generator(self, output=False):
        """
        Yields all items in character's inventory.

        Args:
            output bool(False): Yields a friendly string for printing in-game purposes.

        Usage:
            .inventory_generator(output=True)
        """

        # Generator is also responsible for getting printout data when using show_attribute.
        for item_type, items in self.inventory.items():

            # Yields item type if formatting for output to player.
            if output and items: yield f'    [{item_type}]'

            for item_name, item in items.items():
                if not output:
                    yield item
                    continue

                item_text = f'        {item.inv_capacity_add * item.quantity:.1f}% - {self.inventory[item_type][item_name].quantity}x {item.name}'
                if item.status:  # if has a custom status set.
                    yield item_text + f' ({item.status})'
                else: yield item_text  # Text to be shown for gameplay.

    def show_inventory(self, *args):
        """
        Prints out inventory items, corresponding category, and capacity.

        Usage:
            > inv
        """

        print_header('Inventory')
        print(f'    Capacity: {self.inventory_capacity:.1f}%\n')
        for i in self.inventory_generator(output=True): print(i)

    def update_inventory_capacity(self):
        """Updates inventory_capacity variable by going through all items in inventory and adding them up."""

        total = 0
        for item in self.inventory_generator():
            total += item.quantity * item.inv_capacity_add
        self.inventory_capacity = total

        return total

    def add_inventory(self, item, amount=1, show_acquired_msg=True, show_analysis_msg=None):
        """
        Adds item to character (currently only Rimuru) inventory.

        Args:
            item str, obj: Item to add to inventory.
            amount int(None): Amount of specified item to add to inventory. If not specified, will use item's .add_amount value.
            show_acquired_msg bool(True): Show item acquired message.
            show_analysis_msg bool(None): Show analysis complete message.

        Usage:
            .add_inventory('hipokte grass')
        """

        item = self.get_object(item, new=True)
        if not item: return False  # Does not have game object to add to inventory.

        if self.check_acquired(item):
            self.inventory[item.item_type][item.name].quantity += amount * item.quantity_add
        else:
            if not item.initialized: item = item()
            self.inventory[item.item_type][item.name] = item
            self.inventory[item.item_type][item.name].quantity += amount * item.quantity_add
            if show_analysis_msg is None: show_analysis_msg = True

        self.update_inventory_capacity()

        if show_acquired_msg: gprint(f'< Acquired: {amount * item.quantity_add}x [{item.name}] >')
        if show_analysis_msg: gprint(f'<< Analysis on [{item.name}] Complete. >>')
        return True

    def remove_inventory(self, item=None, amount=1):
        """
        Remove item from inventory.

        Args:
            item str: Item to remove from inventory.
            amount int(1): How many to remove from inventory. -1 to remove all.

        Usage:
            .remove_inventory('hipokte grass')
            .remove_inventory('magic ore', 5)
            .remove_inventory('water' -1)

            > remove hipokte grass
            > remove magic ore 5
            > remove water -1
        """

        # Parses item and amount from user input.
        try: item, amount = parse_input(item)
        except: pass
        if amount == 0: return False

        item = self.get_object(item)
        if not item: return False

        if (item.quantity - amount) <= 0 or amount <= 0:
            del self.inventory[item.item_type][item.name]
            gprint(f"< Removed Item: [{item.name}] >")
        else:
            item.quantity -= amount
            gprint(f"< Removed: {amount}x [{item.name}] >")

        self.update_inventory_capacity()
        return True

    def craft_item(self, args):
        """
        Craft item if have necessary material.

        In in-game command, if not specify amount, will show recipe than ask for amount.

        Args:
            arg str: User input, item to craft and amount.

        Usage:
            > craft full potion
            > craft full potion 10
        """

        try: item, craft_amount = parse_input(args)
        except:
            craft_amount = None
            item = args

        item = self.get_object(item, new=True)
        if item is None: return

        # 'craft full potion 2', or 'craft full potion' to show recipe then input amount.
        if craft_amount is None:
            # Shows recipe.
            recipe = ''
            print_header(f'Recipe for: [{item.name}]', 5)
            for ingredient, amount in item.recipe.items():
                recipe += F"{amount}x {ingredient}, "
            print(f"    {recipe[:-2]}")  # [:-2] will cuts off last comma and space.
            print(f"\n    Inputting 1 will craft {item.quantity_add}. 0 cancel.\n")

            # Asks for how much to make. note that some items are crafted in batches.
            try:
                craft_amount = int(input("Craft > "))
                print()
            except ValueError:
                gprint("\n< Error: need integer input >")
                return False

        if craft_amount <= 0: return False

        # Checks if have all the ingredients.
        for ingredient_name, ingredient_amount in item.recipe.items():
            if self.check_acquired(ingredient_name, ingredient_amount * craft_amount): continue

            gprint("< Missing Ingredient(s) >")
            return False

        # Removes ingredients then adds new crafted item to inventory
        for ingredient_name, ingredient_amount in item.recipe.items():
            self.remove_inventory(ingredient_name, ingredient_amount * craft_amount)
        print()
        self.add_inventory(item, craft_amount)
        return True
