from game_files.game_functions import *
from chapters.tensei_3 import Chapter3


def Chapter2(rimuru):
	class chapter_2:
		def __init__(self):
			sprint("Oh, what's this? Looks like some kind of rock?")
			action_menu(self)

		def predate_ore(self):
			rimuru.add_inventory('magic ore')
			ssprint("<<Information, analysis shows this is the raw form of [Magisteel]. Can be used for crafting weapons, armor, and more.>>")
			sprint("Ok, might be useful in the future. Guess I should get as much as I can")

		def _move_on(self):
			sprint("I'll just leave it, and continue finding my way out.")
			sprint("Now with magic perception I can finally find my way out of this cave.")
			sprint("*But before finding the exit, some small monsters started taking a interest in the little slime.*")
			action_menu(_learn_new_attack())

	class _learn_new_attack:
		def __init__(self):
			sprint("Whoa. It looks like a giant snake serpent thing with big fangs. Or am I just small?")
			ssprint("<<Answer, this is a [Tempest Serpent].>>")
			sprint("Still, it's not as scary as Veldora. I should be able to handle it.")
			sprint("However, I don't think I have any ways to attack or damage it if it's hostile. Hmmmmmm. I wonder...")

			ssprint("<Choose ability to learn and use on tempest serpent>")
			add_level_mob('tempest serpent')
			action_menu(self)

		def _try_escaping(self):
			sprint("Alright, lets try out this new skill.")
			add_level_mob(['giant bat', 'black spider', 'evil spider'])
			action_menu(_after_serpent())

		def _learn_water_bullet(self):
			rimuru.add_attribute('water bullet')
			ssprint("Nice, it worked. After learning [Hydraulic Propulsion], I was thinking I could use water as an attack too.")
			action_menu(_attack_serpent())

		def _learn_water_blade(self):
			rimuru.add_attribute('water blade')
			ssprint("Hey, it worked. Since I already have [Hydraulic Propulsion], I was thinking I could use super high pressure water as a blade attack also.")
			action_menu(_attack_serpent())

	class _attack_serpent:
		def __init__(self):
			ssprint("Now I have a way to attack.")
			ssprint("<Target the Tempest Serpent, then attack with your new skill. 'help' for more info.>")
			action_menu(self)

		def _predate_ore(self): pass

		def _attack(self):
			if not get_mob_status('tempest serpent'):
				sprint("Wow, what a powerful attack. I probably shouldn't use that so openly.")
				ssprint("<<Notice, would you like to use Unique Skill [Predator]?>>")
				sprint("Oh...? What will that do?")
				ssprint("<<Answer, after predation, information and targets skills may be obtained through analysis.>>")
				action_menu(_after_serpent())
			else:
				action_menu(self)

	class _after_serpent:
		def __init__(self):
			add_level_mob(['giant bat', 'black spider'])
			sprint("Are those bats?")
			ssprint("<<Answer, They are [Giant Bat].>>")
			action_menu(self)

		def predate_ore(self):
			rimuru.add_inventory('magic ore')
			ssprint("More of this, might be useful for later.")
			action_menu(self)

		def _sneak_away(self):
			ssprint("I'll try to sneak away.")
			action_menu(_at_exit())

		class _attack:
			def __init__(self):
				if get_mob_status('black spider'):
					sprint("What now...A Spider. Nobody likes spiders, especially giant ones.")

				if get_mob_status('evil centipede'):
					sprint("For real, now a centipede. I just want to get out of this cave already.")
				else:
					action_menu(_at_exit())

				action_menu(_after_serpent)

	class _at_exit:
		def __init__(self):
			sprint("Finally! Found the exit. Wow, that's a pretty big door. How am I going to open that?")
			sprint("Water attack? No, that'll probably be overkill. Wait somethings happening.")
			sprint("*The giant pair of doors slowly creeks open, and three adventurers shows themselves.*")
			sprint("What should I do... I can wait and try to sneak past them if they're going in")
			sprint("Adventurer 1: Phew, it's finally open, even the keyhole was rusted.")
			sprint(
				"Adventurer 2: It is over 300 years old, and nobody is maintaining it. I doubt there's a real dragon in here.")
			sprint("Adventurer 2: Still reckless of the guildmaster to send us to investigate.")
			sprint("I shouldn't show, they'll probably get scared and attack me")

			action_menu(self)

		def _sneak_out(self):
			ssprint("I'll try sneaking out after they go in.")
			sprint("Finally! I'm out of that cave. Where now to though?")
			continue_story(rimuru, Chapter3)

		def _say_hi(self):
			sprint("HELLO THERE!")
			sprint("Adventurers: AHHHHH MONSTER. KILL IT. KILL IT. KILL IT!!!!")
			sprint("WAIT, Wait. I'm a friendly slime! Slurrrr.....")
			ssprint("*The adventurers attacked and killed the little slime monster before he could say anything else.*")

			if rimuru.check_mob_has('veldora'):
				ssprint("*After the little slime died. All of his stomach contents spewed outwards.*")
				ssprint("*Unfortunately this particular slime had somehow absorbed a dragon locked in [Infinity Prison].*")
				ssprint(
					"*The three adventurers where crushed by such a massive object. They Have failed there simple mission*")
			delete_game_save(rimuru)

	chapter_2()
