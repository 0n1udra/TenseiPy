from chapters import *
from items import *
from character import *
import pickle as p
import slime_art

class Game_Saves():
    def __init__(self):
        self.gameProgress = [Chapter1]

    def LoadGame(self):
        global rimuru
        try:
            playerSave = p.load(open('chapters/player_save.p', 'rb'))
        except: pass

        print()
        try:
            rimuru = playerSave.rimuru
            print("INFO: Loaded game save")
        except:
            rimuru = Rimuru_Tempest()
            print("INFO: Creating new game save")

        try:
            self.gameProgress = playerSave.gameProgress
            print("INFO: Continuing story")
        except:
            print("INFO: Starting at beginning")
        print()
        return rimuru

    def SaveGame(self):
        pass
    

    def SaveDelete(self):
        pass


if __name__ == '__main__':
    currentGame = Game_Saves()
    currentGame.gameProgress[0] = Chapter1
    currentGame.gameProgress[0]()


