from chapters import *

# Manga, Chapter 1
def Chapter1():
    

        print()
        print("----------Tensei Shitara Slime Datta Ken (That Time I Got Reincarnated as a Slime)----------")
        print("NOTE: You can access inventory/attributes whenever input is possible, (stats, inv)")
        print("NOTE: ASCII art will be displayed, set window size accordingly (Full screen for best results)")
        print()
        usrCont = input("Press Enter to continue > ")
        print()

        sprint("...")
        sleep(1)
        print(slime_art.great_sage)
        sleep(1)


        ssprint("<<Confirmation Complete. Constructing a body that does not require blood...>>")
        #TODO Add Skill
        ssprint("<<Confirmation Complete. Acquiring Skill [Predator]...>>")
        rimuru.AddAttribute(Predator_Skill())
        ssprint("<<Confirmation Complete. Acquiring Extra Skill [Sage]...>>")
        rimuru.AddAttribute(Sage_Skill())
        ssprint("<<Confirmation Complete. Extra skill [Sage] evolving.>>")
        sprint('...')
        rimuru.SkillUpgrade(Sage_Skill(), Great_Sage_Skill())
        sleep(t3)

        sprint(rimuru.ShowAttributes())

        sprint("...")
        sprint("It's so dark, where is this. What happened to me.")
        sprint("I remembered that I got stabbed while protecting Tamura. Was I... saved?")
        sprint("That said is this the hospital bed? I can't see anything, I can't hear anything.")

        ActionMenu("Move Arms, Twitch Legs",
                        [['move arms', 'move'], ['twitch legs']],
                        [MoveArms, MoveLegs])

        sprint("hm? eh? My limbs don't seem to be responding!?")
        sprint("That's not possible I was only stabbed, my arms and legs should be all fine... Right?...")
        sprint("Don't tell me I was paralyzed because my nerves were cut?")
        sprint("Hey hey hey, Give me a break already... AH!?")
        sprint("I moved!? Below my abdomen(?), is that grass?")
        sprint("There is also no sense of sight, hearing, and smell. There is only 'touch'... What about taste?")
        sprint("Alright, Let's try to taste it. Actually! Where the fuck is my mouth?")
        sprint("The grass melted. Is it being absorbed after melting?")
        sprint("WAIT A MINUTE, am I even human anymore!!?! Eh.. Let's calm down and confirm my appearance.")

        ActionMenu('Move, Puyo',
                        [['squash', 'move', 'twitch'],['puyo', 'poyo']],
                        [squash, puyo])

        sprint("Wait what kind of joke is this! Who would accept something like this!!")
        sprint("ahhhh... but... Dissolving and absorbing plants, this streamlined elastic feeling body shape.")

        ssprint("***Although Minami Satoru didn't want to admins it.***")
        ssprint("***He has reincarnated into a slime!***")

        print(slime_art.slime)
        sleep(3)

        sprint("puyo, puyoyoyo.... stretch....bounce")
        sprint("It's been a long time since I've accepted myself a slime. I've gotten used to this elastic body.")
        sprint("I can't feel heat nor cold. Even after bumping into rocks I'll quickly regenerate.")
        sprint("And there was no need for sleep or eat either. This body isn't so bad. It's just very lonely.")
        sprint("This is the only problem I can't solve, so i started eating grass in order to pass time.")

        ActionMenu('Eat Grass, Move, Wonder, Puyo',
                        [['eat grass'], ['move', 'wonder']],
                        [eatGrass, puyo])

        rimuru.AddInventory(Grass_Item(), capacity=0.9)
        sprint("I've ate what seems like a lot of grass, and yet I haven't pooped yet. So where did all the grass go?")
        ssprint("<<Answer. They are stored inside the Unique Skill [Predator]'s stomach sack.>>")
        sprint("Whoa, somebody actually answered!?!")
        ssprint("<<Note, the current spaced used is less than 1%.>>")
        sprint("I've heard this before, this voice that sounded computer synthesized.... Who is that?")
        ssprint("<<Answer. This is the Unique Skill [Great Sage], the ability has adapted, so it can quickly answer you.>>")
        sprint("Unique skill [Great Sage] heh?")

        sprint("Speakin of which, when I died I seemed to have acquired some of skills. That said, what are skills?")

        ssprint("<<Answer. When growth is recognized by the world, occasionally one will obtain a [Skill].>>")
        sprint("Although I don't understand it too much. It seems like it's just how this world works.")
        sprint("Although it's a skill, I now have someone to talk to.")
        ssprint("***Getting carried away and not having all of his normal senses. The little slime fell into what seemed to be water***")
        sprint("I'm going to die! SHIT! I've finally reincarnated and I'm already going to die!")
        sprint("Great sage how painful is it to suffocate to death!?")
        ssprint("<<Answer. A slime's body does not need oxygen.>>")
        sprint("I am indeed not feeling any pain, at this time my brain cells (or slime body) thought up a strategy.")
        sprint("Lets try swallowing large amounts of water and propelling myself by spitting out a water jet. I hope this works!")
        rimuru.AddAttribute(Hydraulic_Propulsion())
        sleep(t2)

        sprint("*Can you hear me little one.*")
        sprint("Whaaaa? What was that, I almost pissed myself. Who's that speaking to me!?")
        sprint("It's not [Great Sage], so who is it? This is bad, I'm getting nervous. This is the first conversation I'm having since reincarnating.")
        sprint("I'll have to be friendly. But how do I even reply?. It's not like I have a mouth to speak with.")
        sprint("*Hey can you just reply?*")

        ActionMenu('Shut it baldy',
                        [['baldy', 'shut it baldy'], ['move', 'wonder']],
                        [baldy, puyo])

        sprint("Was I heard?")
        sprint("Sorry!, I never expected to be able to speak with anything other than my skill by thought...")
        sprint("Right now I am in a state that's unable to see anythin....Ummmm you are?.")
        sprint("*This is telepathy. It's Hard to converse if you can't see... Alright, I'll help you see.*")
        sprint("eh?")
        sprint("*Just don't be scared when you see my true form. There is something called [Magic Perception], it allows you to perceive the surrounding magic essence.*")
        sprint("Magic essence?...")
        ssprint("<<Answer. This world is covered with magic essence for example, the body of a rimuru can move because it absorbs magic essence.>>")
        sprint("*If you are able to perceive the flow of magic essence outside of your body, then you'll get the skill.*")
        sprint("*With that you will be able to 'see' and 'hear'.*")
        sprint("Eh... this feels really complicated. Wellllll, it won't hurt to try (will it?).")
        sprint("I sense something floating, is this the so called magic essence?")
        rimuru.AddAttribute(Magic_Perception_Skill())

        sprint("Ehh, just like that heh?")
        ssprint("<<Suggestion, in order to organize large amount of information, suggest activating linking [Great Sage] with [Magic Perception].>>")
        ssprint("<<Activate [Magic Perception]?>>")

        ActionMenu('Activate Magic Perception.',
                        [['activate magic perception', 'activate magic sense'], ['move', 'wonder']],
                        [MagicPerception, puyo])
        

        sprint("OH!")
        sprint("Hmmmmmmmm")
        sprint("I can see. I CAN SEE!")
        sprint("*Seems like you did it*")
        sprint("Yes thank you!")
        sprint("*Then let me introduce myagain*")
        sprint("My name is Storm Dragon Veldora!*")
        print(slime_art.cave_veldora)
        sleep(2)

        sprint("*I am one of the four True Dragons of this world.*")
        sprint("HOLY SHIT, it's a real dragon!")
        sprint("*Didn't I tell you not to get scared.*")
        ssprint("***Even with the scary appearance, the little slime and dragon started chatting.***")
        
        sprint("So you are a reincarnate from another world, hmmmm... This type of reincarnation is very rare.*")
        sprint("I wonder if there are more Japanese people here.")
        sprint("*...Is that so, are you leaving now?*")
        sprint("Why does he look so sad?")
        sprint("*I am unable to move from this spot. I was sealed here for over 300 years.*")
        sprint("*By a short, slender, silver-black haired girl. With Snow-white skin and small apple red lips...*")
        sprint("Wow, how observant of him.... and, uh, why is he sealed away???")
        sprint("Okay... sooo, you want to be friends?")


        sprint("*HAHA, WHAT?*")
        sprint("*A mere slime wants to be friends with the great Storm Dragon Veldora!?*")
        sprint("Wellll... If you don't want to, that's fine too.")
        sprint("*WHAAAAAAT, Who said we couldn't!*")
        sprint("I guess I won't have a reason to come back here again, huh.")
        sprint("*Wait. I guess it can't be helped. I'll become your friend!.*")
        sprint("Great. Now I guess I should help you with this seal eh?")
        sprint("[Great Sage]?")
        ssprint("<<Answer, analysis shows it's impossible to destroy [Infinity Prison] using any physical attacks.>>")
        sprint("Is that so...")
        ssprint("<<Note, possible solution may be...")
        sprint("*Hey don't just only talk to your own skill.*")
        sprint("Jealous?")
        sprint("It might be possible if we both analyze [Infinity Prison] inside and out")
        sprint("*My skills were sealed away as well, I can't use analyze.*")
        sprint("If you give me the information [Great Sage] can analyze your side as well")
        sprint("*Won't that take a long time, didn't you want to go find other reincarnates from your world*")
        sprint("I have a suggestion. How would you like to")
        sprint("get in my stomach.")
        sprint("*hahaha*")
        sprint("*ku hahaha*")
        sprint("*HAHAHAHAHAHAHA*")
        sprint("Ummmm, did he just use the 3 stage laugh?")
        sprint("My life is in your hands.*")
        sprint("Wow how trusting.")
        sprint("*Well... The alternative is to stay in this cave for the rest of my time.*")
        sprint("I'll use predator to swallow you.")
        sprint("*Before that, let me give you a name. You think of a name for both of us.*")
        sprint("Like a last name? hmmmmm...")


        sprint("'Storm Dragon'... Storm... How about Tempest?")
        sprint("*What a good name!*")
        sprint("He actually likes it?")
        sprint("*From now on I'll be Veldora Tempest!*")
        sprint("*And as for you.... How about Rimuru.*")


        sprint("Alright, get out of there as quick as you can!")
        sprint("*Leave it to me. Until we meet again*")
        ssprint("<<Use Unique skill [Predator]?>>")

        ActionMenu('Activate Predator, Puyo',
                        [['activate predator', 'predate veldora'], ['move', 'wonder']],
                        [PredateVeldora, puyo])

        ssprint("<<Start analyzing the Unique Skill [Infinity Prison]?>>")
        sprint("Yes, please take care of it [Great Sage].")
        sprint("Now where is the exit?")

def PredateVeldora():
    ssprint("***Rimuru quickly swallows Veldora and his seal with [Predator]***")

def MagicPerception():
    sprint('...')
    print(slime_art.magic_perception)
    sleep(2)

def shutit():
    sprint("*OHOHO, So you want to die, you maggot!*")

def baldy():
    sprint("*BALDY, HAHAHA, SEEMS THAT YOU WANT TO DIE!*")

def eatGrass():
    sprint("Ooooweeee more grass!")


def squash():
    sprint("hehhhh")
    sprint("Is that so....")
    sprint("hmmmmmm, mhmmmm")

def puyo():
    sprint("Puyo!")

def MoveLegs():
    sprint("You can't feel any legs to move, what is happening?")

def MoveArms():
        sprint("Where are my arms, I can't feel them!")

