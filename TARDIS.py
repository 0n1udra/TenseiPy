import sys, random
#TEMP#
#from time import sleep
def sleep(x):
	pass
def wait():
	input(": ")
def Startup():
	print("LOADING")
	sleep(2)
	print(".....")
	sleep(1)
	print(".....")
	sleep(2)
	print(".....")
	sleep(1)
	print("WELCOME")
	print("You are in the T.A.R.D.I.S. what would you like to do")
	options = ["Go outside","Time traval", "Explorer the coaradoors", "Find the Doctor", "Get something to eat", "Go to sleep", "Quit"]
	for i in range(len(options)):
		print(str(i)+")"+options[i])
	wait()
	quit()
	


Startup()
