from game_files.extra import format_info
from game_files.output import gprint

class Item:
    name = ''
    status = ''
    item_type = ''
    damage_type = ''
    damage_level = None
    quantity = 0
    quantity_add = 1
    inv_capacity_add = 0.1
    info_page = ''
    description = ''
    usage = ''
    appearance = ''
    recipe = {}
    ingredient_for = []
    use_requirements = {}
    object_type = 'item'
    initialized = False

    def __init__(self, quantity=0):
        self.recipe, self.use_requirements = self.recipe, self.use_requirements
        self.quantity = quantity
        self.initialized = True
        self.update_info()

    def get_description(self):
        """
        Returns item description variable.

        Returns:
            str: Returns Item description.
        """

        return self.description

    def meet_requirements(self, user):
        """
        Checks if user meets prerequisite requirements to use item.

        Args:
            user obj: Character object that is using item.

        Returns:
            bool: If user meets requirements or not.
        """

        if self.use_requirements:
            # Check if user meets requirement or own prerequisites before using skill.
            for k, v in self.use_requirements.items():
                if not user.check_acquired(k, v):
                    gprint(f"< Usage Requires: {v}x {k} >")
                    return False
        return True

    def expend_requirements(self, user):
        """
        Expends (uses up) items/etc to activate item.

        Args:
            user obj: Character object that is using item.

        Returns:
            bool: If successfully expended requirements.
        """

        if not self.meet_requirements(user): return False

        for k, v in self.use_requirements.items():
            user.remove_inventory(k, v)
        return True

    def consume_item(self, user, amount=1):
        """Uses up item, by default 1."""

        if self.item_type == 'Consumable':
            user.remove_inventory(self, amount)
        return True

    def use(self, user, *args):
        """
        Use Item, by default it'll just return True to signal player has used the item.

        Args:
            user obj: Game character object of item user.

        Returns:
            bool: By default will return True to signal usage or consumption, if function not overwritten.
        """

        if not user: user = self
        self.expend_requirements(user)
        self.consume_item(user)
        return True

    def update_info(self):
        """Updates items info_page depending on what object variables has been set."""

        # If attribute/skill has a special status.
        self.info_page = f'    Name: [{self.name}] {"(" + self.status + ")" if self.status else ""}\n'

        # Only show fields that have set data.
        info_dict = {'Item Type': self.item_type, 'Damage Type': self.damage_type, 'Damage Level': self.damage_level,
                     '*Description': self.description, '*Appearance': self.appearance, '*Usage': self.usage}

        for k, v in info_dict.items():
            if formatted_info := format_info(k, v):
                self.info_page += f"    {formatted_info}\n"

        # If this item is part of another items requirements/recipe.
        if self.ingredient_for:
            self.info_page += "\n    Ingredient for:\n"
            for item in self.ingredient_for:
                self.info_page += f'        [{item}], '
            self.info_page = self.info_page[:-2] + '\n'

        # Show ingredients/prerequisites/requirements to be craft item.
        if self.recipe:
            self.info_page += f'\n    Recipe:\n        Will craft {self.quantity_add} at a time.\n'
            for item, amount in self.recipe.items():
                self.info_page += f'        {amount}x [{item}]\n'

    def __str__(self): return self.name.lower()

