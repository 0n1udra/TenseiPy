
from items import *
from skills import *

# ASCII Art
import ascii

debug = False
if debug:
    from sleep import sleep
    ascii.great_sage, ascii.slime = 'GREAT_SAGE', 'SLIME'
    t2 = t3 = t4 = t5 = 0
else:
    from time import sleep
    t2, t3, t4, t5 = 2, 3, 4, 5  # Custom Sleep times




def sprint(sleepTime, Msg):
    print(Msg)
    sleep(sleepTime)
# TODO add disable sleep function natively

class Scene_Template:


    def __init__(self):
        self.SceneStart()


    def runFuncs(self, usrInp, actions, funcs):
        for i in range(len(funcs)):
            for j in actions[i]:
                if usrInp in j:
                    funcs[i]()
                    return

    def actionMenu(self, msg, actions, funcs):
        menuActions = [['stat', 'stats', 'attributes', 'attrs', 'attr'], ['storage', 'inventory', 'inv', 'stomach']]
        menuActionsFlat = [val for sub in menuActions for val in sub]
        menuFuncs = [slime.showAttributes, slime.showInventory]
        print("\nAvailable Actions:", msg, ' | stats, inv')
        self.usrInp = input("\n> ").lower()
        while self.usrInp in menuActionsFlat:
            self.runFuncs(self.usrInp, menuActions, menuFuncs)
            self.actionMenu(msg, actions, funcs)
        else:
            self.runFuncs(self.usrInp, actions, funcs)

