from character import *
from chapters import *
from items import *
import slime_art
import pickle as p

rimuru = None
def SaveGame(character):
    p.dump(character, open('player_save.p', 'wb'))
    print("Game Saved to: player_save.p")
    
def DeleteSave():
    pass

def LoadGame():
    global rimuru
    if rimuru == None:
        try:
            rimuru = UpdateCharacter(p.load(open('player_save.p', 'rb')))
            rimuru.ShowInventory()
            print("Loaded Player Save\n")
        except:
            rimuru = Rimuru_Tempest()
    return rimuru
LoadGame()

if __name__ == '__main__':
    StartBanner()
    rimuru = LoadGame()
    rimuru.storyProgress[0] = Chapter1
    rimuru.storyProgress[-1](rimuru)


