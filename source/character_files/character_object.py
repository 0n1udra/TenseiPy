import game_files.game_skills as game_skills
import game_files.game_items as game_items
import game_files.game_characters as game_characters
from .character_info import Info
from .character_inventory import Inventory
from .character_attributes import Attributes
from .character_combat import Combat
from .character_subordinates import Subordinates


class Character(Info, Attributes, Inventory, Combat, Subordinates):
    def __init__(self):
        Info.__init__(self)
        Attributes.__init__(self)
        Inventory.__init__(self)
        Combat.__init__(self)
        Subordinates.__init__(self)

        self.starting_state = []
        self.game_object_type = 'character'
        self.friends = {'Special S': [], 'S': [], 'Special A': [], 'A+': [], 'A': [],
                        'A-': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'Other': [],
                        }

        # Game variables.
        self.story_progress = [None]
        self.save_path = ''
        self.text_delay = True
        self.played_paths = set()

    def set_start_state(self):
        """Adds corresponding starter attributes and items to character."""

        for i in self.starting_state:
            self.add_attribute(i, show_acquired_msg=False)

    def get_object(self, item, character=None, mimic=False, new=False, clm=False):
        """
        Can take in either a str or obj, then returns object (initialized if not already in inventory).

        Args:
            item: Either string or object instance of the object you want. If object, will get objects .name attribute.
            mimic: If currently using Mimic ability, will also include mimicked mob attributes.
            new: If first time adding a new object to character.

        Returns:
            Corresponding object, will initialize if one hasn't been already in inventory.

        Usage:
            .get_object('great sage')
            .get_object('hipokte grass')
        """

        if not character:
            character = self

        # If input is an objects, gets objects name (str).
        if not type(item) == str:
            item = item.name

        generators = [*self.inventory_generator(character), *self.attributes_generator(character)]

        try:
            generators.extend([*self.mimic_generator(character)])
        except:
            pass

        # If object not in inventory. Will need to use __subclasses__ method to find, initialize and add to inventory.
        if new:
            generators = [
                *game_items.Item.__subclasses__(),
                *game_skills.Skill.__subclasses__(),
                *game_characters.Character.__subclasses__(),
            ]
        if clm:
            generators.extend(self.current_level_characters)

        # If currently using Mimic ability.
        if mimic:
            generators.extend([*self.mimic_generator()])
            # Adds mimicked monster abilities if currently using mimic.

        try:
            if self.current_mimic:
                generators.extend([*self.mimic_generator()])
        except:
            pass

        for i in generators:
            if new:
                i = i()
            if i.get_name() in item.lower():
                return i
            else:
                del i

    def check_acquired(self, check_object, amount=1, character=None):
        """
        Checks to see if character has object/attribute/item/etc.

        Args:
            check_object: Object to check if specified character has item, attribute, skill, etc.
            character: Check if character has the object.
            amount: Check to see if have this amount of specified item.

        Returns:
            Boolean: If specified character has attribute or object.

        Usage:
            .check_acquired('resist poison')
            .check_acquired('resist poison', 'ranga')

            > rimuru has resist melee
            >>True
        """

        if not character:
            character = self
        else:
            character = self.get_object(character)

        if character:
            item = character.get_object(check_object)
            if item:
                if item.game_object_type == 'Item' and item.amount < amount:
                    return False
                return True

        try:
            for i in self.mimic_generator():
                if i.get_object(check_object):
                    return True
        except:
            pass

