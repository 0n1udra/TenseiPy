import sys, random
from DT_S_lib import *


# TEMP#

# from time import sleep
def sleep(x):
    pass


def wait():
    input(": ")


def Startup():

    # loading screen data
    LOADING = ['LOADING', '.....',
                '\nBooting time drives', '.....',
                '\nPutting on Bowtie!', '.....',
                '\nRecoating blue paint', '.....',
                '\nCalibrating Sonic', '.....',
                ]
    loading_Screen(LOADING) # calls loading screen functionf rom DT_S_lib

    print("\nNote. ':' means press enter, '>' means input data")
    input("Continue: ")

    print("You are in the T.A.R.D.I.S. what would you like to do")
    # menu options data to printout
    options = ["Go outside",
               "Time traval",
               "Explorer the coaradoors",
               "Find the Doctor",
               "Get something to eat",
               "Go to sleep",
               "Quit"]
    game_Menu(options) #
    wait()
    quit()


Startup()
