from game_files.game_functions import *
from chapters.tensei_3 import Chapter3


def ch2_goblin_encounter(rimuru):

    class goblin_encounter:
        __location = "Near the Sealed Cave"

        def __init__(self):
            mobs_reset()
            siprint("Where am I going?")
            action_menu(self)

        class _explore:
            def __init__(self):
                siprint("*While practicing pronunciation with [Ultrasound Waves]. A pack of [Dire Wolves] shows up*")
                siprint("Was I that loud... Eh? Where are those wolves going? What's this...")
                sprint("You strong one.")
                action_menu(_meet_goblins())

    class _meet_goblins:
        def __init__(self):
            mobs_new(['10* goblin'])
            siprint("How should I introduce myself?")
            action_menu(self)

        def _friendly(self):
            sprint("HELLO, MY NAME IS RIMURU. I'M A SLIME.")
            sprint("...")
            sprint("Strong one we have already recognized your strength. Please, lower your voice!")
            sprint("Sorry, I am still adjusting.")
            sprint("T-There is no need to apologize strong one!")
            sprint("I was just exploring around here. Is there something you guys need?")
            sprint("No, you see, our village is ahead of here. We felt a strong demonic aura and decided to immediately investigate.")
            siprint("Demonic aura? what? I don't sense anything.")
            siprint("Great Sage can you set change my viewpoint, I want to see this 'demonic aura'.")
            siprint("OH!, so uh that's why everyone is drawn to me and why the wolves ran away at the sight of me. I should rein that in.")
            siprint("The goblins and I chatted some more then they invited me to there village.")
            action_menu(goto_goblin_village())

        def _ruthless(self):
            sprint("Alright you weaklings. Listen here you little shits. You have two options. You can worship me or you can die.")
            sprint("So. What will it be?")
            sprint("O-of course, we all obey!")
            sprint("Ok, good choice. So, you guys have a base, village, anything?")
            sprint("Y-yes sir, our village is just up ahead. We would be delighted to have you.")
            sprint("Of course you would. Lets start moving.")
            action_menu(goto_goblin_village())

    class goto_goblin_village:
        __locatoin = "Goblin Village"

        def __init__(self):
            mobs_new(['goblin: Goblin Chief'])
            siprint("Wow, this place looks like a dump... ")
            sprint("I am the village elder. I'm sorry we don't have much to serve you.")
            sprint("So I'm guessing you didn't invite me here just for pleasantries.")
            sprint("We've heard about your hidden strength. Would you please listen to our request.")
            sprint("About a month ago our Dragon guardian disappeared, and nearby monsters have started expand there territory.")
            sprint("There is a pack of 100 Dire Wolves that have been attacking us recently, and we are barely fendding them off.")
            action_menu(self)

        class _assist_goblins:
            def __init__(self):
                sprint("Ok, I'll try the best of my abilities to protect your village.")
                sprint("Thank you so much, we will be forever loyal to you.")
                action_menu(self)

            class _heal_wounded:
                def __init__(self):
                    sprint("Show me your wounded")
                    action_menu(self)

                def _heal_goblins(self):
                    if rimuru.check_acquired('full potion', 9):
                        rimuru.remove_inventory('full potion', 9)
                        sprint("Wow, ")
                        action_menu(goto_goblin_village._assist_goblins, remove='_heal_wounded')
                    else:
                        sprint("I need some way to heal them.")
                        action_menu(goto_goblin_village._assist_goblins)

                def _let_them_die(self):
                    siprint("I'm going to save my potions for myself.")
                    sprint("Great one, please! If you can heal our wounded we would be most grateful!")
                    sprint("Nah, I can't waste my precious healing potions on such weak monsters who are so undeserving.")
                    sprint("I see, we are sorry for troubling you.")
                    action_menu(goto_goblin_village._assist_goblins, remove='_heal_wounded')

            class _setup_defenses:
                def __init__(self):
                    sprint("Let's setup defenses.")
                    game_conditions('village_defense', 'up')

                    action_menu(wolf_attack())

        def _compensation(self):
            sprint("So what, you want protection? What would my reward be?")
            sprint("W-we don't have much to reward you with, but we can offer our unwavering loyalty.")
            sprint("That will have to do. For now.")
            action_menu(goto_goblin_village._assist_goblins())

        def _attack(self):
            if mobs_cleared():
                siprint("They're all dead now. They were so weak.")
                siprint("What now?")
                action_menu(hunt_wolves())

            if mob_status('goblin elder'):
                sprint("Listen up! I am now you're new village chief!")
                sprint("Anyone that disagrees will be cut down on the spot!")
                action_menu(self)

    class wolf_attack:
        def __init__(self):
            sprint("The Dire Wolves, they're here!")
            action_menu(self)

        def _attack(self):
            siprint("Lets attack first before they can do anything.")

        def _give_warning(self):
            sprint("Listen up, because I'm only going to say this once!")
            sprint("Acknowledge me as your ki   ng, or retreat now and never show yourselves again!")
            sprint("So, which is it?")

    class hunt_wolves:
        def __init__(self):
            sprint("Lets go chase after those wolves, see if anything interesting happens.")

            action_menu(self)

    goblin_encounter()
