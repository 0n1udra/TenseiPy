from tensei_0 import *

# Manga, Chapter 1
def Chapter1():
    
        print(slimeArt.great_sage)
        sleep(1)
        sprint("...")

        sprint("NOTE: You can access inventory/attributes whenever input is possible, (stats, inv)")
        sprint("NOTE: ASCII art will be displayed, set window size accordingly")

        sprint("<<Confirmation Complete. Constructing a body that does not require blood...>>")
        #TODO Add Skill
        sprint("<<Confirmation Complete. Acquiring Skill [Predator]...>>")
        rimuru.AddAttribute(Predator_Skill())
        sprint("<<Confirmation Complete. Acquiring Extra Skill [Sage]...>>")
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

        ActionMenu("Move Arms, Twitch Legs",
                        [['move arms', 'move'], ['twitch leg']],
                        [MoveArms, MoveLegs])

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

        ActionMenu('Move, Puyo',
                        [['squash', 'move', 'twitch'],['puyo', 'poyo']],
                        [squash, puyo])

        sprint("It's probably is like this!")
        sprint("Wait what kind of joke is this! Who would accept something like this!!")
        sprint("ahhhh... but... dissolving and absorbing plants, this streamlined body shape.")
        sprint("And this sort of elastic feeling")

        sprint("***Although Minami Satoru didn't want to admins it.***")
        sprint("***He has reincarnated into a slime!***")

        print(slimeArt.slime)
        sleep(3)

        sprint("puyo, puyoyoyo.... stretch....bounce")
        sprint("It's been a long time since I've accepted myas a slime.")
        sprint("I've gotten used to this elastic body.")
        sprint("I can't feel heat nor cold. Even after bumping into rocks I'll quickly regenerate.")
        sprint("And there was no need for sleep or eat either.")
        sprint("It's just very lonely")
        sprint("This is the only problem I can't solve, so i started eating grass in order to pass time.")

        ActionMenu('Eat Grass, Move, Wonder, Puyo',
                        [['eat grass'], ['move', 'wonder']],
                        [eatGrass, puyo])

        sprint("I've ate what seems like a lot of grass, and yet I haven't pooped yet")
        rimuru.AddInventory(Grass_Item(), capacity=0.9)
        sprint("So where did all the grass go?")
        sprint("<<Answer. They are stored inside the Unique Skill [Predator]'s stomach sack.>>")
        sprint("Whoa, somebody actually answered!?!")
        sprint("<<Note, the current spaced used is less than 1%.>>")
        sprint("I've heard this before, this voice that sounded computer synthesized....")
        sprint("W-w-w-who is it?")
        sprint("<<Answer. This is the Unique Skill [Great Sage]'s effect.>>")
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
        sprint("Lets try swallowing large amounts of water and propelling myby spitting out a water jet!")
        sprint("I hope this works")
        rimuru.AddAttribute(Hydraulic_Propulsion())
        sleep(t2)

        sprint("*Can you hear me little one.*")
        sprint("Whaaaa? What was that, I almost pissed my")
        sprint("Who's that speaking to me!?")
        sprint("It's not Great Sage, so who is it?")
        sprint("This is bad, I'm getting nervous.")
        sprint("This is the first conversation I'm having since reincarnating into a rimuru.")
        sprint("I'll have to be friendly")
        sprint("But how do I even reply?")
        sprint("It's not like I have a means to speak")
        sprint("*Hey can you just reply?*")

        ActionMenu('Shut it baldy',
                        [['baldy', 'shut it baldy'], ['move', 'wonder']],
                        [baldy, puyo])

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

        ActionMenu('Activate Magic Perception.',
                        [['activate magic perception', 'activate magic sense'], ['move', 'wonder']],
                        [MagicPerception, puyo])
        

        sprint("OH!")
        sprint("Hmmmmmmmm")
        sprint("I can see. I CAN SEE!")
        sprint("*Seems like you did it*")
        sprint("Yes thank you!")
        sprint("*Then let me introduce myagain*")
        sprint("My name is Storm Dragon Veldora.*")
        print(slimeArt.cave_veldora)
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
        sprint("Alright, get out of there as quick as you can!")
        sprint("*Leave it to me. Until we meet again*")
        sprint("<<Use Unique skill [Predator]?>>")

        ActionMenu('Activate Predator, Puyo',
                        [['activate predator', 'predate veldora'], ['move', 'wonder']],
                        [PredateVeldora, puyo])

        sprint("<<Start analyzing the Unique Skill [Infinity Prison]?>>")
        sprint("Yes, please take care of it [Great Sage].")
        sprint("Now where is the exit?")

def PredateVeldora():
    sprint("***Rimuru quickly swallows Veldora and his seal with [Predator]***")

def MagicPerception():
    sprint('...')
    print(slimeArt.magic_perception)
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

