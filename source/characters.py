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
        # Adds mimicked monster abilities 
        if rimuru.mimicObject:
            generators.extend(self.AttributesGenerator(rimuru.mimicObject))

        try:
            for i in generators:
                if i.name.lower() == usrInp.lower():
                    print(i.info)
        except: pass


    # ========== Attack
    def CheckResistance(self, checkResist, character=None):
        # Checks if character has resistance attribute
        for resistName, resistObject in character.attributes['Resistance'].items():
            for resist in resistObject.resistTypes:
                if resist.lower() == checkResist.lower():
                    return True
                    break

    def CanAttack(self, attack, target=None):
        attacked = attackSuccess = False
        if attack == '':
            return False, False
        generators = [*self.AttributesGenerator(self.mimicObject)]
        if rimuru.mimicObject:
            generators.extend(self.AttributesGenerator(rimuru.mimicObject))

        for i in generators:
            if attack == i.name.lower():
                if not self.CheckResistance(i.damageType, target):
                    if target.level <= i.damageLevel:
                        attackSuccess = attacked = True
                        break
                    else:
                        print("\t<Target is too high of a level for that attack\n")
                        attacked = True
                        break
                else:
                    print(f'\t<<Note, target has resistance to {i.damageType}>\n')
                    attacked = True
                    break
        return attacked, attackSuccess


    # ========== Predator Functions
    def MimicGenerator(self):
        for lvl, lvlList in self.attributes['Unique Skill']['Mimic'].mimics.items():
            for name in lvlList:
                yield name

    def AddMimicry(self, character):
        self.attributes['Unique Skill']['Mimic'].mimics[character.rank].append(character)
        print(f'\t<<Note, new mimicry available: {character.name}.>>\n')

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
    def AttributesGenerator(self, target=None, output=False):
        character = self.attributes
        if target:
            character = target.attributes

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

    def ShowAttributes(self, character=None):
        if not character:
            character = rimuru
            showMimic = True
        else:
            showMimic = False
            # Get stats for other monsters
            for i in self.MimicGenerator():
                if i.name.lower() == character.lower():
                    character = i

        print(f"""
-----Attributes/Skills-----
Name: {character.name} {character.familyName}
""")
        for i in self.AttributesGenerator(character, output=True):
            print(i)

        # Only shows mimicry info when not looking at stats of other monsters or in mimicry
        if self.mimicObject and showMimic:
            print("\n-----Mimicry-----")
            print(f"Mimicking: {self.mimic}\n")
            for j in self.AttributesGenerator(self.mimicObject, True):
                print(j)


    def AddAttribute(self, item):
        self.attributes[item.level][item.name] = item
        # Tries to print skill acquisition message
        try: 
            ssprint(item.acquiredMsg)
        except: pass

    def RemoveAttribute(self, skill):
        del self.attributes[skill.level][skill.name]

    def SkillUpgrade(self, skillFrom, skillTo):
        self.RemoveAttribute(skillFrom)
        ssprint(f'<<{skillFrom.level} [{skillFrom}] evolving to {skillTo.level} [{skillTo}]...>>')
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

# ========== Low Level
class Tempest_Serpent(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Tempest Serpent'
        self.rank = 'A-'
        self.info = """
Species: Tempest Serpent
Rank: A-

Appearance:
    The snake has a large, jet-black body with thorned scales and tough skin.
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
