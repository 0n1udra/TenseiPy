def ssprint(Msg):
    print(f'    {Msg}\n')

class Character:
    def __init__(self):
        self.name = ''
        self.familyName = ''
        self.species = ''
        self.info = ''

        self.inventoryCapacity = 0

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
            'Resistence' : {},
            'Attribute' : {},
            'Manas' : {},
            }

        self.inventory = {
            'Items' : {},
            'Material' : {},
            'Potions' : {},
            'Misc' : {},
        }

    def ShowInfo(self, showSkill, character=None):
        for sLvl, skills in self.attributes.items():
            for sName, skill in skills.items():
                if showSkill.lower() == sName.lower():
                    try:
                        print(self.attributes[sLvl][sName].info)
                    except:
                        print("No available description for", sName)

    ##### Attributes #####
    def ShowAttributes(self):
        attrBanner = f"""
-----Attributes/Skills-----
Name: {self.name} {self.familyName}
Species: {self.species}

"""
        print(attrBanner)
        # Prints players current skills, will not print out every type of skill unless player has said skills
        for sLvl, skills in self.attributes.items():
            if skills: # Checks if player has this type of skill
                print(f'{sLvl}:')
                for sName, sOb in skills.items():
                    print(f'\t{sName}')
        print()

    def AddAttribute(self, item):
        self.attributes[item.skillLevel][item.name] = item
        ssprint(item.AcquiredMsg())

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
        ssprint(f'<<{skillFrom.skillLevel} [{skillFrom}] upgrading to {skillTo.skillLevel} [{skillTo}]...>>')
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
        ssprint(f'<Inventory Capacity:, {self.inventoryCapacity}%>')

    def RemoveInventory(self, item):
        for iName, item in self.inventory.items():
            if item:
                if item in item:
                    # Finds corresponding item, and removes it from inventory
                    self.attributes[k].remove(item)

    def SetName(self, inpName, character):
        character.name = inpName

class Rimuru_Tempest(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Slime'
        self.species = 'Slime'
        self.info = """

    """

class Veldora_Tempest(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = "Veldora"
        self.info = """
    Species: True Dragon
    Title: Storm Dragon
    Rank: Disaster Special S
    Status: Alive
    """

