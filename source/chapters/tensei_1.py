# Import all game_functions' funcs for easy access.
from game_files.game_functions import *
# Import the next chapter to continue to.
from chapters.tensei_2 import Chapter2


def Chapter1(rimuru):
    class chapter_1:
        __location = 'Sealed Cave'
        def __init__(self):
            ssprint(".....\n")
            show_art('great sage')
            rimuru.set_start_state()
            ssprint("<< Confirmation Complete. Constructing body that does not require blood... >>\n")
            ssprint("<< Confirmation Complete. Acquiring: Skill [Predator]... >>")
            rimuru.add_attribute('Predator')
            ssprint("<< Confirmation Complete. Acquiring: Extra Skill [Sage]... >>")
            rimuru.add_attribute('Sage')
            rimuru.upgrade_attribute('Sage', 'Great Sage')

            print()
            ssprint("It's so dark...")
            ssprint("where is this...")
            ssprint("What happened to me...?")
            ssprint("I remembered that I got stabbed while protecting _____....")
            ssprint("Was I saved?")
            # Show user HUD and playable actions.
            action_menu(self)

        # Actions starting with '_' will progress the storyline.
        # The ones without it can still have one ore more sub actions, they will just loop back around.
        class _move:
            def __init__(self):
                ssprint("Where are my arms, I can't feel them!")
                ssprint("Hey! HEY!, Give me a break already...")
                ssprint("AH!? I moved!? Below my abdomen(?), is that grass?")
                ssprint("I can't see anything, hear or smell anything as matter of fact.")
                ssprint("This sense of...  absorbing?")
                ssprint("Am I eating it? Actually! Where the fuck is my mouth?")
                ssprint("The grass melted, did it just dissolve?")
                ssprint("WAIT A MINUTE")
                ssprint("Am I even human anymore!?!?!")
                action_menu(self)

            class _inspect:
                def __init__(self):
                    ssprint("Wait what kind of joke is this! Who would want this?")
                    ssprint("But... Dissolving and absorbing plants, this streamlined elastic feeling body shape.")
                    ssprint("*Although _______ didn't want to admit it.*")
                    ssprint("*You have died as a Human and reincarnated into a slime!*")
                    show_art('slime')
                    ssprint("Puyo, Puyoyoyo....")
                    ssprint("It's been a long time since I've accepted myself a slime.")
                    ssprint("I've gotten used to this elastic body.")
                    ssprint("I can't feel heat nor cold.")
                    ssprint("Even after bumping into rocks I'll quickly regenerate.")
                    ssprint("And there was no need for sleep or eating.")
                    ssprint("This body isn't so bad I guess.")
                    ssprint("It's just... very lonely here. Wherever here is.")
                    ssprint("I've been eating grass just to pass the time.")
                    action_menu(self)

                def explore(self):
                    ssprint("Oh... look.....")
                    ssprint("more grass... woooo!")

                def puyo(self):
                    sprint("Puuuuuuuuuuuuyooooooooooo!")

                def _predate_grass(self):
                    ssprint("More grass!")
                    rimuru.add_inventory('Hipokte Grass')
                    action_menu(_learn_skills())

    class _learn_skills():
        def __init__(self):
            ssprint("I've eaten, or I guess absorbed what I thought was a lot of grass.")
            ssprint("So where has it all gone? I haven't had the need to poop yet.")
            ssprint("<< Answer, they are stored inside the Unique Skill [Predator]'s stomach sack. >>")
            ssprint("Whoa, somebody actually answered!?!")
            ssprint("<< Notice, the current spaced used is less than 1%. >>")
            ssprint("< Use 'inv' command to get inventory information, use 'help' for more.  >")
            ssprint("I've heard this voice before, it sounds like a computer....")
            ssprint("Who.... or what is that?")
            ssprint("<< Answer, this is the Unique Skill [Great Sage], the ability has adapted to best assist you. >>")
            ssprint("[Great Sage]? [Predator]? heh?!")
            ssprint("Is that what I was hearing when I was dying")
            ssprint("With that said, what are skills?")
            action_menu(self)

        def predate_grass(self): rimuru.add_inventory('hipokte grass')

        class what_is_predator:
            def __init__(self):
                ssprint("What is this predator?")
                ssprint("<< Answer, unique skill [Predator] allows one to predate targets. store said targets in skill's stomach, or isolate as hazardous material.")
                ssprint("<< Also, after successful analysis a monster, one can use mimicry to replicate appearance and use analyzed target's abilities. >>")
                action_menu(self)

            class _analyze_grass:
                def __init__(self):
                    ssprint("As a test, can you analyze that grass I just ate?")
                    ssprint("<< Analysis complete. >>")
                    rimuru.show_info('hipokte grass')
                    action_menu(self)

                def _craft_full_potion(self):
                    ssprint("I have a feeling these will come in handy.")
                    ssprint("< Item's recipe can be found using 'info' command. Also note that some items are crafted in batches. >")
                    action_menu(_learn_skills)

        class _what_are_skills:
            __location = "Under water?"
            def __init__(self):
                ssprint("<< Answer, when growth is recognized by the world, occasionally one will obtain a [Skill]. >>")
                ssprint("What an interesting world!")
                ssprint("Even as skill, I now have someone to talk to.")
                ssprint("Even though it's basically a one way.")
                ssprint("*Getting carried away and not being aware of it's surroundings. The little slime fell into what seems to be water.*")
                ssprint("I'm going to die!")
                ssprint("SHIT! I've finally reincarnated and I'm already going to die!")
                ssprint("O'Great sage how painful is it to suffocate to death!?")
                ssprint("<< Answer, none. A slime's body does not require oxygen to live. >>")
                ssprint("Hmmmmm. I'm not feeling any pain.")
                ssprint("I just thought of something!")
                ssprint("I could swallow up tons of water then I can and expel it at a high pressure...")
                rimuru.add_attribute('Hydraulic Propulsion')
                action_menu(self)

            def stay_in_water(self):
                sprint(".....")

            class _predate_water:
                def __init__(self):
                    ssprint("Alright, now lets try this out.")
                    action_menu(self)

                def stay_in_water(self):
                    sprint("..........")

                def _use_hydraulic_propulsion(self):
                    ssprint("Finally, I'm back on land!")
                    sprint("~Can you hear me little one.~")
                    ssprint("Whaaaa? What was that, I almost pissed myself (if I could).")
                    ssprint("Who's that speaking to me!?")
                    ssprint("It's not [Great Sage], so who is it?")
                    ssprint("This is bad, I'm getting nervous. This is the first conversation I'm having since reincarnating.")
                    ssprint("I've been only talking to [Great Sage] so far, according to it... her?...")
                    ssprint("I've been in this cave for about 90 days!")
                    action_menu(_find_veldora())

    class _find_veldora:
        __location = "Sealed Cave"
        def __init__(self):
            ssprint("Let's try to find where that voice is coming from")
            ssprint("I'll have to be friendly. But how do I even reply?. It's not like I have a mouth to speak with.")
            sprint("~Hey can you just reply?~")
            ssprint("Was I sensed somehow?")
            action_menu(self)

        class _leave:
            def __init__(self):
                sprint("~Hey, are you just going to keep ignoring me?~")
                sprint("...")
                sprint("~Wait where are you going?~")
                sprint("You seem pretty suspicious...")
                sprint("~Oh, really... Is there anything I can do to ease your mind?~")
                action_menu(self)

            def _help_me_see(self):
                action_menu(_respond())

            def _leave(self):
                sprint("No, I'm just going to move on.")
                sprint("~Oh. Ok, at least it was interesting seeing a higher intelligent monster in my cave for once.~")
                _leave_cave()

        def _hello(self):
            sprint("~Keep following my voice little one.~")
            action_menu(_respond())

        def _shutit_baldy(self):
            ssprint("~BALDY, HAHAHA, SEEMS THAT YOU WANT TO DIE!!!~")
            ssprint("Oh!")
            action_menu(_respond())

        def predate_grass(self): rimuru.add_inventory('hipokte grass')


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

        def predate_grass(self): rimuru.add_inventory('hipokte grass')

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
            ssprint("< Acquired: Storm Crest Divine Protection. >\n")
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

        class _predate_veldora:
            __location = "Sealed Cave"
            def __init__(self):
                ssprint("~The slime little grew big enough to completely engulf the dragon and his seal in mere seconds before turning back to normal~\n")
                rimuru.add_inventory(veldora)

                ssprint("<< Notice, start analyzing Unique Skill [Infinity Prison]? >>")
                action_menu(self)

            def _start_analysis(self):
                ssprint("Yes, Please take care of it [Great Sage].")
                ssprint("I hope you get out quickly!")
                _leave_cave()

            def _move_on(self):
                ssprint("ehehhh... Veldora is gonna be pissed that I didn't immediately start, he'll think I betrayed him...")
                _leave_cave()

    def _leave_cave():
        ssprint("Time to leave this cave already.")
        continue_story(Chapter2)

    chapter_1()
