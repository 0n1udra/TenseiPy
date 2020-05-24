from start_game import *

def Chapter2(rimuru):

    def StartChapter2():
        sprint("Oh, what's this? Looks like some kind of ore.")
        ActionMenu(['*Eat ore', '*Move on'], 
                    [['eat ore'], ['move on']],
                    [EatOre, MoveOn])


        sprint("Now with magic perception I can finally find my way out of this cave")
        sprint("*But before finding the exit, some small monsters started taking a interest in the little slime*")


        sprint("Whoa. It looks like a giant snake serpent thing with big fangs. Or am I just small?")
        sprint("I don't think I have any ways to attack or damage it if it's hostile. Hmmmmmm. I wonder")

        ssprint("<Choose ability to learn and use on serpent>")
        ActionMenu(["*Water Blade Serpent", "*Water Bullet Serpent"],
                    [["water blade serpent"], ['water bullet serpent']],
                    [LearnWaterBlade, LearnWaterBullet])
        

        sprint("Wow, what a powerful attack. I probably shouldn't use that so openly")

        ActionMenu(['*Predate Serpent', '*Move on'],
                    [['predate serpent'], ['move on']],
                    [PredateSerpent, MoveOn])



        #DeleteGame(rimuru)

    def PredateSerpent():
        sprint("Eww. I might as well predate it, see if I get anything out of it")
        rimuru.AddMimicry(characters.Tempest_Serpent())


    def MoveOn():
        sprint("I'll just leave it I guess, and continue finding my way out")


    def LearnWaterBlade():
        rimuru.AddAttribute(skills.Water_Blade())
        sprint("Hey, it worked. Since I already have [Hydraulic Propulsion], I was thinking I could use high pressure water as an attack also")

    def LearnWaterBullet():
        rimuru.AddAttribute(skills.Water_Bullet())
        sprint("Nice, it worked. After learning [Hydraulic Propulsion], I was thinking I could use water as an attack also")


    def EatOre():
        rimuru.AddInventory(items.Magic_Ore())
        ssprint("<<Answer, analysis shows this is the raw form of Magic Steel. Can be used for crafting weapons, armor, etc.>>")
        sprint("Ayy, neato. Guess I should get as much as I can")

    def MoveOn():
        sprint("pass")


    StartChapter2()

