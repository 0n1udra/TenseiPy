
class Inventory:
    def __init__(self):

        inventoryCapacity = 0

        self.playerAttributes = {

        'Ultimate Skill' : [],
        'Unique Skill' : [],
        'Special Skill' : [],
        'Extra Skill' : [],
        'Intrinsic Skill' : [],
        'Battle Skill' : [],
        'Common Skill' : [],
        'Daily Skill' : [],
        'Composite Skill' : [],
        'Resistence' : [],
        'Attribute' : [],
        'Mana' : [],
        }

        self.playerInventory = {
        'Items' : [],
        'Material' : [],
        'Potions' : [],
        'Misc' : [],

        }

    ##### Attributes #####
    def showAttributes(self):
        print('\n-----Attributes/Skills-----\n')
        # Prints players current skills, will not print out every type of skill unless player has said skills
        for k, v in self.playerAttributes.items():
            if v: # Checks if player has this type of skill
                print(f'{k}:')
                for i in v:
                    print(f'\t{i}')
        print('\n-----Attributes/Skills-----\n')

    def addAttribute(self, item):
        self.playerAttributes[item.skillLevel].append(item)
        print(item.acquired())


    def removeAttribute(self, item):
        for k, v in self.playerAttributes.items():
            if v:
                if item in v:
                    # Finds corresponding item, and removes it from inventory
                    self.playerAttributes[k].remove(item)


    def skillUpgrade(self, skillFrom, skillTo):
        for k, v in self.playerAttributes.items():
            if v:
                for i in v:
                    if i.name in skillFrom.name:
                        # Removes skill from inventory
                        self.playerAttributes[k].remove(i)
        print(f'<<{skillFrom.skillLevel} [{skillFrom}] upgrading to {skillTo.skillLevel} [{skillTo}]...>>')
        self.addAttribute(skillTo)


    ##### Inventory #####
    def showInventory(self):
        print('\n-----Inventory-----\n')
        for k, v in self.playerInventory.items():
            if v:
                print(f'{k}:')
                for i in v:
                    print(f'\t{i}')
        print('\n-----Inventory-----\n')

    def addInventory(self, item, amount=0, capacity=0):
        self.playerInventory[item.itemType].append(item)
        #print(item.acquired())


    def removeInventory(self, item):
        for k, v in self.playerIventory.items():
            if v:
                if item in v:
                    # Finds corresponding item, and removes it from inventory
                    self.playerAttributes[k].remove(item)

    #####

class Skill:
    def __init__(self):
        self.name = ''
        self.skillLevel = ''
        self.acquredMsg = ''

        self.skillPower = 0
        self.energy = 0

        self.predate = True

    def acquired(self):
        return(self.acquiredMsg)

    def __str__(self):
        return(self.name)



##### Extra Skills #####

class Sage_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Sage'
        self.skillLevel = 'Extra Skill'
        self.acquiredMsg = "<<Extra skill: [Sage] has been successfully acquired.>>"


##### Unique Skills #####

class Predator_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Predator'
        self.skillLevel = 'Unique Skill'
        self.acquiredMsg = "<<Unqiue skill [Predator] successfully acquired.>>"

class Great_Sage_Skill(Skill):
    def __init__(self):
        Skill.__init__(self)

        self.name = 'Great Sage'
        self.skillLevel = 'Unique Skill'
        self.acquiredMsg = "<<Unqiue skill [Great Sage] acquired.>>"

