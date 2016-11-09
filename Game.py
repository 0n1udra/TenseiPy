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
back = "Go back"
Menu = "Back to main menu"

# leave the text in the lists, because later when the game is finished i'm going to add another version of the text

# GAME#		####################################################################################################################################
class Game1:  # jump off rock > ask for last words > go to hell or die ..

    def __init__(self): self.Game_1()  # init function calles 'Game_1' when 'Game1' class is called

    def Game_1(self):  # jumping off
        # Text        #####         #####         #####         #####         #####
        # you're falling >  still falling > any last words?
        G1 = ["You're now falling to you're DOOM", "Still falling", "Any last words?"]
        # thanks that did nothing > falling..falling > SPLAT > GAME OVER
        G1_2 = ["Thanks, that did nothing", "Falling...Falling...Falling", "SPLAT...you dead!", "GAME OVER"]
        # keywords to go to Hell. kw = keywords
        G1_H_kw = ["dark lord satan, i offer thee my soul", "test", "1"]
        #####         #####         #####         #####         #####        #####

        clear()
        for i in range(len(G1)):
            print(G1[i]) # Prints >> falling to you're DOOM >  still falling > any last words
            sleep(4) # waits for 4 seconds after everytime it loops and prints text

        inp = input("Word(s) > ") # ask for last words before you die
        if inp.lower() in G1_H_kw: # checks if you entered a keyword from the keyword list(G2_H_kw)
            self.Game_1_2() # if so, it starts the next game
        else:
            for i in range(len(G1_2)): # if you didn't input keywords it prints..
                print(G1_2[i]) # Prints >> thanks that did nothing > Falling.. > SPLAT > GAME OVER
                sleep(3) # pauses for 3 seconds every loop
            game_Over() # exits game

    def Game_1_2(self):  # in hell
        # Text        #####         #####         #####         #####         #####
            # Game_1_2 Hell
                # offer soul to Satan > going to hell > HELL LEVEL 1 > you see Satan on his throne > what are you going ot do now?
        G12 = ["You offer to make a pack with Satan to save you're soul", "Now you're going to hell", "HELL LEVEL ",
               "Youre now in Hell, and first thing you see is Satan sitting on dark throne",
               "What the hell ya going to do now?"]
                # Hell level input
        G12_M = ["Attempt to sneak away", "Beg for soul back even though you just sold it",
                 "Live for enternity in Hell"]
        #####         #####         #####         #####         #####        #####
        for i in range(len(G12)):
            print(G12[i])
            sleep(3)
        # going to hell > offer the make a pack > HELL LEVEL

        clear()
        print("\n", G12[3])  # Now in Hell, see satan.
        print("\n", G12[4])  # what are you going to do now
        for i in range(len(G12_M)):
            print(i, ')', G12_M[i])
        # 0 attempt to sneak away, 1, beg for soul, 2 stay for ever.

        run = [] # input options
        inp  = input("Soo > ")  # input for this level
        try:
            inp = int(inp)
            run[x]()
            exit()
        except:
            error()
            self.Game_1_2()

