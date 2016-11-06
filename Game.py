# SETUP#		#########################################################################################################################################
# libraries I use
import os, time, sys, time, random
# makes typing easier, shortcuts
def pr(string): print(string, end=' ') # prints text on same line, unlike 'print' which prints new-lines
def sleep(amount): time.sleep(amount) # sleep funciton does the same as time.sleep(amount)
def sudo(command): os.system(command) # quick os command, so i don't have to type os.system(command)
def clear(): print("\n" * 50) # clear clears the screen
def wait(): # pauses game, press 'enter' to continue
    Wait = ["Press 'Enter' to continue", "Press 'Enter' to continue(is that to complicated for you?)"]
    input(Wait[t])
def again(ans):
    if ans.lower == 'y'
# hides errors
class devNull(): pass
# sys.stderr = devNull

# Variables
# t = niceness, 0 = nice, 1 = mean
t = 0
timeSlept = 12

# TEXT#		####################################################################################################################################

class T:
    # first line is nice
    # second line is mean
    # Story#
    Story = ["You are on a floating rock 1000ft above ground, and all that you have is a bed(for some reason), so what do you do",
             "(This story makes no fucking sense! ok here it is)>> so You're on a fucking rock 1000ft above ground(told you it made no sense), and all you have is a damn bed(why?? just why??), so whatcha going to do bitch"]
    # Startup#		##########			##########			##########
    # Start_menu
    Sm = [["Jump off", "Yell at rock", "Beg rock to go down", "Go to sleep", "Quit"],
          ["Jump to you're worthless death", "Yell at rock, becuase you're dumb", "Beg like a pussy","Go to sleep, becuase that's all you're good for", "Quit becuase you suck at this!"]]
    Sm_err = ["try again > ", "that didn't work dumbass > "]
    # quit
    qt = ["goodbye, thanks for playing :)",
          "are you quiting becuase you suck or some other reason, anyway bye bye wimp"]
    # other#
    # back 99
    back = "Go back"
    Menu = "Back to main menu"
    # extra game menu options
    extra = {69: ["really!?!?", "What the FUCK is wrong with you???"],
             666: ["HAIL HYDRA!!!", "Hail the dark lord"],
             777: ["A blue box well show up soon", "Fuck you, there's your luck!"]
             }
    # Game_1#	##########			##########			##########
    # Time_jump
    G1 = [["You're now falling to your DOOM!", "Still falling", "How long has it been? do you have the time?"],
          ["You're now falling, nice job DUMBASS!", "still fucking falling to you're death","Damn how long has it been, what's the time"]]
    # Time_jump part 2
    G1_2 = [["Thanks, that did nothing", "Falling...Falling...Falling", "SPLAT...you dead!", "GAME OVER"],
            ["Really you thought the time was important, idiot", "Die already", "Splat....now you're dead, LOL","GAME OVER BITCH!"]]
    G1_err = ["That didn't work", "That didn't work jackass, tray a gain"]
    # Game1_2#	#Hell_level
    G12 = [["You offer to make a pack with Satan to save you're soul", "Now you're going to hell", "HELL LEVEL 1","Youre now in Hell, and first thing you see is Satan sitting on dark throne","What the hell ya going to do now?"],
           ["YAY you offer you're worthless soul to Satan(dunno why he wants it?)", "Now you're going to HELL BIATCH!","WELCOME TO HELL MOTHERFUCKER!!!","Woohoo, you're in hell, first thing you see is the Dark Lord him self on his Throne of AWESOME-NESS","I'm so exicting becuase I Hail the Dark Lord!(you should too now)"]]
    # Hell_level input
    G12_M = [["Attempt to sneak away", "Beg for soul back even though you just sold it", "Live for enternity in Hell"],
             ["Try to sneak away from Satan(not smart dumbass)","Beg for you're shitty soul EVEN though you sold it to 'save' it(idiot)","Live in Hell for ever and ever(it's not that bad.. REALLY!)"]]
    # Hell_level try/except
    G12_err = ["dunno what that was, can't use it. Sorry, try again",
              "OK you know that won't work, stop wasting my fucking time asshole!!!. My time is much much much much more important then your's!!. so type something in, useful!"]
    # Game_2#	#########			##########			##########
    # asking the rock
    G2_a = ["How would you like to ask the rock to fly down?",
            "soooo how are you going to ask the rock to fly your sorry ass down\n(if it even can)(great you're talking to a fucking rock, maybe you should just go to sleep and get some sense)"]
    # Game_2 chat y, you, r, rock
    G2_y = ["You told the rock", "You told the rock(why are you talking to the rock? weirdo)"]
    G2_r = ["The rock says","The rock says(how the fuck is a rock talking. Wow this game is fucked up, but you decided to play it"]
    # Game_2 on the ground
    G2_g = ["YAY you're on the ground now, so now what?",
            "whoopdy fucking doo! you're on the ground.\n now you can sleep on the ground, becuase there's nothing there. Up there there was a comfy bed, but whatever......now what?"]
    # Game_2 else response
    G2_e = ["Well that got you nowhere!","Nice, that didn't work, try to be nice for once in you're life(i know that's going to be very difficult for you!)"]
    waysTooAsk = {0: {1: "May you please fly down to the ground, thank you",
                      2: "Fly down to the ground right now, or i'll spit on  you",
                      3: "you better fly down there right now or i'm going to whoop you up real good(in a sassy way)",
                      4: "i'll give you whatever you want except wanting me to stay here",
                      5: "if you don't let me down right now i'll kill your family and then you!"},
                  1: {1: "Can you please get yo ass down to the ground(I siad please",
                      2: "Get you're ass down to the ground right now!", 3: "Fuck sassy, I want ground, get me off",
                      4: "You want money, I don't have money. fuck off, and get me down!",
                      5: "If you don't get me down right now i'll fuck you up and then you're family(if you have one), then piss on you and then shit on you! soo? deal?"}}
    rockAnswers = {0: {1: "OK fine, well you please comeback and visit :)", 2: "then I'll drop you from 100ft",
                       3: "oh don't you talk to me like that(in a sassy rock way(i guess))",
                       4: "I wish to stay here and you can move to the right 1ft, and you won't be in the same place",
                       5: "Then i'll find you fimily and murder then and then the human race! MWHAHAHAHAHA!!!"},
                   1: {1: "Fuck you man, but fine, get you're ass outta here",
                       2: "FUCK OFF! go back to sleep, you may or may not be alive tomorrow!",
                       3: "uh NO, go fuck you're self instead", 4: "Why the fuck would I need money? Dumbass!",
                       5: "Hey you cunt! don't ever fucking talk to me like that, or you're going be in pain for enternity(I know the Devil)"}}
    # Game_2_1#
    G2_1_M = []
    # Game_3#	##########			##########			##########
    G3 = ["You are now yelling at the rock!", "Why the fuck are you yelling at a rock(DUMBASS)"]
    G3_1 = ["..................", "FUCK OFF, go and jack-off you jackwagon!"]
    # GAME_4#	##########			##########			##########
    G4 = []
    G4_M = []
    # Game_5#	##########			##########			##########
    # going to bed
    G51 = ["You are thinking that you can't get off this rock so you decide to go to bed",
           "So since you're too stupid to figure out how to get off this rock, you decide sleep you're ass off(until you die probably)"]
    # you"re now sleeping
    G51_2 = ["You're now sleeping",
             "Now you're sleeping, congrats! this is the most complicated thing you can do(besides pee and being stupid)"]
    # extra message
    G51_3 = ["Hope you rested well", "You snore too fucking loud, SHUT THE FUCK UP DICKHEAD"]
    # morning
    G51_4 = ["Morning, you slept in total of > ",
             "Morning bitch(hope now you can think of something better to do), you have wasted total > "]
    # Game_5_1#	# dream story#
    # congrats
    G52 = ["You slept for too long, you are now in a dream!",
           "wow congrats jackwagon, you slept for too long now you're stuck in a fucking dream!"]
    G52_S = ["Since you slept for too long, you're not trapped in a dream world. whatcha going to do?",
             "You're in a dream world. yay(NOT), if i see any lollipop trees or some rainbow place bullshit,\ni'm going to fuck this place up!"]
    # dream  world menu
    G5_1_M = [["Go eat the candy", "Find a ginger-bread house", "Find a way out"],
              ["Eat the candy until you're fat, and you die(you fatass)","Go and burn down a everything!(burn those gingerbread people to HELL!!)","Find a way out from this shithole!"]]
    # extra text under menu
    G52_M_1 = ["this place look and smell nice, look huge lollipops, rainbows, and candy!",
               "FUCK! this place have lolli-shits and rainbow bullshit!\nI guess this is going to look like hell in a moment!"]

