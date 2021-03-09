import game_files.skills as game_skills
import game_files.items as game_items
import game_files.characters as game_characters
from .info import Info
from .inventory import Inventory
from .attributes import Attributes
from .combat import Combat
from .subordinates import Subordinates
from game_files.map import Map


class Character(Info, Attributes, Inventory, Combat, Subordinates, Map):
    def __init__(self):
        # Main character attributes, inventory, skills, resistances, etc.
        self.starting_state = []
        self.friends = self.subordinates = {'Special S': {}, 'S': {}, 'Special A': {}, 'A+': {}, 'A': {},
                                            'A-': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}, 'F': {}, 'Other': {}}

        self.attributes = {'Manas': {}, 'Ultimate Skill': {}, 'Unique Skill': {}, 'Extra Skill': {}, 'Intrinsic Skill': {},
                           'Common Skill': {}, 'Skill': {}, 'Resistance': {}}

        # Character inventory.
        self.inventory = {'Item': {}, 'Material': {}, 'Consumable': {}, 'Living': {}, 'Weapon': {}, 'Misc': {}}
        self.inventory_capacity = 0  # Inventory capacity in percentage.
        self.inventory_capacity_add = 0.1  # Add to overall capacity when adding items to inventory.
        self.quantity = 0  # Item quantity in inventory.
        self.quantity_add = 1  # Usually items are added in batches, E.g. Hipokte Grass, Magical Ore.

        # Character information and data related variables.
        self.name = ''
        self.family_name = ''
        self.canon_name = ''  # Name from anime or manga storyline.
        self.title = ''  # E.g. True Dragon, Demon Lord.
        self.protections = []  # E.g. Storm Crest (from Veldora)>
        self.shared_protection = ''
        self.species = ''
        self.rank = ''  # E.g. Catastrophe, Calamity.
        self.level = 1  # Same as rank just as integer.
        self.occupations = []
        self.affiliations = []
        self.info_page = ''  # Info page for character.
        self.description = ''
        self.appearance = ''
        self.abilities = []
        self.evolution = ''
        self.acquired_msg = ''
        self.is_alive = True
        self.item_type = 'Living'
        self.status = ''  # E.g. Passive, Active, Analysing, etc
        self.data = {'kills': 0}  # Extra data, that I don't feel like need to be variables.
        self.conditional_data = {}  # Contains data that player has done, paths taken, etc.
        self.game_object_type = 'character'

        # Gameplay variables.
        self.active_mobs = []  # Current mobs around you that you can interact or attack.
        self.targeted_mobs = []  # Targets that will be attacked with 'attack' command.
        self.last_command = ''
        self.last_skill = None  # Last successfully used skill, game object.

        # Map functionality.
        self.available_locations = []
        self.current_location = ''
        self.current_location_object = None  # Current location's class object.

        # Game variables.
        self.save_path = ''
        self.valid_save = None  # If you died in-game, the current save will be unusable.
        self.textcrawl = None  # Slow text crawl effect, letter by letter.
        self.show_hud = None  # Show available actions player can take.
        self.show_art = True  # Show ASCII art. Disable to save room on screen.
        self.show_hints = None  # If hardcore is True, this boolean will be ignored.
        self.hardcore = None  # Hides targets, mimicking, and actions.
        self.fast_mode = None
        self.line_history = []  # So user can see the last x number of lines from game, if screen gets cluttered from other commands.

    def __str__(self):
        return self.name.lower()

    def set_start_state(self):
        """ Adds corresponding starter attributes and items to character. """

        for i in self.starting_state:
            self.add_attribute(i, show_acquired_msg=False)

    def get_object(self, match, item_pool=None, new=False, stricter=True):
        """
        Can take in either a str or obj, then returns object (initialized if not already in inventory).

        Args:
            item_pool: List of game items to search against.
            new: If first time adding a new object to character.
            stricter: Find more of a exact match, still case insensitive. For example, sometimes Sage will be returned instead of Great Sage.

        Returns:
            Corresponding object, will initialize if one hasn't been already in inventory.
            False: If inputted item cannot be used to find object.

        Usage:
            .get_object('great sage')
            .get_object('hipokte grass')
        """

        if item_pool is None: item_pool = []

        if 'character' in self.game_object_type:
            item_pool = ([*self.inventory_generator(), *self.attributes_generator()])

        if new is True:
            item_pool = ([*game_items.Item.__subclasses__(), *game_skills.Skill.__subclasses__(), *game_characters.Character.__subclasses__()])

        for game_object in item_pool:
            if type(game_object) is str: continue

            if new:
                try: game_object = game_object()
                except: pass

            if stricter:
                if str(game_object).lower() == str(match).lower().strip():
                    return game_object
            elif str(game_object).lower() in str(match).lower():
                return game_object

            if new: del game_object

        return None

    def check_acquired(self, check_object, amount=1):
        """ Checks if you pass in a list of strings or just a single string. """

        if type(check_object) is list:
            for i in check_object:
                return self._check_acquired(i, amount)
        else:
            return self._check_acquired(check_object, amount)

    def _check_acquired(self, check_object, amount=1):
        """
        Checks to see if character has object/attribute/item/etc.

        Args:
            check_object: Object to check if specified character has item, attribute, skill, etc.
            amount [int:1]: Check quaintly of item, only works for inventory right now.

        Returns:
            Boolean: If specified character has attribute or object.

        Usage:
            .check_acquired('resist poison')
        """

        if item := self.get_object(check_object):
            if item.quantity >= amount: return item
        return False

    def update_status(self, game_object, new_status):
        """ Update status of character. """

        if game_object := self.get_object(game_object):
            game_object.status = new_status
            game_object.update_info()