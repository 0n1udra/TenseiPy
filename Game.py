# SETUP#		#########################################################################################################################################
# libraries I use
import random, sys
# sys is for errors
import time #from time import sleep # this is temporary
# time is for the delays and pauses
# hides errors, puts errors to devNull, which 'pass', does nothing
class devNull(): pass
sys.stderr = devNull()

def sleep(x): # temporary, to remove pauses
    x = None
    time.sleep(0)
# makes typing easier, shortcuts
def pr(string): print(string, end=' ')
# prints text on same line, so i don't have to add "end=' '" to each line of print

def clear(): print("\n" * 50)
# 'clear' clears the screen, by making new lines 50 times

def wait(): input(": ")
# pauses game, press 'enter' to continue

def print_Back():
    print("99 ) Go back")
    print("100 ) Main menu")
def input_Back(x, pos):
    if x == 99: pos()
    elif x == 100: Startup()
    else: pass

def game_Over():
    inp = input("Would you like to continue? > ")
    try: # this is if somebody inputs something that is not usable it goes to except, instead of crasing
        if inp in ('y', 'yes'):
            Startup()
        else:
            print("Thanks for playing!")
            exit()
    except: pass

def error(): input("That didn't work : ") # simple error message

# Variables
timeSlept = 12 # sets timeSlept variable, starts at 12,

# leave the text in the lists, because later when the game is finished i'm going to add another version of the text

# GAME#		####################################################################################################################################
class Game0:  # jump off rock > ask for last words > go to hell or die ..

    def __init__(self): self.Game_0()  # init function calles 'Game_0' when 'Game0' class is called

    def Game_0(self):  # jumping off
        # Text        #####         #####         #####         #####         #####
        # you're falling >  still falling > any last words?
        G0 = ["You're now falling to you're DOOM", "Still falling", "Any last words?"]
        # thanks that did nothing > falling..falling > SPLAT > GAME OVER
        G0_1 = ["Thanks, that did nothing", "Falling...Falling...Falling", "SPLAT...you dead!", "GAME OVER"]
        # keywords to go to Hell. kw = keywords
        G0_H_kw = ["dark lord satan, i offer thee my soul", "test", "1"]
        #####         #####         #####         #####         #####        #####

        clear()
        for i in range(len(G0)):
            print(G0[i]) # Prints >> falling to you're DOOM >  still falling > any last words
            sleep(4) # waits for 4 seconds after everytime it loops and prints text

        inp = input("Word(s) > ") # ask for last words before you die
        if inp.lower() in G0_H_kw: # checks if you entered a keyword from the keyword list(G2_H_kw)
            self.Game_0_1() # if so, it starts the next game
        else:
            for i in range(len(G0_1)): # if you didn't input keywords it prints..
                print(G0_1[i]) # Prints >> thanks that did nothing > Falling.. > SPLAT > GAME OVER
                sleep(3) # pauses for 3 seconds every loop
            game_Over() # exits game

    def Game_0_1(self):  # in hell
        # Text        #####         #####         #####         #####         #####
            # Game_0_1 Hell
                # offer soul to Satan > going to hell > HELL LEVEL 1 > you see Satan on his throne > what are you going ot do now?
        G01 = ["You offer to make a pack with Satan to save you're soul", "Now you're going to hell", "HELL LEVEL ",
               "Youre now in Hell, and first thing you see is Satan sitting on dark throne",
               "What the hell ya going to do now?"]
                # Hell level input
        G01_M = ["Attempt to sneak away", "Beg for soul back even though you just sold it",
                 "Live for enternity in Hell"]
        #####         #####         #####         #####         #####        #####
        for i in range(len(G01)):
            print(G01[i])
            sleep(3)
        # going to hell > offer the make a pack > HELL LEVEL

        clear()
        print("\n", G01[3])  # Now in Hell, see satan.
        print("\n", G01[4])  # what are you going to do now
        for i in range(len(G01_M)):
            print(i, ')', G01_M[i])
        # 0 attempt to sneak away, 1, beg for soul, 2 stay for ever.
        print_Back()
        run = [] # input options
        inp  = input("Soo > ")  # input for this level
        try:
            inp = int(inp)
            input_Back(inp, Startup)  # runs input_Back function, for if you want to go back to main menu
            run[x]()
            exit()
        except:
            error()
            self.Game_0_1()

