import skills, items

def ssprint(Msg):
    print(f'    {Msg}\n')

class Character:
    def __init__(self):
        self.name = 'N/A'
        self.familyName = ''
        self.title = 'N/A'
        self.species = 'N/A'
        self.rank = 'N/A'
        self.level = 1
        self.divineProtection = 'N/A'
        self.info = 'N/A'
        self.appearance = 'N/A'
        self.description = 'N/A'
        self.alive = True
        self.invisible = False
        self.movement = False # If monster is moving too fast for attack, use sticky thread

        # Game variables
        self.storyProgress = [None]
        self.savePath = ''
        self.textDelay = True
        self.lastCommand = ''
        self.currentMobs = []
        self.focusTargets = set()

        # For predator
        self.amount = 0
        self.addAmount = 1
        self.capacityUse = 0
        self.inventoryCapacity = 0
        self.objectType = 'character'

        self.attributes = {
            'Ultimate Skill' : {},
            'Unique Skill' : {},
            'Special Skill' : {},
            'Extra Skill' : {},
            'Intrinsic Skill' : {},
            'Common Skill' : {},
            'Daily Skill' : {},
            'Composite Skill' : {},
            'Resistance' : {},
            'Attribute' : {},
            'Manas' : {},
            }

        self.inventory = {
            'Items' : {},
            'Material' : {},
            'Potions' : {},
            'Misc' : {},
        }

    def GetName(self):
        return self.name.lower()


    def SetTarget(self, targets):
        if 'reset' in targets:
            self.focusTargets = []
        else:
            for target in targets.split(','):
                for i in self.currentMobs:
                    if i.GetName() in target:
                        self.focusTargets.add(i)
                        break


    # ========== Info
    def Generators(self, inp, mimic=False, new=False):
        try:
            inp = inp.name # If input is an object
        except: pass

        generators = [*self.AttributesGenerator(), *self.InventoryGenerator(), *self.MimicGenerator()]
        if new:
            generators = [*items.Item.__subclasses__(), *skills.Skill.__subclasses__(), *Character.__subclasses__()]
        if mimic:
            generators = [*self.MimicGenerator()]

        # Adds mimicked monster abilities if currently using mimic
        if rimuru.mimicObject:
                generators.extend(self.AttributesGenerator(rimuru.mimicObject))
        try:
            for i in generators:
                if new: 
                    i = i()
                if i.GetName() in inp.lower():
                    return i
        except: pass

    def SetName(self, inpName, character):
        character.name = inpName

    def StartState(self):
        for i in self.startState:
            self.AddAttribute(i, showInfo=False, output=False)

    def UpdateInfo(self):
        self.info = f"""
    Name: {self.name} {self.familyName}
    Title: {self.title}
    Species: {self.species}
    Rank: {self.rank}
    Alive: {self.alive}
    Divine Protection: {self.divineProtection}

    Description:
        {self.description}

    Appearance:
        {self.appearance}
        """

        # Sets ranking according to level
        ranking = ['Special S', 'S', 'Special A' ,'A+', 'A', 'A-', 'B', 'C', 'D', 'E', 'F']
        self.rank = ranking[self.level-1]

    def ShowInfo(self, usrInp):
        try:
            print(self.Generators(usrInp).info)
        except: pass

    def CheckStatus(self, target):
        try:
            for i in self.currentMobs:
                if target in i.getName():
                    return True
        except: pass

    def UpdateRanking(self, level):
        self.level = level
        self.UpdateInfo()
        ssprint(f"<Leveled up to rank {self.rank}>")

    def UseSkill(self, skill):
        try:
            if self.Generators(skill).UseSkill():
                return True
        except: pass


    # ========== Attack
    def CheckResistance(self, character, attack):
        # Checks if character has resistance attribute
        for resistName, resistObject in character.attributes['Resistance'].items():
            for resist in resistObject.resistTypes:
                if resist.lower() == attack.lower():
                    return True
                    break

    def CanAttack(self, usrInput, rimuru=False):
        targets, attacks = self.focusTargets, []
        try:
            splitInput = usrInput.split(',')
        except: 
            splitInput = usrInput

        for i in self.currentMobs:
            if i.GetName() in usrInput and i.alive:
                targets.add(i)
                self.focusTargets.add(i)

        for i in splitInput:
            skill = self.Generators(i)
            if skill:
                if skill.GetName() in i.lower() and skill.objectType == 'skill':
                    attacks.append(self.Generators(skill))

        if 'rimuru' in usrInput:
            targets.add(rimuru)

        attacked = attackSuccess = False

        for currentTarget in targets:
            for currentAttack in attacks:
                if not self.CheckResistance(currentTarget, currentAttack.damageType):
                    if currentTarget.level <= currentAttack.damageLevel:
                        currentTarget.alive = False
                        attackSuccess = attacked = True
                        ssprint(f'<Eliminated {currentTarget.name}.>')
                    else:
                        ssprint(f"<{currentTarget.name} level too for that attack.>")
                        attacked = True
                else:
                    ssprint(f'<<Warning,{currentTarget.name} has resistance to {currentAttack.damageType}.>>')
                    attacked = True
        return attacked, attackSuccess


    # ========== Attribute Functions
    def AttributesGenerator(self, target=None, output=False):
        character = self.attributes
        if target: 
            character = target.attributes # If no specified character

        for skillType, skills in character.items():
            if output and skills: 
                yield(f'{skillType}:') # If output=True prints out skillType
            for skillName, skillObject in skills.items():
                if output: 
                    if skillObject.active:
                        yield(f'\t{skillName} (Active)')
                    elif skillObject.passive:
                        yield(f'\t{skillName} (Passive)')
                    else:
                        yield(f'\t{skillName}')
                else: 
                    yield(skillObject)

    def ShowAttributes(self, character=None):
        if not character:
            character, showMimic = rimuru, True
        else:
            showMimic = False
            # Get stats for other monsters
            try: 
                character = self.Generators(character, True)
            except: pass

        print(f"""
-----Attributes/Skills-----
Name: {character.name} {character.familyName}
""")
        for i in self.AttributesGenerator(character, output=True):
            print(i)

        # Only shows mimicry info when not looking at stats of other monsters or in mimicry
        if self.mimicObject and showMimic:
            print("\n\t-----Mimicry-----")
            print(f"\tMimicking: {self.mimicking}\n")
            for j in self.AttributesGenerator(self.mimicObject, True):
                print(f'\t{j}')


    def AddAttribute(self, item, showInfo=False, output=True):
        try:
            self.attributes[item.skillLevel][item.name]
        except:
            self.attributes[item.skillLevel][item.name] = item
            if output:
                try: 
                    ssprint(item.acquiredMsg)
                except: pass
            if showInfo: self.ShowInfo(item.name) # Shows skill info

    def RemoveAttribute(self, skill):
        try:
            del self.attributes[skill.skillLevel][skill.name]
        except:
            print("ERROR Deleting attribute. If you're seeing this message, please let developer know")

    def SkillUpgrade(self, skillFrom, skillTo):
        self.RemoveAttribute(skillFrom)
        ssprint(f'<<{skillFrom.skillLevel} [{skillFrom}] evolving to {skillTo.skillLevel} [{skillTo}]...>>')
        self.AddAttribute(skillTo)


    # ========== Inventory Functions
    def InventoryGenerator(self, output=False):
        for itemType, items in self.inventory.items():
            if output and items: 
                yield(f'{itemType}:') # If output=True prints out itemType also
            for itemName, itemObject in items.items():
                if output:
                    yield(f'\t{self.inventory[itemType][itemName].amount}x {itemObject.name}')
                else:  
                    yield(itemObject)

    def ShowInventory(self):
        print('\n-----Inventory-----')
        print(f'Capacity: {self.inventoryCapacity}%\n')
        for i in self.InventoryGenerator(True): print(i) # Prints out inventory items

    def AddInventory(self, item):
        try:
            self.inventory[item.itemType][item.name].amount += item.addAmount
        except:
            self.inventory[item.itemType][item.name] = item
            self.inventory[item.itemType][item.name].amount += item.addAmount
            self.ShowInfo(item)
        self.inventoryCapacity += item.capacityUse
        ssprint(item.AcquiredMsg() + f' | Total: {self.inventory[item.itemType][item.name].amount}>')
        ssprint(f'<Inventory Capacity: {self.inventoryCapacity:.2f}%>')

    def RemoveInventory(self, item):
        try:
            self.inventory[item.itemType].remove(item)
        except:
            ssprint(f'<Error deleting {item.name} from inventory>')


