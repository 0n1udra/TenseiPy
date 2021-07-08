import game_files.functions as game
import game_files.extra as extra
from game_files.output import gprint, sprint, siprint, idots, dots, show_art
from game_maps.game_location import subs


def ch2_goblin_encounter(rimuru):
    class goblin_encounter:
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
            else:
                sprint("By the way chief, what your name?")
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
            siprint("<< Notice, estimated time for recovery is three days. >>\n")

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
                if game.conditions('tamed direwolves'):
                    siprint("I wonder if I can scare them away somehow...")
                    siprint("Wait! I think Direwolves have a skill like that...")
                else:
                    siprint("Maybe I can use a skill to attack to show my power without directly targeting them to scare them off.")

        class _attack:
            def __init__(self):
                # Kill the bandits and you go straight to Dwargon jail, and no you can't eat the humans.
                if game.mobs_cleared():
                    sprint("My lord... Was that really necessary? Oh crap here comes the guards!\n")
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
                    siprint("We decided to go back to our group and spend the night just outside the gate and try again tomorrow.\n")
                    dots(25)
                    inside_dwargon()

        class _hfunc_use:
            def __init__(self):
                if game.last_use_skill('coercion'):
                    sprint("HOWWWLLLLLLLLLL!!!!!!!!!!!!")
                    siprint("Hopefully this scares them away.\n")
                    idots(30)
                    dwargon_jail_coercion()
                if game.last_use_skill('water blade'):
                    if extra.get_random(1, 3, 1):  # 1/3 chances, can do it multiple times to try and scare them off.
                        sprint("\nL-lets get out of here, they're not worth our time.")
                        sprint("Finally, they're gone, and nobody got hurt.")
                        sprint("\nMy lord you did it! They won't be troubling us anymore.")
                        sprint("\nFinally, we can go into dwargon with no trouble. Not the best first impression, but at least nobody got hurt.")
                        inside_dwargon()
                    else:
                        if extra.get_random(1, 3, 1):  # 1/3 chance they will charge at you to kill you.
                            sprint("\nYou think you can scare us so easily!")
                            siprint("\nCrap now their charging straight for us with a knife!")
                            sprint("\nMy lord what should we do!")
                            game.actions(self)
                        else:
                            sprint('\nYou think that will scare us you puny slime!')

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

    class dwargon_jail_coercion:
        def __init__(self):
            game.clear_all()
            siprint("\n...First time here and we're already in jail...")
            siprint("I didn't think just screaming would cause so much damage to the environment and the nearby people.")
            siprint("I guess my mimicry evolved with $Ranga$'s evolution.")

    class dwargon_jail_murder:
        def __init__(self):
            game.clear_all()
            siprint("\n...... Since I kinda just murdured two bandits in cold blood, we landed ourselves in jail...")
            siprint("This journey sure is going well...")
            sprint("\nI thought my lord would have more self restraint.")
            sprint("Shut it $Gobta$.")

    class inside_dwargon:
        def __init__(self):
            game.clear_all()
            sprint("\nFinally! We made it inside!")

    welcome_to_dwargon()
    #goblin_encounter()
