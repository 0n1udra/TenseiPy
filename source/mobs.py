from character import Character


def ssprint(Msg):
    print(f'    {Msg}\n')


class Rimuru_Tempest(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Slime'
        self.shared_blessing = 'Protection of Tempest'
        self.level = 7
        self.current_mimic = None
        self.current_mimic_name = 'Slime'
        self.starting_state = ['Mimic', 'Self-Regeneration', 'Absorb/Dissolve', 'Pain Resist', 'Melee Resist',
                               'Electricity Resist']
        self.update_info()

    # ========== Predator Functions
    def mimic_generator(self):
        """
        Yields available mimic mob objects.

        Returns:
            Yields character objects that are in acquired_mimicries dictionary.
        """

        for level, mimicries_list in self.mimic_object().acquired_mimicries.items():
            for mimic in mimicries_list:
                yield mimic

    def predate_targets(self, input_targets=None):
        """
        Predates targets that are being focused. Also adds target mimicry.

        Args:
            input_targets: Target to predate.

        Usage:
            > predate
        """

        targets = list(self.focused_targets)

        try:
            for i in input_targets.split(','):
                targets.append(self.get_object(i))
        except:
            pass

        for target in targets:
            if target:
                if self.is_item(target):
                    self.add_inventory(target)
                elif self.is_attribute(target):
                    self.add_attribute(target)
                elif self.is_character(target):
                    # Get's list of c that are on current level.
                    for mob in self.current_level_characters:
                        # Checks if current mob is alive and checks of current target is in current_level_characters lsit.
                        if not mob.alive and mob.get_name() in target.get_name():
                            self.add_mimic(target)
                        else:
                            print(f"<<Warning, predation of {mob.name} unsuccessful.>>")


        self.focused_targets = set()

    def mimic_object(self, active=None):
        """
        Args:
            active:

        Returns:

        """
        mimic = self.attributes['Unique Skill']['Mimic']
        mimic.active = active
        return mimic

    def add_mimic(self, character):
        """
        Adds new monster mimicry.

        Args:
            character: Character object to add to acquired_mimicries list
        """
        # Checks if already have mimicry.

        self.mimic_object().acquired_mimicries[character.rank].append(character)
        ssprint(f'<<Notice, new mimicry available: {character.name}.>>')

    def use_mimic(self, character):
        """
        Use mimicry ability.

        Args:
            character: Game monster to mimic.

        Usage:
            > mimic tempest serpent
        """
        if character == 'reset':
            # Resets mimic state (default Slime).
            self.current_mimic_name = 'Slime'
            self.current_mimic = None
            ssprint("<Mimicry Reset>")
        else:
            new_mimic = self.get_object(character, mimic=True)
            if new_mimic:
                self.current_mimic_name = new_mimic.name
                self.current_mimic = new_mimic
                ssprint(f'<Now Mimicking: {new_mimic.name}>')


class Veldora_Tempest(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = "Veldora"
        self.title = 'Storm Dragon'
        self.species = 'True Dragon'
        self.blessing = 'Storm Crest'
        self.alive = True
        self.level = 11
        self.item_type = 'Misc'
        self.capacity_add = 10
        self.update_info()


# ========== Low Level
class Tempest_Serpent(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Tempest Serpent'
        self.Species = 'Serpent'
        self.level = 6
        self.appearance = 'The snake has a large, jet-black body with thorned scales and tough skin.'
        self.description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'
        self.starting_state = ['sense heat source', 'poisonous breath']
        self.set_start_state()
        self.update_info()


class Giant_Bat(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Giant Bat'
        self.Species = 'Bat'
        self.level = 4
        self.appearance = '''
        It's a giant bat...
        Due to its wings that regulate its own gravity, it's capable of flight
        '''
        self.description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'
        self.starting_state = ['ultrasound waves', 'vampirism']
        self.set_start_state()
        self.update_info()


class Evil_Centipede(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Evil Centipede'
        self.Species = 'Centipede'
        self.level = 5
        self.appearance = 'Centipede monstrosity, a giant centipede.'
        self.description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'
        self.starting_state = ['paralyzing breath']
        self.set_start_state()
        self.update_info()


class Black_Spider(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Black Spider'
        self.Species = 'Spider'
        self.level = 5
        self.appearance = 'Most of the body is yellow-ish, while the legs are black.'
        self.description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'
        self.starting_state = ['sticky thread', 'steel thread']
        self.set_start_state()
        self.update_info()


# ========== Wolves
class Tempest_Wolf(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Tempest Wolf'
        self.Species = 'Tempest Wolf'
        self.level = 5
        self.appearance = 'Most of the body is yellow-ish, while the legs are black.'
        self.description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'
        self.evolution = 'Direwolf > Tempest Wolf > Star Wolf > Tempest Star Wolf'
        self.starting_state = []
        self.set_start_state()
        self.update_info()


# ========== Rimuru
rimuru = None


def update_character(character):
    global rimuru
    rimuru = character
    return rimuru