# GAME#		####################################################################################################################################

class Game1:  # jump off, ask time, go to hell ..
    def __init__(self): self.Game_1() # init function calles 'Game_1' when 'Game1' class is called

    def Game_1(self):  # jumping off
        for i in range(len(T.G1)): print(T.G1[t][i]), sleep(5)
            # falling to you're DOOM, still falling, what time is it
        wait(), clear()
        inp = input("time? > ")
        def check(inp):
            try:
                inp = str(inp)
                if inp == "6:66": self.Game_1_2()
                else:
                    for i in range(len(T.G1_2)): print(T.G1_2[t][i]), sleep(3) # prints the options, and sleeps for 3 seconds between each print
                        # that did nothing, falling..falling..falling, splat you dead, Game over
                    input("quit > ")
                    exit()
            except:
                print(G1_err[t]), check()
        check(inp)


    def Game_1_2(self):  # in hell
        for i in range(len(T.G12)):
            print(T.G12[t][i])
            sleep(3)
            # going to hell, offer the make a pack, HELL LEVEL 1
        clear()
        print("\n", T.G12[t][3])  # now in hell, see Satan
        print("\n", T.G12[t][4])  # what are you going to do now
        wait(), clear()
        for i in range(len(T.G12_M)): print(i,')',T.G12_M[t][i])
            # 0 attempt to sneak away, 1, beg for soul, 2 stay for ever.
        run = []
        inp = input("Soooo > ")  # input for this level
        try:
            inp = int(inp)
            exit()
            run[x]()
        except: print(T.G12_err[t]), input() # error

