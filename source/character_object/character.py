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
    starting_state = []  # Character's starting skills/attributes.
    inventory_capacity = 0
    inv_capacity_add = 0.1  # Add to overall capacity when adding items to inventory.
    quantity = 0  # Item quantity in inventory.
    quantity_add = 1  # Usually items are added in batches, E.g. Hipokte Grass (50), Magical Ore (25).

    name = ''
    family_name = ''
    canon_name = ''  # Name from manga storyline.
    titles = []  # E.g. True Dragon, Demon Lord.
    species = ''
    rank = ''  # E.g. Catastrophe, Calamity.
    level = 1  # Integer corresponding to rank.
    info_page = ''  # Info page for character.
    status = ''  # E.g. Passive, Active, Analysing, etc
    description = ''
    appearance = ''  # Description of character appearance.
    evolution = ''  # Species evolution of character.
    acquired_msg = ''  # Message for when newly acquired.
    shared_protection = ''  # Divine protection to be shared when giving mob a name.
    protections = []  # E.g. Storm Crest (from Veldora).
    occupations = []
    affiliations = []
    abilities = []  # Extra abilities that are not considered a [Skill].
    is_alive = True
    item_type = 'Mob'

    last_command = ''
    last_use_skill = None  # Last successfully used skill, game object.
    current_location = ''
    current_location_object = None  # Current location's class object.
    available_locations = []
    active_mobs = []  # Current mobs around you that you can interact or attack.
    targeted_mobs = []  # Targets that will be attacked with 'attack' command.

    # Game variables.
    save_path = ''
    source_folder_path = ''
    game_object_type = 'character'
    initialized = False
    valid_save = None  # If you died in-game, the current save will be unusable.
    textcrawl = None  # Slow text crawl effect, letter by letter.
    show_actions = None  # Show available actions player can take.
    show_art = True  # Show ASCII art. Disable to save room on screen.
    show_hints = True  # If hardcore is True, this boolean will be ignored.
    hardcore = None  # Hides targets, mimicking, and actions.
    fast_mode = None
    last_print_func_used = 'sprint'
    storyline_log = game_log = []  # So user can see the last x number of lines from game, if screen gets cluttered from other commands.

    def __init__(self, name=''):
        if name: self.name = name
        else: self.name, self.family_name = self.name, self.family_name

        # Pickle/dill has some issue with dumping dictionaries, so these has to be initialized here.
        self.friends = self.subordinates = {'Special S': {}, 'S': {}, 'Special A': {}, 'A+': {}, 'A': {},
                                            'A-': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}, 'F': {}, 'Other': {}}

        self.attributes = {'Manas': {}, 'Ultimate Skill': {}, 'Unique Skill': {}, 'Extra Skill': {},
                          'Intrinsic Skill': {}, 'Common Skill': {}, 'Skill': {}, 'Resistance': {}}

        self.inventory = {'Item': {}, 'Material': {}, 'Consumable': {}, 'Mob': {}, 'Weapon': {}, 'Misc': {}}

        self.acquired_mimicries = {'Special S': {}, 'S': {}, 'Special A': {}, 'A+': {}, 'A': {},
                                   'A-': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}, 'F': {}, 'Other': {}}

        self.data = {'kills': 0}  # Extra data, that I don't feel like need to be variables.
        self.game_conditions = {}
        self.actions_played = {}
        self.reputations = {}  # Reputation/standing of characters/factions.
        self.initialized = True
        self.set_start_state()
        self.update_info()

    def __str__(self): return self.name

    def set_start_state(self):
        """Adds starter attributes to character."""

        for i in self.starting_state:
            self.add_attribute(i, show_acquired_msg=False)

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
