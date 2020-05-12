
from skills import *

class Scene_Template:

    def __init__(self):
        self.SceneStart()

    def Actions(self, usrInp, actions, funcs):
        # Runs through each function available
        for i in range(len(funcs)):
            for j in actions[i]:
                # Checks if user input matches one of the available actions
                if usrInp.lower() in j:
                    # Runs corresponding function
                    funcs[i]()
#            if usrInp.lower() in actions[i]:
#                print("true")

    def init(self):
        pass

    def SceneStart(self):
        pass




class Inventory:
    def __init__(self):

        self.playerInventory = {

        'Ultimate Skills' : [],
        'Unique Skills' : [],
        'Special Skills' : [],
        'Extra Skills' : [],
        'Intrinsic Skills' : [],
        'Battle Skills' : [],
        'Common Skills' : [],
        'Daily Skills' : [],
        'Composite Skills' : [],
        'Resistences' : [],
        'Attributes' : [],
        'Manas' : []
        }

    def showIventory(self):
        print()
        # Prints players current skills, will not print out every type of skill unless player has said skills
        for k, v in self.playerInventory.items():
            if v: # Checks if player has this type of skill
                print(f'{k}:')
                for i in v:
                    i = i.__str__(self)
                    print(f'\t{i}')

    def removeInventory(self, item):
        for k, v in self.playerInventory.items():
            if v:
                if item in v:
                    print("Test")

class Scene_Intro(Scene_Template):


    def SceneStart(self):
        print("Current Skills:")
        print("<<Confirmation Complete. Acquiring Skill [Predator]>>")
        Predator_Skill.acquireSkill(slime)

        Sage_Skill.acquireSkill(slime)
        print(slime.showIventory())

        slime.playerInventory['Extra Skills'].remove(Sage_Skill)
        print(slime.showIventory())
        print("\nYou wake up, or at least you think you are 'awake'")

        #actions = [MoveArms, MoveLegs]
        print("\nAvailable Actions: Move Arms, Move Legs")
        self.usrInp = input("\n> ")
        self.Actions(self.usrInp, [['move arms', 'twitch arms'], ['move legs']], [self.MoveArms, self.MoveLegs])

        print("You figure out how to move forward")
        print("You feel something rub against your bottom, maybe.")
        print("It feels like grass, ")

    def MoveLegs(self):
        print("You can't feel any legs to move, what is happening?")

    def MoveArms(self):
        print("'Where are my arms, I can't feel them!' You try to scream, and yet you don't have a mouth either")

slime = Inventory()
start = Scene_Intro()

