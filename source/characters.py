import skills

def ssprint(Msg):
    print(f'    {Msg}\n')

class Character:
    def __init__(self):
        self.name = ''
        self.familyName = ''
        self.species = ''
        self.info = ''
        self.rank = ''
        self.level = 1
        self.inventoryCapacity = 0

        self.storyProgress = [None]
        self.savePath = ''
        self.textDelay = True
        self.lastCommand = ''

        # For predation
        self.amount = 0
        self.addAmount = 1
        self.capacityUse = 0

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


    def SetName(self, inpName, character):
        character.name = inpName

    def ShowInfo(self, usrInp, character=None):
        generators = [*self.AttributesGenerator(), *self.InventoryGenerator(), *self.MimicGenerator()]
        if not rimuru.mimicObject == None:
            generators.extend(self.AttributesGenerator(False, rimuru.mimicObject))

        try:
            for i in generators:
                if i.name.lower() == usrInp:
                    print(i.info)
        except: pass


    # ========== Attack
    def CheckResistance(self, character=None):
        for resistance in character['Resistance'].items():
            yield resistance

    def CanAttackA(self, attack, target):
        if self.mimicObject:
            for i in self.AttributesGenerator(self.mimicObject):
                if attack == i.name:
                    if CheckResistance(target) != i.damageType:
                        if target.level <= i.damageLevel:
                            return True
                            break
                        else:
                            print("<Target is too high of a level for that attack")
                    else:
                        print(f'<Target has resistance to {i.damageType}>'))


        

    # ========== Predator Functions
    def MimicGenerator(self):
        for lvl, lvlList in self.attributes['Unique Skill']['Mimic'].mimics.items():
            for name in lvlList:
                yield name

    def AddMimicry(self, character):
        self.attributes['Unique Skill']['Mimic'].mimics[character.rank].append(character)
        print(f'New mimicry available: {character.name}')

    def CanMimic(self, character):
        if character == 'reset':
            self.mimic = 'Slime'
            self.mimicObject = None
            self.attributes['Unique Skill']['Mimic'].active = False
            print("<Mimicry Reset>")
        else:
            for i in self.MimicGenerator():
                if character == i.name.lower():
                    self.mimic = i.name
                    self.mimicObject = i
                    self.attributes['Unique Skill']['Mimic'].active = True
                    print(f'<Now Mimicking: {i.name}>')
                    break


    # ========== Attribute Functions
    def AttributesGenerator(self, output=False, character=None):
        if character:
            character = character.attributes
        else:
            character = self.attributes

        for skillType, skills in character.items():
            # Only shows yields skill type if skill list is not empty
            if output and skills:
                yield(f'{skillType}:')

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

    def ShowAttributes(self):
        print(f"""
-----Attributes/Skills-----
Name: {self.name} {self.familyName}
""")
        for i in self.AttributesGenerator(True):
            print(i)

        if self.mimicObject:
            print("\n-----Mimicry-----\n", end='')
            print(f"Mimicking: {self.mimic}\n")
            for j in self.AttributesGenerator(True, Tempest_Serpent()):
                print(j)


    def AddAttribute(self, item):
        self.attributes[item.rank][item.name] = item
        # Tries to print skill acquisition message
        try: 
            ssprint(item.acquiredMsg)
        except: pass

    def RemoveAttribute(self, skill):
        del self.attributes[skill.rank][skill.name]

    def SkillUpgrade(self, skillFrom, skillTo):
        self.RemoveAttribute(skillFrom)
        ssprint(f'<<{skillFrom.rank} [{skillFrom}] evolving to {skillTo.rank} [{skillTo}]...>>')
        self.AddAttribute(skillTo)


    # ========== Inventory Functions
    def InventoryGenerator(self, output=False):
        for itemType, items in self.inventory.items():
            if output and items:
                yield(f'{itemType}:')
            for itemName, itemObject in items.items():
                if output:
                    yield(f'\t{self.inventory[itemType][itemName].amount}x {itemObject.name}')
                else: 
                    yield(itemObject)

    def ShowInventory(self):
        print('\n-----Inventory-----')
        print(f'Capacity: {self.inventoryCapacity}%\n')
        for i in self.InventoryGenerator(True):
            print(i)

    def AddInventory(self, item):
        try:
            self.inventory[item.itemType][item.name].amount += item.addAmount
        except:
            self.inventory[item.itemType][item.name] = item
            self.inventory[item.itemType][item.name].amount += item.addAmount
        self.inventoryCapacity += item.capacityUse
        ssprint(item.AcquiredMsg() + f' | Total: {self.inventory[item.itemType][item.name].amount}>')
        ssprint(f'<Inventory Capacity: {self.inventoryCapacity:.2f}%>')

    def RemoveInventory(self, item):
        try:
            self.inventory[item.itemType].remove(item)
        except:
            print(f'<Error deleting {item.name} from inventory>')



#                    ========== Characters ==========
class Rimuru_Tempest(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Slime'
        self.mimic = 'Slime'
        self.mimicObject = None
        self.info = """
    Species: Slime

    """
    def StartState(self):
        self.startState = [skills.Predator_Mimicry_Skill(), skills.Self_Regeneration(), skills.Absorb_Dissolve(), 
                skills.Resist_Pain(), skills.Resist_Melee(), skills.Resist_Electricity(), skills.Resist_Temperature()]
        for i in self.startState:
            self.AddAttribute(i)

class Veldora_Tempest(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = "Veldora"
        self.itemType = 'Misc'
        self.familyName = ''
        self.capacityUse = 10

    def AcquiredMsg(self):
        self.info = f"""
    Name: Veldora {self.familyName}
    Species: True Dragon
    Title: Storm Dragon
    Rank: Disaster Special S
    Status: Alive
    """
        return(f"<<Acquired Veldora {self.familyName}>>")

class Tempest_Serpent(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Tempest Serpent'
        self.rank = 'A-'
        self.info = """
Species: Tempest Serpent
Rank: A-
"""
        
        self.startState = [skills.Sense_Heat_Source(), skills.Poisonous_Breath()]
        for i in self.startState:
            self.AddAttribute(i)


# ========== Rimuru
rimuru = None
def UpdateCharacter(character):
    global rimuru
    rimuru = character
    return rimuru
veldora = Veldora_Tempest()
