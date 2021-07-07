import game_files.functions as game
import game_files.extra as extra
from game_files.output import gprint, sprint, siprint, idots, dots, show_art
from game_maps.game_location import subs


def ch2_goblin_encounter(rimuru):
    class goblin_encounter:
        __location = "Near the Sealed Cave"

        def __init__(self):
            game.mobs_reset()
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
                sprint("You have two options. You can worship me or you can die.\n")
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

    class goto_goblin_village:
        __location = "Goblin Village"

        def __init__(self):
            game.mobs_reset()
            game.mobs_add(['goblin:goblin chief', 'goblin'])
            siprint("Wow, this place looks like a dump... Such a primitive house.")
            sprint("\nI am the village elder. I'm sorry we don't have much to offer you.")
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
                    game.conditions('killed goblin chief', True)
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
                        rimuru.update_reputation('goblins', 1)
                        sprint("\n* The slime ate, healed, and spat out the rest of the wounded goblins. *")
                        sprint("\nThere, all healed!")
                        sprint("\nW-w-whoa! You really are magnificent, great one! We thank you!")
                        game.action_playable('_heal_wounded', False)
                    else:
                        siprint("Looks like 9 wounded goblins..... How can I help them?")

    class wolf_attack:
        def __init__(self):
            game.mobs_reset()
            game.mobs_add(['direwolf leader', '10*direwolf'])
            sprint("\n* Meanwhile, the direwolves are getting ready... *")
            sprint("\nTonight we shall lay waste to the goblin village.")
            sprint("And take our first step towards conquering The Forest of Jura!")
            sprint("They no longer have protection from that accursed dragon!")

            sprint("\nMaster! The Direwolves are here!")
            game.actions(self)

        class _hfunc_attack:
            __subs = subs.attack
            def __init__(self):
                if game.mobs_cleared():
                    sprint("That takes care of that...")
                    siprint("Probably unwarranted, but now we don't have to worry about them.")
                    naming_mobs()
                elif not game.mob_status('direwolf leader'):
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
                                rimuru.use_mimic('reset')
                                naming_mobs()

    class naming_mobs:
        def __init__(self):
            siprint("Quite a wild retinue I've built up for myself.")
            siprint("I should probably lay down some rules for everyone to follow.")
            sprint("By the way elder, what your name?")
            sprint("\nMonsters usually don't have names. Not having names do not get in the way of communicating anyways.")
            sprint("\nOk, I see. Still, it would be convenient if I have a way to call you if I need to.")
            sprint("I suppose, I'll just have to give you guys names!")
            sprint("WHAAAAT!!!??? A-are you certain?")
            sprint("\nWhat's the big deal anyways? Everyone get in a line, so I can give you names.")
            dots(5)
            show_art('village elder')
            siprint("What should I name the village elder? He had son named Rigurd, who died protecting this village...")
            rimuru.add_subordinate('goblin', 'Rigurd', level=4)
            sprint("I am honored great one!")
            sprint("\nAlright, next...")
            show_art('rigur')
            siprint("Now... The elder's younger son, the younger brother of the lost Rigurd...")
            rimuru.add_subordinate('goblin', 'Rigur', level=4)
            sprint("Thank you master!")
            show_art('gobta')
            sprint("\nSo, who's next? You seem like a chipper goblin...")
            rimuru.add_subordinate('goblin', 'Gobta', level=4)

            # TODO allow more naming, or add some other functionality to change names....
            siprint("There are so many to name, and I'm running out of ideas...")
            siprint("Alright, the goblins are done. Now for the Direwolves.")
            sprint("You're the son of the Direwolf boss right?")
            show_art('ranga')
            rimuru.add_subordinate('tempest star wolf', 'Ranga')

            siprint("Wait w-what's happening... My [Magic Sense] stopped working!")
            siprint("Why am I so sleepy now? What's happening Great Sage?")
            siprint("<< Answer, going into 'Sleep Mode' due to low magicule levels. >>")
            siprint("I was only giving them names, I didn't know it would use up that much.")
            siprint("<< Notice, estimated time for recovery is three days. >>\n")

            idots(10, 3)

            siprint("\nSo it's been three days already.")
            sprint("\nLord Rimuru you're awake!")
            sprint("\n$Rigurd$ is that you?")
            sprint("\nOf coursed my lord! Now please follow me, the feast is nearly ready.")
            siprint("Wow, it looks lggike almost everyone has changed in some way.")
            sprint("\nAllow me to express my deepest joy at your recovery my lord!")
            sprint("\nIt's $Ranga$! Even he's different. He's so big!")

            sprint("* After the party to celebrate your awakening. *")
            sprint("\nAlright everyone, gather around! I'm going to set some ground rules.")
            sprint("1. No infighting.")
            sprint("2. No discriminating other species.")
            sprint("3. No Attacking Humans.")
            sprint("Also, $Rigurd$ I hereby place in the position of Goblin Lord!")
            #TODO Give player the option to set different rules which will effect story later on
            extra.tbc()

            #game.actions(self)
    goblin_encounter()
