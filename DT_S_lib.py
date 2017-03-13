import sys, os, time, random, colorama

# Game menu
def game_Menu(*x):
    print("MENU")
    for i in range(len(x)):
        print(str(i) + ')', x[i])

# Screen interaction
def clear(): print("\n"*50) # clears the screen

# sleeps, pauses game for a short time
def sleep(x): # temporary, to remove pauses
    time.sleep(0)

# waits for input to continue.
def wait(): input(" :") # pauses game, until press 'enter'

# game back and main menu options
def print_Back():
    print("99 ) Go back")
    print("100 ) Main menu") # prints menu options☻

def input_Back(x, mainMenu, backPosition): # check if input is 99 to go back, or 100 to go to main menu
    if x == 99: backPosition()
    elif x == 100: mainMenu()
    else: pass

# loading screen
def loading_Screen(x):
    for i in range(len(x)):     # finds the length of the 'x' list, so it knows how long to loop.
        # then for each item in list it gives it the variable 'i'; just for one loop.
        print(x[i])
        time.sleep(2)
    print("\nDone Loading...")
    # then on next loop it changes the 'i' value to the next item in list, then prints it out, each loop it pauses for 2sec

# Game over menu
def game_Over(): # if you die, this asks you if you want to play again
    inp = input("Would you like to continue? Y/N > ").lower()
    try: # this is if somebody inputs something that is not usable it goes to except, instead of crasing
        if inp in ('y', 'yes'): Startup() # if inputted 'y' or 'yes' it goes back to main menu
        else: # if anything else, it quits the game
            print("Thanks for playing!")
            exit() # if you don't continue, it says bye
    except: pass

def error(): input("That didn't work : ") # simple error message




### Coloring Text ###############################################################################33


class c:
    # Resets Text and Background color
    def resetA(self): print(colorama.Style.RESET_ALL, end='')

    # Resets text color
    def resetT(self): print(colorama.Fore.RESET, end='')

    # Resets Background color
    def resetB(self): print(colorama.Back.Reset, end='')

    # Brightens the text color
    def bright(self): print(colorama.Style.BRIGHT, end='')

    # Dim text
    def dim(self): print(colorama.Style.DIM, end='')

    def norm(self): print(colorama.Style.NORMAL, end='')

    def rainbow_Text(self, text):
        text.split()
        pass

    # Prints out example text
    def Example():

        print("Normal Text")


        Bright()
        print("bright Text")

        Dim()
        print("dim text")

        print(Fore.RED + "RED")

        ResetA()
        print("A back to normal")




# makes sure this program doesn't run, if runned directly
if __name__ == '__main__': print("Should not be runned directly!")
else: print("Drake's Standard Library... Imported.")
