import characters, skills, items, slime_art 
import chapters.tensei_1 as tensei1
import pickle, sys, os
from time import sleep

usrInpDebug = False

#                    ========== Game Input ==========
def RunFuncs(msg, actions, funcs):
    if usrInpDebug: 
        usrInp = actions[0][0]
    else:
        # Adds () around actions, (*action)
        options = ', '.join('(' + i + ')' for i in msg)
        mimic = characters.rimuru.mimicking
        try:
            targets, = ', '.join([(i.name if i.alive else f'{i.name}(Dead)') for i in characters.rimuru.focusTargets]), 
        except:
            targets = None

        if targets:
            print(f'\nTarget:', str(targets))
            print(f'Actions:', options, f'| {mimic}, (stats, inv, help)')
        else:
            print("\nActions:", options, f'| {mimic}, (stats, inv, help)')
        usrInp = input("\n> ").lower()
        print()

    loop = True
    attacked = attackSuccess = skillSuccess = False
    # Get info on skills, times, etc
    splitInput = ' '.join(usrInp.split()[1:])
    gameActions = {
            'info': characters.rimuru.ShowInfo,
            'stats': characters.rimuru.ShowAttributes,
            'target': characters.rimuru.SetTarget,
            'predate': characters.rimuru.PredateTarget,
            'mimic': characters.rimuru.CanMimic, 
            }

    for k, v in gameActions.items():
        if k in usrInp:
            v(splitInput)

    if 'use' in usrInp:
        skillSuccess = characters.rimuru.UseSkill(splitInput)
    if 'attack' in usrInp:
        splitInput = ' '.join(usrInp.split()[1:])
        attacked, attackSuccess = characters.rimuru.CanAttack(splitInput)
    try: pass
    except: pass

    # If action has *, continues story
    for i in range(len(funcs)):
        contAction = ''
        for j in actions[i]:
            try:
                contAction = msg[i][0]
            except: pass
           # Checks if valid command
            if usrInp.lower() == j.lower():
               # Checks if command continues story
                if contAction == '*':
                    funcs[i]()
                    loop = False
                    characters.rimuru.lastCommand = usrInp
                    break
                else:
                    funcs[i]()
                    characters.rimuru.lastCommand = usrInp
        if skillSuccess:
            funcs[0]()
            loop = False
        elif attacked and not attackSuccess:
            funcs[1]()
        elif attacked and attackSuccess:
            funcs[0]()
            loop = False

        if not loop: break
    else: 
        RunFuncs(msg, actions, funcs)

def ActionMenu(msg, actions, funcs):
    actions.extend([['help'], ['inv'], ['exit']])
    funcs.extend([ShowHelp, characters.rimuru.ShowInventory, ExitGame])
    RunFuncs(msg, actions, funcs)

def ShowHelp():
    print("""
    Commands:
        target TARGET(s)            -- Target commands and abilities. E.g. 'target tempest serpent'
        attack <TARGET> with SKILL  -- Attack optional target(s) with skill(s). E.g. 'attack with water blade', tempest serpent with water blade
          - Multiple targets and/or attacks separated by comma. E.g. 'attack tempest serpent, black spider with water blade, poisonous breath'
        use SKILL(s)                -- Use skill/items. E.g. 'use sense heat source'
        stats                       -- Show yours skills and resistances. 
          - stats TARGET            -- Stats for monsters you have predated. E.g. 'stats tempest serpent'
        inv                         -- Show inventory.
        info                        -- Show info on skill, item or character. E.g. 'info great sage, 'info hipokte grass', 'info tempest serpent'
        help                        -- Show this help page.
        exit                        -- Exit game.

    Abilities:
        mimic ___                   -- Mimics appearance of of predated. E.g. 'mimic tempest serpent'
          - info mimic              -- Shows available mimicries.
          - mimic reset             -- Resets mimic (Back to slime)
        predate <TARGET(s)>         -- Predate target(s). Can be used with 'target' command. E.g. 'predate', 'predate magic ore', 'predate giant bat, black spider'
        
    Game Dialogue:
        ~Message~                   -- Telepathy
        *Message*                   -- Story progression
        <Message>                   -- Acquired item, information, etc
        <<Message>>                 -- Great Sage (Raphael, Ciel)
        <<<Message>>>               -- Voice of the World

    HUD:
        Target: Currently Focused Target(s)
        Actions: (ACTION(s)) | MIMIC, (Extra Actions)
      E.g.
        Target: Giant Bat, Black Spider
        Actions: (*Attack), (*Move on) | Tempest Serpent, (stats, inv, help)

    Level/Ranking:
       Level      Rank         Risk
        11.     Special S   Catastrophe
        10.     S           Disaster
        9.      Special A   Calamity
        8.      A+          Tragedy
        7.      A           Hazard
        6.      A-          Danger
        5.      B           Pro
        4.      C           Advance
        3.      D           Intermediate
        2.      E           Beginner
        1.      F           Novice
    """)

#                    ========== Extra ==========
def ExitGame():
    exit()

def TBC():
    print("---TO BE CONTINUED---")
    input("Press Enter to exit > ")


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
    if characters.rimuru.textDelay:
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
        rimuru.textDelay = False
    else:
        print("Text Delay: ENABLED")
    rimuru.textDelay = False
    sleep(1)
    print("\n\n")

    rimuru.storyProgress[0] = tensei1.Chapter1
    rimuru.storyProgress[-1](rimuru)