class Game1:  # Game 2, ask rock, ground,

    def __init__(self): self.Game_1()

    def Game_1(self):  # ask rock to go to ground
        # Text        #####         #####         #####         #####         #####
            # asking rock to fly down
                # how to ask rock
        G2_a = ["How would you like to ask the rock to fly down?"]
                # Game_1 asking, and responding. y, you, r, rock
        G2_y = ["You told the rock "]
        G2_r = ["The rock says  "]
             # Game_1 else response
        G2_e = ["Well that got you nowhere! "]
             # Ways to ask rock, and rock responses
        waysTooAsk =  {1: "May you please fly down to the ground, thank you",
                          2: "Fly down to the ground right now, or i'll spit on  you",
                          3: "you better fly down there right now or i'm going to whoop you up real good(in a sassy way)",
                          4: "i'll give you whatever you want except wanting me to stay here",
                          5: "if you don't let me down right now i'll kill your family and then you!"}
        rockAnswers =  {1: "OK fine",
                           2: "then I'll drop you from 100ft",
                           3: "oh don't you talk to me like that(in a sassy rock way(i guess))",
                           4: "I wish to stay here and you can move to the right 1ft, and you won't be in the same place",
                           5: "Then i'll find you fimaly and murder then and then the human race! MWHAHAHAHAHA!!!"}

        #####         #####         #####         #####         #####        #####
        clear()

        print("\n", G2_a)  # How would you like to ask
        print("\n1. nicely, 2. Rudely, 3. Sassy, 4. Bribe, .")
        print_Back()

        inp = input("Choose one > ")
        try:  # tries to convert the input to a usable integer for this part
            x = int(inp)
            input_Back(inp, Startup)
        except:
            self.Game_1()  # if it fails, it runs this code(Game_1) again

        print(G2_y[0], "\n >> ", waysTooAsk[x])  # you say >
        wait()
        print(G2_r[0], "\n >> ", rockAnswers[x])  # rock responds with >
        wait()
        if x == 1: # if you choose option 1 you go to the ground
            self.Game_1_1()  # starts the next game 'Game_1_1'
        else:
            input("\n", G2_e[0])  # prints got you nowhere
            wait()
            Game1() # re-runs the program(Game_1)

    def Game_1_1(self):  # on the ground
        # Text        #####         #####         #####         #####         #####
            # Story. on ground now
        G21_S = ["YAY you're on the ground now, so now what?"]
        G2_1_M = ["Go back to rock"]
        #####         #####         #####         #####         #####        #####
        clear()
        print(G21_S[0])
        for i in range(len(G2_1_M)):
            print(i, ')', G2_1_M[i])
        print_Back()
        inp = input()
        try:
            inp = int(inp)
            input_Back(inp, Game1)
        except: pass
        wait()
        Startup()

class Game2: # yelling > nothing

    def __init__(self): self.Game_2()

    def Game_2(self): 
        # Text        #####         #####         #####         #####         #####
        # now yelling at rock
        G3 = ["You are now yelling at the rock!"]
        # .............
        G3_1 = [".................."]
        #####         #####         #####         #####         #####        #####
        print(G3)  # yelling at rock
        print("The rock responds : ")
        print(G3_1)  # .............
        input("That got did nothing, try something else : ")

        wait()
        Startup()

class Game3:  # Begging > nothing

    def __init__(self): self.Game_3()

    def Game_3(self):
        # Text        #####         #####         #####         #####         #####
        G4 = []
        G4_M = []
        #####         #####         #####         #####         #####        #####

        print(G4)
        for i in range(len(G4_M)):
            print(i, ')', G4_M[i])
        wait()

