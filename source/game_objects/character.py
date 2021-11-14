from .object import Base
from .info import Info
from .inventory import Inventory
from .attribute import Attributes
from .combat import Combat
from .subordinate import Subordinates
from game_objects.map import Map


class Character(Base, Info, Attributes, Inventory, Combat, Subordinates, Map):
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
    balance = 50
    inventory_capacity = 0
    inv_capacity_add = 0.1  # Add to overall capacity when adding items to inventory.
    quantity = 0  # Item quantity in inventory.
    quantity_add = 1  # Usually items are added in batches, E.g. Hipokte Grass (50), Magical Ore (25).
    item_type = 'Mob'  # Categorization for inventory items.
    starting_state = []  # Character's starting skills/attributes.

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
    object_type = 'character'  # Different from 'item_type' var, used for backend code differentiation.
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


