from start_game import *

def Chapter2(rimuru):

    serpent = characters.Tempest_Serpent()

    def StartChapter2():
        sprint("Oh, what's this? Looks like some kind of ore.")
        ActionMenu(['*predate ore', '*Move on'], 
                    [['predate ore'], ['move on']],
                    [PredateOre, MoveOn])

        sprint("Now with magic perception I can finally find my way out of this cave.")
        sprint("*But before finding the exit, some small monsters started taking a interest in the little slime.*")


        sprint("Whoa. It looks like a giant snake serpent thing with big fangs. Or am I just small?")


        sprint("I don't think I have any ways to attack or damage it if it's hostile. Hmmmmmm. I wonder...")

        ssprint("<Choose ability to learn and use on serpent>")

        ActionMenu(["*Water Blade", "*Water Bullet"],
                    [["water blade"], ['water bullet']],
                    [LearnWaterBlade, LearnWaterBullet])

        sprint("Alright, lets try out this new skill.")

        attackSuccess = ActionMenu(['*Attack with ___',],
                    [['attack with aspoijf'], []],
                    [AttackSerpent, FailedSerpent], serpent)




        sprint("I wonder what else is in this cave.")


        #DeleteGame(rimuru)


    def AttackSerpent():
        sprint("Wow, what a powerful attack. I probably shouldn't use that so openly.")

        attackSuccess = ActionMenu(['*Predate Serpent', '*Move on'],
                        [['predate serpent'], ['move on']],
                        [PredateSerpent, MoveOn])
    def FailedSerpent():
        sprint("Uh, How did that not work...")

        attackSuccess = ActionMenu(['*Attack with ___'],
                    [['attack with ;lkjp'], []],
                    [AttackSerpent, FailedSerpent], serpent)

    def PredateSerpent():
        sprint("Eww. I might as well predate it, see if I get anything out of it")
        rimuru.AddMimicry(characters.Tempest_Serpent())


    def MoveOn():
        sprint("I'll just leave it I guess, and continue finding my way out")

    def LearnWaterBlade():
        rimuru.AddAttribute(skills.Water_Blade())
        sprint("Hey, it worked. Since I already have [Hydraulic Propulsion], I was thinking I could use high pressure water as an attack also.")

    def LearnWaterBullet():
        rimuru.AddAttribute(skills.Water_Bullet())
        sprint("Nice, it worked. After learning [Hydraulic Propulsion], I was thinking I could use water as an attack too.")


    def PredateOre():
        rimuru.AddInventory(items.Magic_Ore())
        ssprint("<<Answer, analysis shows this is the raw form of Magic Steel. Can be used for crafting weapons, armor and etc.>>")
        sprint("Ayy, neato. Guess I should get as much as I can")

    def MoveOn():
        sprint("pass")


    StartChapter2()

