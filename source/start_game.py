import characters, skills, items, slime_art
import chapters.tensei_1 as tensei1
import pickle, sys, os
from time import sleep

usrInpDebug = False


#                    ========== Game Saves ==========
def LoadGame(path):
    global rimuru
    try:
        rimuru = pickle.load(open(path, 'rb'))
        print("Loaded Player Save\n")
    except: 
        rimuru = characters.Rimuru_Tempest()
    return rimuru

def SaveGame(rimuru):
    pickle.dump(rimuru, open(characters.rimuru.savePath, 'wb'))
    print("Game Saved To: player_save.p")

def DeleteGame(rimuru):
    try:
        os.remove(rimuru.savePath)
        print("Resetting Game. Deleted player_save.p")
    except: pass

def ContinueStory(rimuru, nextChapter):
    print("Continue to next chapter?")
    usrInp = input("Y/N > ")
    if usrInp.lower() == 'y':
        characters.rimuru.storyProgress.append(nextChapter)
        SaveGame(rimuru)
        nextChapter(rimuru)
    else:
        characters.rimuru.storyProgress.append(nextChapter)
        SaveGame(rimuru)
        exit()

#                    ========== Game Functions ==========
def StartBanner():
    print("\n----------Tensei Shitara Slime Datta Ken (That Time I Got Reincarnated as a Slime)----------\n")
    instructions = """
    NOTE: 
    - Set window size for ASCII art accordingly (Fullscreen recommended)
    - Access help, inventory and skills with help, inv and stats
    - * actions continues story (do NOT actually input *, or ()). Try the other actions first maybe, see what happens
    - Delete player_save.p to reset game progress (includes player inventory and skills)
    """
    print(instructions)
    characters.rimuru.ShowAttributes()
    characters.rimuru.ShowInventory()
    print()

# ========== Printing
def sprint(Msg):
    msgLen = len(str(Msg))
    if not characters.rimuru.textDelay:
        if msgLen > 100:
            sTime = 1
        elif msgLen > 70 and msgLen > 80:
            sTime = 4
        elif msgLen > 50 and msgLen > 40:
            sTime = 3
        elif msgLen > 40 and msgLen > 20:
            sTime = 2
        elif msgLen < 10:
            sTime = 2
        elif msgLen < 5:
            sTime = 1
        else: sTime = 1
    else:
        sTime = 0

    print(Msg, '\n')
    sleep(sTime)

def ssprint(Msg):
    sprint(f'    {Msg}')


#                    ========== Game Input ==========
def RunFuncs(msg, actions, funcs):
    if usrInpDebug: 
        usrInp = actions[0][0]
    else:
        # Adds () around actions, (*action)
        options = ', '.join('(' + i + ')' for i in msg)
        print("\nActions:", options, f'| {characters.rimuru.mimic}, inv/stats, help')
        usrInp = input("\n> ").lower()
        print()

    ### Get info on skills, times, etc
    if 'info' in usrInp:
        try:
            inputSkill = ' '.join(usrInp.lower().split()[1:])
            # Can only get info if item exist in rimuru characte
        except:
            print("NOTE: info Usage example: info great sage")
        characters.rimuru.ShowInfo(inputSkill)

    splitInput = ' '.join(usrInp.split()[1:])
    elif 'mimic' in usrInp:
        characters.rimuru.CanMimic(splitInput)
    elif 'attack with' in usrInp:
        characters.rimuru.CanAttack(splitInput[1:])
    elif 'predate' in usrInp:
        characters.rimuru.CanPredate(splitInput)


    # If action has *, continues story
    contGame = False
    for i in range(len(funcs)):
        contAction = ''
        for j in actions[i]:
           try:
               contAction = msg[i][0]
           except: pass
           # Checks if valid command
           if usrInp == j.lower():
               # Checks if command continues story
               if contAction == '*':
                   funcs[i]()
                   contGame = True
                   characters.rimuru.lastCommand = usrInp
                   break
               else:
                   funcs[i]()
                   characters.rimuru.lastCommand = usrInp
                   contGame = False
        if contGame: break
    if contGame: return
    else: 
        RunFuncs(msg, actions, funcs)

def ActionMenu(msg, actions, funcs):
    actions.extend([['help'], ['stats'], ['inv', 'stomach'], ['exit']])
    funcs.extend([ShowHelp, characters.rimuru.ShowAttributes, characters.rimuru.ShowInventory, ExitGame])
    RunFuncs(msg, actions, funcs)

def ShowHelp():
    print("""
    Commands:
        inv             -- Show inventory
        stats           -- Show skills and resistances
        info            -- Show info on skill, item or character. Ex. info great sage, info hipokte grass, info veldora
        help            -- Show this help page
        exit            -- Exit game

    Abilities:
        mimic <___>     -- Mimics appearance of already predated being. Ex. mimic tempest serpent
          - info mimic  -- Shows available mimicries. Use info to get monster abilities, Ex. info Tempest Serpent
        
    Game Dialogue:
        ~Message~       -- Telepathy
        *Message*       -- Story progression
        <Message>       -- Acquired item, etc
        <<Message>>     -- Great Sage (Raphael, Ciel)
        <<<Message>>>   -- Voice of the World
    """)

#                    ========== Extra ==========
def ExitGame():
    exit()

def TBC():
    print("---TO BE CONTINUED---")
    input("Press Enter to exit > ")

if __name__ == '__main__':
    # Get file path depending on Windows or not
    savePath = os.path.dirname(os.path.abspath(__file__)) + '/player_save.p'

    rimuru = characters.UpdateCharacter(LoadGame(savePath))
    rimuru.savePath = savePath
    StartBanner()

    print("\nDisable text delay? (Recommend leaving enabled for easier reading)")
    setSleep = str(input("(Y)es/(N)o > "))
    if setSleep.lower() in ['yes', 'y']:
        print("Text Delay: DISABLED")
    else:
        rimuru.textDelay = False
        print("Text Delay: ENABLED")
    sleep(1)
    print("\n\n")

    rimuru.storyProgress[0] = tensei1.Chapter1
    rimuru.storyProgress[-1](rimuru)
