from character_files.character_object import Character

class Rimuru_Tempest(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Slime'
        self.canon_name = 'Rimuru Tempest'
        self.shared_blessing = 'Protection of Tempest'
        self.level = 7
        self.current_mimic = None
        self.current_mimic_species = 'Slime'
        self.starting_state = ['Mimic', 'Self-Regeneration', 'Absorb/Dissolve', 'Pain Resist', 'Melee Resist',
                               'Electricity Resist']
        self.update_info()

    # ========== Predator Functions
    def mimic_generator(self):
        """
        Yields available mimic mob objects.

        Returns:
            mimic: Yields character objects that are in acquired_mimicries dictionary.
        """

        if not self.mimic_object(): return None

        for level, mimics in self.mimic_object().acquired_mimicries.items():
            for mimic_name, mimic in mimics.items(): yield mimic

    def mimic_object(self, active=None):
        """
        Args:
            active: Sets whether mimic is being used or not.

        Returns:
            mimic: Mimic object from .attributes.

        """

        if 'Mimic' in self.attributes['Unique Skill']:
            mimic = self.attributes['Unique Skill']['Mimic']
            mimic.active = active
            return mimic

    def add_mimic(self, character):
        """
        Adds new monster mimicry.

        Args:
            character: Character object to add to acquired_mimicries list
        """

        # Basically checks if self is the rimuru object (player).
        if not self.mimic_object(): return False

        # Checks if already acquired.
        if character.name in self.mimic_object().acquired_mimicries[character.rank]: return None

        # Adds new mob object to usable mimicries dict.
        self.mimic_object().acquired_mimicries[character.rank][character.name] = character

        # Adds attributes from mob just analyzed.
        for attribute in character.attributes_generator():
            self.add_attribute(attribute)

        print(f"    << Information, analysis on [{character.name}] completed. >>")
        print(f"    << Notice, new skills and mimicry available: [{character.name}]. >>\n")

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
            self.current_mimic_species = 'Slime'
            self.current_mimic = None
            self.mimic_object(active=False)
            print("    < Mimicry reset. >")
        else:
            new_mimic = self.get_object(character, mimic=True)
            if new_mimic:
                self.current_mimic_species = new_mimic.species
                self.current_mimic = new_mimic
                self.mimic_object(active=True)
                print(f'    < Now Mimicking: [{new_mimic.name}]. >')

    def predate_targets(self, input_targets=None):
        """
        Predates targets that are being focused. Also adds target mimicry.

        Args:
            input_targets: Target to predate.

        Usage:
            > predate
        """

        targets = list(self.targeted_mobs)

        try:
            for i in input_targets.split(','):
                targets.append(self.get_object(i))
        except ValueError: pass

        for target in targets:
            if not target: continue

            if target.game_object_type == 'item':
                self.add_inventory(target)
            elif target.game_object_type == 'attribute':
                self.add_attribute(target)
            elif target.game_object_type == 'character':
                # Get's list of c that are on current level.
                for mob in self.active_mobs:
                    # Checks if current mob is is_alive and checks of current target is in active_mobs lsit.
                    if not mob.is_alive and mob.get_name() in target.get_name():
                        self.add_mimic(target)

        self.targeted_mobs = set()


class Veldora_Tempest(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = "Veldora"
        self.title = 'Storm Dragon'
        self.canon_name = 'Veldora Tempest'
        self.species = 'True Dragon'
        self.blessing = 'Storm Crest'
        self.is_alive = True
        self.level = 11
        self.item_type = 'Misc'
        self.inventory_capacity_add = 10
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