# Manga, Chapter 1
class Scene_Intro(Scene_Template):

    def sleep(self): pass

    def SceneStart(self):
        sprint(t2, ascii.great_sage)

        sprint(t3, "NOTE: You can access inventory/attributes whenever input is possible, (stats, inv)")

        sprint(t3, "<<Confirmation Complete. Constructing a body that does not require blood...>>")
        #TODO Add Skill
        sprint(t2, "<<Confirmation Complete. Acquiring Skill [Predator]...>>")
        slime.addAttribute(Predator_Skill())
        sprint(t2, "<<Confirmation Complete. Acquiring extra skill [Sage]...>>")
        slime.addAttribute(Sage_Skill())
        sprint(t2, "<<Confirmation Complete. Extra skill [Sage] evolving.>>")
        sprint(t2, '...')
        slime.skillUpgrade(Sage_Skill(), Great_Sage_Skill())
        sleep(t3)

        sprint(t3, slime.showAttributes())

        sprint(t3, "\nYou wake up, or at least you think you are 'awake'.")
        sprint(t2, "It's so dark, where is this.")
        sprint(t2, "What happened to me.")
        sprint(t3, "I remembered that I got stabbed while protecting Tamura.")
        sprint(t2, "Was I... saved?")
        sprint(t2, "That said is this the hospital bed?")
        sprint(t3, "I can't see anything, I can't hear anything.")
        sprint(t3, "Is it already past the curfew? I should First call the nurse...")

        self.actionMenu("Move Arms, Move Legs",
                        [['move arms', 'twitch arms'], ['move legs']],
                        [self.MoveArms, self.MoveLegs])

        sprint(t2, "hm? eh? My limbs don't seem to be responding!?")
        sprint(t5, "That's not possible I was only stabbed, my arms and legs should be all gone...")
        sprint(t4, "Don't tell me I was paralyzed because my nerves were cut?")
        sprint(t3, "Hey hey hey, Give me a break already... AH!?")

        sprint(t2, "I moved!?")
        sprint(t3, "Below my abdomen (?), is that grass?")
        sprint(t2, "I don't smell anything at all")
        sprint(t5, "There is also no sense of sight, hearing, and smell. There is only touch... What about taste?")
        sprint(t3, "Alright, Let's try to taste it")
        sprint(t3, "Actually! Where the fuck is my mouth?")
        sprint(t3, "The grass melted. Is it being absorbed after melting...?")
        sprint(t3, "WAIT A MINUTE, this isn't even human anymore!!?!")
        sprint(t3, "Eh.. Wait a moment... Let's calm down and confirm my appearance.")

        self.actionMenu('Move, Puyo',
                        [['squash', 'move', 'twitch'],['puyoo', 'poyo']],
                        [self.squash, self.puyo])

        sprint(t2, "It's probably is like this!")
        sprint(t3, "Wait what kind of joke is this! Who would accept something like this!!")
        sprint(t4, "ahhhh... but... dissolving and absorbing plants, this streamlined body shape.")
        sprint(t3, "And this sort of elastic feeling")

        sprint(t4, "***Although Minami Satoru didn't want to admint it.***")
        sprint(t3, "***He has reincarrnated into a slime!***")

        sprint(t3, ascii.slime)


        sprint(t3, "puyo, puyoyoyo.... stretch....bounce")
        sprint(t4, "It's been a long time since I've accepted myself as a slime.")
        sprint(t3, "I've gotten used to this elastic body.")
        sprint(t5, "I can't feel heat nor cold. Even after bumping into rocks I'll quickly self regenerate.")
        sprint(t3, "And there was no need for sleep or eat either.")
        sprint(t2, "It's just very lonely")
        sprint(t3, "This is the only problem I can't solve, so i started eating grass in order to pass time.")

        self.actionMenu('Eat Grass, Move, Wonder, Puyo!',
                        [['eat grass'], ['move', 'wonder']],
                        [self.eatGrass, self.puyo])

        sprint(t4, "I've ate what seems like a lot of grass, and yet I haven't pooped yet")
        slime.addInventory(Grass_Item(), capacity=0.9)
        sprint(t3, "So where did all the grass go?")
        sprint(t4, "<<Answer. They are stored inside the unique skill [Predator]'s stomach sack.>>")
        sprint(t3, "Whoa, somebody actually answered!?!")
        sprint(t2, "<<Also, the current spaced used is less than 1%.>>")
        sprint(t2, "I've heard this before, this voice that sounded computer synthesized....")
        sprint(t2, "W-w-w-who is it?")
        sprint(t3, "<<Answer. This is the unique skill [Great Sage]'s effect.>>")
        sprint(t3, "<<Because the ability had adapted, so it can quickly answer you.>>")

        sprint(t2, "Unique skill [Great Sage] heh?")
        sprint(t3, "Speakin of which, when I died I seemed to have acquired some of of skill")
        sprint(t3, "That said, what are skills?")
        sprint(t5, "<<Answer. When growth is recognized by the world, occasionally one will obtain a [Skill].>>")
        sprint(t4, "Although I don't understand it too much... It seems like that this is just how this world is.")
        sprint(t2, "Are both [Great Sage] and [Predator] my skills?")
        sprint(t3, "The current me completely sank into joyfulness")

        sprint(t4, "Although it's a skill, I now have someone to talk to. I got a little carried away.")
        sprint(t5, "***Getting carried away and not having all of his normal senses. The little slime fell into what seemed to be wt2, ater***")
        sprint(t3, "I'm going to die! I've finally reincarnated and I'm already going to die!")
        sprint(t2, "Great sage how painful is it to suffocate to death!?")
        sprint(t3, "<<Answer. A slime's body does not need oxygen.>>")
        sprint(t5, "I am indeed not feeling any pain, at this time my brain cells (or slime body) thought up a strategy.")
        sprint(t4, "Lets try swallowing large amounts of water and propelling myself by spitting out a water jet!")
        sprint(t2, "I hope this works")
        slime.addAttribute(Hydraulic_Propulsion())
        sleep(t2)

        sprint(t2, "*Can you hear me little one.*")
        sprint(t3, "Whaaaa? What was that, I almost pissed myself.")
        sprint(t2, "Who's that speaking to me!?")
        sprint(t2, "It's not Great Sage, so who is it?")
        sprint(t2, "This is bad, I'm getting nervous.")
        sprint(t4, "This is the first conversation I'm having since reincarnating into a slime.")
        sprint(t2, "I'll have to be friendly")
        sprint(t3, "But how do I even reply?")
        sprint(t3, "It's not like I have a means to speak")
        sprint(t2, "*Hey can you just replay?*")
        

    

        self.actionMenu('Puyo!',
                        ['move', 'wonder'],
                        [self.eatGrass, self.puyo])

    def baldy(self):
        sprint("*BALDY, HAHAHA, SEEMS THAT YOU WANT TO DIE!*")

    def eatGrass(self):
        print("Ooooweeee more grass!")


    def squash(self):
        sprint(t2, "hehhhh")
        sprint(t2, "Is that so....")
        sprint(t2, "hmmmmmm, mhmmmm")

    def puyo(self):
        sprint(t2, "Puyo!")

    def MoveLegs(self):
        sprint(t2, "You can't feel any legs to move, what is happening?")

    def MoveArms(self):
        sprint(t2, "Where are my arms, I can't feel them!")

slime = Inventory()
start = Scene_Intro()

