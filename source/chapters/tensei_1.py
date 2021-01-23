# Import all game_functions' funcs for easy access.
from game_files.game_functions import *
# Import the next chapter to continue to.
from chapters.tensei_2 import Chapter2


def Chapter1(rimuru):
    class chapter_1:
        __location = 'Sealed Cave'

        def __init__(self):
            rimuru.set_start_state()
            idots()
            print()
            siprint("<< Confirmation Complete. Constructing body that does not require blood... >>\n")
            siprint("<< Confirmation Complete. Acquiring skill: [Predator]... >>")
            rimuru.add_attribute('Predator')
            siprint("<< Confirmation Complete. Acquiring: Extra Skill [Sage]... >>")
            rimuru.add_attribute('Sage')
            rimuru.upgrade_attribute('Sage', 'Great Sage')

            print()
            siprint("It's so dark? Where is this? What happened?")
            siprint("I remembered now. I got stabbed!")
            siprint("Was I saved? Can I move? Should I try to say something?")
            # Show user HUD and playable actions.
            action_menu(self)

        class move:
            __subs = ['feel', 'touch']

            def __init__(self):
                siprint("Where are my arms, I can't feel them!")
                siprint("Did I just move? I can't see anything, can't hear, can't even smell anything...")
                siprint("What is this thing? It feels like I'm 'absorbing' something.")
                siprint("This body? Am I even human anymore!?!?!")

        class speak:
            __subs = ['try to speak', 'try speaking', 'try to talk', 'try talking', 'talk', 'say something', 'try to say something', 'yell', 'try to yell', 'try yelling']

            def __init__(self):
                siprint("I can't seem to speak, wait.....")
                siprint("I CAN'T FEEL MY MOUTH!")
                siprint("I. Can't. Feel. Anything!")

        class _inspect_body:
            __subs = ['examine', 'examine body', 'examine self', 'examine myself', 'inspect', 'check body', 'inspect my body', 'feel body', 'feel', 'feel around', 'move around', 'check', 'check if human']

            def __init__(self):
                siprint("Dissolving and absorbing, this streamlined elastic feeling body.")
                show_art('slime')
                print(game_art.rimuru_art.died)
                siprint("It looks like I have been stabbed, died and reincarnated as a slime!\n")
                idots(3, 8)
                siprint("\nIt's been a long time since I have accepted myself a slime. I am getting use to this body.")
                siprint("I don't need sleep or food. I can't feel heat nor cold. Even after bumping into rocks I'll quickly regenerate.")
                siprint("It's just... very lonely here. Wherever here is. I've been eating grass just to pass the time.")
                siprint("There seems to be always some grass to eat, and more to explore!")
                iprint("\n< Hint: Try to 'eat' the grass, see what happens.")
                action_menu(self)

            def eat_grass(self):
                rimuru.add_inventory('hipokte grass')
                action_menu(learn_about_skills())

            class puyo:
                __subs = ['squish', 'bounce']

                def __init__(self):
                    sprint("Puuuuuuuuuuuuyooooooooooo!")

            class _explore:
                __subs = move_subs

                def __init__(self):
                    siprint("Oh... look.....")
                    siprint("More grass... Woooo!")
                    action_menu(learn_about_skills())

    class learn_about_skills:
        def __init__(self):
            if rimuru.check_acquired('hipokte grass'):
                self.where_did_it_go()
            else:
                siprint("All I can do is fumble around in the dark and eat grass... I'M SO BORED!")
            action_menu(self)


        def eat_grass(self):
            if not rimuru.check_acquired('hipokte grass'):
                rimuru.add_inventory('hipokte grass')
                self.where_did_it_go()
            else:
                rimuru.add_inventory('hipokte grass')

        class _hfunc:
            __subs = ['craft full potion', 'craft potion']

            def __init__(self):
                if rimuru.check_acquired('full potion'):
                    siprint("I have a feeling these will come in handy.")

        class _keep_exploring:
            __subs = move_subs + ['fumble around', 'keep fumbling', 'fumble', 'more fumbling', 'fumble more']

            def __init__(self):
                siprint("Lets keep moving!")
                action_menu(in_water())

        class what_are_skills:
            __subs = ['what are skills?', 'skills?', 'tell me more about skills', 'what are these skills?']

            def __init__(self):
                siprint("<< Answer, when growth is recognized by the world, occasionally one will obtain a [Skill]. >>")
                siprint("What an interesting world! It's nice to have someone to talk to, even if it is a one way with a skill.")

        class what_is_predator:
            __subs = ['predator?', 'what is predator?', 'what is this predator?', 'what is this predator skill?', 'predator huh', 'tell me more about predator', 'tell me more about predator']

            def __init__(self):
                siprint("<< Answer, unique skill [Predator] allows one to eat targets, store said targets in skill's stomach, or isolate as hazardous material.")
                siprint("<< Also, after successful analysis on a monster one can use mimicry to replicate appearance, and use replaceable abilities from target. >>")
                iprint("\n< Hint: Try 'info predator' to get more information. >")

        class what_is_great_sage:
            __subs = ['what is this great sage?', 'what is great sage?', 'great sage?', 'tell me more about great sage']
            def __init__(self):
                siprint("<< Answer, my function is to assist my master (you) to the best of my abilities. >>")
                iprint("\n< Hint: Use 'info great sage' to get more information. >")

                if rimuru.check_acquired('hipokte grass'):
                    iprint("\n< Hint: Try getting more 'info' on Hipokte Grass. Than, try making a Full Potion with 'craft' command. >")

        class where_did_it_go:
            __subs = ['where did the grass go?', 'where did that all go?', 'hey where did that go?', "where's the grass?", "where's the grass now?", 'where is the grass?', 'where is the grass now?', 'where did it go?']

            def __init__(self):
                siprint("Where did all that grass go?")
                siprint("<< Answer, they are stored inside the Unique Skill [Predator]'s stomach sack. >>")
                siprint("Whoa! Who's that?")
                siprint("I think I heard this voice before. Who, or what, are you?")
                siprint("<< Answer, this is the Unique Skill [Great Sage], the ability has adapted to best assist you. >>")
                siprint("Skills and predator? huh... Wonder what those are.")
                siprint("\n.... Or should I just forget about that and just move on?")

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
            action_menu(self)

        class stay_in_water:
            __subs = wait_subs + ['stay in water', 'wait in water']

            def __init__(self):
                idots(5)

        class eat_water:
            __subs = ['intake water', 'suck water', 'suck up water', 'suck in water', 'suck up some water', 'intake some water', 'suck water up', 'eat more water', 'predate more water', 'suck up more water']

            def __init__(self):
                rimuru.add_inventory('water')
                rimuru.add_attribute('Hydraulic Propulsion', show_acquired_msg=False)
                siprint("Alright, now lets try this out.")

        class try_getting_out:
            __subs = ['spew water', 'eject water', 'vomit water', 'try getting out', 'try to get out', 'swim', 'swim up', 'swim out', 'try swimming', 'leave water', 'try to swim', 'find a way out', 'get out', 'use water to propel', 'propel with water', 'expel water to propel', 'expel', 'expel water', 'expel the water']

            def __init__(self):
                if rimuru.check_acquired('hydraulic propulsion'):
                    siprint("Let's see if I can get out now.")
                    rimuru.use_skill('hydraulic propulsion')
                    action_menu(find_veldora())
                else:
                    siprint("It's really hard to move in water, I need to find some way out!")

        class _hfunc_use_skill:
            __subs = ['use hydraulic propulsion', 'use new skill', 'use skill']

            def __init__(self):
                if rimuru.check_acquired('hydraulic propulsion'):
                    rimuru.use_skill('hydraulic propulsion')
                    action_menu(find_veldora())

        class hfunc_grab_sword:
            __subs = ['grab sword', 'get sword', 'eat sword', 'predate sword', 'find treasure', 'grab treasure', 'eat treasure', 'predate treasure']
            def __init__(self):
                #rimuru.add_inventory('magisteel sword')
                siprint("HEY! Look! It feels like a sword! Wonder if it's any good?")
                siprint("<< Answer, analysis of sword shows it contains a magisteel core. This sword is above average. >>")
                siprint("Would you look at that, that might come in handy later on. But I'm still stuck down here!")
                in_water.hfunc_grab_sword.__subs = []  # Only able to grab sword once.

    class find_veldora:
        __location = "Sealed Cave"

        def __init__(self):
            siprint("Ouch! I hit something, but at least it seems like I'm back on land.")
            siprint("<< Notice, New skill [Hydraulic Propulsion] acquired. >>")
            siprint("Oh cool, I wonder what else I can do with this skill.")
            sprint("~Can you hear me little one.~")
            siprint("Whaaaa? What was that, I almost pissed myself (if I could). Who's that speaking to me!? It can't be [Great Sage] could it?")
            siprint("This is the first conversation I'm having since reincarnating. According to [Great Sage] I've been in this cave for about 90 days!")
            siprint("Should I be friendly? But how do I even reply?. It's not like I have a mouth to speak with.")
            sprint("~Hey can you just reply?~")
            action_menu(self)

        def eat_grass(self):
            rimuru.add_inventory('hipokte grass')

        class _leave:
            __subs = move_subs

            def __init__(self):
                sprint("~Hey, are you just going to keep ignoring me?~")
                sprint("...")
                sprint("~Wait where are you going?~")
                sprint("You seem pretty suspicious...")
                sprint("~Nooooo.... I'm not suspicious at all.l.l..~")
                leave_cave()

        class hello:
            __subs = ["who's there?", 'who is there?', 'who is that?', 'somebody there?', "who's out there?", "is somebody there?", 'who is that speaking?', 'hello?', 'hello there!', "who's that speaking?", "who's that talking?"]

            def __init__(self):
                sprint("~Keep following my voice little one.~")

        class shut_it:
            __subs = ["shut it you baldy!", "screw you baldy!", 'shut up baldy!', 'shut up!', 'shut it!']

            def __init__(self):
                sprint("~BALDY, HAHAHA, SEEMS LIKE YOU HAVE A DEATH WISH!!!~")
                siprint("I'M SORRY!")
                siprint("I'm sorry! I didn't think you could hear me!")
                sprint("~Come closer little one.~")
                siprint('uh.... Should I follow?')

        class _follow_voice:
            __subs = ['follow the voice', 'locate the voice', 'try locating the voice', 'try locating voice', 'try finding the voce', 'try following the voice', 'seek out voice', 'seek voice', 'follow strange voice', 'seek strange voice', 'follow']

            def __init__(self):
                siprint("Hold on..... I'm trying to find my way!")
                siprint("I hit something, but it's not a rock. And what is this aura that I'm feeling? Could it be?")
                action_menu(found_veldora())

    class found_veldora:
        __location = "Veldora's Prison"

        def __init__(self):
            sprint("I never expected to speak with anyone other than my skill, since I can't see or hear.")
            sprint("It's a kind of telepathy. hmmmm..... ~Alright... fine, I'll help you see. Just don't be scared when you see my true form.")
            sprint("~There is something called [Magic Perception], it allows you to perceive the surrounding magic essence.~")
            sprint("What's this magic essence?...")
            siprint("<< Answer, this world is covered with magic essence for example, the body of a slime can move because it absorbs magic essence from it's surroundings. >>")
            sprint("~If you are able to perceive the flow of magic essence outside of your body, then you'll get the skill.~")
            sprint("~With that you will be able to 'see', 'hear' and much more!~")
            sprint("Eh... this feels really complicated. It won't hurt to try though... Will it?.")

            siprint("<< Suggestion, in order to organize large amount of information, would you like to activate linking with [Great Sage] and [Magic Perception]. >>")
            action_menu(self)

        class _use_magic_perception:
            __subs = ['try magic perception', 'try using magic perception', 'activate magic perception']

            def __init__(self):
                idots(3)
                show_art('magic perception')
                sprint("Like this?")
                rimuru.add_attribute('Magic Perception')
                sprint("I can see. I CAN SEE!")
                sprint("~Seems like you did it. You learn quickly little one.~")
                sprint("Yes, thank you!")
                sprint("~Allow me to formally introduce myself?~")
                action_menu(self)

            def _sure(self):
                sprint("My name is Storm Dragon Veldora!~")
                show_art('cave veldora')
                sprint("~I am one of the four True Dragons of this world.~")
                sprint("HOLY SHIT, you're a real dragon!")
                sprint("~Didn't I tell you not to get scared.~")

                action_menu(become_friends())

            def _nah(self):
                siprint("~Alright then, I won't. Hmmmmph~")
                action_menu(become_friends())

        def eat_grass(self):
            rimuru.add_inventory('hipokte grass')

    class become_friends:
        def __init__(self):
            siprint("Hmmmm, now what?")
            action_menu(self)

        def eat_grass(self):
            rimuru.add_inventory('hipokte grass')

        class _leave:
            __subs = move_subs
            def __init__(self):
                sprint("I guess I'll be heading out now.")
                sprint("~Really, so soon. But we just started!~")
                sprint("~Stay, please, we have so much to talk abo.o.o...~")
                siprint("Phew, I think I lost him.")
                action_menu(leave_cave())

        class _friend_dragon:
            __subs = ['befriend dragon', 'ask to become friends', 'want to be friends?', 'wanna be friends?']

            def __init__(self):
                sprint("Okay... sooo, you want to be friends?")
                sprint("~HAHAHA, WHAT?! A mere slime wants to be friends with the great Storm Dragon Veldora!?~")
                sprint("Wellll... If you don't want to, that's fine too.")
                sprint("~WHAAAAAAT, Who said we could not!~")
                sprint("I guess I won't have a reason to come back here again, huh.")
                sprint("~Wait...")
                sprint("I guess it can't be helped.")
                sprint("I'll become your friend!~")
                sprint("Great. Now I guess I should help you with this seal heh?")
                action_menu(self)

            class help_with_seal:
                def __init__(self):
                    rimuru.add_attribute('mimic')
                    global veldora
                    veldora = mobs.Veldora_Tempest()
                    siprint("[Great Sage]?")
                    siprint("<< Answer, analysis shows it's impossible to destroy [Infinity Prison] using any physical attacks. >>")
                    siprint("<< Notice, possible solution may be...")
                    sprint("~Hey don't just only talk to your own skill.~")
                    sprint("Jealous?")
                    sprint("It might be possible if we both analyze [Infinity Prison] inside and out")
                    sprint("~My skills were sealed away as well, I can't use analyze.~")
                    sprint("If you give me the information [Great Sage] can analyze your side as well")
                    sprint("~Won't that take a long time, didn't you want to go find other reincarnates from your world~")
                    sprint("I have a suggestion.")
                    siprint("How about you get in my belly!")
                    sprint("~hahaha~")
                    sprint("~ku hahaha~")
                    sprint("~HAHAHAHAHAHAHA~")
                    siprint("Ummmm, did he just use the 3 stage laugh...?")
                    sprint("~My life is in your hands.~")
                    sprint("Wow how trusting of you.")
                    sprint("~Well... The alternative is to stay in this cave for the rest of my lonely time.~")
                    sprint("~Before that, let me give you a name and you think of a name for both of us.~")
                    sprint("Like a family name? hmmmmm...")
                    family_name = str(input("\nFamily Name > "))
                    veldora.family_name = family_name

                    rimuru.family_name = family_name
                    rimuru.divineProtection = 'Storm Crest'
                    siprint("< Acquired: Storm Crest Divine Protection >\n")
                    rimuru.update_ranking(8)

                    sprint(f"Hmmmmmm... How about {family_name}~")
                    sprint("~That name is AWESOME!~")
                    siprint("He actually likes it?")
                    sprint(f"~From now on I will be Veldora {family_name}~")
                    sprint("~And as for you...~")
                    rimuru.name = str(input("\nName > "))
                    sprint(f"~How about {rimuru.name}!~")

                    sprint("~Leave it to me. Until we meet again little one!~")
                    siprint("<< Use Unique skill [Predator]? >>")
                    action_menu(self)

                def eat_grass(self):
                    sprint("~Hey what are you doing there? Focus on me... ME!~")
                    rimuru.add_inventory('hipokte grass')

                class _eat_veldora:
                    __subs = ['predate veldora', 'eat dragon', 'eat the dragon', 'predate dragon']
                    __location = "Sealed Cave"

                    def __init__(self):
                        sprint("~The slime little grew big enough to completely engulf the dragon and his seal in mere seconds before turning back to normal~\n")
                        veldora.update_info()
                        rimuru.add_inventory(veldora)
                        rimuru.add_mimic(veldora)
                        siprint("\n<< Notice, start analyzing Unique Skill [Infinity Prison]? >>")
                        action_menu(self)

                    class _start_analysis:
                        __subs = ['yes', 'start it', 'yes please']
                        def __init__(self):
                            siprint("Yes, Please take care of it [Great Sage].")
                            rimuru.update_status('veldora', 'Analyzing')
                            siprint("< Analysis Started >")
                            siprint("I hope you get out quickly!")
                            leave_cave()

                    class ignore:
                        __subs = ['no', "don't start", 'ignore him', 'leave it', 'leave him', 'trap him', "Don't help him", 'do not help him']
                        def __init__(self):
                            siprint("You know what, no. I think I'll just leave that for now. Hehehe...")

                    class _move_on:
                        __subs = move_subs + ['ignore him, lets move on']
                        def __init__(self):
                            siprint("ehehhh... Veldora is gonna be pissed that I didn't immediately start, will he think I betrayed him...")
                            leave_cave()

    def leave_cave():
        siprint("Time to leave this cave already.")
        continue_to(Chapter2)

    chapter_1()
