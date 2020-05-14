
from items import *
from skills import *
from character import *

# ASCII Art
import ascii

debug = True
if debug:
    usrInpDebug = True
    def sleep(x): pass
    #ascii.great_sage, ascii.slime = 'GREAT_SAGE', 'SLIME'
    t2 = t3 = t4 = t5 = t6 = 0
else:
    usrInpDebug = False
    from time import sleep
    t2, t3, t4, t5, t6 = 2, 3, 4, 5, 6  # Custom Sleep times


def sprint(Msg):
    msgLen = len(str(Msg))
    if msgLen > 70:
        sTime = t6
    elif msgLen > 60 and msgLen > 70:
        sTime = t5
    elif msgLen > 50 and msgLen > 40:
        sTime = t4
    elif msgLen > 40 and msgLen > 20:
        sTime = t3
    elif msgLen < 10:
        sTime = t2
    else:
        sTime = t2
    print(Msg)
    sleep(sTime)

# TODO add disable sleep function natively

class Scene_Template:

    # <MSG> -- Acquired item, etc
    # <<MSG>>  --  Great Sage (Raphael, Ciel)
    # <<<MSG>>>  --  Voice of the World

    def __init__(self):
        self.SceneStart()

    def RunFuncs(self, msg, actions, funcs):
        if usrInpDebug:
            self.usrInp = actions[0][0]
        else:
            print("\nAvailable Actions:", msg, '| stats(attributes), inv(entory), info <skill/obj>, exit')
            self.usrInp = input("\n> ").lower()

        ### Get info on skills, times, etc
        if 'info' in self.usrInp:
            try:
                inputSkill = ' '.join(self.usrInp.lower().split()[1:])
                # Can only get info if item exist in rimuru characte
            except:
                print("NOTE: info Usage example (case sensitive): info predator")
            rimuru.ShowInfo(inputSkill, rimuru)

        contGame = False
        for i in range(len(funcs)):
            for j in actions[i]:
                if self.usrInp == j:
                    if i == 0:
                        funcs[i]()
                        contGame = True
                        break
                    else:
                        funcs[i]()
                        contGame = False

        if not contGame:
            self.RunFuncs(msg, actions, funcs)
        else:
            return

    def ActionMenu(self, msg, actions, funcs):
        actions.extend([['stat', 'stats', 'attributes', 'attrs', 'attr'], ['storage', 'inventory', 'inv', 'stomach'], ['stop', 'exit', 'quit']])
        funcs.extend([rimuru.ShowAttributes, rimuru.showInventory, self.ExitGame])
        self.RunFuncs(msg, actions, funcs)

    def ExitGame(self):
        exit()

    def TBC(self):
        print("---TO BE CONTINUED---")