class Game4:  # Sleep > Dreamworld > ..

    def __init__(self): self.Game_4()

    def Game_4(self):  # sleeping
        global timeSlept
        clear()
        # Text        #####         #####         #####         #####         #####
            # going to bed
        G5 = ["You are thinking that you can't get off this rock so you decide to go to bed"]
            # you"re now sleeping
        G5_1 = ["You're now sleeping"]
            # hope you rested well
        G5_2 = ["Hope you rested well"]
            # morning
        G5_3 = ["Morning, you slept in total of > "]
        G5_Snores = ['zz', 'ZzZ', 'ZZzz', 'zzZzZ', 'ZzZzzZ']
        #####         #####         #####         #####         #####        #####

        print(G5)  # thinking can't get off
        print(G5_1)  # go to bed. 2 now sleeping
        amount = random.randint(1, 5)  # this generates random number 1-10
            # random number is to print 'z'(s) in random number of times, just because
        for i in range(5):  # loops the print statment 5 times
            print(G5_Snores[i] * amount) # prints zz(s) from the list by a random amount
        #	sleep(amoun)
        print(G5_2)  # rested well message
        sleep(.3)  # pauses for 5secs
        print(G5_3, timeSlept, "hours")  # prints morning message and tells you how long you slept for in total
        wait()
        timeSlept = timeSlept + 12 * 1.2  # adds time to total time slept,
        # ^ everytime you sleep, you longer you sleep. 1.2x longer everytime
        if timeSlept > 84:  # checks to see if you slept over 84 hours
            self.Game_4_1()  # if you slept for more then 84 hours, you go to dreamworld
        else:  # else you it goes back to main menu
            clear()
            Startup() # go to main menu

    def Game_4_1(self):  # dream
        clear()
        # Text        #####         #####         #####         #####         #####
            # Dreamworld
                # now in dream world, congrats
        G51 = ["You slept for too long, you are now in a dream!"]
                # you're trapped, you slept for too long
        G51_2 = ["Since you slept for too long, you're not trapped in a dream world. whatcha going to do?"]
        # Dreamworld menu
        G51_M = ["Go eat the candy", "Find a ginger-bread house", "Find a way out"]
            # this looks like a nice place
        G51_M_1 = ["this place look and smell nice, look huge lollipops, rainbows, and candy!"]
        #####         #####         #####         #####         #####        #####

        for i in range(len(G51_M)):  # loop to print out menu
            print(i, ')', G51_M[i])
        print(G51)  # prints  you slept for too long, now in dreamworld
        print(G51_2)  # since you slept for too long you're stuck in dreamworld
        print(G51_M_1)  # extra menu message
        inp = input(G51_i)

class Quit:  # quit function, prints message and quits game
    def __init__(self):
        input("Thanks for playing : ")
        quit()  # built-in quit funciton

# STARTUP#		#####################################################################################################################################

class LoadingScreens:

    def Loading_screen_0():  # nice loading screen, <(^.^)> (kirby)

        clear()
        Kirby = ['LOADING ', '<', '(', '^', '.', '^', ')', '>', ' ', '\n:', ')', 'WELCOME']
        # Kirby loading screen items
        for i in range(len(Kirby)):
            print(i)
            sleep(2)
        # finds the length of the 'Kirby' list, so it knows how long to loop.
        # then for each item in list it gives it the variable 'i'; just for one loop.
        # then on next loop it changes the 'i' value to the next item in list, then prints it out, each loop it pauses for 2sec

        input("CONTINUE > ")  # waits until user presses 'Enter'

class Startup:
    def __init__(self): self.Start_menu()

    def Start_menu(self):
        clear()
        # Text        #####         #####         #####         #####         #####
            # Startup menu/Main menu
        Story = ["You are on a floating rock 1000ft above ground, and all that you have is a bed(for some reason), so what do you do"]
                # Start menu, sm=start menu
        Sm = ["Jump off(need work)" ,
              "Ask rock to go down(need work)",
              "Yell at rock(need changing)",
              "Beg rock to go down(need changing)",
              "Go to sleep(need work)",
              "Quit"]
                # in the main menu punch in these numbers, it well print these.
        extra = {69: ["really!?!?"],
                 666: ["HAIL HYDRA!!!"],
                 777: ["A blue box well show up soon"]
                 }
        #####         #####         #####         #####         #####        #####
        print("THE STORY ")
        print(Story)  # the story
        for i in range(len(Sm)):
            print(i, ')', Sm[i])  # this makes it easy to print out all of the options for the menu, instad of using print over and over again
        # 0 jump off, 1 yell at rock, 2 beg rock, 3 sleep, 4 quit
        run = [Game0, Game1, Game2, Game3, Game4, Quit]  # list of the functions for the different options
        inp = input("choose > ")  # ask user to for what option they want to do, and then goes and runs it

        try:  # try and except is for when you know you're code might break,
            # if the 'try' code fails the program goes to except, instead of crashing
            inp = int(inp)  # tries to convert input to integer
            if inp > 5:
                print(extra[inp])
                self.Start_menu()  # checks to see if what you inputed is a extra
            else:
                run[inp]()  # runs the game that corresponds to input
        except:
            error()
            self.Start_menu()  # gives error, then goes back to main menu

Startup()  # starts the program, without this it won't run
###################################################################################################################################################