#                    ========== Characters ==========
class Rimuru_Tempest(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Slime'
        self.mimicking = 'Slime'
        self.level = 7
        self.mimicObject = None
        self.startState = [skills.Predator_Mimicry_Skill(), skills.Self_Regeneration(), skills.Absorb_Dissolve(), 
                    skills.Resist_Pain(), skills.Resist_Melee(), skills.Resist_Electricity(), skills.Resist_Temperature()]
        self.UpdateInfo()

    # ========== Predator Functions
    def MimicGenerator(self):
        for lvl, lvlList in self.MimicObject().mimics.items():
            for name in lvlList:
                yield name

    def PredateTarget(self, inpTargets):
        predateTargets = list(self.focusTargets)
        predateTargets.extend(inpTargets.split(','))
        for target in predateTargets:
            try:
                target = self.Generators(target, new=True)
                targetName = target.GetName()
            except:
                targetName = ''

            for mob in self.currentMobs:
                if not mob.alive:
                    if mob.GetName() in targetName:
                        self.AddMimicry(target)
                        ssprint(f'<<Analysis complete on {mob.name}.>>')

            try:
                if target.objectType == 'item':
                    self.AddInventory(target)
                    ssprint(f'<<Analysis on {target.name} successful.>>')
            except: pass

            self.focusTargets = set()


    def MimicObject(self, active=None):
        mimic = self.attributes['Unique Skill']['Mimic']
        mimic.active = active
        return mimic

    def AddMimicry(self, character):
        if not self.Generators(character, mimic=True): # If already have mimic
            self.MimicObject().mimics[character.rank].append(character)
            ssprint(f'<<Note, new mimicry available: {character.name}.>>')
            self.ShowInfo(character)

    def CanMimic(self, character):
        if character == 'reset':
            self.mimicking, self.mimicObject = 'Slime', None # Resets mimic variables
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
        self.alive = True
        self.level = 11
        self.itemType = 'Misc'
        self.capacityUse = 10
        self.UpdateInfo()

    def AcquiredMsg(self):
        self.UpdateInfo()
        return(f"<<Acquired Veldora {self.familyName}>>")

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

# ========== Rimuru
rimuru = None
def UpdateCharacter(character):
    global rimuru
    rimuru = character
    return rimuru
veldora = Veldora_Tempest()
