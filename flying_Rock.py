# SETUP#		#########################################################################################################################################

# libraries I use
import random as rd
import DT_S_lib as DT
import colorama as clr
# my personal module i made for, since i use the same functions for other games
# hides errors, puts errors to devNull, which 'pass', does nothing
class devNull(): pass
#sys.stderr = devNull()

langOpt = 0

# leave the text in the lists, because later when the game is finished i'm going to add another version of the text

#       GAME 0-4		####################################################################################################################################

# ----- Game 0 -----
def game_0():  # jumping off
    # Text      -----       -----       -----       -----       -----       -----       #
        # you're falling >  still falling > any last words?
    falling = [["You're now falling to you're DOOM", "Still falling", "Any last words?"],[]]
        # thanks that did nothing > falling..falling > SPLAT > GAME OVER
    thanks = [["Thanks, that did nothing", "Falling...Falling...Falling", "SPLAT...you dead!", "GAME OVER"],[]]
        # keywords to go to Hell. kw = keywords
    keywordsToHell = [["dark lord satan, i offer thee my soul", "test", "1"],[]]
    #       -----       -----       -----       -----       -----       -----       #

    DT.clear()
    for i in range(len(falling[langOpt])):
        print(falling[langOpt][i]) # Prints >> falling to you're DOOM >  still falling > any last words
        DT.sleep(4) # waits for 4 seconds after everytime it loops and prints text

    inp = str(input("Word(s) > ")) # ask for last words before you die

    if inp.lower() in keywordsToHell[langOpt]: # checks if you entered a keyword from the keyword list)
        game_0_1() # if so, it starts the next game
    else:
        for i in range(len(thanks[langOpt])): # if you didn't input keywords it prints..
            print(thanks[langOpt][i]) # Prints >> thanks that did nothing > Falling.. > SPLAT > GAME OVER
            DT.sleep(3) # pauses for 3 seconds every loop

        QUIT() # exits game

def game_0_1():  # in hell
    # Text      -----       -----       -----       -----       -----       -----       #
            # offer soul to Satan > going to hell > HELL LEVEL 1 > you see Satan on his throne > what are you going ot do now?
    story = [["You offer to make a pack with Satan to save you're soul", "Now you're going to hell", "HELL LEVEL ",
           "You're now in Hell, and first thing you see is Satan sitting on dark throne",
           "What the hell ya going to do now?"], []]
            # Hell level input
    menuOptions = [["Attempt to sneak away", "Beg for soul back even though you just sold it",
             "Live for eternity in Hell"], []]
    #       -----       -----       -----       -----       -----       -----       #

    print(clr.Fore.RED)
    for i in range(len(story[langOpt])):
        print(story[langOpt][i])
            # prints all text out red
        DT.sleep(3)
    # going to hell > offer the make a pack > HELL LEVEL

    DT.clear()

    print("\n", story[langOpt][3])  # Now in Hell, see satan.
    print("\n", story[langOpt][4])  # what are you going to do now


    # 0 attempt to sneak away, 1, beg for soul, 2 stay for ever.

    DT.print_Back()

    run = [] # input options
    inp = input("Soo > ")  # input for this level

    try:
        x = int(inp)
        DT.input_Back(x, start_Menu(), game_1)  # runs input_Back function, for if you want to go back to main menu
                        #  1.       2.    1) this is the main menu,  2) this well go back which is Game0
        print(x)
        exit() # TMP.  need working on , so it just quits out for how
    except:
        DT.error()
        game_0_1()

