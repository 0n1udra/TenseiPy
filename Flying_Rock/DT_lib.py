import sys, os, time, random, colorama
langOpt = 0

# Game menu
def game_Menu(x):
    print("MENU")
    for i in range(len(x)):
        print(str(i) + ')', x[i])

def option_Menu(x):
    for i in range(len(x)):
        print(str(i) + ')', x[i])


def sleep(x): # temporary, to remove pauses
    time.sleep(1)


def print_Text(text, sleepTime=2):
    for i in range(len(text[langOpt])):
        print(text[langOpt][i])
        sleep(sleepTime)



# Screen interaction

def clear(): 
    print("\n"*50)



def wait(): 
    input("...Enter>")
    
def print_Back():
    print("99) Go back\n100) Main Menu")

# Back to main menu function
def input_Back(x, mainMenu, backPosition):
    if x == 99:
        backPosition()
    elif x == 100:
        mainMenu()
    else:
        pass

# Prints loading screen
def loading_Screen(list):
    for i in list:
        print(i)
        time.sleep(2)
    print("\nDone Loading...")

def game_Over(start):
    inp = input("Would you like to continue? Y/N > ")
    if inp.lower() in ('y', 'yes'):
        start()
    else:
        print("Thanks for playing!\nExiting.")
        exit()

def error():
    input("That didn't work. Enter> ")

# makes sure this program doesn't run, if runned directly
if(__name__ == '__main__'):
    pass
else:
    print("DT_lib Imported.")
