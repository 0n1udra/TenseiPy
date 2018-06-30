#!usr/bin/python3
# Author: Drake Thomas

import random as rd
import DT_lib as DT

# hides errors
class devNull(): pass
#sys.stderr = devNull()

langOpt = 0
# 0 for normal, 1 for mean(I mean REALLY MEAN)

# leave the text in the lists, because later when the game is finished i'm going to add another version of the text

# ----- Game 0 ----- jump off rock > ask for last words > go to hell or dies..
def game_0():  # jumping off
    falling = [["You're now falling to you're DOOM", "Still falling", "Any last words?"],
               []]
    thanks = [["Thanks, that did nothing", "Falling...Falling...Falling", "SPLAT...you dead!", "GAME OVER"],
              []]
    keywordsToHell = [["dark lord satan, i offer thee my soul", "test", "1"],
                      []]

    DT.clear()
    DT.print_Text(falling, 4)

    inp = str(input("Word(s) > ")) # Any last words?

    if(inp.lower() in keywordsToHell[langOpt]):
        game_0_1() # TOO HELL!
    else:
        DT.print_Text(thanks, 3) # GAME OVER
        QUIT()

# HELL
def game_0_1():
    story = [["You offer to make a pack with Satan to save you're soul", "Now you're going to hell", "HELL LEVEL ",
              "You're now in Hell, and first thing you see is Satan sitting on dark throne",
              "What the hell ya going to do now?"],

             []]
    menuOptions = [["Attempt to sneak away", "Beg for soul back even though you just sold it",
                    "Live for eternity in Hell"],

                   []]

    DT.print_Text(story, 3)
    DT.sleep(3)
    DT.clear()

    # 0 attempt to sneak away, 1, beg for soul, 2 stay for ever.

    DT.print_Back()

    run = []
    inp = input("Soo > ")

    try:
        x = int(inp)
        DT.input_Back(x, start_Menu(), game_1)
        print(x)
        exit()  # TMP.  need working on , so it just quits out for how
    except:
        DT.error()
        game_0_1()

# ----- Game 1 ----- ask rock, ground,
def game_1():  # ask rock to go to ground
    howToAsk = [["How would you like to ask the rock to fly down?"],
                []]
    howToAskOptions = [["nicely", "Rudely", "uhhh", "Bribe"],
                       []]

    gotYouNowhere = [["Well that got you nowhere! "],
                     [""]]
    # Ways to ask rock, and rock responses
    waysTooAsk = [{1: "May you please fly down to the ground, thank you.",
                   2: "Fly down to the ground right now, or I'll spit on  you.",
                   3: "You better fly down there right now or I'm going....... I DON'T KNOW!",
                   4: "I'll give you whatever you want except wanting me staying here.",
                   5: "If then I'll be really sad."},

                  {}]
    rockAnswers = [{1: "OK fine.",
                    2: "I'll drop you from 100 feet if you do.",
                    3: "HAHA",
                    4: "I wish to stay here and you can move to the right 1ft, and you won't be in the same place.",
                    5: "Awww. I guess you'll be sad."},

                   {}]

    DT.clear()
    print("\n", howToAsk[langOpt])
    DT.option_Menu(howToAskOptions)
    DT.print_Back()

    try:
        x = int(input("Choose one > "))
    except:
        game_1()
        x = 0 # TODO fix x var problem

    print("You told the rock:\n", waysTooAsk[langOpt][x])  # you say >
    DT.wait()
    print("The rock says:\n", rockAnswers[langOpt][x])  # rock responds with >
    DT.wait()

    if(x == 1):
        game_1_1() # On the ground
    else:
        DT.input_Back(x, start_Menu, game_1) # Go back or main menu?
        print("\n", gotYouNowhere[langOpt])  # You got nowhere :(
        DT.wait()
        game_1()

# On the ground
def game_1_1():
    story = ["YAY you're on the ground now, so now what?", '']
    menuOptions = [["Go back to rock", ''], []]

    DT.clear()
    print(story[langOpt])

    DT.game_Menu(menuOptions[langOpt])
    DT.print_Back()

    inp = input()
    try:
        inp = int(inp)
    except:
        pass

    if(inp != None): # TODO setup input
        pass
    else:
        DT.input_Back(inp, start_Menu(), game_1)

    DT.wait()
    start_Menu()