class Game2:  # Game 2, ask rock, ground,
    def __init__(self): self.Game_2()

    def Game_2(self):  # ask rock to go to ground
        clear()
        print("\n", T.G2_a[t])  # How would you like to ask
        print("\n1. nicely, 2. Rudely, 3. Sassy, 4. Bribe, .")
        ask_input = int(input("Choose one > "))
        x = ask_input
        print(T.G2_y[t], "\n > ", T.waysTooAsk[t][x])  # you say
        wait()
        print(T.G2_r[t], "\n > ", T.rockAnswers[t][x])  # rock responds
        wait()
        if x == 1:
            print("\n", T.G2_g[t])  # on ground now
            wait()
            self.Game_2_1()  # goes to Game_2_1
        else:
            print("\n", T.G2_e[t])  # got you nowhere
            wait()
            self.Game_2()  # re-runs the program(Game_2)

    def Game_2_1(self):  # on the ground
        for i in range(len(T.G2_1_M)): print(i,')',T.G2_1_M[t][i])
        wait(), exit()

class Game3:  # Game 3, yelling
    def __init__(self): self.Game_3()
    def Game_3(self):
        print(T.G3[t])  # yelling at rock
        print("The rock responds > ")
        print(T.G3_1[t])  # .............
        input("That got did nothing, try something else > ")
        wait(), exit()

class Game4:  # Game_4, Begging
    def __init__(self): self.Game_4()

    def Game_4(self):
        print(T.G4[t])
        wait()

