import game_files.game_skills as game_skills
import game_files.game_items as game_items
import game_files.game_characters as game_characters
from .character_info import Info
from .character_inventory import Inventory
from .character_attributes import Attributes
from .character_combat import Combat
from .character_subordinates import Subordinates
from .character_map import Map


class Character(Info, Attributes, Inventory, Combat, Subordinates, Map):
    def __init__(self):
        # Main character attributes, inventory, skills, resistances, etc.
        self.starting_state = []
        self.friends = self.subordinates = {'Special S': {}, 'S': {}, 'Special A': {}, 'A+': {}, 'A': {},
                                            'A-': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}, 'F': {}, 'Other': {}}

        self.attributes = {'Manas': {},
                           'Ultimate Skill': {},'Unique Skill': {},'Special Skill': {},'Extra Skill': {},'Intrinsic Skill': {},
                           'Common Skill': {},'Daily Skill': {},'Composite Skill': {},'Resistance': {},'Attribute': {}}

        # Character inventory.
        self.inventory_capacity = 0  # Inventory capacity in percentage.
        self.inventory_capacity_add = 0  # Add to overall capacity when adding items to inventory.
        self.quantity = 0  # Item quantity in inventory.
        self.quantity_add = 1  # Usually items are added in batches, E.g. Hipokte Grass, Magical Ore.
        self.inventory = {'Items': {}, 'Materials': {}, 'Consumable': {},'Misc': {}}

        # Character information and data related variables.
        self.name = 'N/A'
        self.family_name = ''
        self.canon_name = 'N/A'  # Name from anime or manga storyline.
        self.title = 'N/A'  # E.g. True Dragon, Demon Lord.
        self.blessing = 'N/A'  # E.g. Storm Crest (from Veldora)>
        self.shared_blessing = 'N/A'
        self.species = 'N/A'
        self.rank = 'N/A'  # E.g. Catastrophe, Calamity.
        self.level = 1  # Same as rank just as integer.
        self.info_page = 'N/A'  # Info page for character.
        self.description = 'N/A'
        self.appearance = 'N/A'
        self.evolution = ''
        self.acquired_msg = ''
        self.is_alive = True

        # Combat variables.
        self.current_level_mobs = []  # Current mobs around you that you can interact or attack.
        self.targeted_mobs = set()  # Targets that will be attacked with 'attack' command.

        # Map functionality.
        self.available_locations = []
        self.current_location = 'N/A'

        # Game variables.
        self.game_object_type = 'character'
        self.story_progress = [None]
        self.save_path = ''
        self.text_crawl = True

    def set_start_state(self):
        """Adds corresponding starter attributes and items to character."""

        for i in self.starting_state:
            self.add_attribute(i, show_acquired_msg=False)

    def get_object(self, item, mimic=False, new=False, get_level_mobs=False):
        """
        Can take in either a str or obj, then returns object (initialized if not already in inventory).

        Args:
            item: Either string or object instance of the object you want. If object, will get objects .name attribute.
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

        # Should always return a character object if no object to find was passed in.
        if item is None: return self

        # If input is an objects, gets object's name.
        if item and not type(item) == str:
            item = item.name

        generators = [*self.inventory_generator(), *self.attributes_generator()]
        # If object not in inventory, Will need to use __subclasses__ method to find and create new instance of object.
        if new: generators = [*game_items.Item.__subclasses__(), *game_skills.Skill.__subclasses__(), *game_characters.Character.__subclasses__()]
        # Get mob character objects from current_level_mobs list.
        if get_level_mobs: generators.extend(self.current_level_mobs)
        # Adds all attributes from all acquired mimicries.
        if mimic: generators.extend([*self.mimic_generator()])

        for i in generators:
            # Creates new instance to check for match, idk if there's a better way...
            if new: i = i()
            if type(i) is str: continue
            if i.get_name() in item.lower(): return i
            else: del i

    def check_acquired(self, check_object, amount=1):
        """
        Checks to see if character has object/attribute/item/etc.

        Args:
            check_object: Object to check if specified character has item, attribute, skill, etc.
            amount: Check to see if have this amount of specified item.

        Returns:
            Boolean: If specified character has attribute or object.

        Usage:
            .check_acquired('resist poison')
            .check_acquired('resist poison', 'ranga')

            > rimuru has resist melee
            >>True
        """

        if item := self.get_object(check_object):
            # Check if have item and the specified amount. Even if you have the item but not the specified amount, it'll return False.
            if item.game_object_type == 'item' and item.quantity >= amount:
                return False
            return True
