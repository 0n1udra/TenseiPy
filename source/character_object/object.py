
import game_files.skills as game_skills
import game_files.items as game_items
import game_files.characters as game_characters

class Base:
    def get_object(self, match, item_pool_add=None, item_pool_only=None, new=False, mimic_pool=False, sub_pool=False):
        """
        Can take in either a str or obj, then returns object (will initialize if need to).

        Args:
            match str:
            item_pool_add list(None): Add to item pool.
            item_pool_only list(None): Add custom list of game items to search against only.
            new bool(False): Return new instance of object (already already not necessary).
            mimic_pool bool(False): Adds acquired mimics character objects and their attribute/inventory to pool.
            sub_pool bool(False): Adds subordinates character objects to pool.

        Returns:
            Corresponding object, will initialize if one hasn't been already in inventory.
            False: If inputted item cannot be used to find object.

        Usage:
            .get_object('great sage')
            .get_object('hipokte grass')
        """

        item_pool = []
        if not type(match) is str: match = match.name
        if item_pool_add: item_pool += item_pool_add

        # Gets character's acquired attributes and items in inventory.
        if 'character' in self.game_object_type:
            item_pool += [*self.inventory_generator(), *self.attributes_generator()]

        # Adds all attributes/inventory items to pool from all acquired mimicries, including the character object itself.
        if self.check_if_player() and mimic_pool:
            for mob in self.mimic_generator():
                item_pool += [mob, *mob.inventory_generator(), *mob.attributes_generator()]

        # So far, only allows player to use 'info' and 'stats' command on subordinates (not on their acquried attrs/items).
        if sub_pool: item_pool += [*self.subordinates_generator()]

        # Create item_pool of all the game objects to be able to find match and return new instance of object if matched.
        if new: item_pool = [*game_items.Item.__subclasses__(), *game_skills.Skill.__subclasses__(), *game_characters.Character.__subclasses__()]

        # Use only item pool that was passed in.
        if item_pool_only: item_pool = item_pool_only

        # Somehow strings get in the item_pool, need to filter those out.
        for game_object in list(filter(lambda x: type(x) is not str, item_pool)):
            # Returns game object if match found (uninitialized).
            if game_object.name.lower() == match.lower(): return game_object
        return None

    def check_acquired(self, check_object, amount=1):
        """
        Checks if you pass in a list of strings or just a single string.

        Args:
            check_object str/list: Object(s) to check if acquired.
            amount int(1): Base amount to check if own.

        Usage:
            .check_acquired('resist poison')

        """

        if type(check_object) is list:
            for i in check_object:
                return self._check_acquired(i, amount)
        else: return self._check_acquired(check_object, amount)

    def _check_acquired(self, check_object, amount=1):
        """Check if own skill/item/etc."""

        item = self.get_object(check_object, mimic_pool=True)
        if item and item.quantity >= amount:
            return item
        return False