class Game5:  # Game 5, sleep, dream, ..
    def __init__(self): self.Game_5()

    def Game_5(self):  # sleeping
        global timeSlept
        print(T.G51[t])  # thinking can't get off, go to bed
        print(T.G51_2[t])  # now sleeping
        amount = random.randint(1, 10)
        print("z" * amount)
        sleep(1)
        print("zZ" * amount)
        sleep(1)
        print("zzZzZ" * amount)
        sleep(1)
        print("zzZzzZZzzZZ" * amount)
        sleep(4)
        print(T.G51_3[t])  # rested well
        sleep(6)
        print(T.G51_4[t], timeSlept, "hours")  # Morning, timed slept
        wait()
        timeSlept = timeSlept + 12 * 1.5  # adds time to total time slept
        if timeSlept > 84:  # checks to see if you slept over 84 hours
            self.Game_5_1()
        else:
            clear()
            Menu()

    def Game_5_1(self):  # dream
        for i in range(len(T.G52_M)):
            print(i,')',T.G52_M[t][i])
        print(T.G52[t])
        print(T.G52_S[t])
        print(T.G52_M_1[t])
        inp = input(T.G52_i[t])

# STARTUP#		#####################################################################################################################################

class LoadingScreens:
    def Loading_screen_0():  # nice loading screen, <(^.^)> (kirby)
        clear()
        pr("Welcome "), pr("Loading... ")
        sleep(random.random() + 1)
        pr("<"), sleep(random.random())
        pr("("), sleep(random.random() + .5)
        pr("^"), sleep(random.random())
        pr("."), sleep(random.random() + 2)
        pr("^"), sleep(random.random() + .456)
        pr(")"), sleep(random.random() + .8)
        pr(">"), sleep(random.random() + .55)
        pr(" :) ")
        print("\nLOADED, WELCOME.")
        input("CONTINUE > ")

    def Loading_screen_1():  # mean loading screen, it's in binary(each section is a letter)
        pr(" 01000100"), sleep(random.random() + 1)
        pr(" 01001001"), sleep(random.random() + 2)
        pr(" 01000011"), sleep(random.random() + 3)
        pr(" 01001011"), sleep(random.random() + 2)
        pr(" 01001000"), sleep(random.random() + 1)
        pr(" 01001000"), sleep(random.random() + .5)
        pr(" 01000001"), sleep(random.random() + 3.14)
        pr(" 01000100"), sleep(random.random() + .934)
        pr(" 00100001"), sleep(random.random() + 1)
        input("lol, don't try to translate it! CONTINUE >")
        sleep(3)

class Startup:
    def __init__(self): self.Niceness()

    def Start_menu(self):
        clear()
        print("THE STORY")
        print(T.Story[t])  # the story
        for i in range(len(T.Sm[t])): print(i,')',T.Sm[t][i]) # this makes it easy to print out all of the options for the menu, instad of using print over and over again
        # 0 jump off, 1 yell at rock, 2 beg rock, 3 sleep, 4 quit
        run = [Game1, Game2, Game3, Game4, Game5] # list of the functions for the different options
        inp = input("choose > ")  # ask user to for what option they want to do, and then goes and runs it
        try:
            inp = int(inp) # tries to convert input to integer
            if inp > 4:
                print(T.extra[inp][t])
                self.Start_menu()
            else: run[inp]() # runs the game with the input
        except:
            input(T.Sm_err[t])
            self.Start_menu()

    def Niceness(self):  # ask user if they want the game to be nice or mean, mean is real mean
        global t
        clear()
        print("Do you want to play nice or mean?")
        inp = input("0) nice. 1) mean > ")
        loadingSc = [LoadingScreens.Loading_screen_0, LoadingScreens.Loading_screen_1] # list of the different loading screens
        try:
            inp = int(inp)
            t = inp # sets the niceness of the game
            # loadingSc[inp]() # runs the loading screen for mean or nice
            self.Start_menu() # this is so if i don't want a loading scren it well go streight to the menu
        except: # if what inputted doesn't work this runs
            input("try again > ")
            self.Niceness()

Startup()
###################################################################################################################################################
