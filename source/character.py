class Character:
    def __init__(self):
        self.name = ''
        self.species = ''
        self.status = ''

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

    ##### Attributes #####
    def ShowAttributes(self):
        print('\n-----Attributes/Skills-----\n')
        # Prints players current skills, will not print out every type of skill unless player has said skills
        for sLvl, skills in self.attributes.items():
            if skills: # Checks if player has this type of skill
                print(f'{sLvl}:')
                for sName, sOb in skills.items():
                    print(f'\t{sName}')

        print('\n-----Attributes/Skills-----\n')


    def ShowInfo(self, showSkill, character=None):
        for sLvl, skills in self.attributes.items():
            for sName, skill in skills.items():
                if showSkill.lower() == sName.lower():
                    try:
                        print(self.attributes[sLvl][sName].info)
                    except:
                        print("No available description for", sName)



    def AddAttribute(self, item):
        self.attributes[item.skillLevel][item.name] = item
        print(item.AcquiredMsg())


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
        print(f'<<{skillFrom.skillLevel} [{skillFrom}] upgrading to {skillTo.skillLevel} [{skillTo}]...>>')
        self.AddAttribute(skillTo)

    ##### Inventory #####
    def showInventory(self):
        print('\n-----Inventory-----\n')
        for iType, item in self.inventory.items():
            if iType:
                print(f'{iType}:')
                for iName, iObj in item:
                    print(f'\t{i}')
        print(f'\nCapacity: {self.inventoryCapacity}%')
        print('\n-----Inventory-----\n')

    def AddInventory(self, item, amount=0, capacity=0):
        self.inventory[item.itemType][item.name] = item
        self.inventoryCapacity = capacity
        print(item.AcquiredMsg())

    def RemoveInventory(self, item):
        for iName, item in self.inventory.items():
            if item:
                if item in item:
                    # Finds corresponding item, and removes it from inventory
                    self.attributes[k].remove(item)

class Rimuru_Tempest(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = 'Rimuru Tempest'
        self.species = 'Slime'
        
