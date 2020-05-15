from chapters import *

# Manga, Chapter 1
def Chapter1():
    


        print()
        print("----------Tensei Shitara Slime Datta Ken (That Time I Got Reincarnated as a Slime)----------")
        instructions = """
    NOTE: 
        - ASCII art will be displayed, set window size accordingly (Full screen for best results)
        - You can access inventory/attributes whenever input is possible, (stats, inv)
        - The first action available will always continue the story. (try the other options first maybe, see what happens, idc)
        - Input is not case sensitive, but some symbols may need to be used.
        """
        print(instructions)
        usrcont = input("Press Enter to continue > ")
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
        sprint('.....')
        rimuru.SkillUpgrade(Sage_Skill(), Great_Sage_Skill())
        sleep(t3)

        sprint(rimuru.ShowAttributes())

        ssprint(".....")
        ssprint("It's so dark, where is this. What happened to me?")
        ssprint("I remembered that I got stabbed while protecting Tamura. Was I... saved?")
        ssprint("That said is this the hospital bed? I can't see anything, I can't hear anything.")

        ActionMenu("Move arms, Twitch legs",
                    [['move arms', 'move'], ['twitch legs']],
                    [MoveArms, MoveLegs])

        ssprint("hm? eh? My limbs don't seem to be responding!?")
        ssprint("That's not possible I was only stabbed, my arms and legs should be all fine... Right?...")
        ssprint("Don't tell me I was paralyzed because my nerves were cut?")
        ssprint("Hey hey hey, Give me a break already... AH!?")
        ssprint("I moved!? Below my abdomen(?), is that grass?")
        ssprint("There is also no sense of sight, hearing, and smell. There is only 'touch'... What about taste?")
        ssprint("Alright, Let's try to taste it. Actually! Where the fuck is my mouth?")
        ssprint("The grass melted. Is it being absorbed after melting?")
        ssprint("WAIT A MINUTE, am I even human anymore!!?! Eh.. Let's calm down and confirm my appearance.")

        ActionMenu('Move, Puyo',
                    [['squash', 'move', 'twitch'],['puyo', 'poyo']],
                    [squash, puyo])

        ssprint("Wait what kind of joke is this! Who would accept something like this!!")
        ssprint("ahhhh... but... Dissolving and absorbing plants, this streamlined elastic feeling body shape.")

        ssprint("***Although Minami Satoru didn't want to admins it.***")
        ssprint("***He has reincarnated into a slime!***")

        print(slime_art.slime)
        sleep(3)

        ssprint("puyo, puyoyoyo.... stretch....bounce")
        ssprint("It's been a long time since I've accepted myself a slime. I've gotten used to this elastic body.")
        ssprint("I can't feel heat nor cold. Even after bumping into rocks I'll quickly regenerate.")
        ssprint("And there was no need for sleep or eat either. This body isn't so bad. It's just very lonely.")
        ssprint("This is the only problem I can't solve, so i started eating grass in order to pass time.")

        ActionMenu('Eat grass, Move, Wonder, Puyo',
                    [['eat grass', 'absorb grass'], ['move', 'wonder', 'puyo']],
                    [eatGrass, puyo])

        ssprint("I've ate what seems like a lot of grass, and yet I haven't pooped yet. So where did all the grass go?")
        ssprint("<<Answer. They are stored inside the Unique Skill [Predator]'s stomach sack.>>")
        ssprint("Whoa, somebody actually answered!?!")
        ssprint("<<Note, the current spaced used is less than 1%.>>")
        sprint("I've heard this before, this voice that sounded computer synthesized.... Who is that?")
        ssprint("<<Answer. This is the Unique Skill [Great Sage], the ability has adapted, so it can quickly answer you.>>")
        ssprint("[Great Sage]? [Predator]? heh?!")
        ssprint("Speakin of which, when I died I seemed to have acquired some of skills. That said, what are skills?")

        ActionMenu('Skills?, Great Sage?, Predator?, Eat grass, Wonder',
                    [['skills?', 'what are skills?'], ['great sage?', 'What is Great Sage?'], ['predator?', 'What is predator?'], ['eat grass', 'gras'], ['wonder', 'move']],
                    [WhatAreSkills, WhatIsGreatSage, WhatIsPredator, eatGrass, puyo])


        ssprint("Although I don't understand it too much. It seems like it's just how this world works.")
        ssprint("Although it's a skill, I now have someone to talk to.")
        ssprint("***Getting carried away and not having all of his normal senses. The little slime fell into what seemed to be water***")
        ssprint("I'm going to die! SHIT! I've finally reincarnated and I'm already going to die!")
        ssprint("Great sage how painful is it to suffocate to death!?")
        ssprint("<<Answer. A slime's body does not need oxygen.>>")
        sprint("I am indeed not feeling any pain, at this time my brain cells (or slime body) thought up a strategy.")
        ssprint("Lets try swallowing large amounts of water and propelling myself by spitting out a water jet. I hope this works!")
        rimuru.AddAttribute(Hydraulic_Propulsion())
        sleep(t2)

        sprint("*Can you hear me little one.*")
        ssprint("Whaaaa? What was that, I almost pissed myself. Who's that speaking to me!?")
        ssprint("It's not [Great Sage], so who is it? This is bad, I'm getting nervous. This is the first conversation I'm having since reincarnating.")

        ActionMenu('Follow voice, Eat grass, Wonder',
                    [['follow voice', 'locate voice'], ['eat grass', 'grass'], ['wonder', 'puyo']],
                    [FollowVoice, eatGrass, puyo])


        ActionMenu('Shut it baldy, Wonder, Eat grass, Puyo',
                    [["what's that baldy", 'shut it baldy', 'shut up baldy'], ['eat grass', 'grass'], ['move', 'wonder']],
                    [baldy, eatGrass, puyo])

        ssprint("Was I heard?")
        sprint("Sorry!, I never expected to be able to speak with anything other than my skill by thought...")
        sprint("Right now I am in a state that's unable to see anythin....Ummmm you are?.")
        sprint("*This is telepathy. It's Hard to converse if you can't see... Alright, I'll help you see.*")
        sprint("eh?")
        sprint("*Just don't be scared when you see my true form. There is something called [Magic Perception], it allows you to perceive the surrounding magic essence.*")
        sprint("Magic essence?...")
        ssprint("<<Answer. This world is covered with magic essence for example, the body of a rimuru can move because it absorbs magic essence.>>")
        sprint("*If you are able to perceive the flow of magic essence outside of your body, then you'll get the skill.*")
        sprint("*With that you will be able to 'see' and 'hear'.*")
        sprint("Eh... this feels really complicated. Wellllll, it won't hurt to try... Will it?).")
        sprint("I sense something floating, is this the so called magic essence?")
        rimuru.AddAttribute(Magic_Perception_Skill())

        sprint("Ehh, just like that heh?")
        ssprint("<<Suggestion, in order to organize large amount of information,  activate linking with [Great Sage] and [Magic Perception].>>")
        ssprint("<<Activate [Magic Perception]?>>")

        ActionMenu('Activate Magic Perception.',
                    [['activate magic perception', 'activate magic sense'], ['move', 'wonder']],
                    [MagicPerception, puyo])

        sprint("OH!")
        sprint("Hmmmmmmmm")
        sprint("I can see. I CAN SEE!")
        sprint("*Seems like you did it*")
        sprint("Yes thank you!")
        sprint("*Then shall I introduce myself, again?*")

        ActionMenu('Sure, Nah',
                    [['sure', 'yes'], ['nah', 'no']],
                    [MeetDragon, please])
        
        sprint("So you are a reincarnate from another world, hmmmm... This type of reincarnation is very rare.*")
        sprint("I wonder if there are more Japanese people here.")
        sprint("*...Is that so, are you leaving now?*")
        ssprint("Why does he look so sad?")
        sprint("*I am unable to move from this spot. I was sealed here for over 300 years.*")
        sprint("*By a short, slender, silver-black haired girl. With Snow-white skin and small apple red lips...*")
        ssprint("Wow, how observant of him.... and, uh, why is he sealed away???")
        sprint("Okay... sooo, you want to be friends?")


        sprint("*HAHAHA, WHAT?! A mere slime wants to be friends with the great Storm Dragon Veldora!?*")
        sprint("Wellll... If you don't want to, that's fine too.")
        sprint("*WHAAAAAAT, Who said we could not!*")
        sprint("I guess I won't have a reason to come back here again, huh.")
        sprint("*Wait. I guess it can't be helped. I'll become your friend!.*")
        sprint("Great. Now I guess I should help you with this seal eh? [Great Sage]?")
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
        ssprint("Ummmm, did he just use the 3 stage laugh...?")
        sprint("My life is in your hands.*")
        sprint("Wow how trusting of you.")
        sprint("*Well... The alternative is to stay in this cave for the rest of my time.*")
        sprint("I'll use predator to swallow you now.")
        sprint("*Before that, let me give you a name. You think of a name for both of us.*")
        sprint("Like a last name? hmmmmm...")

        veldoraLName = str(input("\nLast Name > "))
        Veldora_Tempest.familyName = veldoraLName
        rimuru.familyName = veldoraLName

        sprint(f"Hmmmmmm... How about {Veldora_Tempest.familyName}")
        sprint("*What a good name!*")
        sprint("He actually likes it?")
        sprint(f"*From now on I'll be Veldora {Veldora_Tempest.familyName}*")
        sprint("*And as for you...*")

        rimuruName = str(input("\nName > "))
        rimuru.name = rimuruName

        sprint(f"*How about {rimuru.name} {rimuru.familyName}")
        rimuru.ShowAttributes()
        rimuru.ShowInventory()

        sprint("Alright, get out of there as quick as you can!")
        sprint("*Leave it to me. Until we meet again*")
        ssprint("<<Use Unique skill [Predator]?>>")

        ActionMenu('Activate Predator, Puyo',
                        [['activate predator', 'predate veldora'], ['move', 'wonder']],
                        [PredateVeldora, puyo])

        ssprint("***The slime little grew big enough to completely engulf the dragon and his seal in mere seconds before turning back to normal***")

        ssprint("<<Start analyzing the Unique Skill [Infinity Prison]?>>")
    
        ActionMenu('Yes, No, Eat grass, Wonder, Puyo',
                        [['yes', 'y'], ['no', 'n'], ['eat grass', 'grass'], ['move', 'wonder']],
                        [startAnalyse, noAnalyse, eatGrass, puyo])
        
        ssprint("Now where is the exit?")

