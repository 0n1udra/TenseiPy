
from items import *
from skills import *

class Scene_Template:

    def __init__(self):
        self.SceneStart()

    def Actions(self, usrInp, actions, funcs):
        usrInp = usrInp.lower()
        actions.extend([['stats', 'attributes', 'attrs'], ['inventory', 'inv', 'stomach']])
        funcs.extend([slime.showAttributes, slime.showInventory])
        # Runs through each function available
        for i in range(len(funcs)):
            for j in actions[i]:
                # Checks if user input matches one of the available actions
                if usrInp in j:
                    # Runs corresponding function
                    funcs[i]()
#            if usrInp.lower() in actions[i]:
#                print("true")

    def init(self):
        pass

    def SceneStart(self):
        pass


class Scene_Intro(Scene_Template):


    def SceneStart(self):
        print("<<Confirmation Complete. Constructing a body that does not require blood...>>")
        #TODO Add Skill

        print("<<Confirmation Complete. Acquiring Skill [Predator]...>>")
        slime.addAttribute(Predator_Skill())

        print("<<Confirmation Complete. Acquiring extra skill [Sage]...>>")
        slime.addAttribute(Sage_Skill())
        
        print("<<Confirmation Complete. Extra skill [Sage] evolving.>>")
        slime.skillUpgrade(Sage_Skill(), Great_Sage_Skill())


        print(slime.showAttributes())

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
        self.usrInp = 'move' #input("\n> ")
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
        self.usrInp = 'move'#input("\n> ")
        self.Actions(self.usrInp, [['squash', 'move', 'twitch'],['puyoo', 'poyo']], [self.squash, self.puyo])

        print("It's probably is like this!")
        print("Wait what kind of joke is this! Who would accept something like this!!")
        print("ahhhh... but... dissolving and absorbing plants, this streamlined body shape.")
        print("And this sort of elastic feeling")
        print("***Although Minami Satoru didn't want to admint it***")
        print("***He has reincarrnated into a slime!***")

        print("puyo, puyoyoyo.... stretch....bounce")
        print("It's been a long time since I've accepted myself as a slime")
        print("I've gotten used to this elastic body")
        print("I can't feel heat nor cold. Even after bumping into rocks I'll quickly self regenerate")
        print("And there was no need for sleep or eat either")
        print("It's just very lonely")
        print("This is the only problem I can't solve, so i started eating grass in order to pass time")

        print("\nAvailable Actions: Eat Grass, Move, Wonder, Puyo!")
        self.usrInp = input("\n> ")
        self.Actions(self.usrInp, [['eat grass'], ['move', 'wonder']], [self.eatGrass, self.puyo])

        print("I've ate what seems like a lot of grass, and yet I haven't pooped yet")
        print("So where did all the grass go?")
        print("<<Answer. They are stored inside the unique skill [Predator]'s stomach sack>>")
        print("Whoa, somebody actually answered!?!")
        print("<<Also, the current spaced used is less than 1%")
        slime.addInventory(Grass_Item(), capacity=0.9)


    def eatGrass(self):
        print("Ooooweeee more grass!")


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

