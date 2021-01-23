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
        self.starting_state = ['Mimic', 'Self-Regeneration', 'Absorb/Dissolve', 'Pain Resist', 'Melee Resist', 'Electricity Resist']
        self.update_info()

    # ========== Predator Functions
    def mimic_generator(self):
        """
        Yields available mimic mob objects.

        Returns:
            mimic: Yields character objects that are in acquired_mimicries dictionary.
        """

        if not self.mimic_object():
            return None

        for level, mimics in self.mimic_object().acquired_mimicries.items():
            for mimic_name, mimic in mimics.items():
                yield mimic

    def mimic_object(self, active=None):
        """
        Args:
            active: Sets whether mimic is being used or not.

        Returns:
            mimic: Mimic object from .attributes.

        """

        if mimic := self.check_acquired('Mimic'):
            mimic.active = active
            return mimic

    def add_mimic(self, mob):
        """
        Adds new monster mimicry.

        Args:
            mob: Character object to add to acquired_mimicries list
        """

        # Basically checks if self is the rimuru object (player).
        if not self.mimic_object():
            return False

        # Checks if already acquired.
        if mob.name in self.mimic_object().acquired_mimicries[mob.rank]:
            return None

        # Adds new mob object to usable mimicries dict.
        self.mimic_object().acquired_mimicries[mob.rank][mob.name] = mob

        # Adds attributes from mob just analyzed.
        for attribute in mob.attributes_generator():
            self.add_attribute(attribute, top_newline=False, bot_newline=False)

        print(f"\n    << Information, analysis on [{mob.name}] completed. >>")
        print(f"    << Notice, new skills and mimicry available. >>\n")

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
            print("    < Mimicry Reset >")
        else:
            if new_mimic := self.get_object(character, [*self.mimic_generator()]):
                self.current_mimic_species = new_mimic.species
                self.current_mimic = new_mimic
                self.mimic_object(active=True)
                print(f'    < Now Mimicking [{new_mimic.name}] >')

    def check_mimic(self, match=None):
        if m_object := self.mimic_object():
            if match is None:
                return m_object.name
            if match.lower() in m_object.name.lower():
                return m_object.name
            else: return False
        else: return False

    def eat_targets(self, input_targets=''):
        """
        Predates targets that are being focused. Also adds target mimicry.

        Args:
            input_targets: Target to eat.

        Usage:
            > eat
        """

        for target in self.targeted_mobs:
            if not target[0]: continue

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
        for i in self.targeted_mobs:
            if i[0].is_alive is False:
                self.eat_targets()

class Veldora_Tempest(Character):
    def __init__(self, name=None):
        Character.__init__(self)
        self.name = "Veldora"
        if name: self.name = name
        self.title = 'Storm Dragon'
        self.canon_name = 'Veldora Tempest'
        self.species = 'True Dragon'
        self.blessing = 'Storm Crest'
        self.is_alive = True
        self.level = 11
        self.inventory_capacity_add = 10
        self.update_info()


# ========== Low Level
class Tempest_Serpent(Character):
    def __init__(self, name=None):
        Character.__init__(self)
        self.name = 'Tempest Serpent'
        if name: self.name = name
        self.species = 'Serpent'
        self.level = 6
        self.appearance = 'The snake has a large, jet-black body with thorned scales and tough skin.'
        self.description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'
        self.starting_state = ['sense heat source', 'poisonous breath']
        self.set_start_state()
        self.update_info()

class Giant_Bat(Character):
    def __init__(self, name=None):
        Character.__init__(self)
        self.name = 'Giant Bat'
        if name: self.name = name
        self.species = 'Bat'
        self.level = 6
        self.appearance = '''
        It's a giant bat...
        Due to its wings that regulate its own gravity, it's capable of flight
        '''
        self.description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'
        self.starting_state = ['ultrasound waves', 'vampirism']
        self.set_start_state()
        self.update_info()

class Evil_Centipede(Character):
    def __init__(self, name=None):
        Character.__init__(self)
        self.name = 'Evil Centipede'
        if name: self.name = name
        self.species = 'Centipede'
        self.level = 5
        self.appearance = 'Centipede monstrosity, a giant centipede.'
        self.description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'
        self.starting_state = ['paralyzing breath']
        self.set_start_state()
        self.update_info()

class Black_Spider(Character):
    def __init__(self, name=None):
        Character.__init__(self)
        self.name = 'Black Spider'
        if name: self.name = name
        self.species = 'Spider'
        self.level = 5
        self.appearance = 'Most of the body is yellow-ish, while the legs are black.'
        self.description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'
        self.starting_state = ['sticky thread', 'steel thread']
        self.set_start_state()
        self.update_info()


# ========== Wolves
class Tempest_Wolf(Character):
    def __init__(self, name=None):
        Character.__init__(self)
        self.name = 'Tempest Wolf'
        if name: self.name = name
        self.species = 'Tempest Wolf'
        self.level = 5
        self.appearance = 'Most of the body is yellow-ish, while the legs are black.'
        self.description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'
        self.evolution = 'Direwolf > Tempest Wolf > Star Wolf > Tempest Star Wolf'
        self.starting_state = []
        self.set_start_state()
        self.update_info()


# ========== Goblins
class Goblin(Character):
    def __init__(self, name=None):
        Character.__init__(self)
        self.name = 'Goblin'
        if name: self.name = name
        self.species = 'Goblin'
        self.level = 4
        self.appearance = 'They have green skin and a big nose. Their average height is 150 centimeters.'
        self.description = '''
        Goblins are of the monsters that populate The Great Jura Forest, with many different tribes dotting around the forest. 
        Although there are many different tribes of goblins, they will usually stand together in the face of great danger.
        
        Many of the goblins revere the Storm Dragon as their God and protector of the forest.

        For goblins, deaths are very common, to the point they have evolved to reproduce as much as possible to maintain their population.
        '''
        self.evolution = 'Goblin > Hobgoblin > Ogre > Kijin'
        self.update_info()

class Hobgoblin(Goblin):
    def __init__(self, name=None):
        Goblin.__init__(self)
        self.name = 'Hobgoblin'
        if name: self.name = name
        self.species = 'Hobgoblin'
        self.level = 5
        self.appearance = 'They have green skin like their pre-evolved form, but their average height is improved and his height now reaches around 180 centimeters.'
        self.description = 'Hobglins are evolved form of Gobins.'
        self.evolution = 'Goblin > Hobgoblin > Ogre > Kijin'
        self.update_info()