class Game2:  # Game 2, ask rock, ground,

    def __init__(self): self.Game_2()

    def Game_2(self):  # ask rock to go to ground
        # Text        #####         #####         #####         #####         #####
            # asking rock to fly down
                # how to ask rock
        G2_a = ["How would you like to ask the rock to fly down?"]
                # Game_2 asking, and responding. y, you, r, rock
        G2_y = ["You told the rock"]
        G2_r = ["The rock says"]
             # Game_2 on the ground
        G2_g = ["YAY you're on the ground now, so now what?"]
             # Game_2 else response
        G2_e = ["Well that got you nowhere! : "]
             # Ways to ask rock, and rock responses
        waysTooAsk = {0: {1: "May you please fly down to the ground, thank you",
                          2: "Fly down to the ground right now, or i'll spit on  you",
                          3: "you better fly down there right now or i'm going to whoop you up real good(in a sassy way)",
                          4: "i'll give you whatever you want except wanting me to stay here",
                          5: "if you don't let me down right now i'll kill your family and then you!"}}
        rockAnswers = {0: {1: "OK fine",
                           2: "then I'll drop you from 100ft",
                           3: "oh don't you talk to me like that(in a sassy rock way(i guess))",
                           4: "I wish to stay here and you can move to the right 1ft, and you won't be in the same place",
                           5: "Then i'll find you fimily and murder then and then the human race! MWHAHAHAHAHA!!!"}}

        #####         #####         #####         #####         #####        #####
        clear()

        print("\n", G2_a)  # How would you like to ask
        print("\n1. nicely, 2. Rudely, 3. Sassy, 4. Bribe, .")

        ask_input = input("Choose one > ")
        try:  # tries to convert the input to a usable integer for this part
            x = int(ask_input)
        except:
            self.Game_2()  # if it fails, it runs this code(Game_2) again

        print(G2_y, "\n > ", waysTooAsk[x])  # you say
        wait()
        print(G2_r, "\n > ", rockAnswers[x])  # rock responds
        wait()
        if x == 1:
            print("\n", G2_g)  # prints 'you're on the ground'
            wait()  # pasues
            self.Game_2_1()  # starts the next game 'Game_2_1'

        else:
            print("\n", G2_e)  # prints got you nowhere
            wait()  # waits for enter, to continue
            self.Game_2()  # re-runs the program(Game_2)

    def Game_2_1(self):  # on the ground
        # Text        #####         #####         #####         #####         #####
        G2_1_M = []
        #####         #####         #####         #####         #####        #####

        for i in range(len(G2_1_M)):
            print(i, ')', G2_1_M[i])

        wait()
        Startup()

class Game3:  # Game 3, yelling

    def __init__(self): self.Game_3()

    def Game_3(self):
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

class Game4:  # Game_4, Begging

    def __init__(self): self.Game_4()

    def Game_4(self):
        # Text        #####         #####         #####         #####         #####
        G4 = []
        G4_M = []
        #####         #####         #####         #####         #####        #####

        print(G4)
        for i in range(len(G4_M)):
            print(i, ')', G4_M[i])
        wait()

class Game5:  # Game 5, sleep, dream, ..

    def __init__(self): self.Game_5()

    def Game_5(self):  # sleeping
        global timeSlept
        clear()
        # Text        #####         #####         #####         #####         #####
            # going to bed
        G5 = ["You are thinking that you can't get off this rock so you decide to go to bed"]
            # you"re now sleeping
        G5_2 = ["You're now sleeping"]
            # hope you rested well
        G5_3 = ["Hope you rested well"]
            # morning
        G5_4 = ["Morning, you slept in total of > "]
        G5_Snores = ['zz', 'ZzZ', 'ZZzz', 'zzZzZ', 'ZzZzzZ']
        #####         #####         #####         #####         #####        #####

        print(G5)  # thinking can't get off
        print(G5_2)  # go to bed. 2 now sleeping
        amount = random.randint(1, 5)  # this generates random number 1-10
            # random number is to print 'z'(s) in random number of times, just because
        for i in range(5):  # loops the print statment 5 times
            print(G5_Snores * amount) # prints zz(s) from the list by a random amount
        #	sleep(amoun)
        print(G5_3)  # rested well message
        sleep(.3)  # pauses for 5secs
        print(G5_4, timeSlept, "hours")  # prints morning message and tells you how long you slept for in total
        wait()
        timeSlept = timeSlept + 12 * 1.2  # adds time to total time slept,
        # ^ everytime you sleep, you longer you sleep. 1.2x longer everytime
        if timeSlept > 84:  # checks to see if you slept over 84 hours
            self.Game_5_1()  # if you slept for more then 84 hours, you go to dreamworld
        else:  # else you it goes back to main menu
            clear()
            Startup() # go to main menu

    def Game_5_1(self):  # dream
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
        run = [Game1, Game2, Game3, Game4, Game5, Quit]  # list of the functions for the different options
        inp = input("choose > ")  # ask user to for what option they want to do, and then goes and runs it

        try:  # try and except is for when you know you're code might break,
            # if the 'try' code fails the program goes to except, instead of crashing
            inp = int(inp)  # tries to convert input to integer
            if inp > 4:
                print(extra[inp])
                self.Start_menu()  # cheks to see if input goes to extras
            else:
                run[inp]()  # runs the game that corresponds to input
        except:
            error()
            self.Start_menu()  # gives error, then goes back to main menu

Startup()  # starts the program, without this it won't run
###################################################################################################################################################