def startAnalyse():
    ssprint("Yes, please take care of it [Great Sage].")

def noAnalyse():
    sprint("Ummmmm, I guess he's just stuck in my stomach now forever....")

def FollowVoice():
        ssprint("I'll have to be friendly. But how do I even reply?. It's not like I have a mouth to speak with.")
        sprint("*Hey can you just reply?*")

def MeetDragon():
    sprint("My name is Storm Dragon Veldora!*")
    print(slime_art.cave_veldora)
    sleep(1)

    sprint("*I am one of the four True Dragons of this world.*")
    sprint("HOLY SHIT, you're a real dragon!")
    sprint("*Didn't I tell you not to get scared.*")
    ssprint("***even with the scary appearance, the little slime and dragon started chatting.***")

def please():
    sprint("*Please!?*")

def WhatAreSkills():
    ssprint("<<Answer. When growth is recognized by the world, occasionally one will obtain a [Skill].>>")

def WhatIsGreatSage():
    rimuru.ShowInfo("Great Sage")

def WhatIsPredator():
    rimuru.ShowInfo("Predator")

def PredateVeldora():
    ssprint("***Rimuru quickly swallows Veldora and his seal with [Predator]***")

def MagicPerception():
    sprint('...')
    print(slime_art.magic_perception)
    sleep(2)

def shutit():
    sprint("*OHOHO, So you want to die, you little shit!*")

def baldy():
    ssprint("*BALDY, HAHAHA, SEEMS THAT YOU WANT TO DIE!*")

def eatGrass():
    ssprint("Ooooweeee more grass!")
    rimuru.AddInventory(Grass_Item(), capacity=0.01)

def squash():
    ssprint("hehhhh")
    ssprint("Is that so....")
    ssprint("hmmmmmm, mhmmmm")

def puyo():
    sprint("Puyo!")

def MoveLegs():
    ssprint("I can't feel any legs to move, what is happening?!?!")

def MoveArms():
        ssprint("Where are my arms, I can't feel them!")

