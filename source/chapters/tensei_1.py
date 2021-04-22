# Import all game_functions' funcs for easy access.
from game_files.functions import *
# Import the next chapter to continue to.
from chapters.tensei_2 import ch2_goblin_encounter
from game_maps.game_location import *
from game_files.characters import Veldora_Tempest

def ch1_cave():
    class wake_up():
        __location = 'Sealed Cave'

        def __init__(self):
            gprint("\n< Chapter 1 >\n")
            idots()
            gprint("\n<< Confirmation Complete. Constructing body that does not require blood... >>\n")
            gprint("<< Confirmation Complete. Acquiring Extra Skill: [Predator]... >>")
            gprint("<< Acquired Extra Skill [Predator]. >>")
            gprint("\n<< Confirmation Complete. Acquiring: Extra Skill [Sage]... >>")
            gprint("<< Acquired Extra Skill [Sage]. >>")
            rimuru.upgrade_attribute('Sage', 'Great Sage')

            siprint("\nIt's so dark? Where am I? What happened?")
            siprint("I remember now, I got stabbed! A-am I dead?")
            siprint("Was I saved? Can I move? Should I try to say something?")

            # Because I am a dick. There is a 1 in 1,000 chance that you will wake up and just instantly die! kek!
            if get_random(1, 1_000, 666):
                siprint("\nWAIT! WAIT WHAT'S THAT AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
                siprint("SOMETHING IS EATING MEEEEEEEEEEEEEEEEEEEEEEEEEE!!!!!!!!!!!!!!!")
                print("\n\n*You died before you could even do anything, what bad luck you have!*")
                print("* Watch out for [Evil Centipedes] on your next reincarnation little slime! hehehehee.... *")
                game_over()

            # Show user HUD and playable actions.
            game_action(self)

        class speak:
            __subs = ['try to speak', 'try speaking', 'try to talk', 'try talking', 'talk', 'say something', 'try to say something', 'yell', 'try to yell', 'try yelling', 'say something', 'try saying something', 'use mouth']
            def __init__(self):
                siprint("I can't seem to speak, wait.....")
                siprint("I CAN'T FEEL MY MOUTH!")
                siprint("I. Can't. Feel. ANYTHING! I should check the rest of my body!")

        class move:
            __subs = ['move around', 'try to move', 'look around', 'explore']
            def __init__(self):
                siprint("I can't see anything! Where are my arms, I can't feel them!")
                siprint("Did I just move? I can't see anything, can't hear, can't even smell anything...")
                siprint("What is this? Feels like I'm 'absorbing' something. This body? Am I even human anymore!?!?!")

        class _inspect_body(cave_actions):
            __subs = ['examine', 'examine body', 'examine self', 'examine myself', 'inspect', 'check body', 'confirm body', 'inspect my body', 'feel body', 'feel', 'feel around', 'move around', 'check', 'check if human']
            def __init__(self):
                siprint("What is that feeling? Is....is that grass?! It feels like it's dissolving...")
                gprint("\n< Tutorial: Try to 'eat grass' or 'eat ore', see what happens. >")
                game_action(self)

            class puyo:
                __subs = ['squish', 'bounce']
                def __init__(self):
                    sprint("Puuuuuuuuuuuuyooooooooooo!")

            class eat_grass:
                __subs = cave_actions.eat_grass.__subs
                def __init__(self):
                    rimuru.add_inventory('hipokte grass')
                    wake_up._inspect_body._explore()

            class eat_ore:
                __subs = cave_actions.eat_ore.__subs
                def __init__(self):
                    rimuru.add_inventory('magic ore')
                    siprint("What is this hard feeling stuff?")
                    siprint("<< Information, analysis shows this is the raw form of [Magisteel]. Can be used for crafting weapons, armor, and more. >>")
                    siprint("Ok, might be useful in the future. Guess I should get as much as I can")
                    wake_up._inspect_body._explore()

            class _explore(cave_actions):
                __subs = subs.move_on
                def __init__(self):
                    show_art('slime')
                    print(game_art.rimuru_art.died)
                    idots()
                    siprint("Dissolving and absorbing, this streamlined elastic feeling body....")
                    siprint("It looks like I have been stabbed, died and reincarnated as a slime!")
                    idots(10, 2)
                    siprint("\nIt's been a long time since I have accepted myself a slime. I am getting use to this body.")
                    siprint("No need for sleep or food. I don't feel too hot nor cold. Even after taking some damage I can heal myself..\n")
                    siprint("All I can do is fumble around in the dark and eat what I find... I'M SO BORED!")

                    game_action(self)

                class _hfunc_craft_full_potion:
                    def __init__(self):
                        if rimuru.check_acquired('full potion'):
                            siprint("I have a feeling these will come in handy.")

                class _keep_exploring:
                    __subs = subs.move_on + ['fumble around', 'keep fumbling', 'fumble', 'more fumbling', 'fumble more']
                    def __init__(self):
                        siprint("It's just... very lonely here. Wherever here is. I've been eating grass just to pass the time.")
                        siprint("There seems to be always some grass to eat, the occasional magic ore, and more to explore!")
                        siprint("But lets keep moving!")
                        in_water()

                class what_are_skills:
                    __subs = ['what are skills', 'skills', 'tell me more about skills', 'what are these skills']
                    def __init__(self):
                        siprint("<< Answer, when growth is recognized by the world, occasionally one will obtain a [Skill]. >>")
                        siprint("What an interesting world! It's nice to have someone to talk to, even if it is a one way with a skill.")

                class what_is_predator:
                    __subs = ['predator', 'what is predator', 'what is this predator', 'what is this predator skill', 'predator huh', 'tell me more about predator', 'tell me more about predator']
                    def __init__(self):
                        siprint("<< Answer, unique skill [Predator] allows one to 'eat' targets, store said targets in skill's stomach, or isolate as hazardous material. >>")
                        siprint("<< Also, after successful analysis on a monster one can use mimicry to replicate appearance, and use replaceable abilities from target. >>")
                        gprint("\n< Tutorial: Try 'info predator' to get more information. >")

                class what_is_great_sage:
                    __subs = ['what is this great sage', 'what is great sage', 'great sage', 'tell me more about great sage', 'what are you', 'tell me more about you', 'tell me more about yourself great sage', 'tell me more about yourself', 'what are you', 'who are you', 'what is you']
                    def __init__(self):
                        siprint("<< Answer, my function is to assist my master (you) to the best of my abilities. >>")
                        siprint("<< Information, some of my basic functions are: Analysis, skill control and manipulation, crafting, and more. >>")
                        gprint("\n< Tutorial: Use 'info great sage' to get more information. >")

                        if rimuru.check_acquired('hipokte grass'):
                            gprint("< Tutorial: Try 'info hipokte grass'. Then try 'craft full potion'. >")

                class where_did_it_go:
                    __subs = ['where it go', 'where did the grass go', 'where did that all go', 'hey where did that go', "where's the grass", "where's the grass now", 'where is the grass', 'where is the grass now', 'where did it go', 'where does it go', 'where does it all go', 'where do they go', 'where do they all go', 'where does it all go', 'where has it gone', 'where has it all gone']
                    def __init__(self):
                        siprint("Where does the stuff I eat go?")
                        siprint("<< Answer, they are stored inside the Unique Skill [Predator]'s stomach sack. >>")
                        siprint("Whoa! Who's that? I think I heard this voice before. Who, or what, are you?")
                        siprint("<< Answer, this is the Unique Skill [Great Sage], the ability has adapted to best assist you. >>")
                        siprint("Skills, Great Sage, Predator? huh... Wonder what those are. I should get moving too.")

    class in_water:
        __location = "Under water?"
        def __init__(self):
            print(game_art.rimuru_art.fall_in_water)
            siprint("I'M GOING TO DIE... AGAIN!")
            siprint("SHIT! I've finally reincarnated and I'm already going to die!")
            siprint("O'Great sage how painful thy death will be? Am I really going to suffocate to death?!?!")
            siprint("<< Information, A slime's body does not require oxygen to survive. >>")
            siprint("Huh.... I'm not feeling any pain. But what am I going to do now?\n")
            idots()
            siprint("I thought of something... I could suck up some of water then I can and expel it at a high pressure...")
            game_action(self)

        class stay_in_water:
            __subs = subs.wait + ['stay in water', 'wait in water']
            def __init__(self):
                idots()

        class eat_water:
            __subs = ['suck it up', 'intake water', 'suck water', 'suck up water', 'suck in water', 'suck up some water', 'intake some water', 'suck water up', 'eat more water', 'predate more water', 'suck up more water']
            def __init__(self):
                rimuru.add_inventory('water')
                siprint("\nAlright, now lets try this out.")

        class try_getting_out:
            __subs = ['spew water', 'eject water', 'vomit water', 'try getting out', 'try to get out', 'swim', 'swim up', 'swim out', 'try swimming', 'leave water', 'try to swim', 'find a way out', 'get out', 'use water to propel', 'propel with water', 'expel water to propel', 'expel', 'expel water', 'expel the water', 'use hydraulic propulsion']
            def __init__(self):
                if rimuru.check_acquired('water'):
                    rimuru.add_attribute('Hydraulic Propulsion')
                    rimuru.use_action('hydraulic propulsion')
                    siprint("\nLet's see if I can get out now.")
                    siprint("\nOuch! I went flying and hit something, but at least it seems like I'm back on land.")
                    siprint("I also got a new skill too, wonder what else I can do with it.")
                    veldora_encounter()
                else:
                    siprint("I need figure out a way to get out of this situation.")

        class hfunc_grab_sword:
            __subs = ['look for treasure', 'look for things', 'search for things', 'search for treasure', 'grab sword', 'get sword', 'eat sword', 'predate sword', 'find treasure', 'grab treasure', 'eat treasure', 'predate treasure']
            def __init__(self):
                rimuru.add_inventory('magic sword')
                siprint("\nHEY! Look! This shape, feels like a sword! Wonder if it's any good?")
                siprint("<< Answer, analysis of sword shows it contains a magisteel core. This sword is above average. >>")
                siprint("Would you look at that, that might come in handy later on. But I'm still stuck down here!")
                clear_subs(self)  # Only able to grab sword once.

    class veldora_encounter(cave_actions):
        __location = "Sealed Cave"

        def __init__(self):
            sprint("\n~ Can you hear me small one. ~")
            siprint("\nI almost pissed myself, if I could that is. Who's that speaking to me!? It can't be [Great Sage] could it?")
            siprint("This is the first conversation I'm having since reincarnating. According to [Great Sage] I've been in this cave for about 90 days!")
            siprint("Should I be friendly? But how do I even reply?. It's not like I have a mouth to speak with.")
            sprint("\n~ Hey, can you just reply? ~")
            game_action(self)

        class hello:
            __subs = ['hi', 'reply', 'reply hi', 'reply with hi', 'repy with hello', "who's there", 'who is there', 'who is that', 'somebody there', "who's out there", "is somebody there", 'who is that speaking', 'hello', 'hello there', "who's that speaking", "who's that talking"]
            def __init__(self):
                sprint("~ Keep following my voice small one. ~")

        class great_sage:
            __subs = ['that you great sage', 'is that you great sage', 'was that you great sage', 'was it great sage', 'great sage']
            def __init__(self):
                siprint("<< Information, negative, that was not me. I am detecting incoming telepathy, source unknown. >>")
                siprint("Maybe I can try to following it if I keep moving, it seems to be getting stronger.")

        class _leave:
            __subs = subs.move_on
            def __init__(self):
                sprint("...")
                sprint("~ Wait where are you going? ~")
                sprint("\nYou seem pretty suspicious...")
                sprint("\n~ Nooooo.... I'm not suspicious at all.l.l.. ~")
                tempest_serpent_encounter()

        class shut_it:
            __subs = ["shut it you baldy", "screw you baldy", 'shut up baldy', 'shut up', 'shut it']
            def __init__(self):
                sprint("~ HAHAHA, SEEMS LIKE YOU HAVE A DEATH WISH!!! ~")
                sprint("\nI'M SORRY!")
                sprint("I'm sorry! I didn't think you could hear me!")
                sprint("\n~ Come closer small one. ~")
                siprint('\nuh.... Should I follow the voice?')

        class _follow_voice:
            __subs = ['follow the voice', 'locate the voice', 'try locating the voice', 'try locating voice', 'try finding the voce', 'try following the voice', 'seek out voice', 'seek voice', 'follow strange voice', 'seek strange voice', 'follow']
            def __init__(self):
                siprint("I hit something, but it's not a rock. And what is this aura that I'm feeling? Could it be?")
                sprint("\nHello? I never expected to speak with anyone other than my skill, since I can't see or hear.")
                sprint("\n~ This is telepathy. hmmmm..... Alright... fine, I'll help you see. Just don't be scared when you see my true form.")
                sprint("~ There is something called [Magic Perception], it allows you to perceive the surrounding magic essence. ~")
                sprint("\nWhat's this magic essence?...")
                siprint("<< Answer, this world is covered with magic essence for example, the body of a slime can move because it absorbs magic essence from it's surroundings. >>")
                sprint("\n~ With this skill you will be able to 'see', 'hear' and much more! ~")
                sprint("\nEh... this feels really complicated. It won't hurt to try though... Will it???")
                siprint("<< Suggestion, in order to organize large amount of information, would you like to activate linking with [Great Sage] and [Magic Perception]. >>")
                game_action(self)

            class _use_magic_perception(cave_actions):
                __subs = ['try magic perception', 'try using magic perception', 'activate magic perception', 'yes', 'yes please', 'yes do it', 'activate', 'activate it', 'yes, activate it']
                def __init__(self):
                    idots(3)
                    show_art('magic perception')
                    rimuru.add_attribute('Magic Perception')
                    rimuru.use_action('magic perception')
                    sprint("\nLike this?")
                    sprint("I can see. I CAN SEE!")
                    sprint("\n~ Looks like you did it. You learn quickly small one. ~")
                    sprint("Yes, thank you!")
                    sprint("\n~ Shall I formally introduce myself now? ~")
                    game_action(self)

                class _yes:
                    __subs = ['sure', 'why not', 'go ahead']
                    def __init__(self):
                        sprint("~ My name is Storm Dragon Veldora! ~")
                        show_art('cave veldora')
                        sprint("~ I am one of the four True Dragons of this world. ~")
                        sprint("\nHOLY SHIT, you're a real dragon!")
                        sprint("\n~ Didn't I tell you not to get scared. ~")
                        friend_veldora()

                class _no:
                    __subs = ['no', 'nah', "let's move on", "don't", 'skip', 'skip it']
                    def __init__(self):
                        sprint("~ Alright fine, I won't. Hmmmmph ~")
                        friend_veldora()

            class wait:
                __subs = subs.no
                def __init__(self):
                    sprint("~ Welllll? I'm waiting..... ~")
                    siprint("\n<< Notice, activate linking? >>")

            class _leave:
                __subs = subs.move_on + ['no, leave', 'leave', 'leave him', 'leave dragon', 'escape']
                def __init__(self):
                    sprint("Wait where are you going small one! Weren't we getting somewhere......")
                    sprint("Hello? Hellooooooooooo?!")
                    sprint("FINE! I don't need you anyways!")
                    tempest_serpent_encounter()

    class friend_veldora(cave_actions):
        def __init__(self):
            sprint("\nHmmmm, now what?")
            siprint("Should I try make a friend? Or just leave, there's something suspicious about him...")
            game_action(self)

        class _leave:
            __subs = subs.move_on
            def __init__(self):
                sprint("I guess I'll be heading out now.")
                sprint("\nReally, so soon. But we just started!")
                sprint("Stay, please, we have so much to talk abo.o.o...")
                siprint("\nPhew, I think I lost him.\n")
                tempest_serpent_encounter()

        class _friend_dragon(cave_actions):
            __subs = ['befriend dragon', 'ask to become friends', 'want to be friends', 'wanna be friends', 'become friends', 'friend', 'friend him', 'ask to be friends', 'make friend']
            def __init__(self):
                sprint("Okay... sooo, you want to be friends?")
                sprint("\nHAHAHA, WHAT?! A mere slime wants to be friends with the great Storm Dragon Veldora!?")
                sprint("\nWellll... If you don't want to, that's fine too.")
                sprint("\nNow hold on, who said we can't!")
                sprint("\nI guess it can't be helped.")
                sprint("\nGreat. Now I guess I should look this seal heh?")
                siprint("Wonder how he got imprisoned in the first place.....")
                game_action(self)

            class _look_at_seal(cave_actions):
                __subs = ['take a look', 'analyze seal', 'analyze', 'scan', 'scan seal', 'scan prison', 'look at prison', 'analyse seal', 'analyse prison', 'check seal', 'check prison', 'scan seal', 'scan prison', 'check out seal', 'check out prison', 'look', 'inspect', 'inspect seal', 'inspect prison', 'inspect prison seal', 'analyse prison seal']
                def __init__(self):
                    global veldora
                    veldora = Veldora_Tempest()
                    siprint("Great Sage?")
                    siprint("<< Answer, analysis shows it's impossible to destroy [Infinity Prison] using any physical attacks. >>")
                    siprint("<< Notice, possible solution may be... >>")
                    sprint("\nHey, don't ignore me. :(")
                    sprint("\nIt might be possible if we both analyze [Infinity Prison] inside and out")
                    sprint("\nMy skills were sealed away as well, I can't use analyze.")
                    sprint("\nIf you give me the information [Great Sage] can analyze your side as well")
                    sprint("\nWon't that take a long time? Didn't you say something about going out to find other reincarnates?")
                    sprint("\nI have a suggestion!")
                    dots(10)
                    sprint("\nHow about you get in my belly!")
                    sprint("\nhahaha")
                    sprint("ku hahaha")
                    sprint("HAHAHAHAHAHAHA")
                    siprint("\nUmmmm, did he just use the 3 stage laugh?!?")
                    dots(5)
                    sprint("\nMy life is in your hands.")
                    sprint("\nWow how trusting of you.")
                    sprint("\nWell... The alternative is to stay in this cave for the rest of my lonely time. Which is about another 100 years.")
                    sprint("Before that, let me give you a name, and you think of a name for both of us.")
                    sprint("\nLike a family name? hmmmmm...")

                    new_family_name = str(input("\nPick a shared family name (last name) > "))
                    veldora.update_lname(new_family_name)
                    print()
                    rimuru.update_lname(new_family_name)
                    rimuru.add_protection('Storm Crest')
                    rimuru.update_level(8)

                    sprint(f"Hmmmmmm... How about {new_family_name}")
                    sprint("\nThat. Name. Is. AWESOME!")
                    siprint("\nHe actually likes it?")
                    sprint(f"\nFrom now on I will be Veldora {new_family_name}")
                    sprint("\nAnd as for you...")
                    rimuru.update_name(str(input("\nPick name for yourself > ")))
                    sprint(f"\nHow about {rimuru.name}!")
                    rimuru.update_standing('veldora', 1)

                    sprint("\nI am ready now, until we meet again small one!")
                    siprint("\n<< Use Unique skill [Predator]? >>")
                    game_action(self)

                class eat_grass:
                    __subs = cave_actions.eat_grass.__subs
                    def __init__(self):
                        rimuru.add_inventory('hipokte grass')
                        sprint("Hey what are you doing there? Focus on me... ME!")

                class _eat_veldora:
                    __subs = subs.all_yes + ['predate veldora', 'eat dragon', 'eat the dragon', 'predate dragon', 'predate the dragon', 'swallow dragon', 'swallow veldora']
                    def __init__(self):
                        global veldora
                        rimuru.add_inventory(veldora, show_analysis_msg=False)
                        rimuru.update_standing('veldora')
                        siprint("<< Notice, start analyzing Unique Skill [Infinity Prison]? >>")
                        game_action(self)

                    class _start_analysis:
                        __subs = subs.all_yes + ['start it', 'yes start it please', 'yes start it']
                        def __init__(self):
                            siprint("Yes! Please take care of it [Great Sage].")
                            rimuru.update_status('veldora', 'Analyzing')
                            gprint("< Starting Analysis: Unique Skill [Unlimited Imprisonment] >")
                            rimuru.update_standing('veldora', 1)
                            siprint("I hope you get out quickly Veldora!")
                            tempest_serpent_encounter()

                    class _move_on:
                        __subs = subs.move_on + ['ignore him, lets move on']
                        def __init__(self):
                            siprint("ehehhh... Veldora is gonna be pissed that I didn't immediately start, will he think I betrayed him...")
                            rimuru.update_standing('veldora', -2)
                            tempest_serpent_encounter()

                class ask_about_seal:
                    __subs = ['so how did you get here anyways', 'ask about seal', 'ask about his story', 'how did you get imprisoned', 'how did you get here', 'who did this to you']
                    def __init__(self):
                        sprint("Will you see, that's kind of a long story. Not one to be told here.")

            class _leave_veldora(cave_actions):
                __subs = subs.move_on + ['leave veldora', 'leave friend', 'abandon veldora', 'abandon him', 'abandon friend']
                def __init__(self):
                    siprint("OK, I go now.")
                    siprint("\nWAIT! WHAAAAAT!")
                    siprint("I thought we were friends! :(.......")
                    siprint("\nPlease come back friend!")
                    sprint("\nI got to go! Bye!")
                    tempest_serpent_encounter()

    class tempest_serpent_encounter:
        def __init__(self):
            mobs_add(['tempest serpent', 'giant bat', 'black spider', 'evil centipede'])
            siprint("\nI've been looking for the cave exit for a bit now.... This cave is so big! Or am I just small?")
            siprint("<< Answer, you are just small. >>")
            siprint("Oh, thanks for that.")
            siprint("\n* But before long some monsters started taking a interest in the small slime. *")
            siprint("\nWhat is that? it looks like a big snake!")
            siprint("<< Answer, analysis indicating [Tempest Serpent]. >>")
            siprint("Still, it's not as scary as Veldora. I should be able to handle it.")
            siprint("However, I don't think I have any ways to attack or damage it if it's hostile. Hmmmmmm. I wonder...\n")
            rimuru.add_attribute('water blade')
            siprint("\nHey, it worked. Since I already have [Hydraulic Propulsion], I was thinking I could use super high pressure water as a blade attack also.")
            gprint("\n< Tutorial: First target with 'target tempest serpent'. Then attack with 'attack water blade'. >")
            game_action(self)

        class sneak_away:
            __subs = ['sneak out', 'try sneaking out', 'try to sneak out', 'try escaping', 'try to sneak away', 'try sneaking away', 'try sneaking out', 'try slipping out', 'try to slip away', 'try to slip out', 'slip away']
            def __init__(self):
                siprint("Crap! It noticed me, no sneaking out now!")

        class _move_on:
            __subs = subs.move_on
            def __init__(self):
                if mobs_cleared():
                    at_cave_exit()
                else:
                    siprint("I still sense some enemies around. I should clear them out before they give me trouble.")
                    if rimuru.check_acquired('sense heat source'):
                        siprint("Oh yeah! I have that new [Sense Heat Source] skill, that might be useful.")
                        gprint("\n< Tutorial: Try Mimicking [Tempest Serpent] and using it's [Sense Heat Source] to locate nearby mobs. '/help' for more info on commands. >")
                        gprint("< Tutorial: While mimicking, use 'stats' to see your's and mimicked monster's attributes and skills. > ")
                    if rimuru.check_acquired('magic perception'):
                        gprint("\n< Hint: If acquired [Magic Perception], you can use 'nearby' command to see nearby mobs. >")

        class hfunc_attack:
            __subs = ['attack water blade']
            def __init__(self):
                if not mob_status('tempest serpent'):
                    siprint("Wow, what a powerful attack. I should probably use that only when needed.")
                    siprint("<< Suggestion, Use Unique Skill [Predator]? >>")
                    siprint("Oh...? What will that do?")
                    siprint("<< Answer, after predation, information and target's skills may be obtained through analysis. >>")
                    gprint("\n< Tutorial: Try 'eat' or 'predate' on targeted mobs that are dead to use predation. >")

                if mobs_cleared():
                    at_cave_exit()

    class at_cave_exit:
        def __init__(self):
            mobs_reset()
            mobs_add(['kaval', 'gido', 'eren grimwold'])
            siprint("Finally! Found the exit. Wow, that's a pretty big door. How am I going to open that?")
            siprint("Water attack? No, that'll probably be overkill. Wait somethings happening.")
            siprint("Wait! They look like people! Three of them. What are they doing here?")
            siprint("I should wait and sneak out when they leave.")
            sprint("\nPhew, it's finally open, even the keyhole was rusted.")
            sprint("\nIt is over 300 years old, and nobody is maintaining it. I doubt there's a real dragon in here.")
            sprint("\nStill reckless of the guildmaster to send us to investigate.")
            siprint("\nHow can I understand them?")
            siprint("<< Answer, [Magic Perception] converts sound waves to comprehensible sentences which I interpret for you. >>")
            siprint("<< Also, sound waves can also be used to communicate your thoughts. >>")
            sprint("\nI shouldn't show, they'll probably get scared and attack me")
            game_action(self)

        class _attack:
            __subs = ['attack adventurers', 'attack them']
            def __init__(self):
                if mobs_cleared():
                    siprint("Wasn't necessary, but I suppose it had to be done.")
                    at_cave_exit._hfunc_leave_cave()
                else:
                    siprint("CRAP! I didn't kill all of them, the rest will kill me!")
                    siprint("\n* Before the little slime could do or say anything else, he was swiftly smushed to death! *")
                    game_over()

        class _say_hi:
            def __init__(self):
                sprint("HELLO THERE! My name is Rimu........")
                sprint("\nAHHHHHHHHHHHHHH MONSTER.")
                sprint("\nKILL IT. KILL IT.")
                sprint("\nKILL IT!!!!")
                sprint("\nWAIT, Wait. I'm not a bad slime slurrrr.....")
                siprint("\n* The adventurers attacked and killed the little slime monster before he could say anything else. *")

                if rimuru.check_acquired('veldora'):
                    siprint("* After the little slime died. All of his stomach contents spewed outwards. *")
                    siprint("* Unfortunately, this particular little slime had somehow absorbed a whole dragon! *")
                    siprint("* Now with the three low-level adventurers swiftly flattened by such a massive object. They Have failed there simple mission. *")
                    sprint("\nWhat is this? Where is that little slime? Hello.... Friend?")
                    sprint("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")

                game_over()

        class _wait:
            __subs = ['wait', 'sneak out', 'wait to sneak out', 'wait to slip out', 'try to slip out', 'sneak away', 'sneak out after them', 'wait to sneak away', 'sneak past them']
            def __init__(self):
                if get_random(1, 20, 1):
                    siprint("I sense a monster nearby! There! A slime!")
                    siprint("\nCrap! How did they notice me!")
                    siprint("\n* And before another word could be uttered by the little slime, he was swiftly smushed. *\n")
                    game_over()

                if game_cond('friend veldora', True):
                    siprint("Or... uhm... Should I go back to that pouty dragon or just move on?")

                mobs_reset()
                siprint("Phew, their gone now. I can finally leave now. They even left the door open for me, how nice.")

                game_action(self)

            class _go_to_veldora:
                __subs = ['go find veldora', 'veldora', 'go back to veldora', 'go back to dragon', 'go find that voice', 'find voice', 'follow voice', 'follow voice again', 'go follow voice', 'follow weird voice', 'locate voice', 'search for voice', 'search for weird voice', 'voice', 'what was that voice', 'where is that voice coming from', 'where is that voice', 'where was that voice', 'where was that voice again', 'go back to voice']
                def __init__(self):
                    if rimuru.check_acquired('veldora'): return

                    mobs_reset()
                    if game_cond('friend veldora'):
                        siprint("Let's go check on that dragon.")
                        siprint("\n~ What are you doing back? ~")
                        friend_veldora()
                    else:
                        siprint("I want to go find that weird voice in the cave!")
                        veldora_encounter()

            class _leave:
                __subs = ['leave', 'leave cave', 'exit', 'exit cave', 'move on', 'continue']
                def __init__(self):
                    siprint("Let's leave this cave already!")
                    continue_to(ch2_goblin_encounter)

    wake_up()
