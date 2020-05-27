from start_game import *

def Chapter2(rimuru):

    serpent = characters.Tempest_Serpent()
    giantBat = characters.Giant_Bat()
    rimuru.currentMobs = [serpent, giantBat]

    def StartChapter2():
        sprint("Oh, what's this? Looks like some kind of ore.")
        ActionMenu(['*predate Magic Ore', '*Move on'], 
                    [['predate magic ore'], ['move on']],
                    [PredateOre, MoveOn])

        ssprint("<<Answer, analysis shows this is the raw form of Magic Steel. Can be used for crafting weapons, armor, etc.>>")
        sprint("Ok, might be useful in the future. Guess I should get as much as I can")

        sprint("Now with magic perception I can finally find my way out of this cave.")
        sprint("*But before finding the exit, some small monsters started taking a interest in the little slime.*")


        sprint("Whoa. It looks like a giant snake serpent thing with big fangs. Or am I just small?")
        sprint("Still, it's not as scary as Veldora. I should be able to handle it.")

        sprint("However, I don't think I have any ways to attack or damage it if it's hostile. Hmmmmmm. I wonder...")

        ssprint("<Choose ability to learn and use on serpent>")

        ActionMenu(["*Water Blade", "*Water Bullet"],
                    [["water blade"], ['water bullet']],
                    [LearnWaterBlade, LearnWaterBullet])

        sprint("Alright, lets try out this new skill.")

        ActionMenu(['*Attack with ___'],
                [['attack with :#%^@'], []],
                    [AttackSerpent, FailedSerpent], serpent)

        sprint("I wonder what else is in this cave.")

        ActionMenu(['*Use Sense Heat Source', 'Predate Magic Ore'],
                [['use :$%^'], ['predate magic ore']],
                [UseSense, PredateOre])

        sprint("Are those bats? I wonder...")

        ActionMenu(['*Attack with ___'],
                [['attack with $%:@'], []],
                    [AttackBat, FailedBat], giantBat)

        #DeleteGame(rimuru)

        ActionMenu(['*Wonder',],
                [['Wonder'], []],
                    [Wonder])

    def Wonder():
        sprint("Wondering")


    # ========== Giant Bat
    def AttackBat():
        sprint("Alright, got it. Now lets see what skills I can learn.")
        attackSuccess = ActionMenu(['*Predate Giant Bat', 'Predate Magic Ore', '*Move on'],
                        [['predate giant bat'], ['predate magic ore'], ['move on']],
                        [PredateBat, PredateOre, MoveOn])

    def FailedBat():
        sprint("That didn't work...")
        ActionMenu(['*Attack with ___'],
                [['attack with $%:@'], []],
                    [AttackBat, failedBat], giantBat)

    def PredateBat():
        rimuru.AddMimicry(giantBat)
        sprint("Now with [Ultrasound Waves] I can communicate with sound, I hope.")

    # ========== Sense heat source
    def UseSense():
        print("OK")
        
    # ========== Tempest Serpent
    def AttackSerpent():
        sprint("Wow, what a powerful attack. I probably shouldn't use that so openly.")
        ssprint("<<Suggestion, use Unique Skill [Predator] on serpent.>>")
        sprint("Oh...? What will that do?")
        ssprint("<<Answer, after predation and using analysis, it is possible to learn the targets skills.>>")

        ActionMenu(['*Predate Tempest Serpent', 'Predate Magic Ore', '*Move on'],
                        [['predate tempest serpent'], ['predate magic ore'], ['move on']],
                        [PredateSerpent, PredateOre, MoveOn])

    def FailedSerpent():
        sprint("Uh, How did that not work...")

        ActionMenu(['*Attack with ___'],
                [['attack with :#@$^'], []],
                    [AttackSerpent, FailedSerpent], serpent)

    def PredateSerpent():
        rimuru.AddMimicry(serpent)
        ssprint("<Use info mimic for mimicry info, and stats/info tempest serpent for info on monster.>")

        ssprint("<Currently only able to use predated monster's skills when using mimicry.>")
        sprint("If I encounter another monster, I should use mimicry and try out those serpent's skills.")

    def MoveOn():
        sprint("I'll just leave it I guess, and continue finding my way out.")

    # ========== Learn Water Blade/Bullet
    def LearnWaterBlade():
        rimuru.AddAttribute(skills.Water_Blade())
        sprint("Hey, it worked. Since I already have [Hydraulic Propulsion], I was thinking I could use super high pressure water as a blade attack also.")

    def LearnWaterBullet():
        rimuru.AddAttribute(skills.Water_Bullet())
        sprint("Nice, it worked. After learning [Hydraulic Propulsion], I was thinking I could use water as an attack too.")

    # ========== Magic Ore 
    def PredateOre():
        rimuru.AddInventory(items.Magic_Ore())


    StartChapter2()