# ----- Game 1 -----
def game_1():  # ask rock to go to ground
    # Text      -----       -----       -----       -----       -----       #
        # asking rock to fly down
            # how to ask rock
    howToAsk = ["How would you like to ask the rock to fly down?", '']
            # Game_1 asking, and responding. y, you, r, rock
    youSaid = ["You told the rock ",'']
    rockSaid = ["The rock says  ",'']
         # Game_1 else response
    gotYouNowhere = ["Well that got you nowhere! ",'']
         # Ways to ask rock, and rock responses
    waysTooAsk =  [{1: "May you please fly down to the ground, thank you",
                      2: "Fly down to the ground right now, or i'll spit on  you",
                      3: "you better fly down there right now or i'm going to whoop you up real good(in a sassy way)",
                      4: "i'll give you whatever you want except wanting me to stay here",
                      5: "if you don't let me down right now i'll kill your family and then you!"},
                   {} ]
    rockAnswers =  [{1: "OK fine",
                       2: "then I'll drop you from 100ft",
                       3: "oh don't you talk to me like that(in a sassy rock way(i guess))",
                       4: "I wish to stay here and you can move to the right 1ft, and you won't be in the same place",
                       5: "Then i'll find you fimaly and murder then and then the human race! MWHAHAHAHAHA!!!"},
                    {} ]
    #       -----       -----       -----       -----       -----       -----       #

    DT.clear()

    print("\n", howToAsk[langOpt])  # How would you like to ask
    print("\n1. nicely, 2. Rudely, 3. Sassy, 4. Bribe, .")
    DT.print_Back()

    try:  # tries to convert the input to a usable integer for this part
        x = int(input("Choose one > "))
        DT.input_Back(x, start_Menu(), game_1)
    except:
        game_1()  # if it fails, it runs this code(Game_1) again

    print(youSaid[langOpt], "\n >> ", waysTooAsk[langOpt][x])  # you say >
    DT.wait()
    print(rockSaid[langOpt], "\n >> ", rockAnswers[langOpt][x])  # rock responds with >
    DT.wait()

    if x == 1: # if you choose option 1 you go to the ground
        game_1_1()  # starts the next game 'Game_1_1'
    else:
        input("\n", gotYouNowhere[langOpt])  # prints got you nowhere
        DT.wait()
        game_1() # re-runs the program(game_1())

def game_1_1():  # on the ground
    # Text      -----       -----       -----       -----       -----       #
        # Story. on ground now
    story = ["YAY you're on the ground now, so now what?", '']
    menuOptions = [["Go back to rock",''],[]]
    #       -----       -----       -----       -----       -----       #

    DT.clear()

    print(story[langOpt])

    DT.game_Menu(*menuOptions[langOpt])
    DT.print_Back()

    inp = input()
    try:
        inp = int(inp)
        DT.input_Back(inp, start_Menu(), game_1)
    except: pass

    DT.wait()
    start_Menu()

# ----- Game 2 -----
def game_2():
    # Text  -----       -----       -----       -----       -----       -----       #
    # now yelling at rock
    youSay = ["You are now yelling at the rock!", '']
    # .............
    rockSay = ["..................", '']
    #       -----       -----       -----       -----       -----       -----       #

    print(youSay[langOpt])  # yelling at rock
    print("The rock responds : ")
    print(rockSay[langOpt])  # .............
    input("That got you nothing, try something else : ")

    DT.wait()
    start_Menu()

# ----- Game 3 -----
def game_3():
    # Text  -----       -----       -----       -----       -----       @
    story = []
    menuOptions = [[], []]
    #       -----       -----       -----       -----       -----       @

    print(story[langOpt])

    DT.game_Menu(*menuOptions[langOpt])

    DT.wait()

# ----- Game 4 -----
timeSlept = 12  # sets timeSlept variable, starts at 12,

def game_4():  # sleeping
    global timeSlept
    DT.clear()
    # Text  -----       -----       -----       -----       -----       #
        # going to bed
    story = ["You are thinking that you can't get off this rock so you decide to go to bed"
             ""]
        # you"re now sleeping
    sleeping = ["You're now sleeping", ""]
        # hope you rested well
    doneSleeping = ["Hope you rested well", ""]
        # morning
    morning = ["Morning, you slept in total of :", ""]
    snoring = [['zz', 'ZzZ', 'ZZzz', 'zzZzZ', 'ZzZzzZ'],[''] ]
        #       -----       -----       -----       -----       -----       #

    print(story[langOpt] + sleeping[langOpt])  # thinking can't get off, your now sleeping

        # random number is to print 'z'(s) in random number of times, just because
    for i in range(5):  # loops the print statment 5 times
        print(snoring[langOpt][i] * rd.randint(1,5)) # prints zz(s) from the list by a random amount

    #	sleep(amount)
    print(doneSleeping)  # rested well message
    DT.sleep(.3)  # pauses for 5secs
    print(morning[langOpt], timeSlept, "hours")  # prints morning message and tells you how long you slept for in total
    DT.wait()

    timeSlept = timeSlept + 12 * 1.2  # adds time to total time slept,
    # ^ every time you sleep, the you longer you sleep. 1.2x longer every time
    if timeSlept > 84: game_4_1()  # if you slept for more then 84 hours, you go to dreamworld
    else:  # else you it goes back to main menu
        DT.clear()
        start_Menu() # go to main menu

