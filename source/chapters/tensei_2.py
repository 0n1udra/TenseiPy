from game_files.functions import *
from game_maps.game_location import *
from chapters.tensei_3 import Chapter3


def ch2_goblin_encounter():
    class goblin_encounter:
        __location = "Near the Sealed Cave"

        def __init__(self):
            mobs_reset()
            mobs_add(['10* goblin'])
            siprint("Where am I going?")
            siprint("\n* While practicing pronunciation with [Ultrasound Waves]. A pack of [Dire Wolves] shows up *")
            sprint("\nYou strong one.")
            siprint("\nWho's that? Wait... They look like goblins! Should I talk to them?")
            game_action(self)

        class _talk_to_goblins:
            __subs = ['talk', 'say hi', 'speak to goblins', 'interact with goblin', 'say hi to goblin', 'meet goblins', 'talk to them']
            def __init__(self):
                siprint("How should I introduce myself? Should I be friendly or....?")
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

        class move_on:
            __subs = subs.move_on
            def __init__(self):
                tbc()
                siprint("Nah... Lets move on.")
                siprint("<< Warning, dangerous monsters are near. >>")
                siprint("Oh crap! Is that a wolf pack!?! I should probably run!")
                siprint("~ You there, slime! What is such a weak creature doing out here? ~")

            class nice:
                __subs = ['minding my own business', 'none of your business', "Don't mind me", "I'm just a slime", "I'm just a cute little slime"]
                def __init__(self):
                    siprint("Just a cute little slime minding his own business.")

            class rude:
                __subs = ['weak', 'weak', 'who are you calling weak', "you're the weak one", "bad dog", "you talking to me?"]
                def __init__(self):
                    siprint("Weak!?! Who are you calling weak, you mutt.")

            class what_you_want:
                __subs = ['you need something', 'what do you want', 'what you guys want']
                def __init__(self):
                    siprint("What do you want?")

            class attack:
                def __init__(self):
                    if mobs_cleared():
                        siprint("They looked dangerous. So I attacked first.")
                        siprint("But now looking at them up close, they look pretty weak and scrawny.")
                    else:
                        siprint("I didn't get them all, crap there's one running towards me!")
                        game_over()

    class goto_goblin_village:
        __location = "Goblin Village"

        def __init__(self):
            mobs_add(['goblin: Goblin Chief'])
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

        class _attack:
            def __init__(self):
                if mobs_cleared():
                    print("Yeahhhhh.... Hello, developer here! First off, WTF is wrong with you. Second, sorry but as of now the story NEEDS those weak goblins.")
                    print("ikik, I'm sooooo sorry that you can't go on a genocidal rampage right now (just yet), but yes, sadly the story just won't work with them all dead.")
                    game_over()
                    #siprint("They're all dead now. They were so weak.")
                    #siprint("What now?")

                if mob_status('goblin elder'):
                    sprint("Listen up! I am now you're new village chief!")
                    sprint("Anyone that disagrees will be cut down on the spot!")
                    game_action(self)

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
                    wolf_attack()

            class _heal_wounded:
                __subs = ['heal wounded', 'heal wounded victims', 'give potions', 'gift full potions', 'gift potions', 'give healing potions', 'see wounded', 'see wounded victims', 'go to wounded victims', 'any wounded', 'any hurt', 'any goblins wounded', 'show me your wounded', 'who is hurt', 'any victims', 'show me your injured', 'injured goblins', 'wounded goblins', 'hurt goblins']
                def __init__(self):
                    mobs_add(['9*goblin'])
                    sprint("Show me your wounded")
                    siprint("Looks like 9 wounded goblins..... How can I help them?")
                    game_action(self)

                class _heal_goblins:
                    __subs = ['use full potions', 'use healing potions', 'use potions']
                    def __init__(self):
                        if rimuru.check_acquired('full potion', 9):
                            rimuru.remove_inventory('full potion', 9)
                            sprint("Wow, ")
                            clear_subs(self)
                            rimuru.update_standing('goblins', 1)
                            goto_goblin_village._assist_goblins()
                        else:
                            sprint("I need some way to heal them.")
                            goto_goblin_village._assist_goblins()

                class _let_them_die:
                    __subs = ['let them die', 'just let them die']
                    def __init__(self):
                        siprint("I'm going to save my potions for myself.")
                        sprint("Great one, please! If you can heal our wounded we would be most grateful!")
                        sprint("Nah, I can't waste my precious healing potions on such weak monsters who are so undeserving.")
                        sprint("I see, we are sorry for troubling you.")
                        rimuru.update_standing('goblins', -1)
                        goto_goblin_village._assist_goblins()

    class wolf_attack:
        def __init__(self):
            mobs_add(['25* direwolf'])
            sprint("The Dire Wolves, they're here!")
            game_action(self)

        class _attack:
            def __init__(self):
                siprint("Best defence is a good offense, right?")

        class _give_warning:
            __subs = ['give them a warning', 'take over', 'take over as king', 'become new king', 'subjugate goblins', 'subjugate them']
            def __init__(self):
                sprint("Listen up, because I'm only going to say this once!")
                sprint("Acknowledge me as your king, or retreat now and never show yourselves again!")
                sprint("So, which is it?")
                if get_random(1, 3, 1):
                    siprint("We accept you as our new leader!")
                else:
                    siprint("How dare you! We not accept this!")

    goblin_encounter()
