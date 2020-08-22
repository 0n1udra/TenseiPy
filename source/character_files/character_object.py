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
        self.friends = {'Special S': {}, 'S': {}, 'Special A': {}, 'A+': {}, 'A': {},
                        'A-': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}, 'F': {}, 'Other': {},
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

    def get_object(self, item, character=None, mimic=False, new=False, get_level_mobs=False):
        """
        Can take in either a str or obj, then returns object (initialized if not already in inventory).

        Args:
            item: Either string or object instance of the object you want. If object, will get objects .name attribute.
            character: Character to get object from.
            mimic: If currently using Mimic ability, will also include mimicked mob attributes.
            new: If first time adding a new object to character.
            get_level_mobs: Gets character objects from current_level_mobs list

        Returns:
            Corresponding object, will initialize if one hasn't been already in inventory.
            False: If inputted item cannot be used to find object.

        Usage:
            .get_object('great sage')
            .get_object('hipokte grass')
        """

        # This function does a lot of heavy lifting for the game, since it looks, finds, and grabs game objects.

        # Set's character to player character (Rimuru) if none specified
        if not character:
            character = self

        # If input is an objects, gets objects name (str).
        if item and not type(item) == str:
            item = item.name

        if item is None:
            return None

        generators = [*self.inventory_generator(character), *self.attributes_generator(character)]

        # If object not in inventory, Will need to use __subclasses__ method to find and create new instance of object.
        if new:
            generators = [
                *game_items.Item.__subclasses__(),
                *game_skills.Skill.__subclasses__(),
                *game_characters.Character.__subclasses__(),
            ]

        # Get mob character objects from current_level_mobs list.
        if get_level_mobs:
            generators.extend(self.current_level_mobs)

        # Adds objects from all acquired mimicries.
        if mimic:
            generators.extend([*self.mimic_generator()])

        # Iterates through the generators and looks for a match.
        for i in generators:
            # Creates new instance to check for match, idk if there's a better way...
            if new:
                i = i()
            if i.get_name() in item.lower():
                return i
            # Deletes newly created instances if it wasn't a match.
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

        # If no specified character, default is player.
        if not character:
            character = self
        else:
            character = self.get_object(character)

        if character:
            item = character.get_object(check_object)
            if item:
                # Check if have item and the specified amount. Even if you have the item but not the specified amount, it'll return False.
                if item.game_object_type == 'Item' and item.amount < amount:
                    return False
                return True

