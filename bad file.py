G1_err = ["That didn't work : ", "That didn't work jackass, try again :"]
G12_err = ["dunno what that was, can't use it. Sorry, try again : ",
				   "OK you know that won't work, stop wasting my fucking time! : "]
G12 = [["You offer to make a pack with Satan to save you're soul", "Now you're going to hell", "HELL LEVEL 1",
				"Youre now in Hell, and first thing you see is Satan sitting on dark throne",
				"What the hell ya going to do now?"],
			   ["YAY you offer you're worthless soul to Satan(dunno why he wants it?)",
				"Now you're going to HELL BIATCH!", "WELCOME TO HELL MOTHERFUCKER!!!",
				"Woohoo, you're in hell, first thing you see is the Dark Lord him self on his Throne of AWESOME-NESS",
				"I'm so exicting becuase I Hail the Dark Lord!(you should too now)"]]
G12_M = [
			["Attempt to sneak away", "Beg for soul back even though you just sold it", "Live for enternity in Hell"],
			["Try to sneak away from Satan(not smart dumbass)",
			 "Beg for you're shitty soul EVEN though you sold it to 'save' it(idiot)",
			 "Live in Hell for ever and ever(it's not that bad.. REALLY!)"]]
G3 = ["You are now yelling at the rock!", "Why the fuck are you yelling at a rock(DUMBASS)"]
G3_1 = ["..................", "FUCK OFF, go and jack-off you jackwagon!"]
G5 = ["You are thinking that you can't get off this rock so you decide to go to bed",
			   "So since you're too stupid to figure out how to get off this rock, you decide sleep you're ass off(until you die probably)"]
G5_2 = ["You're now sleeping",
				 "Now you're sleeping, congrats! this is the most complicated thing you can do(besides pee and being stupid)"]
G5_3 = ["Hope you rested well", "You snore too fucking loud, SHUT THE FUCK UP DICKHEAD"]
G5_4 = ["Morning, you slept in total of > ",
				 "Morning bitch(hope now you can think of something better to do), you have wasted total > "]
G51 = ["You slept for too long, you are now in a dream!",
			   "wow congrats jackwagon, you slept for too long now you're stuck in a fucking dream!"]
		G51_2 = ["Since you slept for too long, you're not trapped in a dream world. whatcha going to do?",
				 "You're in a dream world. yay(NOT), if i see any lollipop trees or some rainbow place bullshit,\ni'm going to fuck this place up!"]
		# dream  world menu
		G51_M = [["Go eat the candy", "Find a ginger-bread house", "Find a way out"],
				 ["Eat the candy until you're fat, and you die(you fatass)",
				  "Go and burn down a everything!(burn those gingerbread people to HELL!!)",
				  "Find a way out from this shithole!"]]
		# extra text under menu
		G51_M_1 = ["this place look and smell nice, look huge lollipops, rainbows, and candy!",
				   "FUCK! this place have lolli-shits and rainbow bullshit!\nI guess this is going to look like hell in a moment!"]
Qt = ["goodbye, thanks for playing :)",
			  "are you quiting becuase you suck or some other reason, anyway bye bye wimp"]


def Loading_screen_1():  # mean loading screen, it's in binary(each section is a letter)

    Binary = ['LOADING \n', '01000100', ' 01001001', ' 01000011', ' 01001011', ' 01001000', '  01000001',
              ' 01000100', ' 00100001']
    # this is a list for the loading screen, and i use loop to print it out one by one, instead of using print over and over

    for i in range(len(Binary)): print(i), sleep(2)
    # goes through the 'Binary' list and prints it out one by one, with pauses in between

    input("lol, don't try to translate it! CONTINUE >")  # waits till person is ready to play
