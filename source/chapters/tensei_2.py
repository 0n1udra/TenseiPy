import game_files.functions as game
import game_files.extra as extra
from game_files.output import gprint, sprint, siprint, idots, dots, show_art
from game_maps.locations import subs


def ch2_dwargon(rimuru):
    class welcome_to_dwargon():
        def __init__(self):
            if game.conditions('tamed direwolves'):
                sprint("\n* After 3 days of travel. *\n")
            else: sprint("\n* After 5 days of travel. *")
            siprint("Bringing the whole group might attract unwanted attention.")
            siprint("So we'll just continue with $Gobta$ and $Ranga$ in my shadow.")

            game.mobs_add(['2*human:Bandit'])
            siprint("We're at the gate now and it's a pretty long line.")
            sprint("\nOnce we get inside, we can go anywhere.")
            sprint("\nLook what we have here, we got some monsters here!")
            sprint("Since we're not technically not in Dwargon we can do whatever we want!")
            game.actions(self)

        class try_talking:
            __subs = ['try talking it out', 'try calming them down', 'chat', 'talk']
            def __init__(self):
                sprint("Why would we talk to such pathetic monsters that are below us!")
                siprint("\nOk.... That isn't going to work...")

        class scare_them_away:
            __subs = ['make them fear', 'scare them']
            def __init__(self):
                siprint("I wonder if I can scare them away somehow...")
                if rimuru.check_acquired('coercion'):
                    siprint("Wait! Can't I use that Direwolves skill?")
                else:
                    siprint("Maybe I can use a skill to attack to show my power without directly targeting them to scare them off.")

        class _attack:
            def __init__(self):
                # Kill the bandits and you go straight to Dwargon jail, and no you can't eat the humans.
                if game.mobs_cleared():
                    sprint("My lord... Was that really necessary? Oh crap here comes the guards!")
                    idots(50)
                    dwargon_jail_murder()

        class _run_away:
            __subs = ['run', 'flee', 'escape', 'try fleeing', 'try running away', 'try escaping']
            def __init__(self):
                if game.conditions('no fleeing'):
                    sprint("\n* The thugs stabbed and killed the both of you while you were trying to flee. *")
                    game.game_over()  # No running away for you!

                if extra.get_random(1, 10):  # 1/10 chance they won't let you flee.
                    siprint("Crap they won't even us flee. What a pain!")
                    game.conditions('no fleeing', True)
                else:
                    siprint("We successful fled from those thugs. What a pain!")
                    siprint("We decided to go back to our group and spend the night just outside the gate and try again tomorrow.")
                    dots(25)
                    inside_dwargon()

        class _hfunc_use:
            def __init__(self):
                if game.last_use_skill('coercion'):
                    sprint("HOWWWLLLLLLLLLL!!!!!!!!!!!!")
                    siprint("Hopefully this scares them away.")
                    idots(30)
                    dwargon_jail_coercion()
                if game.last_use_skill('water blade'):
                    if extra.get_random(1, 3, 1):  # 1/3 chances, can do it multiple times to try and scare them off.
                        sprint("\nL-lets get out of here, they're not worth our time.")
                        sprint("Finally, they're gone, and nobody got hurt.")
                        sprint("\nMy lord you did it! They won't be troubling us anymore.")
                        sprint("\nNot the best first impression of Dwargon, but at least nobody got hurt.")
                        inside_dwargon()
                    else:
                        if extra.get_random(1, 3, 1):  # 1/3 chance they will charge at you to kill you.
                            sprint("\nYou think you can scare us so easily!")
                            siprint("\nCrap now their charging straight for us with a knife!")
                            sprint("\nMy lord what should we do!")
                            game.actions(self)
                        else: sprint('\nYou think that will scare us you puny slime!')

            class _do_nothing:
                __subs = ['nothing']
                def __init__(self):
                    sprint("AHHHHH MY LORD THEY GOT ME!")
                    sprint("I-I think i-i'm dying!")
                    sprint("* In an instant both you and $Gobta$ died from the two bandits. *")
                    game.game_over()

            class _attack:
                def __init__(self):
                    if game.mobs_cleared():
                        sprint("My lord! You saved me! I am forever grateful!")
                        sprint("However... The guards are now on there way!")
                        siprint("\n*sigh* This trip has not been going well at all!")
                        dwargon_jail_murder()
                    else:
                        sprint("I-I'm sorry my lord! I have failed you!")
                        siprint("\nNot good, not good, now we're both going to die!")
                        siprint("I should have done something! WHY DIDN'T I DO ANYTHING!")
                        game.game_over()

    # Go to Dwargon jail after using [Coercion] skill on bandits.
    class dwargon_jail_coercion:
        def __init__(self):
            game.clear_all()
            siprint("\n...First time here and we're already in jail...")
            siprint("I didn't think just screaming would cause so much damage to the environment and the nearby people.")
            siprint("I guess my mimicry evolved with $Ranga$'s evolution.")
            sprint("\nYou guys sit tight while we wait to decide what to do with---.")
            sprint("\nCAPTAIN COME QUICK! There was a beast in the Mines! It was delt with, however.")
            sprint("We need to get all the healing potions to help the injured.")
            game.actions(self)

        class _make_potions:
            def __init__(self):
                if rimuru.check_acquired('full potion', 50):
                    sprint("\nHey, you said you need healing potions?")
                    sprint("\nShut it, this is important!")
                    sprint("\nCalm down, I want to help. Here's a barrel of healing potions for ya.")
                    sprint("\nHmmmm... How can we trust someone behind bars...")
                    sprint("\nIt sounds like you don't have much of a choice, that is if you want to help your friends...")
                    sprint("\nFine. Stay here!")
                    rimuru.remove_inventory('full potion', 50)
                    game.conditions('helped dwarves', True)
                    dots(10)
                    sprint("We're back, and your potions was somethin else!")
                    sprint("Some of my friends wanted to come by and say thanks to their savior.")
                    sprint("\nYEAH! If it wasn't for your medicine I would definitely be dead by now!")
                    sprint("\nThank you! It was even able to regrow my entire arm!")
                    sprint("\nMmmmmmmhmmmmmmmm")
                    sprint("\nThanks again slime, my friends and I are indebted to you, if there's anything you need, let me know!")
                    sprint("Also, we got some good news for you! You guys are free to go.")
                else:
                    siprint("I should make sure I give them enough to help everyone, who knows how many were injured.")

        class _do_nothing:
            def __init__(self):
                sprint("\n.....")

        class hfunc_jail_break:
            def __init__(self):
                siprint("")

    # To jail and then death penalty after murdering bandits.
    class dwargon_jail_murder:
        def __init__(self):
            game.clear_all()
            siprint("\n...... Since I kinda just murdered two bandits in cold blood, we are now in jail...")
            siprint("This journey sure is going well...")
            sprint("\nI thought my lord would have more self restraint.")
            sprint("\nShut it.")
            # TODO Add trial?
            sprint("\n* After a swift trial, the both of you were executed shortly after for murder. *")
            game.game_over()

    # Got into Dwargon.
    class inside_dwargon:
        def __init__(self):
            game.clear_all()
            sprint("\nWe made it inside!")

    welcome_to_dwargon()
