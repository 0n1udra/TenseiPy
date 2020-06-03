from start_game import *
from chapters.tensei_3 import Chapter3

def Chapter2(rimuru):


    def StartChapter2():
        sprint("Oh, what's this? Looks like some kind of ore.")
        ActionMenu(['*Predate Magic Ore', '*Move on'], 
                    [['predate magic ore'], ['move on']],
                    [PredateOre, MoveOn])

        ssprint("<<Information, analysis shows this is the raw form of Magic Steel. Can be used for crafting weapons, armor, etc.>>")
        sprint("Ok, might be useful in the future. Guess I should get as much as I can")

        sprint("Now with magic perception I can finally find my way out of this cave.")
        sprint("*But before finding the exit, some small monsters started taking a interest in the little slime.*")


        sprint("Whoa. It looks like a giant snake serpent thing with big fangs. Or am I just small?")
        ssprint("<<Answer, this is a Tempest Serpent.>>")
        sprint("Still, it's not as scary as Veldora. I should be able to handle it.")

        sprint("However, I don't think I have any ways to attack or damage it if it's hostile. Hmmmmmm. I wonder...")

        ssprint("<Choose ability to learn and use on tempest serpent>")

        ActionMenu(["*Water Blade", "*Water Bullet"],
                    [["water blade"], ['water bullet']],
                    [LearnWaterBlade, LearnWaterBullet])

        AddMob('tempest serpent')

        sprint("Alright, lets try out this new skill.")
        ssprint("<Target the Tempest Serpent, then attack with your new skill. 'help' for more info.>")

        ActionMenu(['*Attack ___'],
                [['attack :#%^@']],
                    [AttackSerpent], FailedSerpent)

        sprint("I wonder what else is in this cave.")

        AddMob(['giant bat', 'black spider', 'evil spider'])

        ssprint("<Use [Predator]'s mimic and tryout Tempest Serpent's [Sense Heat Source].>")
        ActionMenu(['*Use Sense Heat Source', 'Predate Magic Ore', '*Move on'],
                [['use :$%^'], ['predate magic ore'], ['*move on']],
                [UseSense, PredateOre, StoryContinues])

        sprint("Are those bats?")
        ssprint("<<Answer, They are called Giant Bat.>>")

        ActionMenu(['*Attack ___'],
                    [['attack $$"%']],
                    [AttackBat], FailBat)

        if CheckStatus('giant spider'):
            sprint("What now...A Spider. Nobody likes spiders, especially giant ones.")
            ssprint("<<Information, These are called Giant Spider.>>")
        
            ActionMenu(['*Attack ___', '*Move on'],
                    [['attack $%:$%$'], ['move on']],
                    [AttackSpider, MoveOn], FailSpider)

        if CheckStatus('evil centipede'):
            sprint("For real, now a centipede. I just want to get out of this cave already.")
            ssprint("<<Information, Analysis shows this a Evil Centipede.>>")


            ActionMenu(['*Attack ___', '*Move on'],
                    [['attack $%:$%$'], ['move on']],
                    [AttackCentipede, MoveOn], FailCentipede)

        ActionMenu(['*Find exit', 'Predate Magic Ore'],
                [['find exit'], ['predate magic ore']],
                    [Wonder, PredateOre])

        sprint("Finally! Found the exit. Wow, that's a pretty big door. How am I going to open that?")
        sprint("Water attack? No, that'll probably be overkill. Wait somethings happening.")
        sprint("*The giant pair of doors slowly creeks open, and three adventurers shows themselves.*")
        sprint("What should I do... I can wait and try to sneak past them if they're going in")
        sprint("Adventurer 1: Phew, it's finally open, even the keyhole was rusted.")
        sprint("Adventurer 2: It is over 300 years old, and nobody is maintaining it. I doubt there's a real dragon in here.")
        sprint("Adventurer 2: Still reckless of the guildmaster to send us to investigate.")
        sprint("I shouldn't show, they'll probably get scared and attack me")

        ActionMenu(['*Exit cave', '*Say hi'],
                [['exit cave'], ['say hi']],
                [ExitCave, SayHi])
        


    # ========== Exit Cave
    def ExitCave():
        sprint("Finally! I'm out of that cave. Where now to though?")
        ContinueStory(rimuru, Chapter3)

    def FailSlime():
        if CheckHas('veldora'):
            ssprint("*After the little slime died. All of his stomach contents spewed outwards.*")
            ssprint("*Unfortunately this particular slime had somehow absorbed a dragon locked in [Infinity Prison].*")
            ssprint("*The three adventurers where crushed by such a massive object. They Have failed there simple mission*")
        DeleteGame(rimuru)

    def SayHi():
        sprint("HELLO THERE!")
        sprint("Adventurers: AHHHHH MONSTER. KILL IT. KILL IT. KILL IT!!!!")
        sprint("WAIT, Wait. I'm a friendly slime! Slurrrr.....")
        ssprint("*The adventurers attacked and killed the little slime monster before he could say anything else.*")
        FailSlime()


    def AttackAdventures():
        ssprint("*The slime's attack did not affect the adventurers at all.*")
        sprint("Adventurers: AHHHHH MONSTER. KILL IT. KILL IT. KILL IT!!!!")
        sprint("Well.... That didn't wor....")
        FailSlime()


    # ========== Evil Centipede 
    def AttackCentipede():
        sprint('Can I please leave now?!')
        ActionMenu(['*Predate', 'Predate Magic Ore', '*Move on'],
                        [['predate'], ['predate magic ore'], ['move on']],
                        [PredateSerpent, PredateOre, MoveOn])
    def FailCentipede():
        sprint("Didn't work, huh...")

    # ========== Black Spider
    def AttackSpider():
        sprint("Took care of that, moving on")
    def FailSpider():
        sprint("Didn't work.")
        ActionMenu(['*Attack ___'],
                [['attack $%:$%$']],
                [AttackSpider], FailSpider)

    # ========== Giant Bat
    def AttackBat():
        sprint("Alright, got it. Now lets see what skills I can learn.")
        ActionMenu(['*Predate', 'Predate Magic Ore', '*Move on'],
                    [['predate'], ['predate magic ore'], ['move on']],
                    [PredateBat, PredateOre, MoveOn])
    def FailBat():
        sprint("That didn't work.")
        ActionMenu(['*Attack ___'],
                    [['attack $$"%']],
                    [AttackBat], FailBat)

    def PredateBat():
        sprint("Now with [Ultrasound Waves] I can communicate with sound, I hope.")

    # ========== Sense heat source
    def UseSense(): 
        sprint("\nThat's a pretty handy skill. Range isn't very far though.")
        
    # ========== Tempest Serpent
    def AttackSerpent():
        sprint("Wow, what a powerful attack. I probably shouldn't use that so openly.")
        ssprint("<<Suggestion, use Unique Skill [Predator] on serpent.>>")
        sprint("Oh...? What will that do?")
        ssprint("<<Answer, after predation and using analysis, it is possible to learn the targets skills.>>")

        ActionMenu(['*Predate', 'Predate Magic Ore', '*Move on'],
                        [['predate'], ['predate magic ore'], ['move on']],
                        [PredateSerpent, PredateOre, MoveOn])

    def FailedSerpent():
        sprint("Uh, How did that not work...")

        ActionMenu(['*Attack ___'],
                [['attack :#@$^']],
                    [AttackSerpent], FailedSerpent)

    def PredateSerpent():
        ssprint("<Use info mimic for mimicry info, and stats/info tempest serpent for info on monster.>")

        ssprint("<Currently only able to use predated monster's skills when using mimicry.>")
        sprint("If I encounter another monster, I should use mimicry and try out those serpent's skills.")

    def MoveOn():
        sprint("I'll just leave it, and continue finding my way out.")

    # ========== Learn Water Blade/Bullet
    def LearnWaterBlade():
        rimuru.AddAttribute(skills.Water_Blade())
        sprint("Hey, it worked. Since I already have [Hydraulic Propulsion], I was thinking I could use super high pressure water as a blade attack also.")

    def LearnWaterBullet():
        rimuru.AddAttribute(skills.Water_Bullet())
        sprint("Nice, it worked. After learning [Hydraulic Propulsion], I was thinking I could use water as an attack too.")

    # ========== Magic Ore 
    def PredateOre(): pass

    def StoryContinues():
        ssprint("Lets keep moving")

    def Wonder():
        sprint("Wondering")
    StartChapter2()

