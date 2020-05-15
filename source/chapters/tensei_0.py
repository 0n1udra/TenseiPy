
from items import *
from skills import *
from character import *


# ASCII Art
import slime_art

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
    setSleep = str(input("\n(Y)es/(N)o> "))
    if setSleep.lower() in ['yes', 'y']:
        t2 = t3 = t4 = t5 = t6 = 0
    else:
        pass

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
    print()
    sleep(sTime)

def ssprint(Msg):
    sprint(f'    {Msg}')

# <MSG> -- Acquired item, etc
# <<MSG>>  --  Great Sage (Raphael, Ciel)
# <<<MSG>>>  --  Voice of the World


def RunFuncs(msg, actions, funcs):
    if usrInpDebug:
        usrInp = actions[0][0]
    else:
        print("\nAvailable Actions:", ', '.join(msg), '| stats(attributes), inv(entory), info <skill/obj>, exit')
        usrInp = input("\n> ").lower()
        print()

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
    actions.extend([['stat', 'stats', 'attributes', 'attrs', 'attr'], ['storage', 'inventory', 'inv', 'stomach'], ['stop', 'exit', 'quit']])
    funcs.extend([rimuru.ShowAttributes, rimuru.ShowInventory, ExitGame])
    RunFuncs(msg, actions, funcs)

def ExitGame():
    exit()

def TBC():
    print("---TO BE CONTINUED---")


rimuru = Rimuru_Tempest()
veldora = Veldora_Tempest()
