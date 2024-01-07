import game_files.functions as game
import game_files.extra as extra
import game_files.art as game_art
from game_files.output import gprint, sprint, siprint, idots, dots, show_art
# Import the next chapter to continue to.
from chapters.tensei_2 import ch2_dwargon
from game_maps.locations import cave_actions, subs
from game_objects.characters import Veldora_Tempest

def ch1_cave(rimuru):
    # Manga Ch.1
    class wake_up():
        __location = 'Sealed Cave'

        def __init__(self):
            rimuru.add_mimic('slime', show_msg=False)
            print("\n    < Chapter 1 >")
            idots()
            gprint("<< Confirmation Complete. Constructing body that does not require blood... >>\n")
            gprint("<< Confirmation Complete. Acquiring Extra Skill: [Predator]... >>")
            gprint("<< Acquired Extra Skill [Predator]. >>")
            gprint("<< Confirmation Complete. Acquiring: Extra Skill [Sage]... >>")
            gprint("<< Acquired Extra Skill [Sage]. >>")
            rimuru.upgrade_attribute('Sage', 'Great Sage')

            siprint("It's so dark? Where am I? What happened?")
            siprint("I remember now, I got stabbed! A-am I dead?")
            siprint("Was I saved? Can I move? Should I try to say something?")

            # Because I am a dick. There is a 1 in 1,000 chance that you will wake up and just instantly die! kek!
            if extra.get_random(1, 1_000, 666):
                siprint("\nWAIT! WAIT WHAT'S THAT AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
                siprint("SOMETHING IS EATING MEEEEEEEEEEEEEEEEEEEEEEEEEE!!!!!!!!!!!!!!!")
                print("\n\nYOU DIED BEFORE YOU COULD EVEN DO ANYTHING, WHAT BAD LUCK YOU HAVE!")
                game.game_over()

            # Show user HUD and playable actions.
            game.actions(self)

        class speak:
            __subs = ['try to speak', 'try speaking', 'try to talk', 'try talking', 'talk', 'say something', 'try to say something', 'yell', 'try to yell', 'try yelling', 'say something', 'try saying something', 'use mouth']
            def __init__(self):
                idots(3)
                siprint("I can't seem to speak, wait.....")
                siprint("I CAN'T FEEL MY MOUTH!")
                siprint("I. Can't. Feel. ANYTHING! I should check the rest of my body!")
                print(game.conditions('speak'))
                print(game.action_played('speak'))

        class move:
            __subs = ['move around', 'try to move', 'look around', 'explore']
            def __init__(self):
                dots()
                siprint("I can't see anything! Where are my arms, I can't feel them!")
                siprint("Did I just move? I can't see anything, can't hear, can't even smell anything...")
                siprint("What is this? Feels like I'm 'absorbing' something. This body? Am I even human anymore!?!?!")

        class _inspect_body:
            __subs = ['examine', 'examine body', 'examine self', 'examine myself', 'inspect', 'check body', 'confirm body', 'inspect my body', 'feel body', 'feel', 'feel around', 'move around', 'check', 'check if human']
            def __init__(self):
                siprint("What is that feeling? Is....is that grass?! It feels like it's dissolving...")
                game.actions(self)

            class puyo:
                __subs = ['squish', 'bounce']
                def __init__(self):
                    sprint("Puuuuuuuuuuuuyooooooooooo!")

            class _explore:
                __subs = subs.move_on
                def __init__(self):
                    show_art('slime')
                    print(game_art.rimuru_art.died)
                    idots()
                    siprint("Dissolving and absorbing, this streamlined elastic feeling body....")
                    siprint("It looks like I have been stabbed, died and reincarnated as a slime!")
                    idots(10, 2)
                    siprint("\nIt has been a long time now since I have accepted myself a slime. I am getting use to this body.")
                    siprint("No need for sleep or food. I don't feel too hot nor cold. Even after taking some damage I can heal myself..\n")
                    siprint("All I can do is fumble around in the dark and eat what I find... I'M SO BORED!")

                    game.actions(self)

                class eat_grass:
                    __subs = cave_actions.eat_grass.__subs
                    def __init__(self):
                        rimuru.add_inventory('hipokte grass')
                        siprint("What is this I'm feeling... Could it be?")
                        siprint("<< Information, analysis indicates [Hipokte Grass]. Commonly used for crafting healing potions. >>")
                        siprint("Healing potions? Like in those fantasy video game... Interesting.")

                class eat_ore:
                    __subs = cave_actions.eat_ore.__subs
                    def __init__(self):
                        rimuru.add_inventory('magic ore')
                        siprint("What is this hard feeling stuff?")
                        siprint("<< Information, analysis indicates [Magisteel]. Can be used for crafting weapons, armor, and more. >>")
                        siprint("Ok, might be useful in the future. Guess I should get as much as I can")

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
                    __subs = ['what is predator', 'what is this predator', 'what is this predator skill', 'predator huh', 'tell me more about predator', 'tell me more about predator']
                    def __init__(self):
                        siprint("<< Answer, unique skill [Predator] 'predates' targets, stashes in skill's 'stomach'. >>")
                        siprint("<< Addendum, after successful analysis of monster, [Mimic] can be used to replicate appearance and skills.")
                        siprint("Wow, that sounds like a OP skill!")
                        gprint("< Tutorial: Try 'info predator' to get more information. >")

                class what_is_great_sage:
                    __subs = ['what is this great sage', 'what is great sage', 'tell me more about great sage', 'what are you', 'tell me more about you', 'tell me more about yourself great sage', 'tell me more about yourself', 'what are you', 'who are you', "what's this voice"]
                    def __init__(self):
                        siprint("<< Answer, my function is to assist my master to the best of my abilities. >>")
                        siprint("<< Information, some of my basic functions are: Analysis, skill control and manipulation, crafting, and more. >>")
                        gprint("< Tutorial: Use 'info great sage' to get more information on skill. >")

                        if rimuru.check_acquired('hipokte grass'):
                            gprint("< Tutorial: Try 'info hipokte grass'. Then try 'craft full potion'. >")

                class where_did_it_go:
                    __subs = ['where it go', 'where did the grass go', 'where did that all go', 'hey where did that go', "where's the grass", "where's the grass now", 'where is the grass', 'where is the grass now', 'where did it go', 'where does it go', 'where does it all go', 'where do they go', 'where do they all go', 'where does it all go', 'where has it gone', 'where has it all gone']
                    def __init__(self):
                        siprint("Where does the stuff I eat go?")
                        siprint("<< Answer, they are stored inside the Unique Skill [Predator]'s stomach sack. >>")
                        siprint("I think I heard this voice before. Who, or what, are you?")
                        siprint("<< Answer, this is the Unique Skill [Great Sage], the ability has adapted to best assist you. >>")
                        siprint("Skills, Great Sage, Predator? huh... Wonder what those are. I should get moving too.")

    class in_water:
        __location = "Under water?"
        def __init__(self):
            print(game_art.rimuru_art.fall_in_water)
            siprint("SHIT! I've finally reincarnated and I'm already going to die!")
            siprint("O'Great sage how painful thy death will be? Am I really going to suffocate to death?!?!")
            siprint("<< Answer, A slime's body does not require oxygen to survive. >>")
            siprint("Huh.... Feeling pain I am not... But what am I going to do now?")
            idots()
            game.actions(self)

        class stay_in_water:
            __subs = subs.wait + ['stay in water', 'wait in water']
            def __init__(self):
                idots()
                siprint("It's boring down here, I gotta find a way out.")

        class eat_water:
            __subs = ['suck it up', 'intake water', 'suck water', 'suck up water', 'suck in water', 'suck up some water', 'intake some water', 'suck water up', 'eat more water', 'predate more water', 'suck up more water']
            def __init__(self):
                rimuru.add_inventory('water')
                siprint("Alright, now lets try this out.")

        class try_getting_out:
            __subs = ['spew water', 'eject water', 'vomit water', 'try getting out', 'try to get out', 'swim', 'swim up', 'swim out', 'try swimming', 'leave water', 'try to swim', 'find a way out', 'get out', 'use water to propel', 'propel with water', 'expel water to propel', 'expel', 'expel water', 'expel the water', 'use hydraulic propulsion']
            def __init__(self):
                if rimuru.check_acquired('water'):
                    rimuru.add_attribute('Hydraulic Propulsion')
                    rimuru.use('hydraulic propulsion')
                    siprint("\nOuch! I went flying and hit something, but at least it seems like I'm back on land.")
                    siprint("Sucking up the water and expelling it at a high pressure sure did the trick!")
                    siprint("I also got a new skill too, wonder what else I can do with it.")
                    veldora_encounter()
                else:
                    siprint("I need figure out a way to get out of this situation.")

        class hfunc_grab_sword:
            __subs = ['look for treasure', 'look for things', 'search for things', 'search for treasure', 'grab sword', 'get sword', 'eat sword', 'predate sword', 'find treasure', 'get treasure', 'grab treasure', 'eat treasure', 'predate treasure']
            def __init__(self):
                rimuru.add_inventory('magic sword')
                siprint("HEY! Look! This shape, feels like a sword! Wonder if it's any good?")
                siprint("<< Answer, analysis of [Magic Sword] indicates a magisteel core, sword is above average grade. >>")
                siprint("Would you look at that, that might come in handy later on. But I'm still stuck down here!")
                game.clear_subs(self)  # Only able to grab sword once.

    class veldora_encounter(cave_actions):
        __location = "Sealed Cave"

        def __init__(self):
            sprint("\n Can you hear me small one. ")
            siprint("\nI almost pissed myself, if I could that is. Who's that speaking to me!? It can't be [Great Sage] could it?")
            siprint("This is the first conversation I'm having since reincarnating. According to [Great Sage] I've been in this cave for about 90 days!")
            siprint("Should I be friendly? But how do I even reply?. It's not like I have a mouth to speak with.")
            sprint("\n Hey, can you just reply? ")
            game.actions(self)

        class hello:
            __subs = ['say hi', 'reply', 'reply hi', 'reply with hi', 'repy with hello', "who's there", 'who is there', 'who is that', 'somebody there', "who's out there", "is somebody there", 'who is that speaking', 'hello', 'hello there', "who's that speaking", "who's that talking"]
            def __init__(self):
                siprint("Hello, who's there?")
                sprint("Keep following my voice small one. ")

        class great_sage:
            __subs = ['that you great sage', 'is that you great sage', 'was that you great sage', 'was it great sage', 'great sage']
            def __init__(self):
                siprint("Is that you Great Sage?")
                siprint("<< Answer, negative. Detecting incoming telepathy, source unknown. >>")
                siprint("Maybe I can try to following it if I keep moving, it seems to be getting stronger.")

        class _leave:
            __subs = subs.move_on
            def __init__(self):
                sprint("Bye now.")
                sprint("\nWait where are you going? ")
                sprint("\nYou seem pretty suspicious...")
                sprint("\nNooooo.... I'm not suspicious at all.l.l..")
                tempest_serpent_encounter()

        class shut_it:
            __subs = ["shut it you baldy", "screw you baldy", 'shut up baldy', 'shut up', 'shut it']
            def __init__(self):
                sprint("SHUT UP!")
                sprint("\nHAHAHA, SEEMS LIKE YOU HAVE A DEATH WISH!!!")
                sprint("\nI'M SORRY! I didn't think you could hear me!")
                sprint("\nCome closer small one. ")
                siprint('\nuh.... Should I follow the voice?')

        class _follow_voice:
            __subs = ['follow the voice', 'locate the voice', 'try locating the voice', 'try locating voice', 'try finding the voce', 'try following the voice', 'seek out voice', 'seek voice', 'follow strange voice', 'seek strange voice', 'follow']
            def __init__(self):
                siprint("I hit something, but it's not a rock. And what is this aura that I'm feeling? Could it be?")
                sprint("\nHello? I never expected to speak with anyone other than my skill, since I can't see or hear.")
                sprint("\nThis is telepathy.")
                sprint("....Alright... fine, I'll help you see. Just don't be scared when you see my true form.")
                sprint("There is something called [Magic Sense], it allows you to perceive the surrounding magic essence.")
                sprint("\nWhat's this magic essence?...")
                siprint("<< Answer, this world is covered with magic essence. The body of a slime can move because it absorbs magic essence from it's surrounding. >>")
                sprint("\n With this skill you will be able to 'see', 'hear' and much more! ")
                sprint("\nEh... this feels really complicated. It won't hurt to try though... Will it???")
                siprint("<< Notice, to help parse the large amount of incoming data, activating sync with [Great Sage] and [Magic Sense]. >>")
                game.actions(self)

            class _use_magic_sense(cave_actions):
                __subs = ['try magic sense', 'try using magic sense', 'activate magic sense', 'yes', 'yes please', 'yes do it', 'activate', 'activate it', 'yes, activate it']
                def __init__(self):
                    idots(5)
                    show_art('magic sense')
                    rimuru.add_attribute('Magic Sense')
                    rimuru.update_status('magic sense', 'Active')
                    sprint("nike this?")
                    sprint("I can see. I CAN SEE!")
                    sprint("\n Looks like you did it. You learn quickly small one. ")
                    sprint("Yes, thank you!")
                    sprint("\n Shall I formally introduce myself now? ")
                    game.actions(self)

                class _yes:
                    __subs = ['sure', 'why not', 'go ahead']
                    def __init__(self):
                        sprint("Sure.... Go ahead...")
                        sprint("\nMy name is Storm Dragon Veldora! ")
                        show_art('cave veldora')
                        sprint("I am one of the four True Dragons of this world. ")
                        sprint("\nHOLY SHIT, you're a real dragon!")
                        sprint("\nDidn't I tell you not to get scared. ")
                        friend_veldora()

                class _no:
                    __subs = ['no', 'nah', "let's move on", "don't", 'skip', 'skip it']
                    def __init__(self):
                        sprint("Uh. no.")
                        sprint("\nAlright fine, I won't. Hmmmmph ")
                        friend_veldora()

            class _leave:
                __subs = subs.move_on + ['no, leave', 'leave', 'leave him', 'leave dragon', 'escape']
                def __init__(self):
                    sprint("Ok.... bye!")
                    sprint("\nWait where are you going small one! Weren't we getting somewhere...... ")
                    sprint("Hello? Hellooooooooooo?! ")
                    sprint("FINE! I don't need you anyways! ")
                    tempest_serpent_encounter()

    class friend_veldora(cave_actions):
        def __init__(self):
            sprint("\nHmmmm, now what?")
            siprint("Should I try make a friend? Or just leave, there's something suspicious about him...")
            game.actions(self)

        class _leave:
            __subs = subs.move_on
            def __init__(self):
                sprint("I guess I'll be heading out now.")
                sprint("\nReally, so soon. But we just started! ")
                sprint("Stay, please, we have so much to talk abo.o.o... ")
                siprint("\nPhew, I think I lost him.\n")
                tempest_serpent_encounter()

        class _friend_dragon(cave_actions):
            __subs = ['befriend dragon', 'ask to become friends', 'want to be friends', 'wanna be friends', 'become friends', 'friend', 'friend him', 'ask to be friends', 'make friend']
            def __init__(self):
                sprint("Okay... Sooo, you want to be friends?")
                sprint("\nHAHAHA, WHAT?! A mere slime wants to be friends with the great Storm Dragon Veldora!?~ ")
                sprint("\nWellll... If you don't want to, that's fine too.")
                sprint("\nNow hold on, who said we can't! I guess it can't be helped. ")
                sprint("\nGreat. Now I guess I should look this seal heh?")
                siprint("Wonder how he got imprisoned in the first place.....")
                game.actions(self)

            class _look_at_seal(cave_actions):
                __subs = ['take a look', 'analyze seal', 'analyze', 'scan', 'scan seal', 'scan prison', 'look at prison', 'analyse seal', 'analyse prison', 'check seal', 'check prison', 'scan seal', 'scan prison', 'check out seal', 'check out prison', 'look', 'inspect', 'inspect seal', 'inspect prison', 'inspect prison seal', 'analyse prison seal']
                def __init__(self):
                    global veldora
                    veldora = Veldora_Tempest()
                    siprint("Great Sage, what can you tell me about this prison?")
                    siprint("<< Answer, analysis shows it's impossible to destroy [Infinity Prison] using any physical attacks. >>")
                    siprint("<< Notice, possible solution may be... >>")
                    sprint("\nHey, don't ignore me. :(")
                    sprint("\nIt might be possible if we both analyze [Infinity Prison] inside and out")
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
                    veldora.set_lname(new_family_name)
                    print()
                    rimuru.set_lname(new_family_name)
                    rimuru.add_protection('Storm Crest')
                    rimuru.add_level()

                    sprint(f"Hmmmmmm... How about {new_family_name}")
                    sprint("\nThat. Name. Is. AWESOME!")
                    siprint("\nHe actually likes it?")
                    sprint(f"\nFrom now on I will be Veldora {new_family_name}")
                    sprint("And as for you...")
                    rimuru.set_name(str(input("\nPick name for yourself > ")))
                    sprint(f"\nHow about {rimuru.name}!")
                    rimuru.update_reputation('veldora', 1)

                    sprint("\nI am ready now, until we meet again small one!")
                    siprint("\n<< Activate Unique skill [Predator]? >>")
                    game.actions(self)

                class eat_grass:
                    __subs = cave_actions.eat_grass.__subs
                    def __init__(self):
                        rimuru.add_inventory('hipokte grass')
                        sprint("Hey what are you doing there? Focus on me... ME!")

                class _use_predator:
                    __subs = subs.all_yes + ['predate', 'eat', 'predate veldora', 'eat dragon', 'eat the dragon', 'predate dragon', 'predate the dragon', 'swallow dragon', 'swallow veldora']
                    def __init__(self):
                        global veldora
                        rimuru.add_inventory(veldora, show_analysis_msg=False)
                        rimuru.update_reputation('veldora', 1)
                        siprint("<< Notice, start analyzing Unique Skill [Infinity Prison]? >>")
                        game.actions(self)

                    class _start_analysis:
                        __subs = subs.all_yes + ['start', 'start it', 'yes start it please', 'yes start it']
                        def __init__(self):
                            siprint("Yes, of course.")
                            rimuru.update_status('veldora', 'Analyzing')
                            gprint("< Starting Analysis: Unique Skill [Unlimited Imprisonment] >")
                            rimuru.update_reputation('veldora', 1)
                            siprint("I hope you get out quickly Veldora!")
                            tempest_serpent_encounter()

                    class _move_on:
                        __subs = subs.move_on + subs.no + ['no', 'ignore him, lets move on']
                        def __init__(self):
                            siprint("ehehhh... Veldora is gonna be pissed that I didn't immediately start, will he think I betrayed him...")
                            rimuru.update_reputation('veldora', -10)
                            tempest_serpent_encounter()

                class ask_about_seal:
                    __subs = ['so how did you get here anyways', 'ask about seal', 'ask about his story', 'how did you get imprisoned', 'how did you get here', 'who did this to you']
                    def __init__(self):
                        sprint("So how did you end up here?")
                        sprint("\nWill you see, that's kind of a long story. Not one to be told here.")
                        # TODO Add story.

            class _leave_veldora(cave_actions):
                __subs = subs.move_on + ['leave veldora', 'leave friend', 'abandon veldora', 'abandon him', 'abandon friend']
                def __init__(self):
                    siprint("OK, I go now.")
                    siprint("\nWAIT! WHAAAAAT!")
                    siprint("I thought we were friends! :(.......")
                    siprint("\nPlease come back friend!")
                    sprint("\nI got to go! Bye!")
                    rimuru.update_reputation('veldora', -1)
                    tempest_serpent_encounter()

    # Ch.2
    class tempest_serpent_encounter:
        def __init__(self):
            game.mobs_add(['tempest serpent', 'giant bat', 'black spider', 'evil centipede'])
            siprint("\nI've been looking for the cave exit for a bit now.... This cave is so big! Or am I just small?")
            siprint("<< Answer, you are just small. >>")
            siprint("Oh, thanks for that.")
            siprint("\n* But before long some monsters started taking a interest in the small slime. *")
            siprint("\nWhat is that? it looks like a big snake!")
            siprint("<< Answer, analysis indicating [Tempest Serpent]. >>")
            siprint("Still, it's not as scary as Veldora. I should be able to handle it.")
            siprint("However, I don't think I have any ways to attack or damage it if it's hostile. Hmmmmmm. I wonder...\n")
            rimuru.add_attribute('water blade')
            siprint("Hey, it worked. Since I already have [Hydraulic Propulsion], I was thinking I could use super high pressure water as a blade attack also.")
            gprint("< Tutorial: First target with 'target tempest serpent'. Then attack with 'attack water blade'. >")
            game.actions(self)

        class sneak_away:
            __subs = ['sneak out', 'try sneaking out', 'try to sneak out', 'try escaping', 'try to sneak away', 'try sneaking away', 'try sneaking out', 'try slipping out', 'try to slip away', 'try to slip out', 'slip away']
            def __init__(self):
                siprint("Imma just try and sneak on outta here...")
                if not game.mob_status('tempest serpent'):
                    at_cave_exit()

                siprint("Crap! It noticed me, no sneaking out now!")

        class _move_on:
            __subs = subs.move_on
            def __init__(self):
                siprint("Let's get moving.")
                if game.mobs_cleared():
                    at_cave_exit()
                else:
                    siprint("I still sense some enemies around. I should clear them out before they give me trouble.")
                    if rimuru.check_acquired('sense heat source'):
                        siprint("Oh yeah! I have that new [Sense Heat Source] skill, that might be useful.")
                        gprint("< Tutorial: Try Mimicking [Tempest Serpent] and using it's [Sense Heat Source] to locate nearby mobs. '/help' for more info on commands. >")
                        gprint("< Tutorial: While mimicking, use 'stats' to see your's and mimicked monster's attributes and skills. > ")
                    if rimuru.check_acquired('magic sense'):
                        gprint("< Hint: If acquired [Magic Sense], you can use 'nearby' command to see nearby mobs. >")

        class attack:
            __subs = ['attack water blade']
            def __init__(self):
                if not game.mob_status('tempest serpent'):
                    siprint("Wow, what a powerful attack. I should probably use that only when needed.")
                    siprint("<< Suggestion, Use Unique Skill [Predator]? >>")
                    siprint("Oh...? What will that do?")
                    siprint("<< Answer, after predation, information and target's skills may be obtained through analysis. >>")
                    gprint("< Tutorial: Try 'predate' or 'eat' on targeted mobs that are dead to use [Predator] skill. >")

    class at_cave_exit:
        def __init__(self):
            game.clear_all()
            game.mobs_add(['kaval', 'gido', 'eren grimwold'])
            siprint("Finally! Found the exit. Wow, that's a pretty big door. How am I going to open that?")
            siprint("Water attack? No, that'll probably be overkill. Wait somethings happening.")
            siprint("Wait! They look like people! Three of them. What are they doing here?")
            sprint("\nPhew, it's finally open, even the keyhole was rusted.")
            sprint("\nIt is over 300 years old, and nobody is maintaining it. I doubt there's a real dragon in here.")
            sprint("\nStill reckless of the guildmaster to send us to investigate.")
            siprint("\nHow can I understand them?")
            siprint("<< Answer, [Magic Sense] converts sound waves to comprehensible sentences which I interpret for you. >>")
            sprint("\nI shouldn't show, they'll probably get scared and attack me. I should wait for them to move on.")
            game.actions(self)

        class hfunc_attack:
            __subs = ['attack adventurers', 'attack them']
            def __init__(self):
                if game.mobs_cleared():
                    siprint("Wasn't necessary, but I suppose it had to be done.")
                    at_cave_exit._hfunc_leave_cave()

                if game.check_attack_success():  # Will only run if you successfully killed at least one of them.
                    siprint("CRAP! I didn't kill all of them, the rest will kill me!")
                    siprint("\n* Before the little slime could do or say anything else, he was swiftly smushed to death! *")
                    game.game_over()

        class _say_hi:
            def __init__(self):
                sprint("HELLO THERE! My name is.....")
                sprint("\nAHHHHHHHHHHHHHH MONSTER.")
                sprint("\nKILL IT. KILL IT.")
                sprint("\nKILL IT!!!!")
                sprint("\nWAIT, Wait. I'm not a bad slime slurrrr.....")
                siprint("\n* The adventurers attacked and killed the little slime monster before he could say anything else. *")

                if rimuru.check_acquired('veldora'):
                    sprint("* After the little slime died. All of his stomach contents spewed outwards. *")
                    sprint("* Unfortunately, this particular little slime had somehow absorbed a whole dragon! *")
                    sprint("* Now with the three low-level adventurers swiftly flattened by such a massive object. They Have failed there simple mission. *")
                    sprint("\nWhat is this? Where is that little slime? Hello.... Friend?")
                    sprint("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!")

                game.game_over()

        class _wait:
            __subs = ['wait', 'sneak out', 'wait to sneak out', 'wait to slip out', 'try to slip out', 'sneak away', 'sneak out after them', 'wait to sneak away', 'sneak past them']
            def __init__(self):
                game.clear_all()
                siprint("C'mon just go already!")
                if extra.get_random(1, 20, 1):  # 1/20 chance they will notice you.
                    siprint("I sense a monster nearby! There! A slime!")
                    siprint("\nCrap! How did they notice me!")
                    siprint("\n* And before another word could be uttered by the little slime, he was swiftly smushed. *")
                    game.game_over()

                siprint("Phew, their gone now. I can finally leave now. They even left the door open for me, how nice.")

                # Only if you met veldora, and you haven't already 'eaten' him.
                if game.conditions('friend veldora') and not rimuru.check_acquired('veldora'):
                    siprint("Or... uhm... Should I go back to that pouty dragon or just move on?")
                    game.action_playable('_x_go_to_veldora', True)

                game.actions(self)

            class _x_go_to_veldora:
                __subs = ['go find veldora', 'veldora', 'go back to veldora', 'go back to dragon', 'go find that voice', 'find voice', 'follow voice', 'follow voice again', 'go follow voice', 'follow weird voice', 'locate voice', 'search for voice', 'search for weird voice', 'voice', 'what was that voice', 'where is that voice coming from', 'where is that voice', 'where was that voice', 'where was that voice again', 'go back to voice']
                def __init__(self):
                    if game.conditions('friend veldora'):
                        siprint("Let's go check on that dragon.")
                        siprint("\n What are you doing back? ")
                        friend_veldora()
                    else:
                        siprint("I want to go find that weird voice in the cave!")
                        veldora_encounter()

            class _leave:
                __subs = ['leave', 'leave cave', 'exit', 'exit cave', 'move on', 'continue']
                def __init__(self):
                    game.clear_all()
                    siprint("Let's leave this cave already!")
                    goblin_village()

    class goblin_village:
        __location = "Near the Sealed Cave"

        def __init__(self):
            game.clear_all()
            gprint("< Chapter 2 >\n")
            game.mobs_add(['10* goblin'])
            siprint("Where am I going?")
            siprint("\n* While practicing pronunciation with [Ultrasound Waves]. A pack of [Dire Wolves] shows up *")
            sprint("\nYou strong one.")
            siprint("\nWho's that? Wait... They look like goblins! Should I be nice?")
            game.actions(self)

        class _be_friendly:
            __subs = subs.be_nice_subs + ['say hi', 'talk', 'chat', 'talk to goblins']
            def __init__(self):
                if rimuru.name:
                    sprint(f"HELLO, MY NAME IS {rimuru.name.upper()}. I'M A SLIME.")
                else: sprint("HELLO I AM $Rimuru$!, I'M A SLIME!!!.")
                sprint("...")
                sprint("Strong one we have already recognized your strength. Please, lower your voice!")
                sprint("Oh, ok. I was just exploring around here. Is there something you need?")
                if rimuru.check_acquired('veldora'):
                    sprint("No, you see, our village is near. We felt a strong demonic aura and decided to immediately investigate.")
                    siprint("\nDemonic aura? What? Great Sage can you change my viewpoint, I want to see this demonic aura.")
                    siprint("OH!, so uh that's why everyone is drawn to me and why the wolves ran away at the sight of me. I should rein that in.")
                else:
                    sprint("We were just patrolling our village borders. We now recognize you are not just another simple slime.")
                siprint("\nThey're inviting me to their village. It looks like they need some help.")
                goto_goblin_village()

        class _subjugate_goblins:
            __subs = ['subjugate', 'subjugate goblins', 'rule goblins', 'ruthless', 'be ruthless', 'enslave', 'enslave goblins']
            def __init__(self):
                sprint("Alright you weaklings, listen here you little shits, I'll only say this once!")
                sprint("You have two options. You can worship me or you can die.")
                dots(5, 2)
                if extra.get_random(1, 10, 1):  # 1/10 chance of goblins revolting
                    sprint("\nNEVER! We will never surrender to you!")
                    sprint("ATTACK!!!!!!!!")
                    game.game_over()

                sprint("\nWe offer our loyalty to you strong one!")
                sprint("\nOk, good choice. So, you guys have a base, village, anything?")
                sprint("Y-yes sir, our village is just up ahead. We would be delighted to have you.")
                goto_goblin_village()

        class hfunc_attack:
            def __init__(self):
                if game.mobs_cleared():
                    siprint("Uhhhh....... Was that totally necessary...")
                    game.game.conditions('killed village', True)
                    siprint("Anyways.... Lets keep moving. WAIT! What are those? Are those wolves?!")
                    sprint("\nLook at what we have here boys, it's a weak little slime.")
                    sprint("\nAhahahahahaha")
                    sprint("\nI've heard slimes tastes good!")
                    sprint("\n* Before the little slime could do anything else, the wolves charged at it... and they had a little snack. *")
                    game.game_over()
                elif game.check_attack_success():
                    sprint("HOW COULD YOU! ATTACK!")
                    siprint("\nCRAP, now there pissed!")
                    sprint("* Before anything else could happen, the rest of the goblins charged to kill the slime. *")
                    game.game_over()

    # Ch.3
    class goto_goblin_village:
        __location = "Goblin Village"

        def __init__(self):
            game.clear_all()
            game.mobs_add(['goblin:goblin chief', 'goblin'])
            siprint("Wow, this place looks like a dump... Such a primitive house.")
            sprint("\nI am the village chief. I'm sorry we don't have much to offer you.")
            sprint("\nAnyway, what's up? I assume you invited me here for a reason.")
            sprint("\nI've heard about your incredible strength. Would you please listen to our request.")
            sprint("\nSpeak.")
            sprint("\nAbout a month ago our Dragon guardian disappeared, and nearby monsters have started expand there territory.")
            sprint("\nThere is a pack of 100 Direwolves that have been attacking us recently, and we are barely fending them off.")
            sprint("\nRigur, my older brother, died to bring us this information. A Demon gifted him the name.")
            sprint("He was the village's greatest warrior, we have survived this long because of him.")
            siprint("\nHmmmmm... 100 huh... That's a lot. Should I help them? What about compensation?")
            game.actions(self)

        class hfunc_more_about_rigur:
            __subs = ['so rigur is not around anymore', 'rigur died', 'sorry for your lost', "rigur's not around anymore"]
            def __init__(self):
                sprint("So, Rigur is no longer around?")
                sprint("\nYes, my son was the pride of my life.")
                sprint("Even if we weaklings are destined to perish, we must find a way to survive and honor his strength!")

        class hfunc_attack:
            def __init__(self):
                if not game.mob_status('goblin chief'):
                    sprint("W-why... Why would you do this!")
                    sprint("\nListen up, I'm the new leader of this village!")
                    sprint("If anyone has a problem with that, you will end up like your previous leader here!")
                    sprint("\nW-w-we will give our fealty to you.")
                    game.conditions('killed village chief', True)
                    rimuru.update_reputation('goblins', -5)
                elif not game.mob_status('goblin'):
                    siprint("Now they're pissed!")
                    sprint("\nYou will not get away with this!")
                    sprint("YOU WILL NOT LEAVE THIS VILLAGE ALIVE!")
                    sprint("\n* The little slime couldn't not escape the fury of the whole goblin village. *")
                    game.game_over()

        class compensation:
            __subs = ['ask for compensation', 'ask for reward', 'what about pay', 'reward', 'is there a reward', 'will i be compensated', 'compensation']
            def __init__(self):
                sprint("\nIf I do decide to help save your village, what will I get in return?")
                sprint("\nW-we don't have much to reward you with, but we can offer our unwavering loyalty.")
                sprint("That will have to do, for now.")

        class _assist_goblins:
            __subs = ['assist', 'lend help', 'assist them', 'assist the goblins', 'help goblins', 'help the goblins', 'help them', 'assist them']
            def __init__(self):
                sprint("Ok, I'll try the best of my abilities to protect your village.")
                sprint("\nThank you so much, we will be forever loyal to you.")
                siprint("This village has no defenses, those might help... And a goblin said something about wounded victims?")
                game.actions(self)

            class _setup_defenses:
                __subs = ['setup', 'go setup defenses', 'setup some defenses', 'setup border defenses']
                def __init__(self):
                    sprint("Hey! Get some goblins to setup defenses around the parameter.")
                    sprint("Setup some fences, and start training anyone that can do battle!")

                    if rimuru.check_acquired('steel thread'):
                        siprint("I can use [Steel Thread] as invisible traps.")
                        game.conditions('steel thread trap', True)
                    if rimuru.check_acquired('sticky thread'):
                        siprint("I wonder what I can do with [Sticky Thread].")
                        game.conditions('sticky thread trap', True)

                    wolf_attack()

            class _heal_wounded:
                __subs = ['heal wounded', 'heal wounded victims', 'heal hurt', 'help injured', 'heal injured', 'assist injured', 'assist wounded']
                def __init__(self):
                    sprint("Show me your wounded")
                    if rimuru.check_acquired('full potion', 9):
                        siprint("I could try eating them and splashing them with the potion...")
                        sprint("\nMy lord... What are you doing...")
                        idots(5)
                        sprint("Wow, those potions are really impressive.\n")
                        rimuru.remove_inventory('full potion', 9)
                        rimuru.update_reputation('goblins', 2)
                        sprint("\n* The slime ate, healed, and spat out the rest of the wounded goblins. *")
                        sprint("\nThere, all healed!")
                        sprint("\nW-w-whoa! You really are magnificent, great one! We thank you!")
                    else:
                        siprint("Looks like 9 wounded goblins..... How can I help them?")

    class wolf_attack:
        def __init__(self):
            game.clear_all()
            game.mobs_add(['direwolf leader', '10*direwolf'])
            sprint("\n* Meanwhile, the direwolves are getting ready... *")
            sprint("\nTonight we shall lay waste to the goblin village.")
            sprint("And take our first step towards conquering The Forest of Jura!")
            sprint("They no longer have protection from that accursed dragon!")

            sprint("\nMaster! The Direwolves are here!")
            game.actions(self)

        class _do_nothing:
            __subs = ['wait', 'stall', 'nothing']
            def __init__(self):
                sprint("My lord please help us! We will all surely die if you don't do anything!")
                sprint("\nNah I'm just going to sit here and do nothing!")
                rimuru.update_reputation('goblins', -10)
                sprint("* The Direwolf pack killed every last goblin including you. *")
                game.game_over()

        class _hfunc_attack:
            __subs = subs.attack
            def __init__(self):
                if game.mobs_cleared():
                    sprint("That takes care of that...")
                    siprint("Probably unwarranted, but now we don't have to worry about them.")
                    rimuru.update_reputation('goblins', 1)
                    naming_mobs()
                elif not game.mob_status('direwolf leader'):
                    wolf_attack._give_warning._attack()

        class _give_warning:
            __subs = ['give them a warning', 'warn direwolves', 'warn wolves', 'give direwolf warning', 'warn them']
            def __init__(self):
                sprint("Stop where you are! Listen up, because I'm only going to say this once!")
                sprint("Acknowledge me as your king, or retreat now and never show yourselves again!")
                sprint('\nOur wolf pack will not be intimidated by a mere slime!')
                sprint("ATTACK!!!")
                siprint("\nIntimidating not working...")
                siprint("Some of the goblins that are using bows are getting a few of them, but it's not enough.")

                if game.conditions('steel thread trap'):
                    sprint("\nWhat was that!")
                    sprint("That would be [Steel Thread].")
                    sprint("\nYour tricks will not stop us!")

                siprint("\nSome are still getting past my traps.")
                sprint("\nEnough of this! I will kill you slime!")
                sprint("\nFather! No!")
                if game.conditions('steel thread trap'):
                    sprint("\nW-w-what is this! Why can't I move!")
                    sprint("\nThat would be [Steel Thread]!")
                # Without setting up steel thread as defense, the pack leader will kill you!
                else:
                    siprint("\nThat wolf is coming at me way to fast! I have nothing to stop him!")
                    sprint("\nYOU'RE DEAD, YOU SLIME!")
                    sprint("\n*CHOMP*")
                    game.game_over()
                game.set_targets('direwolf leader')
                game.actions(self)

            class _attack:
                __subs = []
                def __init__(self):
                    if not game.mob_status('direwolf leader'):
                        sprint("No, Dad!")
                        sprint("\nYour leader is dead. Your choice now is fealty or death!")
                        siprint("They're not doing anything now... What are they waiting for? Do they need a leader perhaps?")
                    else:
                        sprint("You're DEAD you puny slime!")
                        siprint("\nHow did he get free!?")
                        game.game_over()

                    game.actions(self)

                class _eat:
                    __subs = subs.eat
                    def __init__(self):
                        sprint("\nMaybe they need a push...")
                        game.actions(self)

                    class _mimic_direwolf_leader:
                        def __init__(self):
                            siprint("This skill looks useful!")
                            game.actions(self)

                        class _use_coercion:
                            def __init__(self):
                                sprint("HOOWWWLLLLLL!!!!!..........")
                                siprint("I know I said fealty or death, but I'm hoping they would just run away in fear....")
                                dots(5)
                                sprint("HOWWLLLL!!!!......")
                                sprint("\nWE WILL FOLLOW YOU TO THE ENDS OF THE EARTH, MASTER!!!")
                                sprint("\nhuh?")
                                game.conditions('tamed direwolves', True)
                                rimuru.update_reputation('direwolves', 1)
                                rimuru.update_reputation('goblins', 2)  # You get better reputation for taming them instead of killing them all.
                                naming_mobs()

    class naming_mobs:
        def __init__(self):
            game.clear_all()
            siprint("Quite a wild retinue I've built up for myself.")
            siprint("I should probably lay down some rules for everyone to follow.")
            if game.conditions('killed village chief'):
                sprint("You, goblin, what are your names?")
            else: sprint("By the way chief, what your name?")
            sprint("\nMonsters usually don't have names. Not having names do not get in the way of communicating anyways.")
            sprint("\nOk, I see. Still, it would be convenient if I have a way to call you if I need to.")
            sprint("I suppose, I'll just have to give you guys names!")
            sprint("WHAAAAT!!!??? A-are you certain?")
            sprint("\nWhat's the big deal anyways? Everyone get in a line, so I can give you names.")
            dots(5)
            if not game.conditions('killed village chief'):
                show_art('village chief')
                siprint("What should I name the village chief? He had son named Rigurd, who died protecting this village...")
                rimuru.add_subordinate('goblin', 'Rigurd', level=4)
                sprint("I am honored great one!")
                sprint("\nAlright, next...")
            show_art('rigur')
            siprint("Now... The chief's younger son, the younger brother of the lost Rigurd...")
            rimuru.add_subordinate('goblin', 'Rigur', level=4)
            sprint("Thank you master!")
            show_art('gobta')
            sprint("\nSo, who's next? You seem like a chipper goblin...")
            rimuru.add_subordinate('goblin', 'Gobta', level=4)

            # TODO allow more naming, or add some other functionality to change names....
            siprint("There are so many to name, and I'm running out of ideas...")

            if game.conditions('tamed direwolves'):
                siprint("Alright, the goblins are done. Now for the Direwolves.")
                sprint("You're the son of the Direwolf boss right?")
                show_art('ranga')
                rimuru.add_subordinate('tempest star wolf', 'Ranga')
                game.multi_attr_adder(['gobta', 'rigurd', 'rigur'], ['thought communication'])

            siprint("Wait w-what's happening... My [Magic Sense] stopped working!")
            siprint("Why am I so sleepy now? What's happening Great Sage?")
            siprint("<< Answer, going into 'Sleep Mode' due to low magicule levels. >>")
            siprint("I was only giving them names, I didn't know it would use up that much.")
            siprint("<< Notice, estimated time for recovery is three days. >>")

            idots(10, 3)

            siprint("\nSo it's been three days already.")
            sprint("\nLord $Rimuru$ you're awake!")
            sprint("\n$Rigurd$ is that you?")
            sprint("\nOf coursed my lord! Now please follow me, the feast is nearly ready.")
            siprint("Wow, it looks like almost everyone has changed in some way.")

            if game.conditions('tamed direwolves'):
                sprint("\nAllow me to express my deepest joy at your recovery my lord!")
                sprint("\nIt's $Ranga$! Even he's different. He's so big!")

            sprint("* After the party to celebrate your awakening. *")
            sprint("\nAlright everyone, gather around! I'm going to set some ground rules.")
            sprint("One, No infighting. Two, No discriminating other species. Three, No Attacking Humans.")
            #TODO Give player the option to set different rules which will effect story later on
            sprint("That's it. Oh and also, $Rigurd$ I hereby place in the position of Goblin Lord!")
            sprint("\nMy lord! I will not let you down!")
            siprint("\nI just gave him that title so I have less responsibilities...")

            if game.conditions('tamed direwolves'):
                siprint("I also had the direwolves pair up with some goblins so they can start working together more productively.")
                siprint("I have a feeling having these direwolves on our side, it'll be benefit us in the combat and transportation department.")

            siprint("\nAfter looking at the state of the village I decided to take some goblins and go to a nearby Dwarven kingdom.")
            siprint("Since these goblins can't build or craft for shit, hearing about Dwarves gave me a great idea.")

            if game.conditions('tamed direwolves'):
                siprint("Since it was hard talking while riding Direwolves so fast, we used our new skill [Thought Communication].")

            siprint("$Gobta$ told me about how this Gelmud guy gave Rigur his name. I also learned there are Demon Lords in this world.")
            siprint("Also, apparently there's more than just Dwarves in this kingdom, there's also humans and elves!")
            siprint("\n$Gobta$ also explained how Dwargon is a bastion of free trade, and there's a rule of no fighting in there borders.")
            siprint("So us monsters should be ok going in. $Gobta$ did seem to have some hesitations though, but it shouldn't be a big problem.")
            welcome_to_dwargon()


    wake_up()
