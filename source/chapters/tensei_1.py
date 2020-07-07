from start_game import *
from chapters.tensei_2 import Chapter2
import slime_art


# Manga, Chapter 1
def Chapter1(rimuru):
    class Chapter_1:
        def __init__(self):
            sprint(".....")
            sprint(slime_art.great_sage)
            rimuru.set_start_state()
            ssprint("<<Confirmation Complete. Constructing a body that does not require blood...>>")
            ssprint("<<Confirmation Complete. Acquiring Skill [Predator]...>>")
            rimuru.add_attribute('Predator')
            ssprint("<<Confirmation Complete. Acquiring Extra Skill [Sage]...>>")
            rimuru.add_attribute('Sage')
            ssprint("<<Confirmation Complete. Extra skill [Sage] evolving.>>")
            sprint('.....')
            rimuru.upgrade_attribute('Sage', 'Great Sage')

            rimuru.show_attributes()
            rimuru.show_inventory()

            ssprint(".....")
            ssprint("It's so dark, where is this. What happened to me?")
            ssprint("I remembered that I got stabbed while protecting Tamura. Was I... saved?")
            ssprint("That said is this the hospital bed? I can't see anything, I can't hear anything.")
            action_menu(self)

        class _move:
            def __init__(self):
                ssprint("Where are my arms, I can't feel them!")
                ssprint("hm? eh? My limbs don't seem to be responding!?")
                ssprint("That's not possible I was only stabbed, my arms and legs should be all fine... Right?...")
                ssprint("Hey hey hey, Give me a break already... AH!? I moved!? Below my abdomen(?), is that grass?")
                ssprint("There is also no sense of sight, hearing, and smell. There is only 'touch'... What about taste?")
                ssprint("Alright, Let's try to taste it. Actually! Where the fuck is my mouth?")
                ssprint("The grass melted. Is it being absorbed?")
                ssprint("WAIT A MINUTE, am I even human anymore!!?! Eh.. Let's calm down and confirm my appearance.")
                action_menu(self)

            class _inspect():
                def __init__(self):
                    ssprint("Wait what kind of joke is this! Who would accept something like this!!")
                    ssprint("ahhhh... but... Dissolving and absorbing plants, this streamlined elastic feeling body shape.")
                    ssprint("*Although Minami Satoru didn't want to admins it.*")
                    ssprint("*He has reincarnated into a slime!*")
                    sprint(slime_art.slime)
                    ssprint("Puyo, Puyoyoyo.... stretch....bounce")
                    ssprint("It's been a long time since I've accepted myself a slime. I've gotten used to this elastic body.")
                    ssprint("I can't feel heat nor cold. Even after bumping into rocks I'll quickly regenerate.")
                    ssprint("And there was no need for sleep or eat either. This body isn't so bad. It's just very lonely.")
                    ssprint("This is the only problem I can't solve, so i started eating grass in order to pass time.")
                    action_menu(self)

                def explore(self):
                    ssprint("Oh, look, more grass. Wow!")

                def puyo(self):
                    sprint("Puyo!")

                def _predate_grass(self):
                    ssprint("Ooooweeee more grass!")
                    rimuru.add_inventory('Hipokte Grass')
                    action_menu(Learn_Skills())

    class Learn_Skills:
        def __init__(self):
            ssprint("I've ate what seems like a lot of grass, and yet I haven't pooped yet. So where did all the grass go?")
            ssprint("<<Answer. They are stored inside the Unique Skill [Predator]'s stomach sack.>>")
            ssprint("Whoa, somebody actually answered!?!")
            ssprint("<<Notice, the current spaced used is less than 1%.>>")
            sprint("I've heard this before, this voice that sounded computer synthesized.... Who is that?")
            ssprint("<<Answer. This is the Unique Skill [Great Sage], the ability has adapted, so it can quickly answer you.>>")
            ssprint("[Great Sage]? [Predator]? heh?!")
            ssprint("Speakin of which, when I died I seemed to have acquired some of skills. That said, what are skills?")
            action_menu(self)

        class what_is_predator:
            def __init__(self):
                ssprint("What is this predator?")
                ssprint("<<Answer, Unique skill [Predator] allows one to predate targets. [Predator] can store predated targets in this unique skill's stomach or able to isolate dangerous material.")
                ssprint("<<After successful analysis a monster, one can use mimicry to replicate and use analyzed target's abilities.>>")
                action_menu(self)

            def analyze_grass(self):
                ssprint("As a test, can you analyze that grass I just ate?")
                ssprint("<<Analysis complete.>>")
                rimuru.show_info('hipokte grass')

            def _create_potions(self):
                ssprint("")
                action_menu(Learn_Skills)

        def predate_grass(self):
            rimuru.add_inventory('Hipokte Grass')

        class _what_are_skills:
            def __init__(self):
                ssprint("<<Answer. When growth is recognized by the world, occasionally one will obtain a [Skill].>>")
                ssprint("Although I don't understand it too much. It seems like it's just how this world works.")
                ssprint("Even if it's a skill, I now have someone to talk to.")
                ssprint("~Getting carried away and not having all of his normal senses. The little slime fell into what seemed to be water~")
                ssprint("I'm going to die! SHIT! I've finally reincarnated and I'm already going to die!")
                ssprint("Great sage how painful is it to suffocate to death!?")
                ssprint("<<Answer. A slime's body does not need oxygen.>>")
                ssprint("I am indeed not feeling any pain, at this time my brain cells (or slime body) thought up a strategy.")
                ssprint("How can I get out of here?")
                ssprint("<<Suggestion, use predator to intake water then expel at high velocity.>>")
                action_menu(self)

            def stay_in_water(self):
                sprint(".....")

            class _predate_water:
                def __init__(self):
                    ssprint("Alright, now lets try this out.")
                    action_menu(self)

                def stay_in_water(self):
                    sprint("..........")

                def _expel_water(self):
                    rimuru.add_attribute('Hydraulic Propulsion')
                    ssprint("Finally, I'm back on land!")
                    sprint("~Can you hear me little one.~")
                    ssprint("Whaaaa? What was that, I almost pissed myself (if I could). Who's that speaking to me!?")
                    ssprint("It's not [Great Sage], so who is it? This is bad, I'm getting nervous. This is the first conversation I'm having since reincarnating.")
                    action_menu(Find_Veldora())

    class Find_Veldora:
        def __init__(self):
            ssprint("Let's try to find where that voice is coming from")
            ssprint("I'll have to be friendly. But how do I even reply?. It's not like I have a mouth to speak with.")
            ssprint("Was I sensed somehow?")
            sprint("~Hey can you just reply?~")
            action_menu(self)

        def _leave(self):
            sprint("~Hey, are you just going to keep ignoring me?~")
            action_menu(Leave_Veldora())

        def _hello(self):
            sprint("~Keep following my voice little one.~")
            action_menu(Respond())

        def _shutit_baldy(self):
            ssprint("~BALDY, HAHAHA, SEEMS THAT YOU WANT TO DIE!!!~")
            ssprint("Oh!")
            action_menu(Respond())

    class Leave_Veldora:
        def __init__(self):
            sprint("...")
            sprint("~Wait where are you going?~")
            sprint("You seem pretty suspicious...")
            sprint("~Oh, really... Is there anything I can do to ease your mind?~")
            action_menu(self)

        def _help_me_see(self):
            action_menu(Respond())

        def _leave(self):
            sprint("No, I'm just going to move on.")
            sprint("~Oh. Ok, at least it was interesting seeing a higher intelligent monster in my cave for once.~")
            Leave_Cave()

    class Respond:
        def __init__(self):
            sprint("I never expected to be able to speak with anything other than my skill by thought...")
            sprint("Right now I am in a state that's unable to see anything....Ummmm you are?.")
            sprint("~This is telepathy. It's Hard to converse if you can't see... Alright, I'll help you see.~")
            sprint("~Just don't be scared when you see my true form. There is something called [Magic Perception], it allows you to perceive the surrounding magic essence.~")
            sprint("Magic essence?...")
            ssprint("<<Answer. This world is covered with magic essence for example, the body of a slime can move because it absorbs magic essence.>>")
            sprint("~If you are able to perceive the flow of magic essence outside of your body, then you'll get the skill.~")
            sprint("~With that you will be able to 'see' and 'hear'.~")
            sprint("Eh... this feels really complicated. Wellllll, it won't hurt to try... Will it?).")
            sprint("I sense something floating, is this the so called magic essence?")

            sprint("Ehh, just like that heh?")
            ssprint("<<Suggestion, in order to organize large amount of information,  activate linking with [Great Sage] and [Magic Perception].>>")
            ssprint("<<Activate [Magic Perception]?>>")
            rimuru.add_attribute('Magic Perception')
            action_menu(self)

        # ========== Veldora introduce himself
        class _use_magic_perception:
            def __init__(self):
                sprint('...')
                sprint(slime_art.magic_perception)
                sprint("OH!")
                sprint("Hmmmmmmmm")
                sprint("I can see. I CAN SEE!")
                sprint("~Seems like you did it. You learn quickly little one.~")
                sprint("Yes, thank you!")
                sprint("~Allow me to formally introduce myself?~")
                action_menu(self)

            def _sure(self):
                sprint("My name is Storm Dragon Veldora!~")
                sprint(slime_art.cave_veldora)
                sprint("~I am one of the four True Dragons of this world.~")
                sprint("HOLY SHIT, you're a real dragon!")
                sprint("~Didn't I tell you not to get scared.~")
                ssprint("~even with the scary appearance, the little slime and dragon started chatting.~")
                action_menu(Become_Friends())

            def _nah(self):
                ssprint("~Alright then, I won't. Hmmmmph~")
                action_menu(Become_Friends())

    class Become_Friends:
        def __init__(self):
            ssprint("Hmmmm, now what?")

        class _leave:
            def __init__(self):
                sprint("I guess I'll be heading out now.")
                ssprint("~Really, so soon. But we just started!~")
                ssprint("~Stay, please, we have so to talk about.~")
                action_menu(self)


            def _stay(self):
                ssprint("~Oh, I'm so glad you decided to stay!.~")
                action_menu(Become_Friends())

            def _leave(self):
                ssprint("~I guess there's nothing I can say or do to make you stay. How rude of you to just leave me here all by myself!~")
                Leave_Cave()

        def _friend_dragon(self):
            sprint("Okay... sooo, you want to be friends?")
            sprint("~HAHAHA, WHAT?! A mere slime wants to be friends with the great Storm Dragon Veldora!?~")
            sprint("Wellll... If you don't want to, that's fine too.")
            sprint("~WHAAAAAAT, Who said we could not!~")
            sprint("I guess I won't have a reason to come back here again, huh.")
            sprint("~Wait. I guess it can't be helped. I'll become your friend!.~")
            sprint("Great. Now I guess I should help you with this seal eh?")
            action_menu(Help_With_Seal())

    class Help_With_Seal:
        def __init__(self):
            global veldora
            veldora = mobs.Veldora_Tempest()
            ssprint("[Great Sage]?")
            ssprint("<<Answer, analysis shows it's impossible to destroy [Infinity Prison] using any physical attacks.>>")
            ssprint("<<Notice, possible solution may be...")
            sprint("~Hey don't just only talk to your own skill.~")
            sprint("Jealous?")
            sprint("It might be possible if we both analyze [Infinity Prison] inside and out")
            sprint("~My skills were sealed away as well, I can't use analyze.~")
            sprint("If you give me the information [Great Sage] can analyze your side as well")
            sprint("~Won't that take a long time, didn't you want to go find other reincarnates from your world~")
            sprint("I have a suggestion. How would you like to")
            sprint("get in my stomach.")
            sprint("~hahaha~")
            sprint("~ku hahaha~")
            sprint("~HAHAHAHAHAHAHA~")
            ssprint("Ummmm, did he just use the 3 stage laugh...?")
            sprint("~My life is in your hands.~")
            sprint("Wow how trusting of you.")
            sprint("~Well... The alternative is to stay in this cave for the rest of my time.~")
            sprint("I'll use predator to swallow you now.")
            sprint("~Before that, let me give you a name. You think of a name for both of us.~")
            sprint("Like a last name? hmmmmm...")
            family_name = str(input("\nLast Name > "))
            veldora.family_name = family_name
            rimuru.family_name = family_name
            rimuru.divineProtection = 'Storm Crest'
            ssprint("<Acquired Storm Crest Divine Protection>\n")
            rimuru.update_ranking(8)

            sprint(f"Hmmmmmm... How about {family_name}")
            sprint("~What a good name!~")
            sprint("He actually likes it?")
            sprint(f"~From now on I'll be Veldora {family_name}~")
            sprint("~And as for you...~")
            rimuru.name = str(input("\nName > "))
            sprint(f"~How about {rimuru.name} {family_name}")

            sprint("~Leave it to me. Until we meet again little one!~")
            ssprint("<<Use Unique skill [Predator]?>>")
            action_menu(self)

        class _predate_veldora:
            def __init__(self):
                ssprint("~The slime little grew big enough to completely engulf the dragon and his seal in mere seconds before turning back to normal~\n")
                rimuru.add_inventory(veldora)
                rimuru.show_inventory()

                ssprint("<<Notice, start analyzing Unique Skill [Infinity Prison]?>>")
                action_menu(self)

            def _start_analysis(self):
                ssprint("Yes, Please take care of it [Great Sage].")
                ssprint("I hope you get out quickly!")
                Leave_Cave()

            def _move_on(self):
                ssprint("Ummmmm, I guess he's imprisoned in my stomach now forever....")
                ssprint("Note, you can start analysis whenever you choose.")
                ssprint("ehehhh... Veldora is gonna be pissed that I didn't immediately start, he'll think I betrayed him...")
                Leave_Cave()

    def Leave_Cave():
        ssprint("Time to leave this cave already.")
        continue_story(rimuru, Chapter2)

    Chapter_1()
