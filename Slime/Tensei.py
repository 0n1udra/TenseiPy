
from items import *
from skills import *
#from time import sleep
from sleep import *

class Scene_Template:

    def __init__(self):
        self.SceneStart()

    def actionMenu(self, msg, actions, funcs):

        menuActions = [['stats', 'attributes', 'attrs'], ['inventory', 'inv', 'stomach']]
        menuFuncs = [slime.showAttributes, slime.showInventory]
        # Runs through each function available
        while True:
            print("\nAvailable Actions:", msg, ' | stats, inv')
            self.usrInp = input("\n> ").lower()
            for i in range(len(menuFuncs)):
                for j in menuActions[i]:
                    if self.usrInp in j:
                        menuFuncs[i]()
                else:
                    for i in range(len(funcs)):
                        for j in actions[i]:
                            if self.usrInp in j:
                                funcs[i]()
                                return





    def init(self):
        pass

    def SceneStart(self):
        pass


class Scene_Intro(Scene_Template):

    def sleep(self): pass

    def SceneStart(self):
        print("NOTE: You can access inventory/attributes whenever input is possible, (stats, inv)")
        sleep(3)

        print("<<Confirmation Complete. Constructing a body that does not require blood...>>")
        #TODO Add Skill
        sleep(3)

        print("<<Confirmation Complete. Acquiring Skill [Predator]...>>")
        sleep(2)
        slime.addAttribute(Predator_Skill())
        sleep(2)

        print("<<Confirmation Complete. Acquiring extra skill [Sage]...>>")
        sleep(2)
        slime.addAttribute(Sage_Skill())
        sleep(2)
        
        print("<<Confirmation Complete. Extra skill [Sage] evolving.>>")
        sleep(2)
        slime.skillUpgrade(Sage_Skill(), Great_Sage_Skill())
        sleep(3)


        print(slime.showAttributes())
        sleep(3)


        print("\nYou wake up, or at least you think you are 'awake'.")
        sleep(3)
        print("It's so dark, where is this.")
        sleep(2)
        print("What happened to me.")
        sleep(2)
        print("I remembered that I got stabbed while protecting Tamura.")
        sleep(3)
        print("Was I... saved?")
        sleep(2)
        print("That said is this the hospital bed?")
        sleep(2)
        print("I can't see anything, I can't hear anything.")
        sleep(2)
        print("Is it already past the curfew? I should First call the nurse...")
        sleep(3)



        self.actionMenu("Move Arms, Move Legs",
                        [['move arms', 'twitch arms'], ['move legs']],
                        [self.MoveArms, self.MoveLegs])

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
        print("Eh.. Wait a moment... Let's calm down and confirm my appearance.")

        self.actionMenu('Available Actions: Move, Puyo',
                        [['squash', 'move', 'twitch'],['puyoo', 'poyo']],
                        [self.squash, self.puyo])

        print("It's probably is like this!")
        print("Wait what kind of joke is this! Who would accept something like this!!")
        print("ahhhh... but... dissolving and absorbing plants, this streamlined body shape.")
        print("And this sort of elastic feeling")
        print("***Although Minami Satoru didn't want to admint it.***")
        print("***He has reincarrnated into a slime!***")

        print("puyo, puyoyoyo.... stretch....bounce")
        print("It's been a long time since I've accepted myself as a slime.")
        print("I've gotten used to this elastic body.")
        print("I can't feel heat nor cold. Even after bumping into rocks I'll quickly self regenerate.")
        print("And there was no need for sleep or eat either.")
        print("It's just very lonely")
        print("This is the only problem I can't solve, so i started eating grass in order to pass time.")

        self.actionMenu('nAvailable Actions: Eat Grass, Move, Wonder, Puyo!',
                        [['eat grass'], ['move', 'wonder']],
                        [self.eatGrass, self.puyo])

        print("I've ate what seems like a lot of grass, and yet I haven't pooped yet")
        print("So where did all the grass go?")
        print("<<Answer. They are stored inside the unique skill [Predator]'s stomach sack.>>")
        print("Whoa, somebody actually answered!?!")
        print("<<Also, the current spaced used is less than 1%.>>")
        slime.addInventory(Grass_Item(), capacity=0.9)

        print("I've heard this before, this voice that sounded computer synthesized....")
        print("W-w-w-who is it?")
        print("<<Answer. This is the unique skill [Great Sage]'s effect.>>")
        print("<<Because the ability had adapted, so it can quickly answer you.>>")

        print("Unique skill [Great Sage] heh?")
        print("Speakin of which, when I died I seemed to have acquired some of of skill")
        print("That said, what are skills?")
        
        print("<<Answer. When growth is recognized by the world, occasionally one will obtain a [Skill].>>")
        print("Although I don't understand it too much... It seems like that this is just how this world is.")
        print("Are both [Great Sage] and [Predator] my skills?")
        print("The current me completely sank into joyfulness")

        print("Although it's a skill, I now have someone to talk to. I got a little carried away.")
        print("***Getting carried away and not having all of his normal senses. The little slime fell into what seemed to be water***")
        print("I'm going to die! I've finally reincarnated and I'm already going to die!")
        print("Great sage how painful is it to suffocate to death!?")
        print("<<Answer. A slime's body does not need oxygen.>>")

        print("I am indeed not feeling any pain, at this time my brain cells (or slime body) thought up a strategy.")


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

