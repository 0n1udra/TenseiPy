import skills, items
from info import Info
from inventory import Inventory
from attributes import Attributes
from combat import Combat
from subordintes import Subordinates
zz


def ssprint(Msg):
    print(f'    {Msg}\n')


class Character():
    def __init__(self):
        self.Inv = Inventory()
        self.Data = Info()
        self.Attrs = Attributes()
        self.Combat = Combat()
        self.Subs = Subordinates()
        # Game variables.
        self.story_progress = [None]
        self.save_path = ''
        self.text_delay = True
        self.last_command = ''

        # Predator ability variables.
        self.game_object_type = 'character'

        self.friends = {'Special S': [], 'S': [], 'Special A': [], 'A+': [], 'A': [],
                        'A-': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'Other': [],
                        }

    def set_start_state(self):
        """Adds corresponding starter attributes and items to character."""

        for i in self.starting_state:
            self.add(i, show_acquired_msg=False)

    def get_object(self, inp, mimic=False, new=False):
        """
        Can take in either a str or obj, then returns object (initialized if not already in inventory).


        Args:
            inp: Either string or object instance of the object you want. If object, will get objects .name attribute.
            mimic: If currently using Mimic ability, will also include mimicked mob attributes.
            new: If first time adding a new object to inventory.

        Returns:
            Corresponding object, will initialize if one hasn't been already in inventory.
        """

        # If input is an objects, gets objects name (str).
        try:
            inp = inp.name
        except AttributeError:
            pass

        generators = [*self.generator(), *self.generator(), *self.generator()]

        try:
            generators.extend([*self.mimic_generator()])
        except ModuleNotFoundError:
            pass

        # If object not in inventory. Will need to use __subclasses__ method to find, initialize and add to inventory.
        if new:
            generators = [
                *items.Item.__subclasses__(),
                *skills.Skill.__subclasses__(),
                *Character.__subclasses__()
            ]

        # If currently using Mimic ability.
        if mimic:
            generators = [self.mimic_generator()]
        # Adds mimicked monster abilities if currently using mimic.
        if self.current_mimic:
            generators.extend(self.generator(self.current_mimic))

        for i in generators:
            if new:
                i = i()
            if i.get_name() in inp.lower():
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

