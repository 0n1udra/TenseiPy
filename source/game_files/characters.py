from character_files.character import Character


# ========== Characters
class Rimuru_Tempest(Character):
    name = 'Slime'
    canon_name = 'Rimuru Tempest'
    shared_protection = 'Protection of Tempest'
    level = 7
    current_mimic = None
    current_mimic_species = 'Slime'
    acquired_mimicries = {'Special S': {}, 'S': {}, 'Special A': {}, 'A+': {}, 'A': {},
                          'A-': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}, 'F': {}, 'Other': {}}
    starting_state = ['Sage', 'Predator', 'Mimic', 'Self-Regeneration', 'Absorb/Dissolve', 'Pain Resist', 'Melee Resist', 'Electricity Resist']

    # ========== Predator Functions
    def mimic_generator(self):
        """
        Yields available mimic mob objects.

        Returns:
            mimic: Yields character objects that are in acquired_mimicries dictionary.
        """

        if not self.mimic_object(): return None

        for level, mimics in self.acquired_mimicries.items():
            for mimic_name, mimic in mimics.items():
                yield mimic

    def mimic_object(self, active=None):
        """
        Return mimic ability game object, and can also set active status.

        Args:
            active: Sets whether mimic is being used or not.

        Returns:
            mimic: Mimic game object from character.
        """

        if mimic := self.check_acquired('Mimic'):
            mimic.active = active
            return mimic

    def add_mimic(self, mob, show_msg=True):
        """
        Adds new monster mimicry.

        Args:
            mob: Character object to add to acquired_mimicries list
            show_msg bool(True): Show acquired message.
        """

        # Basically checks if self is the rimuru object (player).
        if not self.mimic_object(): return False

        # Checks if already acquired.
        if mob.name in self.acquired_mimicries[mob.rank]: return None

        # Adds new mob object to usable mimicries dict.
        self.acquired_mimicries[mob.rank][mob.name] = mob

        # Adds attributes from mob just analyzed.
        for attribute in mob.attributes_generator(): self.add_attribute(attribute)

        if show_msg:
            print(f"\n    << Information, analysis on [{mob.name}] completed. >>")
            print("    << Notice, new skills and mimicry available. >>\n")

    def use_mimic(self, character):
        """
        Use mimicry ability.

        Args:
            character str: Game monster to mimic.

        Usage:
            > mimic tempest serpent
        """

        # Resets mimic state (default Slime).
        if character == 'reset':
            self.current_mimic_species = 'Slime'
            self.current_mimic = None
            self.mimic_object(active=False)
            print("    < Mimicry Reset >")
        else:
            if new_mimic := self.get_object(character, [*self.mimic_generator()]):
                self.current_mimic_species = new_mimic.species
                self.current_mimic = new_mimic
                self.mimic_object(active=True)
                print(f'    < Now Mimicking [{new_mimic.name}] >')

    def check_mimic(self, match=None):
        """
        Return name (string) of character currently mimicking, can also check if using specific mimic.

        Args:
            match str: Check if currently mimicking specified mob by name.

        Returns:
            str: Returns name of mob currently mimicking.
        """

        if m_object := self.mimic_object():
            if match is None:
                return m_object.name
            if match.lower() in m_object.name.lower():
                return m_object.name
        return False

    def show_mimics(self, *args):
        print("    ----- Mimicries -----")
        for mob_level, mobs in self.acquired_mimicries.items():
            print(f'    {mob_level}:')
            for mob_name, mob in mobs.items():
                print(f'        {mob_name}')
        print("\n    Note: To reset mimicry use 'mimic reset'. use 'info predator' for more info on mimicry.")

    def eat_targets(self, *args):
        """
        Predates targets that are being targeted. Also adds new mimicry.

        Args:
            args: Catch all for use from game_action function.

        Usage:
            > eat
        """

        for target in self.targeted_mobs:
            if not target[0]: continue  # If no game object found.

            if target[0].game_object_type == 'item':
                self.add_inventory(target[0])
            elif target[0].game_object_type == 'attribute':
                self.add_attribute(target[0])
            elif target[0].game_object_type == 'character':
                # Can only eat targeted mobs that are dead.
                if target[0].is_alive is False:
                    self.add_mimic(target[0])
                    self.add_inventory(target[0], target[1])
                    self.targeted_mobs.remove(target)
                    try:
                        self.active_mobs.remove(target)
                    except: pass

        # For some reason I need this to check if it cleared out all dead mobs.
        # If not it'll just run this function again. Have not ran into bugged looping, yet. Should probably change this huh?
        for i in self.targeted_mobs:
            if i[0].is_alive is False:
                self.eat_targets()

