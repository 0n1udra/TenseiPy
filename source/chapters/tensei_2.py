from game_files.functions import *
from game_maps.game_location import *
from chapters.tensei_3 import Chapter3


def ch2_goblin_encounter(rimuru):
    class goblin_encounter:
        __location = "Near the Sealed Cave"

        def __init__(self):
            mobs_reset()
            siprint("Where am I going?")
            siprint("*While practicing pronunciation with [Ultrasound Waves]. A pack of [Dire Wolves] shows up*")
            sprint("You strong one.")
            siprint("Who's that? Wait... They look like goblins! Should I talk to them?")
            game_action(self)

        class _talk_to_goblins:
            __subs = ['speak to goblins', 'interact with goblin', 'say hi to goblin', 'meet goblins', 'talk to them']
            def __init__(self):
                mobs_add(['10* goblin'])
                siprint("How should I introduce myself?")
                game_action(self)

            class _friendly:
                __subs = []
                def __init__(self):
                    sprint("HELLO, MY NAME IS RIMURU. I'M A SLIME.")
                    sprint("...")
                    sprint("Strong one we have already recognized your strength. Please, lower your voice!")
                    sprint("oh, ok. I was just exploring around here. Is there something you need?")
                    sprint("No, you see, our village is near. We felt a strong demonic aura and decided to immediately investigate.")
                    siprint("Demonic aura? what? Great Sage can you change my viewpoint, I want to see this demonic aura.")
                    siprint("OH!, so uh that's why everyone is drawn to me and why the wolves ran away at the sight of me. I should rein that in.")
                    siprint("After some more clarification, they invited to their village. It looks like they need some help. Should I go?")
                    goto_goblin_village()

            class _subjugate:
                 __subs = ['subjugate goblins', 'rule goblins', 'ruthless', 'be ruthless', 'enslave', 'enslave goblins']
                 def __init__(self):
                     sprint("Alright you weaklings, listen here you little shits, I'll only say this once!")
                     sprint("You have two options. You can worship me or you can die.")
                     dots(2, 10)
                     if get_random(1, 10, 1):
                         sprint("NEVER! We will never surrender to you!")
                         sprint("ATTACK!!!!!!!!")
                     game_over()

                     sprint("Ok, good choice. So, you guys have a base, village, anything?")
                     sprint("Y-yes sir, our village is just up ahead. We would be delighted to have you.")
                     sprint("Of course you would. Lets start moving.")
                     goto_goblin_village()

        class move_on:
            __subs = subs.move_on
            def __init__(self):
                siprint("Nah... Lets move on.")
                siprint("<< Warning, dangerous monsters are near. >>")
                siprint("Oh crap! Is that a wolf pack!?! I should probably run!")
                siprint("~You there, slime! What is such a weak creature doing out here?~")

            class nice:
                __subs = ['minding my own business', 'none of your business', 'why?', "Don't mind me", "I'm just a slime", "I'm just a cute little slime"]
                def __init__(self):
                    siprint("Just a cute little slime minding his own business.")

            class rude:
                __subs = ['weak?', 'weak', 'who are you calling weak', "you're the weak one", "bad dog", "you talking to me?"]
                def __init__(self):
                    siprint("Weak!?! Who are you calling weak, you mutt.")

            class what_you_want:
                def __init__(self):
                    siprint("What do you want?")

            class attack:
                def __init__(self):
                    if mobs_cleared():
                        siprint("They looked dangerous.")
                    else:
                        siprint("I didn't get them all, crap there's one running towards me!")
                        game_over()


    class goto_goblin_village:
        __locatoin = "Goblin Village"

        def __init__(self):
            mobs_add(['goblin: Goblin Chief'])
            siprint("Wow, this place looks like a dump... ")
            sprint("I am the village elder. I'm sorry we don't have much to serve you.")
            sprint("So I'm guessing you didn't invite me here just for pleasantries.")
            sprint("We've heard about your hidden strength. Would you please listen to our request.")
            sprint("About a month ago our Dragon guardian disappeared, and nearby monsters have started expand there territory.")
            sprint("There is a pack of 100 Dire Wolves that have been attacking us recently, and we are barely fendding them off.")
            game_action(self)

        class _assist_goblins:
            def __init__(self):
                sprint("Ok, I'll try the best of my abilities to protect your village.")
                sprint("Thank you so much, we will be forever loyal to you.")
                game_action(self)

            class _heal_wounded:
                __subs = ['any wounded', 'any hurt', 'any goblins wounded']
                def __init__(self):
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
                            goto_goblin_village._assist_goblins()
                        else:
                            sprint("I need some way to heal them.")
                            goto_goblin_village._assist_goblins()

                def _let_them_die(self):
                    siprint("I'm going to save my potions for myself.")
                    sprint("Great one, please! If you can heal our wounded we would be most grateful!")
                    sprint("Nah, I can't waste my precious healing potions on such weak monsters who are so undeserving.")
                    sprint("I see, we are sorry for troubling you.")
                    goto_goblin_village._assist_goblins()

            class _setup_defenses:
                def __init__(self):
                    sprint("Let's setup defenses.")
                    game_cond('village_defense', 'up')

                    wolf_attack()

        def _compensation(self):
            sprint("So what, you want protection? What would my reward be?")
            sprint("W-we don't have much to reward you with, but we can offer our unwavering loyalty.")
            sprint("That will have to do. For now.")
            goto_goblin_village._assist_goblins()

        def _attack(self):
            if mobs_cleared():
                siprint("They're all dead now. They were so weak.")
                siprint("What now?")
                hunt_wolves()

            if mob_status('goblin elder'):
                sprint("Listen up! I am now you're new village chief!")
                sprint("Anyone that disagrees will be cut down on the spot!")
                game_action(self)

    class wolf_attack:
        def __init__(self):
            sprint("The Dire Wolves, they're here!")
            game_action(self)

        def _attack(self):
            siprint("Lets attack first before they can do anything.")

        def _give_warning(self):
            sprint("Listen up, because I'm only going to say this once!")
            sprint("Acknowledge me as your ki   ng, or retreat now and never show yourselves again!")
            sprint("So, which is it?")

    class hunt_wolves:
        def __init__(self):
            sprint("Lets go chase after those wolves, see if anything interesting happens.")

            game_action(self)

    goblin_encounter()
