import skills

def ssprint(Msg):
    print(f'    {Msg}\n')

class Character:
    def __init__(self):
        self.name = ''
        self.familyName = ''
        self.species = ''
        self.info = ''
        self.level = ''
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
        for i in (*self.AttributesGenerator(), *self.InventoryGenerator()):
            if i.name.lower() == usrInp:
                print(i.info)


    # ========== Predator Functions
    def AddMimicry(self, character):
        self.attributes['Unique Skill']['Mimic'].mimics[character.level].append(character)
        print(f'New mimicry available: {character.name}')

    def CanMimic(self, character):
        if character == 'reset':
            self.mimic = 'Slime'
            self.attributes['Unique Skill']['Mimic'].active = False
            print("<Mimicry Reset>")
        else:
            for lvl, lvlList in self.attributes['Unique Skill']['Mimic'].mimics.items():
                for name in lvlList:
                    if character == name.name.lower():
                        self.mimic = name.name
                        print(f'<Now Mimicking: {name.name}>')
                        self.attributes['Unique Skill']['Mimic'].active = True
                        break


    # ========== Attribute Functions
    def AttributesGenerator(self, output=False):
        for skillType, skills in self.attributes.items():
            # Only shows yields skill type if skill list is not empty
            if output and skills:
                yield(f'{skillType}:')
            for skillName, skillObject in skills.items():
                if output: 
                    if skillObject.active:
                        yield(f'\t{skillObject.name} (Active)')
                    elif skillObject.passive:
                        yield(f'\t{skillObject.name} (Passive)')
                    else:
                        yield(f'\t{skillObject.name}')
                else: 
                    yield(skillObject)

    def ShowAttributes(self):
        print(f"""
-----Attributes/Skills-----
Name: {self.name} {self.familyName}
Mimic: {self.mimic}\n
""")
        for i in self.AttributesGenerator(True):
            print(i)

    def AddAttribute(self, item):
        self.attributes[item.level][item.name] = item
        # Tries to print skill acquisition message
        try: ssprint(item.acquiredMsg)
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
                    yield(f'\t{self.inventory[itemType][itemName].amount}x {itemName}')
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
            self.inventory[item.itemType].remove(item.name)
        except:
            print(f'<Error deleting {item.name} from inventory>')



#                    ========== Characters ==========
class Rimuru_Tempest(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Slime'
        self.mimic = 'Slime'
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

    @property
    def acquiredMsg(self):
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
        self.level = 'A-'
        self.info = ''
        self.attributes = {
                'Intrinsic Skill': [skills.Sense_Heat_Source(), skills.Poisonous_Breath()],
                }

# ========== Rimuru
rimuru = None
def UpdateCharacter(character):
    global rimuru
    rimuru = character
    return rimuru
veldora = Veldora_Tempest()