class Veldora_Tempest(Character):
    name = "Veldora"
    title = 'Storm Dragon'
    canon_name = 'Veldora Tempest'
    species = 'True Dragon'
    protections = ['Protection of the Storm']
    shared_protection = 'Storm Crest'
    is_alive = True
    level = 11
    inventory_capacity_add = 10


# ===== Adventurers
class Eren_Grimwold(Character):
    name = "Eren Grimwold"
    level = 5
    species = 'Human'
    occupations = ['Adventurer']
    affiliations = ['Freedom Association', "Kaval's Party", "Brumund"]
    description = "A Mage part of Cabal's Party."
    appearance = "A blonde, 16y/o, green eyed adventurer from the Freedom Association."
    abilities = ['Mud Hand', 'Cleaning Magic', 'Elemental Magic']

class Kaval(Character):
    name = "Kaval"
    level = 5
    species = 'Human'
    occupations = ['Adventurer']
    affiliations = ["Kaval's Party", "Freedom Association"]
    description = """Leader of his adventure's party, where he serves as the 'fighter' role. Alongside Gido,
    he is also tasked as the secret bodyguard of Lady Elyune under the guise of an adventurer.'"""
    appearance = 'A young man with medium length hair, seemingly in his prime.'
    abilities = ['Fighting Spirit', 'Heavy Collision']

class Gideo(Character):
    name = 'Gido'
    level = 5
    species = 'Human'
    occupations = ['Adventurer']
    affiliations = ["Kaval's Party", "Freedom Association"]
    description = """A member of Kaval's Party who serves as the 'thief' role. However,
    he is actually serving as one of the bodyguards of Lady Elyune secretly while under the guise of an adventurer."""
    appearance = """Gido has a tall and strong build and a rectangular head. 
    His brown hair is cut short and has a goatee, whereas his cheeks have distinct depressions."""
    abilities = ['Stealth']


# ========== Low Level
class Tempest_Serpent(Character):
    name = 'Tempest Serpent'
    species = 'Black Serpent'
    level = 6
    appearance = 'The snake has a large, jet-black body with thorned scales and tough skin.'
    description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'
    starting_state = ['sense heat source', 'poisonous breath']

class Giant_Bat(Character):
    name = 'Giant Bat'
    species = 'Bat'
    level = 6
    appearance = '''
    It's a giant bat...
    Due to its wings that regulate its own gravity, it's capable of flight
    '''
    description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'
    starting_state = ['ultrasound waves', 'vampirism']

class Evil_Centipede(Character):
    name = 'Evil Centipede'
    species = 'Centipede'
    level = 5
    appearance = 'Centipede monstrosity, a giant centipede.'
    description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'
    starting_state = ['paralyzing breath']

class Black_Spider(Character):
    name = 'Black Spider'
    species = 'Spider'
    level = 5
    appearance = 'Most of the body is yellow-ish, while the legs are black.'
    description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'
    starting_state = ['sticky thread', 'steel thread']


# ========== Wolves
class Direwolf(Character):
    name = 'Direwolf'
    species = 'Direwolf'
    level = 5
    appearance = 'Most of the body is yellow-ish, while the legs are black.'
    description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'
    evolution = 'Direwolf > Tempest Wolf > Star Wolf > Tempest Star Wolf'
    starting_state = []


# ========== Goblins
class Goblin(Character):
    name = 'Goblin'
    species = 'Goblin'
    level = 4
    appearance = 'They have green skin and a big nose. Their average height is 150 centimeters.'
    description = '''
    Goblins are of the monsters that populate The Great Jura Forest, with many different tribes dotting around the forest. 
    Although there are many different tribes of goblins, they will usually stand together in the face of great danger.
    
    Many of the goblins revere the Storm Dragon as their God and protector of the forest.

    For goblins, deaths are very common, to the point they have evolved to reproduce as much as possible to maintain their population.
    '''
    evolution = 'Goblin > Hobgoblin > Ogre > Kijin'


class Hobgoblin(Goblin):
    name = 'Hobgoblin'
    species = 'Hobgoblin'
    level = 5
    appearance = 'They have green skin like their pre-evolved form, but their average height is improved and his height now reaches around 180 centimeters.'
    description = 'Hobglins are evolved form of Gobins.'
    evolution = 'Goblin > Hobgoblin > Ogre > Kijin'
