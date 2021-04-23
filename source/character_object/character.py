import game_files.skills as game_skills
import game_files.items as game_items
import game_files.characters as game_characters
from .info import Info
from .inventory import Inventory
from .attributes import Attributes
from .combat import Combat
from .subordinates import Subordinates
from character_object.map import Map


class Character(Info, Attributes, Inventory, Combat, Subordinates, Map):
    # Character inventory.
    starting_state = []  # Character's starting skills/attributes.
    inventory_capacity = 0  # Inventory capacity in percentage.
    inv_capacity_add = 0.1  # Add to overall capacity when adding items to inventory.
    quantity = 0  # Item quantity in inventory.
    quantity_add = 1  # Usually items are added in batches, E.g. Hipokte Grass, Magical Ore.

    # Character information and data related variables.
    name = ''
    family_name = ''
    canon_name = ''  # Name from anime or manga storyline.
    title = ''  # E.g. True Dragon, Demon Lord.
    protections = []  # E.g. Storm Crest (from Veldora)>
    shared_protection = ''  # Divine protection to be shared.
    species = ''
    rank = ''  # E.g. Catastrophe, Calamity.
    level = 1  # Same as rank just as integer.
    occupations = []
    affiliations = []
    info_page = ''  # Info page for character.
    description = ''
    appearance = ''  # Description of character appearance.
    abilities = []
    evolution = ''  # Species evolution of character.
    acquired_msg = ''  # Message for when newly acquired.
    is_alive = True
    item_type = 'Living'
    status = ''  # E.g. Passive, Active, Analysing, etc

    # Level/Map functionality.
    active_mobs = []  # Current mobs around you that you can interact or attack.
    targeted_mobs = []  # Targets that will be attacked with 'attack' command.
    last_command = ''
    last_use_skill = None  # Last successfully used skill, game object.
    available_locations = []
    current_location = ''
    current_location_object = None  # Current location's class object.

    # Game variables.
    game_object_type = 'character'
    initialized = False
    save_path = ''
    valid_save = None  # If you died in-game, the current save will be unusable.
    textcrawl = None  # Slow text crawl effect, letter by letter.
    show_actions = None  # Show available actions player can take.
    show_art = True  # Show ASCII art. Disable to save room on screen.
    show_hints = True  # If hardcore is True, this boolean will be ignored.
    hardcore = None  # Hides targets, mimicking, and actions.
    fast_mode = None
    storyline_log = game_log = []  # So user can see the last x number of lines from game, if screen gets cluttered from other commands.
    source_folder_path = ''

    def __init__(self, name='', lname=''):
        if name or lname:
            self.name, self.family_name = name, lname
        else: self.name, self.family_name = self.name, self.family_name

        # Pickle/dill has some issue with dumping dictionaries, so these has to be initialized here.
        self.friends = self.subordinates = {'Special S': {}, 'S': {}, 'Special A': {}, 'A+': {}, 'A': {},
                                            'A-': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}, 'F': {}, 'Other': {}}

        self.attributes = {'Manas': {}, 'Ultimate Skill': {}, 'Unique Skill': {}, 'Extra Skill': {},
                          'Intrinsic Skill': {}, 'Common Skill': {}, 'Skill': {}, 'Resistance': {}}

        self.inventory = {'Item': {}, 'Material': {}, 'Consumable': {}, 'Living': {}, 'Weapon': {}, 'Misc': {}}

        self.data = {'kills': 0}  # Extra data, that I don't feel like need to be variables.
        self.game_conditions = {}
        self.actions_played = {}
        self.reputations = {}  # Reputation/standing of characters/factions.
        self.initialized = True
        self.set_start_state()
        self.update_info()

    def __str__(self): return self.name.lower()

    def set_start_state(self):
        """Adds starter attributes and items to character."""

        for i in self.starting_state:
            self.add_attribute(i, show_acquired_msg=False)

    def get_object(self, match, item_pool=None, new=False, mimic_pool=False):
        """
        Can take in either a str or obj, then returns object (will initialize if need to).

        Args:
            match str:
            item_pool list: Add custom list of game items to search against.
            new bool(False): Return new instance of object (already already not necessary).

        Returns:
            Corresponding object, will initialize if one hasn't been already in inventory.
            False: If inputted item cannot be used to find object.

        Usage:
            .get_object('great sage')
            .get_object('hipokte grass')
        """

        if not type(match) is str: match = match.name
        if item_pool is None: item_pool = []

        # Gets character's acquired attributes and items in inventory.
        if 'character' in self.game_object_type:
            item_pool += [*self.inventory_generator(), *self.attributes_generator()]

        # Adds all attributes/inventory items to pool from all acquired mimicries.
        if self.check_if_player() and mimic_pool:
            for mob in self.mimic_generator():
                item_pool += [mob, *mob.inventory_generator(), *mob.attributes_generator()]

        # Create item_pool of all the game objects to be able to find match and return new instance of object if matched.
        if new: item_pool = [*game_items.Item.__subclasses__(), *game_skills.Skill.__subclasses__(), *game_characters.Character.__subclasses__()]

        # Somehow strings get in the item_pool, need to filter those out.
        for game_object in list(filter(lambda x: type(x) is not str, item_pool)):
            # Returns game object if match found (uninitialized).
            if game_object.name.lower() == match.lower(): return game_object
        return None

    def check_acquired(self, check_object, amount=1):
        """
        Checks if you pass in a list of strings or just a single string.

        Args:
            check_object str: Object to check if acquired.
            amount int(1): Base amount to check if own.
        """

        if type(check_object) is list:
            for i in check_object:
                return self._check_acquired(i, amount)
        else: return self._check_acquired(check_object, amount)

    def _check_acquired(self, check_object, amount=1):
        """
        Checks to see if character has object/attribute/item/etc.

        Args:
            check_object str: Object to check if specified character has item, attribute, skill, etc.
            amount int(1): Check quaintly of item, only works for inventory right now.

        Returns:
            bool: If specified character has attribute or object.

        Usage:
            .check_acquired('resist poison')
        """

        item = self.get_object(check_object, mimic_pool=True)
        if item and item.quantity >= amount: return item
        return False

    def set_status(self, game_object, new_status):
        """Update status of character."""

        if game_object := self.get_object(game_object):
            game_object.status = new_status
            game_object.update_info()