# Manga, Chapter 1
class Scene_Intro(Scene_Template):

    def SceneStart(self):
        print(ascii.great_sage)
        sleep(1)
        sprint("...")

        sprint("NOTE: You can access inventory/attributes whenever input is possible, (stats, inv)")
        sprint("NOTE: ASCII art will be displayed, set window size accordingly")

        sprint("<<Confirmation Complete. Constructing a body that does not require blood...>>")
        #TODO Add Skill
        sprint("<<Confirmation Complete. Acquiring Skill [Predator]...>>")
        rimuru.AddAttribute(Predator_Skill())
        sprint("<<Confirmation Complete. Acquiring extra skill [Sage]...>>")
        rimuru.AddAttribute(Sage_Skill())
        sprint("<<Confirmation Complete. Extra skill [Sage] evolving.>>")
        sprint('...')
        rimuru.SkillUpgrade(Sage_Skill(), Great_Sage_Skill())
        sleep(t3)

        sprint(rimuru.ShowAttributes())

        sprint("\nYou wake up, or at least you think you are 'awake'.")
        sprint("It's so dark, where is this.")
        sprint("What happened to me.")
        sprint("I remembered that I got stabbed while protecting Tamura.")
        sprint("Was I... saved?")
        sprint("That said is this the hospital bed?")
        sprint("I can't see anything, I can't hear anything.")
        sprint("Is it already past the curfew? I should First call the nurse...")

        self.ActionMenu("Move Arms, Twitch Legs",
                        [['move arms', 'move'], ['twitch leg']],
                        [self.MoveArms, self.MoveLegs])

        sprint("hm? eh? My limbs don't seem to be responding!?")
        sprint("That's not possible I was only stabbed, my arms and legs should be all gone...")
        sprint("Don't tell me I was paralyzed because my nerves were cut?")
        sprint("Hey hey hey, Give me a break already... AH!?")

        sprint("I moved!?")
        sprint("Below my abdomen(?), is that grass?")
        sprint("I don't smell anything at all")
        sprint("There is also no sense of sight, hearing, and smell. There is only touch... What about taste?")
        sprint("Alright, Let's try to taste it")
        sprint("Actually! Where the fuck is my mouth?")
        sprint("The grass melted. Is it being absorbed after melting...?")
        sprint("WAIT A MINUTE, this isn't even human anymore!!?!")
        sprint("Eh.. Wait a moment... Let's calm down and confirm my appearance.")

        self.ActionMenu('Move, Puyo',
                        [['squash', 'move', 'twitch'],['puyo', 'poyo']],
                        [self.squash, self.puyo])

        sprint("It's probably is like this!")
        sprint("Wait what kind of joke is this! Who would accept something like this!!")
        sprint("ahhhh... but... dissolving and absorbing plants, this streamlined body shape.")
        sprint("And this sort of elastic feeling")

        sprint("***Although Minami Satoru didn't want to admins it.***")
        sprint("***He has reincarnated into a slime!***")

        print(ascii.slime)
        sleep(3)

        sprint("puyo, puyoyoyo.... stretch....bounce")
        sprint("It's been a long time since I've accepted myself as a slime.")
        sprint("I've gotten used to this elastic body.")
        sprint("I can't feel heat nor cold. Even after bumping into rocks I'll quickly self regenerate.")
        sprint("And there was no need for sleep or eat either.")
        sprint("It's just very lonely")
        sprint("This is the only problem I can't solve, so i started eating grass in order to pass time.")

        self.ActionMenu('Eat Grass, Move, Wonder, Puyo',
                        [['eat grass'], ['move', 'wonder']],
                        [self.eatGrass, self.puyo])

        sprint("I've ate what seems like a lot of grass, and yet I haven't pooped yet")
        rimuru.AddInventory(Grass_Item(), capacity=0.9)
        sprint("So where did all the grass go?")
        sprint("<<Answer. They are stored inside the unique skill [Predator]'s stomach sack.>>")
        sprint("Whoa, somebody actually answered!?!")
        sprint("<<Note, the current spaced used is less than 1%.>>")
        sprint("I've heard this before, this voice that sounded computer synthesized....")
        sprint("W-w-w-who is it?")
        sprint("<<Answer. This is the unique skill [Great Sage]'s effect.>>")
        sprint("<<Because the ability had adapted, so it can quickly answer you.>>")

        sprint("Unique skill [Great Sage] heh?")
        sprint("Speakin of which, when I died I seemed to have acquired some of of skill")
        sprint("That said, what are skills?")
        sprint("<<Answer. When growth is recognized by the world, occasionally one will obtain a [Skill].>>")
        sprint("Although I don't understand it too much... It seems like that this is just how this world is.")
        sprint("Are both [Great Sage] and [Predator] my skills?")
        sprint("The current me completely sank into joyfulness")

        sprint("Although it's a skill, I now have someone to talk to. I got a little carried away.")
        sprint("***Getting carried away and not having all of his normal senses. The little slime fell into what seemed to be water***")
        sprint("I'm going to die! I've finally reincarnated and I'm already going to die!")
        sprint("Great sage how painful is it to suffocate to death!?")
        sprint("<<Answer. A slime's body does not need oxygen.>>")
        sprint("I am indeed not feeling any pain, at this time my brain cells (or slime body) thought up a strategy.")
        sprint("Lets try swallowing large amounts of water and propelling myself by spitting out a water jet!")
        sprint("I hope this works")
        rimuru.AddAttribute(Hydraulic_Propulsion())
        sleep(t2)

        sprint("*Can you hear me little one.*")
        sprint("Whaaaa? What was that, I almost pissed myself.")
        sprint("Who's that speaking to me!?")
        sprint("It's not Great Sage, so who is it?")
        sprint("This is bad, I'm getting nervous.")
        sprint("This is the first conversation I'm having since reincarnating into a rimuru.")
        sprint("I'll have to be friendly")
        sprint("But how do I even reply?")
        sprint("It's not like I have a means to speak")
        sprint("*Hey can you just reply?*")

        self.ActionMenu('"Shut it baldy"',
                        [['baldy', 'shut it baldy'], ['move', 'wonder']],
                        [self.baldy, self.puyo])

        sprint("Don't be so inconsiderate BALDY!! (ahh, how annoying).")
        sprint("Was I heard?")
        sprint("Sorry!, I never expected to be able to speak with anything other than my skill by thought...")
        sprint("Right now I am in a state that's unable to see anythin....um you are?.")
        sprint("*This is telepathy.*")
        sprint("*Mmmmm, My name is....*")
        sprint("*It's Hard to converse if you can't see...*")
        sprint("*Alright, I'll help you see.*")
        sprint("eh?")
        sprint("*Just don't be scared when you see my true form*")
        sprint("*There is something called [Magic Perception], it allows you to perceive the surrounding magic essence.*")
        sprint("Magic essence?...")
        sprint("<<Answer. This world is covered with magic essence for example, the body of a rimuru can move because it absorbs magic essence.>>")
        sprint("*If you are able to perceive the flow of magic essence outside of your body, then you'll get the skill*.")
        sprint("*With that you will be able to 'see' and 'hear'.*")
        sprint("Eh... this feels really complicated.")
        sprint("Well, it won't hurt to try (will it?).")
        sprint("I sense something floating, is this the so called magic essence?")
        rimuru.AddAttribute(Magic_Perception_Skill())

        sprint("Ehh, just like that heh?")
        sprint("<<Suggestion, in order to organize large amount of information, suggest activating linking [Great Sage] with [Magic Perception].>>")
        sprint("<<Activate [Magic Perception]?>>")

        self.ActionMenu('"Activate Magic Perception."',
                        [['activate magic perception', 'activate magic sense'], ['move', 'wonder']],
                        [self.MagicPerception, self.puyo])
        

        sprint("OH!")
        sprint("Hmmmmmmmm")
        sprint("I can see. I CAN SEE!")
        sprint("*Seems like you did it*")
        sprint("Yes thank you!")
        sprint("*Then let me introduce myself again*")
        sprint("My name is Storm Dragon Veldora.*")
        print(ascii.cave_veldora)
        sleep(2)
        sprint("*I am one of the four True Dragons of this world.*")
        sprint("HOLY SHIT, is that a dragon?")
        sprint("*Didn't I tell you not to get scared.*")
        sprint("***Even with the scary appearance, the little slime and dragon started chatting.***")
        
        sprint("So you are a reincarnate from another world, hm.*")
        sprint("This type of reincarnation is very rare.*")
        sprint("I wonder if there are more japaenese people here")
        sprint("*...Is that so, are you leaving now?*")
        sprint("Why does he look so sad?")
        sprint("*I am unable to move from this spot.*")
        sprint("*I was sealed here for over 300 years.*")
        sprint("By a short, slender, silver-black haired girl. With Snow-white skin and small apple red lips...*")
        sprint("Wow, how observant of him....")
        sprint("Hm, for some reason I'm not so Frightened by him now.")
        sprint("Okay... you want to be friends?")
        sprint("*HAHA, WHAT?*")
        sprint("*A mere slime wants to be friends with the great Storm Dragon Veldora!?*")
        sprint("wellll... If you don't want to, that's fine too")
        sprint("*WHAAAAAAT, Who said we couldn't!*")
        sprint("I guess I won't have a reason to come back here again")
        sprint("Wait. I guess it can't be helped.*")
        sprint("*I'll become your friend!.*")
        sprint("Great. Now I guess I should help you with this seal heh?")
        sprint("[Great Sage] how can we remove the seal?")
        sprint("<<Answer, It is impossible to destroy [Nifty Prison] using physical attacks.>>")
        sprint("Is that so...")
        sprint("<<Possible solution may be...")
        sprint("*Hey don't only talk to your own skill.*")
        sprint("Jealous?")
        sprint("It might be possible if we both analyze [Infinity Prizon] inside and out")
        sprint("*My skills were sealed away as well, I can't use analyze.*")
        sprint("If you give me the information [Great Sage] can analyze your side as well")
        sprint("*Won't that take a long time, didn't you want to go find other reincarnates from your world*")
        sprint("I have a suggestion")
        sprint("How would you like to get in my stomach")
        sprint("*hahaha*")
        sprint("*ku hahaha*")
        sprint("*HAHAHAHAHAHAHA*")
        sprint("Ummmm, did he just use the 3 stage laugh?")
        sprint("My life is in your hands.*")
        sprint("Wow how trusting.")
        sprint("*Well... The alternative is to stay in the cave for the rest of time.*")
        sprint("I'll use predator to swallow you")
        sprint("*Before that, let me give you a name*")
        sprint("*You think of a name for both of us*")
        sprint("Like a last name? hmmmmm")
        sprint("'Storm Dragon', Storm, Tempest?")
        sprint("*What a good name!*")
        sprint("He actually likes it?")
        sprint("*From now on I'll be Veldora Tempest!*")
        sprint("*And as for you.... How about Rimuru.*")
        sprint("Rimuru- Alright, get out of there as quick as you can!")
        sprint("Veldora- *Leave it to me. Until we meet again*")
        sprint("<<Use Unique skill [Predator]?>>")

        self.ActionMenu('"Activate Predator, Puyo"',
                        [['activate magic perception', 'activate magic sense'], ['move', 'wonder']],
                        [self.PredateVeldora, self.puyo])










        self.TBC()

    def PredateVeldora(self):
        sprint("***Rimuru quickly swallows Veldora and his seal with [Predator]***")

    def MagicPerception(self):
        sprint('...')
        print(ascii.magic_perception)
        sleep(2)

    def shutit(self):
        sprint("*OHOHO, So you want to die, you maggot!*")

    def baldy(self):
        sprint("*BALDY, HAHAHA, SEEMS THAT YOU WANT TO DIE!*")

    def eatGrass(self):
        sprint("Ooooweeee more grass!")


    def squash(self):
        sprint("hehhhh")
        sprint("Is that so....")
        sprint("hmmmmmm, mhmmmm")

    def puyo(self):
        sprint("Puyo!")

    def MoveLegs(self):
        sprint("You can't feel any legs to move, what is happening?")

    def MoveArms(self):
        sprint("Where are my arms, I can't feel them!")

rimuru = Rimuru_Tempest()
start = Scene_Intro()

