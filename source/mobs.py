from mob funcs import Character

class Rimuru_Tempest(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Slime'
        self.mimicking = 'Slime'
        self.giveBlessing = 'Protection of Tempest'
        self.level = 7
        self.mimicObject = None
        self.startState = ['Mimic', 'Self-Regeneration', 'Absorb/Dissolve', 'Pain Resist', 'Melee Resist', 'Electricity Resist']
        self.UpdateInfo()

    # ========== Predator Functions
    def get_mimic(self):
        for lvl, lvlList in self.mimic_object().mimics.items():
            for name in lvlList:
                yield name

    def predate_targets(self, inpTargets):
        predateTargets = list(self.focusTargets)
        predateTargets.extend(inpTargets.split(','))
        for target in predateTargets:
            try:
                target = self.Generators(target, new=True)
                targetName = target.get_name()
            except:
                targetName = ''

            for mob in self.currentMobs:
                if not mob.alive:
                    if mob.get_name() in targetName:
                        self.add_mimicry(target)
                        ssprint(f'<<Analysis complete on {mob.name}.>>')

            try:
                if target.objectType == 'item':
                    self.AddInventory(target)
            except: pass

            self.focusTargets = set()

    def mimic_object(self, active=None):
        try:
            mimic = self.attributes['Unique Skill']['Mimic']
            mimic.active = active
            return mimic
        except: pass

    def add_mimicry(self, character):
        if not self.Generators(character, mimic=True):  # If already have mimic
            self.mimic_object().mimics[character.rank].append(character)
            ssprint(f'<<Note, new mimicry available: {character.name}.>>')
            self.ShowInfo(character)

    def can_mimic(self, character):
        if character == 'reset':
            self.mimicking, self.mimicObject = 'Slime', None  # Resets mimic variables
            ssprint("<Mimicry Reset>")
        else:
            try:
                currentMimic = self.Generators(character, True)
                self.mimicking, self.mimicObject = currentMimic.name, currentMimic
                ssprint(f'<Now Mimicking: {currentMimic.name}>')
            except: pass


class Veldora_Tempest(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = "Veldora"
        self.title = 'Storm Dragon'
        self.species = 'True Dragon'
        self.blessing = 'Storm Crest'
        self.alive = True
        self.level = 11
        self.itemType = 'Misc'
        self.capacityUse = 10
        self.UpdateInfo()

    def acquired_msg(self):
        self.UpdateInfo()
        return f"<<Acquired Veldora {self.familyName}>>"


# ========== Low Level
class Tempest_Serpent(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Tempest Serpent'
        self.Species = 'Serpent'
        self.level = 6
        self.appearance = 'The snake has a large, jet-black body with thorned scales and tough skin.'
        self.description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'

        self.startState = [skills.Sense_Heat_Source(), skills.Poisonous_Breath()]
        self.StartState()
        self.UpdateInfo()


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
        self.startState = [skills.Ultrasound_Waves(), skills.Vampirism_Skill()]
        self.StartState()
        self.UpdateInfo()


class Evil_Centipede(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Evil Centipede'
        self.Species = 'Centipede'
        self.level = 5
        self.appearance = '''
        Centipede monstrosity, a giant centipede.
        '''
        self.description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'
        self.startState = [skills.Paralyzing_Breath()]
        self.StartState()
        self.UpdateInfo()


class Black_Spider(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Black Spider'
        self.Species = 'Spider'
        self.level = 5
        self.appearance = '''
        Most of the body is yellow-ish, while the legs are black.
        '''
        self.description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'
        self.startState = [skills.Sticky_Thread(), skills.Steel_Thread()]
        self.StartState()
        self.UpdateInfo()

# ========== Wolves
class Tempest_Wolf(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Tempest Wolf'
        self.Species = 'Tempest Wolf'
        self.level = 5
        self.appearance = '''
        Most of the body is yellow-ish, while the legs are black.
        '''
        self.description = 'Found in the Sealed cave, spawned from the massive amount of magic essence emanating from the sealed Veldora.'
        self.evolution = 'Direwolf > Tempest Wolf > Star Wolf > Tempest Star Wolf'
        self.startState = [skills.Sticky_Thread(), skills.Steel_Thread()]
        self.StartState()
        self.UpdateInfo()
