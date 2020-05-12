
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
        'Mana' : []
        }

    def showIventory(self):
        print()
        # Prints players current skills, will not print out every type of skill unless player has said skills
        for k, v in self.playerInventory.items():
            if v: # Checks if player has this type of skill
                print(f'{k}:')
                for i in v:
                    print(f'\t{i}')

    def addInventory(self, item):
        self.playerInventory[item.skillLevel].append(item)
        print(item.acquired())


    def removeInventory(self, item):
        for k, v in self.playerInventory.items():
            if v:
                if item in v:
                    # Finds corresponding item, and removes it from inventory
                    self.playerInventory[k].remove(item)

    def skillUpgrade(self, skillFrom, skillTo):
        for k, v in self.playerInventory.items():
            if v:
                for i in v:
                    if i.name in skillFrom.name:
                        # Removes skill from inventory
                        self.playerInventory[k].remove(i)

        print(f'<<{skillFrom.skillLevel} [{skillFrom}] upgrading to {skillTo.skillLevel} [{skillTo}]...>>')
        self.addInventory(skillTo)


class Scene_Intro(Scene_Template):


    def SceneStart(self):
        print("<<Confirmation Complete. Constructing a body that does not require blood...>>")
        #TODO Add Skill

        print("<<Confirmation Complete. Acquiring Skill [Predator]...>>")
        slime.addInventory(Predator_Skill())

        print("<<Confirmation Complete. Acquiring extra skill [Sage]...>>")
        slime.addInventory(Sage_Skill())
        
        print("<<Confirmation Complete. Extra skill [Sage] evolving.>>")
        slime.skillUpgrade(Sage_Skill(), Great_Sage_Skill())



        print("\n-----Current Skills-----")
        print(slime.showIventory())

        print("\nYou wake up, or at least you think you are 'awake'.")
        print("It's so dark, where is this.")
        print("What happened to me.")
        print("I remembered that I got stabbed while protecting Tamura")
        print("Was I... saved?")
        print("That said is this the hospital bed?")
        print("I can't see anything, I can't hear anything")
        print("Is it already past the curfew? I should First call the nurse...")


        #actions = [MoveArms, MoveLegs]
        print("\nAvailable Actions: Move Arms, Move Legs")
        self.usrInp = input("\n> ")
        self.Actions(self.usrInp, [['move arms', 'twitch arms'], ['move legs']], [self.MoveArms, self.MoveLegs])

        print("hm? eh? My limbs don't seem to be responding!?")

        print("That's not possible I was only stabbed, my arms and legs should be all gone...")
        print("Don't tell me I was paralyzed because my nerves were cut?")
        print("Hey hey hey, Give me a break already... AH!?")

        print("I moved!?")
        print("Below my abdomen (?), is that grass?")
        print("I don't smell anything at all")
        print("There is also no sense of sight, hearing, and smell. There is only touch... What about taste?")
        print("Alright, Let's try to taste it")
        print("Actually! Where the fuck is my mouth?")
        print("The grass melted. Is it being absorbed after melting...?")

        print("WAIT A MINUTE, this isn't even human anymore!!?!")
        print("Eh.. Wait a moment... Let's calm down and confirm my appearance")

        print("\nAvailable Actions: Move, Puyo")
        self.usrInp = input("\n> ")
        self.Actions(self.usrInp, [['squash', 'move', 'twitch'],['puyoo', 'poyo']], [self.squash, self.puyo])

        print("It's probably is like this!")
        print("Wait what kind of joke is this! Who would accept something like this!!")
        print("ahhhh... but... dissolving and absorbing plants, this streamlined body shape.")
        print("And this sort of elastic feeling")
        print("***Although Minami Satoru didn't want to admint it***")
        print("***He has reincarrnated into a slime!***")
        
    def squash(self):
        print("hehhhh")
        print("Is that so....")
        print("hmmmmmm, mhmmmm")

    def puyo(self):
        print("Puyo!")

    def MoveLegs(self):
        print("You can't feel any legs to move, what is happening?")

    def MoveArms(self):
        print("Where are my arms, I can't feel them!")

slime = Inventory()
start = Scene_Intro()

