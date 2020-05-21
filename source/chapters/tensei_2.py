from start_game import *

def Chapter2(rimuru):

    def StartChapter2():
        sprint("Oh, what's this? Looks like some kind of ore.")
        ActionMenu(['*Eat ore', '*Move on'], 
                    [['eat ore'], ['move on']],
                    [EatOre, MoveOn])


        sprint("Now with magic perception I can finally find my way out of this cave")
        sprint("***But before finding the exit, some small monsters started taking a interest in the little slime***")











    def EatOre():
        rimuru.AddInventory(items.Magic_Ore())
        ssprint("<<Answer, analysis shows this is the raw form of Magic Steel. Can be used for crafting weapons, armor, etc.>>")
        sprint("Ayy, neato. Guess I should get as much as I can")

    def MoveOn():
        sprint("pass")


    StartChapter2()

