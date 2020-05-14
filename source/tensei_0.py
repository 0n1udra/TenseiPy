
from items import *
from skills import *
from character import *


# ASCII Art
import slimeArt

debug = True
if debug:
    usrInpDebug = True
    def sleep(x): pass
    #ascii.great_sage, ascii.slime = 'GREAT_SAGE', 'SLIME'
    t2 = t3 = t4 = t5 = t6 = 0
else:
    usrInpDebug = False
    from time import sleep
    t2, t3, t4, t5, t6 = 2, 3, 4, 5, 6  # Custom Sleep times


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
    print(Msg)
    sleep(sTime)

# <MSG> -- Acquired item, etc
# <<MSG>>  --  Great Sage (Raphael, Ciel)
# <<<MSG>>>  --  Voice of the World


def RunFuncs(msg, actions, funcs):
    if usrInpDebug:
        usrInp = actions[0][0]
    else:
        print("\nAvailable Actions:", msg, '| stats(attributes), inv(entory), info <skill/obj>, exit')
        usrInp = input("\n> ").lower()

    ### Get info on skills, times, etc
    if 'info' in usrInp:
        try:
            inputSkill = ' '.join(usrInp.lower().split()[1:])
            # Can only get info if item exist in rimuru characte
        except:
            print("NOTE: info Usage example (case sensitive): info predator")
        rimuru.ShowInfo(inputSkill, rimuru)

    contGame = False
    for i in range(len(funcs)):
        for j in actions[i]:
            if usrInp == j:
                if i == 0:
                    funcs[i]()
                    contGame = True
                    break
                else:
                    funcs[i]()
                    contGame = False

    if not contGame:
        RunFuncs(msg, actions, funcs)
    else:
        return

def ActionMenu(msg, actions, funcs):
    actions.extend([['stat', 'stats', 'attributes', 'attrs', 'attr'], ['storage', 'inventory', 'inv', 'stomach'], ['stop', 'exit', 'quit']])
    funcs.extend([rimuru.ShowAttributes, rimuru.showInventory, ExitGame])
    RunFuncs(msg, actions, funcs)

def ExitGame():
    exit()

def TBC():
    print("---TO BE CONTINUED---")


rimuru = Rimuru_Tempest()
