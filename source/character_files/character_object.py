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
        """

        if not character:
            character = self

        # If input is an objects, gets objects name (str).
        if not self.is_str(item):
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

    def check_mob_has(self, check_object, character=None):
        """
        Checks to see if character has object/attribute/item/etc.

        Args:
            check_object: Object to check if specified character has item, attribute, skill, etc.
            character: Check if character has the object.

        Usage:
            .check_mob_has('resist poison')
            .check_mob_has('resist poison', 'ranga')

            > rimuru has resist melee
            >>True
        """

        if not character:
            character = self
        else:
            character = self.get_object(character)
        check_object = self.get_object(check_object)

        if character and check_object:
            if character.get_object(check_object):
                return True

    def is_character(self, character):
        """
        Check if game character object.

        Args:
            character: Check game character object.

        Returns:
            True if game character object.
        """

        try:
            character = self.get_object(character, new=True)
            if character.game_object_type == 'character':
                del character
                return True
        except:
            return False

    def is_item(self, item):
        """
        Check if game item object.

        Args:
            item: If game item object.

        Returns:
            True of game item object.
        """

        try:
            item = self.get_object(item, new=True)
            if item.game_object_type == 'item':
                del item
                return True
        except:
            return False

    def is_attribute(self, attribute):
        """
        Checks if is game attribute object.

        Args:
            attribute: Check if is attribute object.

        Returns:
            True if is attribute object.
        """

        try:
            attribute = self.get_object(attribute, new=True)
            if attribute.game_object_type == 'attribute':
                del attribute
                return True
        except:
            return False

    def is_obj(self, object):
        try:
            object = self.get_object(object)
            if self.is_item(object) or self.is_attribute(object):
                return True
            else:
                return False
        except:
            return False


    def is_str(self, string):
        """
        Check if is a string.

        Args:
            string: Check string.

        Returns:
            True if is string.
        """

        if type(string) == str:
            return True
        else:
            return False
