from game_files.functions import *
from game_maps.game_location import *
from chapters.tensei_3 import Chapter3


def ch2_goblin_encounter(rimuru):
    class goblin_encounter:
        __location = "Near the Sealed Cave"

        def __init__(self):
            mobs_reset()
            gprint("< Chapter 2 >\n")
            mobs_add(['10* goblin'])
            siprint("Where am I going?")
            siprint("\n* While practicing pronunciation with [Ultrasound Waves]. A pack of [Dire Wolves] shows up *")
            sprint("\nYou strong one.")
            siprint("\nWho's that? Wait... They look like goblins! Should I be nice?")
            game_action(self)

        class _be_friendly:
            __subs = subs.be_nice_subs + ['say hi', 'talk', 'chat', 'talk to goblins']
            def __init__(self):
                if rimuru.name:
                    sprint(f"HELLO, MY NAME IS {rimuru.name.upper()}. I'M A SLIME.")
                else: sprint(f"HELLO, I'M A SLIME.")
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
                sprint("You have two options. You can worship me or you can die.\n")
                dots(5, 2)
                if get_random(1, 10, 1):  # 1/10 chance of goblins revolting
                    sprint("\nNEVER! We will never surrender to you!")
                    sprint("ATTACK!!!!!!!!")
                    game_over()

                sprint("\nWe offer our loyalty to you strong one!")
                sprint("\nOk, good choice. So, you guys have a base, village, anything?")
                sprint("Y-yes sir, our village is just up ahead. We would be delighted to have you.")
                sprint("Of course you would. Lets start moving.\n")
                goto_goblin_village()

        class hfunc_attack:
            def __init__(self):
                if mobs_cleared():
                    siprint("Uhhhh....... Was that totally necessary...")
                    game_cond('killed village', True)
                    siprint("Anyways.... Lets keep moving. WAIT! What are those? Are those wolves?!")
                    sprint("\nLook at what we have here boys, it's a weak little slime.")
                    sprint("Hahahaha")
                    sprint("\nAhahahahahaha")
                    sprint("\nI've heard slimes tastes good!")
                    sprint("\n* Before the little slime could do anything else, the wolves charged at it... and they had a little snack. *")
                    game_over()
                elif check_attack_success():
                    sprint("HOW COULD YOU! ATTACK!")
                    siprint("\nCRAP, now there pissed!")
                    sprint("* Before anything else could happen, the rest of the goblins charged to kill the slime. *")
                    game_over()

    class goto_goblin_village:
        __location = "Goblin Village"

        def __init__(self):
            mobs_reset()
            mobs_add(['goblin:goblin chief', 'goblin'])
            siprint("Wow, this place looks like a dump... Such a primitive house.")
            sprint("\nThank you for waiting visitor.")
            sprint("I am the village elder. I'm sorry we don't have much to offer you.")
            sprint("\nAnyway, what's up? I assume you invited me here for a reason.")
            sprint("\nI've heard about your incredible strength. Would you please listen to our request.")
            sprint("\nSpeak.")
            sprint("\nAbout a month ago our Dragon guardian disappeared, and nearby monsters have started expand there territory.")
            sprint("\nThere is a pack of 100 Direwolves that have been attacking us recently, and we are barely fending them off.")
            sprint("\nRigur, my older brother, died to bring us this information. A Demon gifted him the name.")
            sprint("He the vilage's greatest warrior, we have survived this long because of him.")
            siprint("\nHmmmmm... 100 huh... That's a lot. Should I help them? What about compensation?")
            game_action(self)

        class hfunc_more_about_rigur:
            __subs = ['so rigur is not around anymore', 'rigur died', 'sorry for your lost', "rigur's not around anymore"]
            def __init__(self):
                sprint("So, Rigur is no longer around?")
                sprint("\nYes, my son was the pride of my life.")
                sprint("Even if we weaklings are destined to perish, we must find a way to survive and honor his strength!")

        class hfunc_attack:
            def __init__(self):
                if not mob_status('goblin chief'):
                    sprint("W-why... Why would you do this!")
                    sprint("\nListen up, I'm the new leader of this village!")
                    sprint("If anyone has a problem with that, you will end up like your previous leader here!")
                    sprint("\nW-w-we will give our fealty to you.")
                    game_cond('killed goblin chief', True)
                elif not mob_status('goblin'):
                    siprint("Now they're pissed!")
                    sprint("\nYou will not get away with this!")
                    sprint("YOU WILL NOT LEAVE THIS VILLAGE ALIVE!")
                    sprint("\n* The little slime couldn't not escape the fury of the whole goblin village. *")
                    game_over()

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
                game_action(self)

            class _setup_defenses:
                __subs = ['setup', 'go setup defenses', 'setup some defenses', 'setup border defenses']
                def __init__(self):
                    sprint("Hey! Get some goblins to setup defenses around the parameter.")
                    sprint("Setup some fences, and start training anyone that can do battle!")

                    if rimuru.check_acquired('steel thread'):
                        siprint("I can use [Steel Thread] as invisible traps.")
                        game_cond('steel thread trap', True)
                    if rimuru.check_acquired('sticky thread'):
                        siprint("I wonder what I can do with [Sticky Thread].")
                        game_cond('sticky thread trap', True)

                    wolf_attack()

            class _heal_wounded:
                __subs = ['heal wounded', 'heal wounded victims', 'heal hurt', 'help injured', 'heal injured', 'assist injured', 'assist wounded']
                def __init__(self):
                    sprint("Show me your wounded")

                    if rimuru.check_acquired('full potion', 9):
                        siprint("I could try eating them and splashing them with the potion...")
                        sprint("\nLord ")
                        idots(5)
                        sprint("Wow, those potions are really impressive.\n")
                        rimuru.remove_inventory('full potion', 9)
                        sprint("\nW-w-whoa! You really are a powerful, great one!")
                        rimuru.add_reputation('goblins', 1)
                        action_playable('_heal_wounded', False)
                    else:
                        siprint("Looks like 9 wounded goblins..... How can I help them?")

    class wolf_attack:
        def __init__(self):
            mobs_add(['direwolf leader', '10*direwolf'])
            sprint("\n* Meanwhile... *")
            sprint("\nIt is a full and bright moon tonight.")
            sprint("Tonight we shall lay waste to the goblin village.")
            sprint("And take our first step towards conquering The Forest of Jura!")
            sprint("They no longer have protection from that accursed dragon!")

            sprint("\nMaster! The Direwolves are here!")
            game_action(self)

        class _hfunc_attack:
            __subs = subs.attack
            def __init__(self):
                if mobs_cleared():
                    sprint("That takes care of that...")
                    siprint("Probably unwarranted, but now we don't have to worry about them.")
                    naming_mobs()
                elif not mob_status('direwolf leader'):
                    wolf_attack._give_warning._attack_water_blade()

        class _give_warning:
            __subs = ['give them a warning', 'warn direwolves', 'warn wolves', 'give direwolf warning', 'warn them']
            def __init__(self):
                sprint("Stop where you are! Listen up, because I'm only going to say this once!")
                sprint("Acknowledge me as your king, or retreat now and never show yourselves again!")
                sprint('\nOur wolf pack will not be intimidated by a mere slime!')
                sprint("ATTACK!!!")
                siprint("\nIntimidating not working...")
                siprint("Some of the goblins that are using bows are getting a few of them, but it's not enough.")

                if game_cond('steel thread trap'):
                    sprint("\nWhat was that!")
                    sprint("That would be [Steel Thread].")
                    sprint("\nYour tricks will not stop us!")

                siprint("\nSome are still getting past my traps.")
                sprint("\nEnough of this! I will kill you slime!")
                sprint("\nFather! No!")
                if game_cond('steel thread trap'):
                    sprint("\nW-w-what is this! Why can't I move!")
                    sprint("\nThat would be [Steel Thread]!")
                # Without setting up steel thread as defense, the pack leader will kill you!
                else:
                    siprint("\nThat wolf is coming at me way to fast! I have nothing to stop him!")
                    sprint("\nYOU'RE DEAD, YOU SLIME!")
                    sprint("\n*CHOMP*")
                    game_over()
                set_targets('direwolf leader')
                game_action(self)

            class _attack_water_blade:
                __subs = []
                def __init__(self):
                    if not mob_status('direwolf leader'):
                        sprint("No, Dad!")
                        sprint("\nYour leader is dead. Your choice now is fealty or death!")
                        siprint("They're not doing anything now... What are they waiting for? Do they need a leader perhaps?")
                    else:
                        sprint("You're DEAD you puny slime!")
                        siprint("\nHow did he get free!?")
                        game_over()

                    game_action(self)

                class _eat:
                    __subs = subs.eat
                    def __init__(self):
                        sprint("\nMaybe they need a push...")
                        game_action(self)

                    class _mimic_direwolf_leader:
                        def __init__(self):
                            siprint("This skill looks useful!")
                            game_action(self)

                        class _use_coercion:
                            def __init__(self):
                                sprint("HOOWWWLLLLLL!!!!!..........")
                                siprint("I know I said fealty or death, but I'm hoping they would just run away in fear....")
                                dots(5)
                                sprint("HOWWLLLL!!!!......")
                                sprint("\nWE WILL FOLLOW YOU TO THE ENDS OF THE EARTH, MASTER!!!")
                                sprint("\nhuh?")
                                naming_mobs()

    class naming_mobs:
        def __init__(self):
            tbc()
            pass

    goblin_encounter()
