from game_files.functions import *
from game_maps.game_location import *
from chapters.tensei_3 import Chapter3


def ch2_goblin_encounter(rimuru):
    class goblin_encounter:
        __location = "Near the Sealed Cave"

        def __init__(self):
            mobs_reset()
            mobs_add(['10* goblin'])
            siprint("Where am I going?")
            siprint("\n* While practicing pronunciation with [Ultrasound Waves]. A pack of [Dire Wolves] shows up *")
            sprint("\nYou strong one.")
            siprint("\nWho's that? Wait... They look like goblins! Should I be nice?")
            game_action(self)

        class _friendly:
            __subs = subs.be_nice_subs + ['my name is rimuru', 'say hi', 'talk', 'chat', 'talk to goblins']
            def __init__(self):
                sprint("HELLO, MY NAME IS RIMURU. I'M A SLIME.")
                sprint("...")
                sprint("Strong one we have already recognized your strength. Please, lower your voice!")
                sprint("Oh, ok. I was just exploring around here. Is there something you need?")
                sprint("No, you see, our village is near. We felt a strong demonic aura and decided to immediately investigate.")
                siprint("\nDemonic aura? what? Great Sage can you change my viewpoint, I want to see this demonic aura.")
                siprint("OH!, so uh that's why everyone is drawn to me and why the wolves ran away at the sight of me. I should rein that in.")
                siprint("After some more clarification, they invited to their village. It looks like they need some help.")
                goto_goblin_village()

        class _subjugate_goblins:
            __subs = ['subjugate', 'subjugate goblins', 'rule goblins', 'ruthless', 'be ruthless', 'enslave', 'enslave goblins']
            def __init__(self):
                sprint("\nAlright you weaklings, listen here you little shits, I'll only say this once!")
                sprint("You have two options. You can worship me or you can die.")
                dots(2, 10)
                if get_random(1, 10, 1):  # 1/10 chance of goblins revolting
                    sprint("\nNEVER! We will never surrender to you!")
                    sprint("ATTACK!!!!!!!!")
                    game_over()

                sprint("\nOk, good choice. So, you guys have a base, village, anything?")
                sprint("Y-yes sir, our village is just up ahead. We would be delighted to have you.")
                sprint("Of course you would. Lets start moving.")
                goto_goblin_village()

        class hfunc_attack:
            def __init__(self):
                if mobs_cleared():
                    print("Yeahhhhh.... Hello, developer here! First off, WTF is wrong with you. Second, sorry but as of now the story NEEDS those weak goblins.")
                    print("ikik, I'm sooooo sorry that you can't go on a genocidal rampage right now (just yet), but yes, sadly the story just won't work with them all dead.")
                    game_over()
                elif check_attack_success():
                    siprint("oh")

    class goto_goblin_village:
        __location = "Goblin Village"

        def __init__(self):
            mobs_reset()
            siprint("\nWow, this place looks like a dump... ")
            sprint("\nI am the village elder. I'm sorry we don't have much to serve you.")
            sprint("So I'm guessing you didn't invite me here just for pleasantries.")
            sprint("We've heard about your hidden strength. Would you please listen to our request.")
            sprint("About a month ago our Dragon guardian disappeared, and nearby monsters have started expand there territory.")
            sprint("There is a pack of 100 Dire Wolves that have been attacking us recently, and we are barely fending them off.")
            siprint("\nHmmmmm... Should I help them? What about compensation?")
            game_action(self)

        class compensation:
            __subs = ['ask for compensation', 'ask for reward', 'what about pay', 'reward', 'is there a reward', 'will i be compensated', 'compensation']
            def __init__(self):
                sprint("W-we don't have much to reward you with, but we can offer our unwavering loyalty.")
                sprint("That will have to do. For now.")

        class _assist_goblins:
            __subs = ['assist', 'lend help', 'assist them', 'assist the goblins', 'help goblins', 'help the goblins', 'help them', 'assist them']
            def __init__(self):
                sprint("Ok, I'll try the best of my abilities to protect your village.")
                sprint("Thank you so much, we will be forever loyal to you.")
                siprint("This village has no defenses, that might help. And a goblin said something about wounded victims.")
                game_action(self)

            class _setup_defenses:
                __subs = ['go setup defenses', 'setup some defenses', 'setup border defenses']
                def __init__(self):
                    sprint("Let's setup defenses.")
                    siprint("Hey! Get some goblins to setup defenses around the parameter.")

                    if rimuru.check_acquired('sticky thread'):
                        siprint("I can use [Sticky Thread] as a trap also.")
                        game_cond('sticky thread trap', True)
                    if rimuru.check_acquired('steel thread'):
                        siprint("Perhaps [Steel Thread] can be use as a last line of defense.")
                        game_cond('steel thread trap', True)

                    wolf_attack()

            class _heal_wounded:
                __subs = ['heal wounded', 'heal wounded victims']
                def __init__(self):
                    sprint("Show me your wounded")
                    if rimuru.check_acquired('full potion', 9):
                        siprint("I could try eating them and splashing them with the potion...")
                        sprint("Wow, those potions are really impressive.\n")
                        rimuru.remove_inventory('full potion', 9)
                        rimuru.add_reputation('goblins', 1)
                        action_playable('_heal_wounded', False)
                    else:
                        siprint("Looks like 9 wounded goblins..... How can I help them?")
                        sprint("I need some way to heal them.")

    class wolf_attack:
        def __init__(self):
            sprint("\nMaster! The Direwolves are here!")
            game_action(self)

        class _give_warning:
            __subs = ['give them a warning', 'take over', 'take over as king', 'become new king', 'subjugate goblins', 'subjugate them']
            def __init__(self):
                sprint("Listen up, because I'm only going to say this once!")
                sprint("Acknowledge me as your king, or retreat now and never show yourselves again!")
                sprint("So, which is it?")
                sprint('\nOur wolf pack will not be initimdated by a mere slime!')
                sprint("ATTACK!!!")
                siprint("\nWelp.... That didn't work...")

                if game_cond('sticky thread trap'):
                    siprint("Those [Sticky Thread] traps are working well I see.")
                    sprint("\nYour tricks will not stop me! I am the pack leader!")

                if game_cond('steel thread trap'):
                    sprint("W-w-what is this!?")
                    sprint("That would be [Steel Thread]! Can't bite through that, can you!")
                # Without setting up steel thread as defense, the pack leader will kill you!
                else:
                    siprint("\nThat wolf is coming at me way to fast! I have nothing to stop him!")
                    sprint("\nYOU'RE DEAD, YOU SLIME!")
                    sprint("\n*CHOMP*")
                    game_over()

                game_action(self)

            class _kill_leader:
                __subs = []
                def __init__(self):
                    mobs_add(['direwolf boss'])

    goblin_encounter()
