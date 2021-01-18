# Import all game_functions' funcs for easy access.
from game_files.game_functions import *
# Import the next chapter to continue to.
from chapters.tensei_2 import Chapter2


def Chapter1(rimuru):
    class chapter_1:
        __location = 'Sealed Cave'

        def __init__(self):
            rimuru.set_start_state()
            sdots()
            print()
            ssprint("<< Confirmation Complete. Constructing body that does not require blood... >>\n")
            ssprint("<< Confirmation Complete. Acquiring skill: [Predator]... >>")
            rimuru.add_attribute('Predator')
            ssprint("<< Confirmation Complete. Acquiring: Extra Skill [Sage]... >>")
            rimuru.add_attribute('Sage')
            rimuru.upgrade_attribute('Sage', 'Great Sage')

            print()
            ssprint("It's so dark? Where is this? What happened?")
            ssprint("I remembered now. I got stabbed!")
            ssprint("Was I saved? Can I move?")
            # Show user HUD and playable actions.
            action_menu(self)

        # Actions starting with '_' will progress the storyline.
        # The ones without it can still have one ore more sub actions, they will just loop back around.
        class _move:
            __subs = ['feel', 'touch']

            def __init__(self):
                ssprint("Where are my arms, I can't feel them!")
                ssprint("Did I just move? I can't see anything, can't hear, can't even smell anything...")
                ssprint("What is this thing? It feels like I'm 'absorbing' something.")
                ssprint("This body? Am I even human anymore!?!?!")
                action_menu(self)

            class _inspect_body:
                __subs = ['inspect', 'move', 'check body', 'inspect my body', 'feel body', 'feel', 'feel around', 'move around']

                def __init__(self):
                    ssprint("Dissolving and absorbing, this streamlined elastic feeling body.")
                    show_art('slime')
                    print(game_art.rimuru_art.died)
                    ssprint("It looks like I have been stabbed, died and reincarnated as a slime!\n")
                    sdots(3, 8)
                    ssprint("\nIt's been a long time since I have accepted myself a slime. I am getting use to this body.")
                    ssprint("I don't need sleep or food. I can't feel heat nor cold. Even after bumping into rocks I'll quickly regenerate.")
                    ssprint("It's just... very lonely here. Wherever here is. I've been eating grass just to pass the time.")
                    ssprint("There seems to be always some grass to eat, and more to explore!\n")
                    print("< Hint: Try to 'eat' the grass, see what happens.")
                    action_menu(self)

                def eat_grass(self):
                    rimuru.add_inventory('Hipokte Grass')
                    ssprint("Where did all that grass go?")
                    ssprint("<< Answer, they are stored inside the Unique Skill [Predator]'s stomach sack. >>")
                    ssprint("Whoa! Who's that?")
                    ssprint("I think I heard this voice before. Who, or what, are you?")
                    ssprint("<< Answer, this is the Unique Skill [Great Sage], the ability has adapted to best assist you. >>")
                    ssprint("Skills, [Great Sage], [Predator], huh... Wonder what those are.")
                    ssprint("\n.... Or should I just forget about that and just move on?")
                    action_menu(learn_about_skills())

                class puyo:
                    __subs = ['squish', 'bounce']
                    def __init__(self):
                        sprint("Puuuuuuuuuuuuyooooooooooo!")

                class _explore:
                    __subs = move_subs
                    def __init__(self):
                        ssprint("Oh... look.....")
                        ssprint("More grass... Woooo!")
                        action_menu(learn_about_skills())

    class learn_about_skills:
        def __init__(self):
            ssprint("All I can do is fumble around in the dark and eat grass... I'M SO BORED!")
            action_menu(self)

        def eat_grass(self):
            rimuru.add_inventory('hipokte grass')

        def craft_full_potion(self):
            if rimuru.check_acquired('full potion'):
                ssprint("I have a feeling these will come in handy.")

        class _keep_exploring:
            __subs = move_subs
            def __init__(self):
                ssprint("Lets keep moving!")
                action_menu(in_water())

        class what_are_skills:
            __subs = ['what are skills?', 'skills?', 'tell me more about skills', 'what are these skills?']
            def __init__(self):
                ssprint("<< Answer, when growth is recognized by the world, occasionally one will obtain a [Skill]. >>")
                ssprint("What an interesting world! It's nice to have someone to talk to, even if it is a one way with a skill.")

        class what_is_predator:
            __subs = ['predator?', 'what is predator?', 'what is this predator?', 'what is this predator skill?', 'predator huh', 'tell me more about predator', 'tell me more about predator']
            def __init__(self):
                ssprint("<< Answer, unique skill [Predator] allows one to eat targets. store said targets in skill's stomach, or isolate as hazardous material.")
                ssprint("<< Also, after successful analysis a monster, one can use mimicry to replicate appearance and use analyzed target's abilities. >>")
                print("\n< Hint: Try getting more 'info' on [Hipokte Grass]. >")
                print("< Hint: Try to 'crafting' a Full Potion. >")

    class in_water:
        __location = "Under water?"

        def __init__(self):
            print(game_art.rimuru_art.fall_in_water)
            ssprint("I'M GOING TO DIE... AGAIN!")
            ssprint("SHIT! I've finally reincarnated and I'm already going to die!")
            ssprint("O'Great sage how painful thy death will be? Am I really going to suffocate to death?!?!")
            ssprint("<< Information, A slime's body does not require oxygen to survive. >>")
            ssprint("Huh.... I'm not feeling any pain. But what am I going to do now?\n")
            sdots()
            ssprint("I thought of something... I could suck up some of water then I can and expel it at a high pressure...")
            action_menu(self)

        class stay_in_water:
            __subs = wait_subs + ['stay in water', 'wait in water']
            def __init__(self):
                sdots(5)

        class eat_water:
            __subs = ['intake water', 'suck water', 'suck up water', 'suck in water', 'suck up some water', 'intake some water', 'use water to propel', 'propel with water', 'expel water to propel']
            def __init__(self):
                rimuru.add_inventory('water')
                rimuru.add_attribute('Hydraulic Propulsion')
                ssprint("Alright, now lets try this out.")

        class try_getting_out:
            __subs = ['spew water', 'eject water', 'vomit water', 'get_out', 'swim', 'swim up', 'swim out', 'try swimming', 'leave water', 'try to swim', 'find a way out', 'get out']
            def __init__(self):
                ssprint("It's really hard to move in water, I need to find some way out!")

        class _use_hydraulic_propulsion:
            __subs = ['use new skill', 'use skill']
            def __init__(self):
                if rimuru.check_acquired('hydraulic propulsion'):
                    ssprint("Finally, I'm back on land!")
                    sprint("~Can you hear me little one.~")
                    ssprint("Whaaaa? What was that, I almost pissed myself (if I could).")
                    ssprint("Who's that speaking to me!? It can't be [Great Sage] could it?")
                    ssprint("This is bad, I'm getting nervous. This is the first conversation I'm having since reincarnating.")
                    ssprint("According to [Great Sage] I've been in this cave for about 90 days!")
                    action_menu(_find_veldora())


    class _find_veldora:
        __location = "Sealed Cave"

        def __init__(self):
            ssprint("I'll have to be friendly. But how do I even reply?. It's not like I have a mouth to speak with.")
            sprint("~Hey can you just reply?~")
            ssprint("Was I seen?")
            action_menu(self)

        class _leave:
            __subs = ['wonder', 'explore', 'move on']
            def __init__(self):
                sprint("~Hey, are you just going to keep ignoring me?~")
                sprint("...")
                sprint("~Wait where are you going?~")
                sprint("You seem pretty suspicious...")
                sprint("~Nooooo.... I'm not suspicious at all.l.l..~")
                _leave_cave()

        class _hello:
            __subs = ["who's there?", 'who is therer?', 'who is that?']
            def __init__(self):
                sprint("~Keep following my voice little one.~")
                action_menu(_respond())

        def _shutit_baldy(self):
            ssprint("~BALDY, HAHAHA, SEEMS THAT YOU WANT TO DIE!!!~")
            ssprint("Oh!")
            action_menu(_respond())

        def eat_grass(self):
            rimuru.add_inventory('hipokte grass')

    class _respond:
        __location = "Veldora's Prison"

        def __init__(self):
            sprint("I never expected to speak with anyone other than my skill")
            sprint("I can't 'see' or 'hear' anything.")
            sprint("~This is telepathy. It's Hard to converse if you can't see.")
            sprint("Alright... fine, I'll help you see.~")
            sprint("~Just don't be scared when you see my true form.")
            sprint("There is something called [Magic Perception], it allows you to perceive the surrounding magic essence.~")
            sprint("What's this magic essence?...")
            ssprint("<< Answer, this world is covered with magic essence for example, the body of a slime can move because it absorbs magic essence from it's surroundings. >>")
            sprint("~If you are able to perceive the flow of magic essence outside of your body, then you'll get the skill.~")
            sprint("~With that you will be able to 'see', 'hear' and much more!~")
            sprint("Eh... this feels really complicated.")
            sprint("It won't hurt to try though... Will it?).")
            sprint("I sense something floating, is this the so called magic essence?")

            sprint("Ehh, just like that heh?")
            ssprint("<< Suggestion, in order to organize large amount of information,  activate linking with [Great Sage] and [Magic Perception]. >>")
            rimuru.add_attribute('Magic Perception')
            action_menu(self)

        class _use_magic_perception:
            def __init__(self):
                sprint('...')
                show_art('magic perception')
                sprint("OH!")
                sprint("Hmmmmmmmm")
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
                ssprint("~even with the scary appearance, the little slime and dragon started chatting.~")

                action_menu(_become_friends())

            def _nah(self):
                ssprint("~Alright then, I won't. Hmmmmph~")
                action_menu(_become_friends())

        def eat_grass(self):
            rimuru.add_inventory('hipokte grass')

    class _become_friends:
        def __init__(self):
            ssprint("Hmmmm, now what?")
            action_menu(self)

        def _leave(self):
            sprint("I guess I'll be heading out now.")
            ssprint("~Really, so soon. But we just started!~")
            ssprint("~Stay, please, we have so to talk about.~")
            action_menu(_leave_cave())

        def _friend_dragon(self):
            sprint("Okay... sooo, you want to be friends?")
            sprint("~HAHAHA, WHAT?! A mere slime wants to be friends with the great Storm Dragon Veldora!?~")
            sprint("Wellll... If you don't want to, that's fine too.")
            sprint("~WHAAAAAAT, Who said we could not!~")
            sprint("I guess I won't have a reason to come back here again, huh.")
            sprint("~Wait...")
            sprint("I guess it can't be helped.")
            sprint("I'll become your friend!~")
            sprint("Great. Now I guess I should help you with this seal heh?")
            action_menu(_help_with_seal())

    class _help_with_seal:
        def __init__(self):
            rimuru.add_attribute('mimic')
            global veldora
            veldora = mobs.Veldora_Tempest()
            ssprint("[Great Sage]?")
            ssprint("<< Answer, analysis shows it's impossible to destroy [Infinity Prison] using any physical attacks. >>")
            ssprint("<< Notice, possible solution may be...")
            sprint("~Hey don't just only talk to your own skill.~")
            sprint("Jealous?")
            sprint("It might be possible if we both analyze [Infinity Prison] inside and out")
            sprint("~My skills were sealed away as well, I can't use analyze.~")
            sprint("If you give me the information [Great Sage] can analyze your side as well")
            sprint("~Won't that take a long time, didn't you want to go find other reincarnates from your world~")
            sprint("I have a suggestion!")
            sprint("How. Would. You. Like. To...")
            ssprint("Get in my belly!")
            sprint("~hahaha~")
            sprint("~ku hahaha~")
            sprint("~HAHAHAHAHAHAHA~")
            ssprint("Ummmm, did he just use the 3 stage laugh...?")
            sprint("~My life is in your hands.~")
            sprint("Wow how trusting of you.")
            sprint("~Well... The alternative is to stay in this cave for the rest of my lonely time.~")
            sprint("I'll use predator to swallow you now.")
            sprint("~Before that, let me give you a name and you think of a name for both of us.~")
            sprint("Like a family name? hmmmmm...")
            family_name = str(input("\nFamily Name > "))
            veldora.family_name = family_name

            rimuru.family_name = family_name
            rimuru.divineProtection = 'Storm Crest'
            ssprint("< Acquired: Storm Crest Divine Protection >\n")
            rimuru.update_ranking(8)

            sprint(f"Hmmmmmm... How about {family_name}~")
            sprint("~What a good name!~")
            sprint("He actually likes it?")
            sprint(f"~From now on I'll be Veldora {family_name}~")
            sprint("~And as for you...~")
            rimuru.name = str(input("\nName > "))
            sprint(f"~How about {rimuru.name} {family_name}")

            sprint("~Leave it to me. Until we meet again little one!~")
            ssprint("<< Use Unique skill [Predator]? >>")
            action_menu(self)

        class _eat_veldora:
            __location = "Sealed Cave"

            def __init__(self):
                ssprint("~The slime little grew big enough to completely engulf the dragon and his seal in mere seconds before turning back to normal~\n")
                veldora.update_info()
                rimuru.add_inventory(veldora)
                rimuru.add_mimic(veldora)

                ssprint("\n<< Notice, start analyzing Unique Skill [Infinity Prison]? >>")
                action_menu(self)

            def _start_analysis(self):
                ssprint("Yes, Please take care of it [Great Sage].")
                rimuru.update_status('veldora', 'Analyzing')
                ssprint("< Analysis Started >")
                ssprint("I hope you get out quickly!")
                _leave_cave()

            def _move_on(self):
                ssprint("ehehhh... Veldora is gonna be pissed that I didn't immediately start, he'll think I betrayed him...")
                _leave_cave()

    def _leave_cave():
        ssprint("Time to leave this cave already.")
        next_location(Chapter2)

    chapter_1()
