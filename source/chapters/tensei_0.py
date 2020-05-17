from skills import *
from run import rimuru

print("----------Tensei Shitara Slime Datta Ken (That Time I Got Reincarnated as a Slime)----------\n")

# ========== Debug ========== debug = False
debug = False
if debug:
    usrInpDebug = False
    def sleep(x): pass
    #ascii.great_sage, ascii.slime = 'GREAT_SAGE', 'SLIME'
    t2 = t3 = t4 = t5 = t6 = 0
else:
    usrInpDebug = False
    from time import sleep
    t2, t3, t4, t5, t6 = 1, 2, 3, 4, 4  # Custom Sleep times

    # Lets user choose to disable text delay, without breaking debug code
    print("Disable text delay?")
    setSleep = str(input("(Y)es/(N)o > "))
    if setSleep.lower() in ['yes', 'y']:
        t2 = t3 = t4 = t5 = t6 = 0
    else: pass


# ========== Print ==========
def sprint(Msg):
    msgLen = len(str(Msg))
    if msgLen > 70:
        sTime = t6
    elif msgLen > 60 and msgLen > 70:
        sTime = t5
    elif msgLen > 50 and msgLen > 40:
        sTime = t4
    elif msgLen > 40 and msgLen > 20:
        sTime = t3
    elif msgLen < 10:
        sTime = t2
    else:
        sTime = t2
    print(Msg, '\n')
    sleep(sTime)

def ssprint(Msg):
    sprint(f'    {Msg}')


# ========== Input ==========
def RunFuncs(msg, actions, funcs):
    if usrInpDebug: 
        usrInp = actions[0][0]
    else:
        # Adds () around actions, (*action)
        options = ', '.join('(' + i + ')' for i in msg)
        print("\nAvailable Actions:", options, '| inv, stats, help')
        usrInp = input("\n> ").lower()
        print()

    ### Get info on skills, times, etc
    if 'info' in usrInp:
        try:
            inputSkill = ' '.join(usrInp.lower().split()[1:])
            # Can only get info if item exist in rimuru characte
        except:
            print("NOTE: info Usage example: info great sage")
        rimuru.ShowInfo(inputSkill)

    # If action has *, continues story
    contGame = False
    for i in range(len(funcs)):
        contAction = ''
        for j in actions[i]:
           try:
               contAction = msg[i][0]
           except: pass
           if usrInp == j.lower():
               if contAction == '*':
                   funcs[i]()
                   contGame = True
                   break
               else:
                   funcs[i]()
                   contGame = False
        if contGame: break
    if contGame: return
    else: 
        RunFuncs(msg, actions, funcs)

def ActionMenu(msg, actions, funcs):
    actions.extend([['help'], ['stats'], ['inv', 'stomach'], ['exit']])
    funcs.extend([ShowHelp, rimuru.ShowAttributes, rimuru.ShowInventory, ExitGame])
    RunFuncs(msg, actions, funcs)

def ShowHelp():
    print("""
    Commands:
        inv   -- Show inventory
        stats -- Show skills and resistances
        info  -- Show info on skill or item. ex. info great sage
        help  -- Show this help page
        exit  -- Exit game

    Game Dialogue:
        *Message*       -- Telepathy
        <Message>       -- Acquired item, etc
        <<Message>>     -- Great Sage (Raphael, Ciel)
        <<<Message>>>   -- Voice of the World
    """)
def ExitGame():
    exit()

def TBC():
    print("---TO BE CONTINUED---")

    