def game_4_1():  # dream
    DT.clear()
    # Text      -----       -----       -----       -----       -----       -----       #
        # Dreamworld
            # now in dream world, congrats
    story = ["You slept for too long, you are now in a dream!", '']
            # you're trapped, you slept for too long
    story2 = ["Since you slept for too long, you're not trapped in a dream world. whatcha going to do?",
              '']
    # Dreamworld menu
    menuOptions = [["Go eat the candy", "Find a ginger-bread house", "Find a way out"], []]
        # this looks like a nice place
    extraText = ["this place look and smell nice, look huge lollipops, rainbows, and candy!", '']
    #       -----       -----       -----       -----       -----       -----       @

    print(story[langOpt])  # prints  you slept for too long, now in dreamworld
    print(story2[langOpt])  # since you slept for too long you're stuck in dreamworld
    print(extraText[langOpt])  # extra menu message

    DT.game_Menu(*menuOptions[langOpt])
    inp = input("> ")

######  Menu/Startup/etc		#####################################################################################################################################

# ----- Extra -----
def super_Secret():
    # Text -----        -----       -----       -----       -----       -----       #
    secretMenu = ["Yell for TARDIS", "1", "2"]
    #   -----       -----       -----       -----       -----       -----       @

    print("Welcome to the super secret, but ain't so secret anymore I guess")
    print("Here are some extra options")
    DT.game_Menu(*secretMenu)
    
# ----- Quit -----
def QUIT():
    quitText = ["Thanks for playing!", ""]
    input(quitText[langOpt])
    exit()  # built-in exit function to exit the script, quit() was also a built-in function, until this function overwritten it

def Loading():
    DT.c.resetA()
    # Starts the program, first runs the loading screen, then runs the Start_menu function

    # loading screen data, inputs list to 'loading_Screen' function from DT_S_lib
    Kirby =   ['LOADING ', '<', '(', '^', '.', '^', ')', '>', ' ', '\n:', ')', ' WELCOME']
    # Kirby loading screen items
    DT.loading_Screen(*Kirby)

    input("CONTINUE > ")  # waits until user presses 'Enter'
    start_Menu()

def start_Menu():
    # Text      -----   -----       -----       -----       -----       #
        # Startup menu/Main menu
    Story = ["You are on a floating rock 1000ft above ground, and all that you have is a bed(for some reason), so what do you do", '']
            # Start menu, sm=start menu
    menuOptions = [["Jump off(need work)" ,
          "Ask rock to go down(need work)",
          "Yell at rock(need changing)",
          "Beg rock to go down(need changing)",
          "Go to sleep(need work)",
          "Super Secret Menu!",
          "Quit"], [] ]
            # in the main menu punch in these numbers, it well print these.
    extra = {69: ["really!?!?"],
             666: ["HAIL HYDRA!!!"],
             777: ["A blue box well show up soon"]
             }
    #         -----     -----         -----         -----        -----      #

    DT.clear()

    print("THE STORY\n" +  Story[langOpt])  # the story

    # this is well print the game menu, by inputting the list options, it'll print out the number and )
    DT.game_Menu(*menuOptions[langOpt])
    # same as if you did this >
    #for i in range(len(Sm)): print(str(i) + ')', Sm[i])  # this makes it easy to print out all of the options for the menu, instad of using print over and over again

    # 0 jump off, 1 yell at rock, 2 beg rock, 3 sleep, 4 quit

    run = [game_0, game_1, game_2, game_3, game_4, super_Secret, QUIT]  # list of the functions for the different options
    inp = input("choose > ")  # ask user to for what option they want to do, and then goes and runs it

    try:  # try and except is for when you know you're code might break,
        # if the 'try' code fails the program goes to except, instead of crashing
        inp = int(inp)  # tries to convert input to integer
        if inp > 5:
            print(extra[inp])
            start_Menu()  # checks to see if what you inputted is a extra
        else: run[inp]()  # runs the game that corresponds to input
    except:
        DT.error()
        start_Menu() # gives error, then goes back to main menu

start_Menu()
###################################################################################################################################################