
from items import *
from skills import *

#from time import sleep
from sleep import *

# ASCII Art
import ascii


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

        print(ascii.great_sage)
        sleep(2)
        
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
        print('...')
        sleep(2)
        slime.skillUpgrade(Sage_Skill(), Great_Sage_Skill())
        sleep(3)


        print(slime.showAttributes())
        sleep(3)


        print("\nYou wake up, or at least you think you are 'awake'.")
        sleep(4)
        print("It's so dark, where is this.")
        sleep(3)
        print("What happened to me.")
        sleep(2)
        print("I remembered that I got stabbed while protecting Tamura.")
        sleep(3)
        print("Was I... saved?")
        sleep(2)
        print("That said is this the hospital bed?")
        sleep(3)
        print("I can't see anything, I can't hear anything.")
        sleep(3)
        print("Is it already past the curfew? I should First call the nurse...")
        sleep(3)



        self.actionMenu("Move Arms, Move Legs",
                        [['move arms', 'twitch arms'], ['move legs']],
                        [self.MoveArms, self.MoveLegs])

        print("hm? eh? My limbs don't seem to be responding!?")
        sleep(3)
        print("That's not possible I was only stabbed, my arms and legs should be all gone...")
        sleep(5)
        print("Don't tell me I was paralyzed because my nerves were cut?")
        sleep(3)
        print("Hey hey hey, Give me a break already... AH!?")
        sleep(3)

        print("I moved!?")
        sleep(2)
        print("Below my abdomen (?), is that grass?")
        sleep(3)
        print("I don't smell anything at all")
        sleep(3)
        print("There is also no sense of sight, hearing, and smell. There is only touch... What about taste?")
        sleep(5)
        print("Alright, Let's try to taste it")
        sleep(2)
        print("Actually! Where the fuck is my mouth?")
        sleep(3)
        print("The grass melted. Is it being absorbed after melting...?")
        sleep(3)

        print("WAIT A MINUTE, this isn't even human anymore!!?!")
        sleep(3)
        print("Eh.. Wait a moment... Let's calm down and confirm my appearance.")
        sleep(3)

        self.actionMenu('Move, Puyo',
                        [['squash', 'move', 'twitch'],['puyoo', 'poyo']],
                        [self.squash, self.puyo])

        print("It's probably is like this!")
        sleep(2)
        print("Wait what kind of joke is this! Who would accept something like this!!")
        sleep(3)
        print("ahhhh... but... dissolving and absorbing plants, this streamlined body shape.")
        sleep(5)
        print("And this sort of elastic feeling")
        sleep(3)
        print("***Although Minami Satoru didn't want to admint it.***")
        sleep(4)
        print("***He has reincarrnated into a slime!***")
        sleep(3)
        print(ascii.slime)
        sleep(3)


        print("puyo, puyoyoyo.... stretch....bounce")
        sleep(3)
        print("It's been a long time since I've accepted myself as a slime.")
        sleep(4)
        print("I've gotten used to this elastic body.")
        sleep(3)
        print("I can't feel heat nor cold. Even after bumping into rocks I'll quickly self regenerate.")
        sleep(5)
        print("And there was no need for sleep or eat either.")
        sleep(3)
        print("It's just very lonely")
        sleep(2)
        print("This is the only problem I can't solve, so i started eating grass in order to pass time.")
        sleep(3)

        self.actionMenu('Eat Grass, Move, Wonder, Puyo!',
                        [['eat grass'], ['move', 'wonder']],
                        [self.eatGrass, self.puyo])

        print("I've ate what seems like a lot of grass, and yet I haven't pooped yet")
        sleep(4)
        print("So where did all the grass go?")
        sleep(3)
        print("<<Answer. They are stored inside the unique skill [Predator]'s stomach sack.>>")
        sleep(5)
        print("Whoa, somebody actually answered!?!")
        sleep(3)
        print("<<Also, the current spaced used is less than 1%.>>")
        sleep(3)
        slime.addInventory(Grass_Item(), capacity=0.9)

        print("I've heard this before, this voice that sounded computer synthesized....")
        sleep(5)
        print("W-w-w-who is it?")
        sleep(2)
        print("<<Answer. This is the unique skill [Great Sage]'s effect.>>")
        sleep(3)
        print("<<Because the ability had adapted, so it can quickly answer you.>>")
        sleep(4)

        print("Unique skill [Great Sage] heh?")
        sleep(3)
        print("Speakin of which, when I died I seemed to have acquired some of of skill")
        sleep(4)
        print("That said, what are skills?")
        sleep(3)

        print("<<Answer. When growth is recognized by the world, occasionally one will obtain a [Skill].>>")
        sleep(5)
        print("Although I don't understand it too much... It seems like that this is just how this world is.")
        sleep(4)
        print("Are both [Great Sage] and [Predator] my skills?")
        sleep(3)
        print("The current me completely sank into joyfulness")
        sleep(3)

        print("Although it's a skill, I now have someone to talk to. I got a little carried away.")
        sleep(4)
        print("***Getting carried away and not having all of his normal senses. The little slime fell into what seemed to be water***")
        sleep(5)
        print("I'm going to die! I've finally reincarnated and I'm already going to die!")
        sleep(4)
        print("Great sage how painful is it to suffocate to death!?")
        sleep(3)
        print("<<Answer. A slime's body does not need oxygen.>>")
        sleep(3)

        print("I am indeed not feeling any pain, at this time my brain cells (or slime body) thought up a strategy.")
        sleep(5)


    def eatGrass(self):
        print("Ooooweeee more grass!")


    def squash(self):
        print("hehhhh")
        sleep(1)
        print("Is that so....")
        sleep(1)
        print("hmmmmmm, mhmmmm")
        sleep(1)

    def puyo(self):
        print("Puyo!")
        sleep(1)

    def MoveLegs(self):
        print("You can't feel any legs to move, what is happening?")
        sleep(3)

    def MoveArms(self):
        print("Where are my arms, I can't feel them!")
        sleep(3)

slime = Inventory()
start = Scene_Intro()

