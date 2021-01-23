from game_files.game_functions import *
from chapters.tensei_3 import Chapter3


def Chapter2(rimuru):
    class chapter_2:
        __location = 'Sealed Cave'

        def __init__(self):
            mobs_new(['tempest serpent', 'giant bat', 'black spider', 'evil centipede'])
            siprint("Oh, what's this? Feels like some kind of ore.?")
            action_menu(self)

        class _eat_ore:
            subs = ['']
            def __init__(self):
                rimuru.add_inventory('magic ore')
                siprint("<< Information, analysis shows this is the raw form of [Magisteel]. Can be used for crafting weapons, armor, and more. >>")
                siprint("Ok, might be useful in the future. Guess I should get as much as I can")
                action_menu(_learn_new_attack())

        def _move_on(self):
            siprint("I can always come back for it I guess.")
            siprint("With [Magic Perception] I can finally find my way out.")
            siprint("*But before that... Some monsters started taking a interest in the little slime.*\n")
            action_menu(_learn_new_attack())

        def _explore(self): self._move_on()

    class _learn_new_attack:
        def __init__(self):
            siprint("Now that's a big snake! Or am I just small?")
            siprint("<< Answer, this is a [Tempest Serpent]. >>")
            siprint("Still, it's not as scary as Veldora. I should be able to handle it.")
            siprint("However, I don't think I have any ways to attack or damage it if it's hostile. Hmmmmmm. I wonder...")
            iprint("\n< Hint: Choose ability to learn and use it on [Tempest Serpent]. >")
            action_menu(self)

        def try_escaping(self):
            siprint("Oh no, it noticed me!")

        def _learn_water_bullet(self):
            rimuru.add_attribute('water bullet')
            siprint("Nice, it worked. After learning [Hydraulic Propulsion], I was thinking I could use water as an attack too.")
            siprint("Now I have a way to attack.\n")
            action_menu(_attack_serpent())

        def _learn_water_blade(self):
            rimuru.add_attribute('water blade')
            siprint("Hey, it worked. Since I already have [Hydraulic Propulsion], I was thinking I could use super high pressure water as a blade attack also.")
            siprint("Lets try it out!")
            action_menu(_attack_serpent())

        def eat_ore(self): rimuru.add_inventory('magic ore')

    class _attack_serpent:
        def __init__(self):
            iprint("\n< Hint: Try to 'target' the Tempest Serpent, than try to 'attack' it with your new skill. 'help' for more.")
            action_menu(self)

        class _attack:
            def __init__(self):
                if not mob_status('tempest serpent'):
                    sprint("Wow, what a powerful attack. I probably shouldn't use that so carelessly.")
                    siprint("<< Notice, would you like to use Unique Skill [Predator]? >>")
                    sprint("Oh...? What will that do?")
                    siprint("<< Answer, after predation, information and target's skills may be obtained through analysis. >>\n")

                    sprint("Are those bats?")
                    siprint("<< Answer, they are commonly known as [Giant Bat]. >>")
                    siprint("And it seems like there's some other small monsters dwelling in here aswell.")
                    siprint("I should clear them out before they notice me.\n")

                    siprint("\n< HINT: Try [Sense Heat Source] to detect foes using the 'use' command, or use 'nearby'. 'help' for more info. >")

                if mobs_cleared():
                    action_menu(_at_exit())
                else:
                    action_menu(_attack_serpent())

        def eat_ore(self):
            rimuru.add_inventory('magic ore')

        def _sneak_away(self):
            siprint("I'll try to sneak away.")
            action_menu(_at_exit())

    class _at_exit:
        def __init__(self):
            siprint("Finally! Found the exit. Wow, that's a pretty big door. How am I going to open that?")
            siprint("Water attack? No, that'll probably be overkill. Wait somethings happening.")
            siprint("*The giant pair of doors slowly creeks open, and three adventurers shows themselves.*")
            siprint("What should I do... I can wait and try to sneak past them if they're going in")
            sprint("Adventurer 1: Phew, it's finally open, even the keyhole was rusted.")
            sprint("Adventurer 2: It is over 300 years old, and nobody is maintaining it. I doubt there's a real dragon in here.")
            sprint("Adventurer 2: Still reckless of the guildmaster to send us to investigate.")
            sprint("I shouldn't show, they'll probably get scared and attack me")

            action_menu(self)

        def _sneak_out(self):
            siprint("I'll try sneaking out after they go in.")
            siprint("Finally! I'm out of that cave. Where now to though?")
            action_menu(_the_encounter())

        def _say_hi(self):
            sprint("HELLO THERE!")
            sprint("Adventurers: AHHHHH MONSTER.")
            sprint("KILL IT. KILL IT.")
            sprint("KILL IT!!!!")
            sprint("WAIT, Wait. I'm a friendly slime! Slurrrr.....")
            siprint("*The adventurers attacked and killed the little slime monster before he could say anything else.*")

            if rimuru.check_acquired('veldora'):
                siprint("* After the little slime died. All of his stomach contents spewed outwards. *")
                siprint("* Unfortunately this particular slime had somehow absorbed a whole dragon! *")
                siprint("* Now with the three low-level adventurers swiftly flattened by such a massive object. They Have failed there simple mission. *")

            game_over()

    class _the_encounter:
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
                siprint("Wait, are those... Goblins? Also, How can I understand them?")
                siprint("<< Answer, [Magic Perception] converts sound waves to comprehensible sentences. >>")
                siprint("<< Also, sound waves can also be used to communicate your thoughts. >>")
                siprint("Is that so, let's try that.")
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
            action_menu(_goblin_village())

        def _ruthless(self):
            sprint("Alright you weaklings. Listen here you little shits. You have two options. You can worship me or you can die.")
            sprint("So. What will it be?")
            sprint("O-of course, we all obey!")
            sprint("Ok, good choice. So, you guys have a base, village, anything?")
            sprint("Y-yes sir, our village is just up ahead. We would be delighted to have you.")
            sprint("Of course you would. Lets start moving.")
            action_menu(_goblin_village())

    class _goblin_village:
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
                        action_menu(_goblin_village._assist_goblins, remove='_heal_wounded')
                    else:
                        sprint("I need some way to heal them.")
                        action_menu(_goblin_village._assist_goblins)

                def _let_them_die(self):
                    siprint("I'm going to save my potions for myself.")
                    sprint("Great one, please! If you can heal our wounded we would be most grateful!")
                    sprint("Nah, I can't waste my precious healing potions on such weak monsters who are so undeserving.")
                    sprint("I see, we are sorry for troubling you.")
                    action_menu(_goblin_village._assist_goblins, remove='_heal_wounded')

            class _setup_defenses:
                def __init__(self):
                    sprint("Let's setup defenses.")
                    game_conditions('village_defense', 'up')

                    action_menu(_wolf_attack_village())

        def _compensation(self):
            sprint("So what, you want protection? What would my reward be?")
            sprint("W-we don't have much to reward you with, but we can offer our unwavering loyalty.")
            sprint("That will have to do. For now.")
            action_menu(_goblin_village._assist_goblins())

        def _attack(self):
            if mobs_cleared():
                siprint("They're all dead now. They were so weak.")
                siprint("What now?")
                action_menu(_hunt_wolves())

            if mob_status('goblin elder'):
                sprint("Listen up! I am now you're new village chief!")
                sprint("Anyone that disagrees will be cut down on the spot!")
                action_menu(self)

    class _wolf_attack_village:
        def __init__(self):
            sprint("The Dire Wolves, they're here!")
            action_menu(self)

        def _attack(self):
            siprint("Lets attack first before they can do anything.")

        def _give_warning(self):
            sprint("Listen up, because I'm only going to say this once!")
            sprint("Acknowledge me as your ki   ng, or retreat now and never show yourselves again!")
            sprint("So, which is it?")

    class _hunt_wolves:
        def __init__(self):
            sprint("Lets go chase after those wolves, see if anything interesting happens.")

            action_menu(self)


    chapter_2()