# ----- Game 2 ----- yelling > nothing
def game_2():
    youSay = ["You are now yelling at the rock!", '']
    rockSay = ["..................", '']

    print(youSay[langOpt])
    print("The rock responds : ")
    print(rockSay[langOpt]) # ....
    input("That got you nothing, try something else. Enter> ")

    DT.wait()
    start_Menu()

# ----- Game 3 ----- Begging > nothing
def game_3():
    story = []
    menuOptions = [[], []]

    print(story[langOpt])

    DT.game_Menu(*menuOptions[langOpt])

    DT.wait()

# ----- Game 4 ----- Sleep > Dreamworld > ..
timeSlept = 12  # sets timeSlept variable, starts at 12,
# zzZZzz Sleep
def game_4():
    global timeSlept
    DT.clear()
    story = ["You are thinking that you can't get off this rock so you decide to go to bed"
             ""]
    sleeping = ["You're now sleeping",
                ""]
    doneSleeping = ["Hope you rested well",
                    ""]
    sleepingAmount = ["Morning, you slept in total of ",
               ""]
    snoring = [['zz', 'ZzZ', 'ZZzz', 'zzZzZ', 'ZzZzzZ'],
               ['']]

    print(story[langOpt])
    print(sleeping[langOpt])

    # Random number of snoring. Get's longer the more you sleep
    for i in range(5):
        print(snoring[langOpt][rd.randint(len(snoring))] * rd.randint(1, 5) + (timeSlept/2))

    print(doneSleeping)
    DT.sleep(.3)
    print(sleepingAmount[langOpt], timeSlept, "hours")
    DT.wait()

    timeSlept += (12 * 1.2)

    if(timeSlept > 84):
        game_4_1()  # Dream Level
    else:
        DT.clear()
        start_Menu()

# Dream Level
def game_4_1():
    DT.clear()
    story = ["You slept for too long, you are now in a dream!", '']
    story2 = ["Since you slept for too long, you're not trapped in a dream world. whatcha going to do?",
              '']
    menuOptions = [["Go eat the candy", "Find a ginger-bread house", "Find a way out"], []]
    extraText = ["this place look and smell nice, look huge lollipops, rainbows, and candy!", '']

    print(story[langOpt])
    print(story2[langOpt])
    print(extraText[langOpt])

    DT.game_Menu(menuOptions[langOpt])
    inp = input("> ") # TODO Dream Level

######  Menu/Startup/etc        #####################################################################################################################################

# ----- Extra -----
def super_Secret():
    secretMenu = ["Yell for TARDIS", "1", "2"]

    print("Welcome to the super secret, but ain't so secret anymore I guess")
    print("Here are some extra options")
    DT.game_Menu(*secretMenu)

# ----- Quit ----- quit function, prints message and quits game
def QUIT():
    quitText = ["Thanks for playing!", ""]
    input(quitText[langOpt])
    exit()

# Loading screen animation(kinda)
def Loading():
    # loading screen data
    Kirby = ['LOADING ', '<', '(', '^', '.', '^', ')', '>', ' ', '\n:', ')', ' WELCOME']
    DT.loading_Screen(Kirby)

    input("Enter to Continue > ")  # waits for user
    start_Menu()

# Game start menu
def start_Menu():
    Story = ["You are on a floating rock 1000ft above ground, and all that you have is a bed(for some reason), so what do you do",
        '']

    menuOptions = [["Jump off(need work)",
                    "Ask rock to go down(need work)",
                    "Yell at rock(need changing)",
                    "Beg rock to go down(need changing)",
                    "Go to sleep(need work)",
                    "Super Secret Menu!",
                    "Quit"], []]

    extra = {69: ["really!?!?"],
             666: ["HAIL HYDRA!!!"],
             777: ["A blue box well show up soon"]
             }

    DT.clear()
    print("THE STORY\n" + Story[langOpt])

    DT.game_Menu(menuOptions[langOpt]) # for i in range(len(Sm)): print(str(i) + ')', Sm[i])


    run = [game_0, game_1, game_2, game_3, game_4, super_Secret,
           QUIT]
    inp = input("choose > ")

    try:
        inp = int(inp)
    except:
        DT.error()
        start_Menu()  # gives error, then goes back to main menu

    if(inp > 6):
        print(extra[inp])
        start_Menu() # Did you find a secret?
    else:
        run[inp]()

if(__name__ == "__main__"):
    start_Menu()
###################################################################################################################################################