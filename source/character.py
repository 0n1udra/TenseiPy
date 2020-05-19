from skills import *
from items import *

def ssprint(Msg):
    print(f'    {Msg}\n')

class Character:
    def __init__(self):
        self.name = ''
        self.familyName = ''
        self.species = ''
        self.info = ''

        self.inventoryCapacity = 0

        self.storyProgress = [None]

        self.attributes = {
            'Ultimate Skill' : {},
            'Unique Skill' : {},
            'Special Skill' : {},
            'Extra Skill' : {},
            'Intrinsic Skill' : {},
            'Battle Skill' : {},
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
        try:
            for sLvl, skills in self.attributes.items():
                for sName, skill in skills.items():
                    if usrInp.lower() == sName.lower():
                        try:
                            print(self.attributes[sLvl][sName].info)
                        except:
                            print("No available description for", sName)
        except: pass

        try:
            for iType, items in self.inventory.items():
                for iName, iObj  in items.items():
                    if usrInp.lower() == iName.lower():
                        try:
                            print(self.inventory[iType][iName].info)
                        except:
                            print("No available description for", iName)
        except: pass


    ##### Attributes #####
    def ShowAttributes(self):
        print(f"""
-----Attributes/Skills-----
Name: {self.name} {self.familyName}
""")
        # Prints players current skills, will not print out every type of skill unless player has said skills
        for sLvl, skills in self.attributes.items():
            if skills: # Checks if player has this type of skill
                print(f'{sLvl}:')
                for sName, sOb in skills.items():
                    print(f'\t{sName}')
        print()

    def AddAttribute(self, item):
        self.attributes[item.skillLevel][item.name] = item
        try:
            ssprint(item.acquiredMsg)
        except: pass

    def RemoveAttribute(self, item):
        for sLvl, skills in self.attributes.items():
            for sName, skill in skills.items():
                if item in skill:
                    # Finds corresponding item, and removes it from inventory
                    del self.attributes[sLvl][sName]

    def SkillUpgrade(self, skillFrom, skillTo):
        for sLvl, skills in self.attributes.items():
            for sName, skill in skills.items():
                if sName in skillFrom.name:
                    # Removes skill from inventory
                    del self.attributes[sLvl][sName]
                    break
        ssprint(f'<<{skillFrom.skillLevel} [{skillFrom}] evolving to {skillTo.skillLevel} [{skillTo}]...>>')
        self.AddAttribute(skillTo)


    ##### Inventory #####
    def ShowInventory(self):
        print('\n-----Inventory-----\n')
        for iType, item in self.inventory.items():
            if iType:
                print(f'{iType}:')
                for iName, iObj in item.items():
                    print(f'\t{iName}')
        print(f'\nCapacity: {self.inventoryCapacity}%\n')

    def AddInventory(self, item, amount=0, capacity=0):
        self.inventory[item.itemType][item.name] = item
        self.inventoryCapacity += capacity
        ssprint(item.AcquiredMsg())
        ssprint(f'<Inventory Capacity:, {self.inventoryCapacity:.2f}%>')

    def RemoveInventory(self, item):
        for iName, item in self.inventory.items():
            if item:
                if item in item:
                    # Finds corresponding item, and removes it from inventory
                    self.attributes[k].remove(item)



class Rimuru_Tempest(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Slime'
        self.info = """
    Species: Slime

    """
    def StartState(self):
        self.startState = [Self_Regeneration_Skill(), Absorb_Dissolve_Skill(), 
                Resist_Pain(), Resist_Melee(), Resist_Electricity(), Resist_Temperature()]
        for i in self.startState:
            self.AddAttribute(i)

class Veldora_Tempest():
    def __init__(self):
        self.name = "Veldora"
        self.itemType = 'Misc'
        self.familyName = ''


    def AcquiredMsg(self):
        self.info = f"""
    Name: Veldora {self.familyName}
    Species: True Dragon
    Title: Storm Dragon
    Rank: Disaster Special S
    Status: Alive
    """
        return(f"<<Acquired Veldora {self.familyName}>>")
        
veldora = Veldora_Tempest()

