from start_game import *
def Chapter3(rimuru):
    def StartChapter3():

        ActionMenu(['*Use Sticky Thread', '*Explore'],
                [['use sticky thread'], ['explore']],
                [StickySwing1, Explore])

        ssprint("*While practicing pronunciation with [Ultrasound Waves]. A pack of Star Wolfs shows up*")
        ssprint("Was I that loud... Eh? Where are those wolves going? What's this...")
        sprint("You strong one.")
        ssprint("Wait, are those... Goblins? Also, How can I understand them?")
        ssprint("<<Answer, [Magic Perception] converts sound waves to comprehensible sentences.>>")
        ssprint("<<Also, sound waves can also be used to communicate your thoughts.>>")

        ActionMenu(['*Speak to Goblins', '*Chase Wolves', '*Run'],
                [['speak to goblins'], ['chase wolves'], ['run']],
                [Goblins, Wolves, Run])
        ssprint("Is that so, let's try that.")




    # ========== Goblins 
    def Goblins():
        ActionMenu(['*Friendly', '*Mad', '*Coerce', '*Attack'],
                [['friendly'], ['mad'], ['coerce'], ['attack #$%']],
                [FriendlyGoblin, MadGoblin, CoerceGoblin, AttackGoblin])

        sprint("HELLO, I'M A SLIME. MY NAME IS RIMURU")
        sprint("...")
        sprint("Strong one we have already recognized your strength. Please, lower your voice!")
        ssprint("Oh. I guess my thoughts were to loud?")
        sprint("Sorry, I am still adjusting.")
        sprint("T-There is no need to apologize strong one!")
        sprint("Ok, I wasn't planning on doing anything ahead of here. Is there anything you need from me?")
        sprint("No, that is our village ahead of here. We felt a strong demonic aura and decided to immediately investigate.")
        ssprint("Demonic aura? where?")
        sprint("I didn't feel.")

    def FriendlyGoblin():
        pass

    def MadGoblin():
        pass

    def CoerceGoblin():
        pass

    def AttackGoblin():
        pass


    # ========== Wolves
    def Wolves():
        pass


    # ========== Run
    def Run():
        pass


    def StickySwing1():
        ssprint("Swinging from tree to tree with [Sticky Thread] seems to be a pretty effective way to travel.")

    def StickySwing2():
        sprint("Weeeeee")

    def Explore():
        sprint("Where am I going?")


    StartChapter3()

