import os, pickle
from time import sleep
import game_files.game_characters as mobs
import game_files.game_art as art

debug_mode = False

rimuru = None


def update_character(character):
	global rimuru
	rimuru = character
	return rimuru


def action_menu(current_class):
	"""
	Takes user input and runs corresponding actions.


	Args:
		current_class: Current story progress class object.

	Usage:
		> inv
		> stats
		> attack tempest serpent with water blade
	"""

	# Gets class functions and subclasses if it doesn't start with __
	class_funcs = [i for i in dir(current_class) if i[1] != '_']
	funcs = [i.replace('_', ' ') for i in class_funcs]
	# Functions starting with _ replaced with *, then replaces _ with space
	actions = [('*' + i[1:]) if i[0] == '_' else i for i in class_funcs]
	actions = [i.replace('_', ' ') for i in actions]

	show_hud(actions)

	if debug_mode:
		for i in actions:
			if i[0] == '*':
				user_input = i[1:]

	else:
		user_input = input("\n> ").lower()
		print()

	# Get info on skills, times, etc
	split_user_input = user_input.split(' ')
	command = split_user_input[0]
	parameter = ' '.join(split_user_input[1:])

	level_actions = {
		'target': rimuru.set_targets,
		'predate': rimuru.predate_targets,
		'mimic': rimuru.use_mimic,
		'help': show_help,
		'inv': rimuru.show_inventory,
		'stats': rimuru.show_attributes,
		'info': rimuru.show_info,
		'exit': exit,
	}
	if 'attack' in command:
		if rimuru.attack(parameter):
			user_input = 'attack'
	if 'use' in command:
		rimuru.use_skill(parameter, character=rimuru)


	for k, v in level_actions.items():
		if k in command:
			v(parameter)

	loop = True

	for i in actions:
		current_action = i.replace('*', '_').replace(' ', '_')
		run_action = f'current_class.{current_action}()'
		if i[0] == '*':
			if user_input.lower() == i.lower()[1:]:
				eval(run_action)
				loop = False
				break
		else:
			if user_input.lower() == i.lower():
				eval(run_action)

	if loop:
		action_menu(current_class)


def show_hud(actions):
	"""Shows user HUD with available actions and targets (if any)."""

	# Adds () around actions, (*action)
	options = ', '.join('(' + i + ')' for i in actions)
	mimicking = rimuru.current_mimic_name
	try:
		targets, = ', '.join([(i.name if i.alive else f'{i.name}(Dead)') for i in rimuru.focused_targets]),
	except:
		targets = None

	if targets:
		# print(f'\nTarget:', str(targets))
		print(f'\nTarget: {targets}\nActions:', options, f'| {mimicking}, (stats, inv, help)')
	else:
		print("\nActions:", options, f'| {mimicking}, (stats, inv, help)')


def get_mob_status(target):
	"""
	Returns whether mob in current_mob list is alive.

	Args:
		target: Target to check alive status.

	Usage:
		.get_mob_status('tempest serpent')
	"""

	for i in rimuru.current_level_characters:
		if target.lower() in i.get_name():
			if i.alive:
				return True


def add_level_mob(characters):
	"""
	Adds new mob to current level in game.

	Args:
		level_characters: Mob character(s) to add to current level. Can be single mob (string) or multiple (list).

	Usage:
		.add_level_mob('tempest serpent')
		.add_level_mob(['tempest serpent', 'giant bat'])
	"""
	if type(characters) == list:
		for i in characters:
			mob = rimuru.get_object(i, new=True)
			if mob:
				rimuru.current_level_characters.append(mob)
	else:
		mob = rimuru.get_object(characters, new=True)
		rimuru.current_level_characters.append(mob)


#                    ========== Extra ==========
def tbc():
	""" To Be Continued function."""
	print("---TO BE CONTINUED---")
	input("Press Enter to exit > ")


#                    ========== Game Saves ==========
def save_game(rimuru_object):
	"""
	Save game state.

	Args:
		rimuru_object: Game state object to save.
	"""

	pickle.dump(rimuru_object, open(rimuru_object.save_path, 'wb'))
	print("Game Saved To: player_save.p")


def load_save_game(path):
	"""
	Load game save.

	Args:
		path: Path of game save.

	Returns:
		Loaded game save object.
	"""

	try:
		rimuru = pickle.load(open(path, 'rb'))
		print("Loaded Player Save\n")
	except:
		rimuru = mobs.Rimuru_Tempest()
	return rimuru


def delete_game_save(rimuru_object):
	"""
	Deletes game save.

	Args:
		rimuru_object: Deletes game save object.
	"""
	os.remove(rimuru_object.save_path)
	print("Resetting Game. Deleted player_save.p\n")


def continue_story(rimuru_object, next_chapter):
	"""
	Continues story progress from last save point.

	Args:
		rimuru_object: Save state object.
		next_chapter: Next chapter to play.
	"""

	print("Continue to next chapter?")
	user_input = input("Y/N > ")
	rimuru_object.story_progress.append(next_chapter)
	save_game(rimuru_object)
	if user_input.lower() == 'y':
		next_chapter(rimuru_object)
	else:
		exit()


#                    ========== Game Functions ==========
def show_start_banner(rimuru):
	"""Show game start banner."""

	print("\n----------Tensei Shitara Slime Datta Ken (That Time I Got Reincarnated as a Slime)----------\n")
	instructions = """
    NOTE: 
    - Set window size for ASCII art accordingly (Fullscreen recommended)
    - Access help, inventory and skills with help, inv and stats
    - * actions continues story (do NOT actually input *, or ()). Try the other actions first maybe, see what happens
    - Delete player_save.p to reset game progress (includes player inventory and skills)
    """
	print(instructions)
	rimuru.show_attributes()
	rimuru.show_inventory()
	print()


def ssprint(Msg):
	"""Print tabbed in message."""
	sprint(f'    {Msg}')


def sprint(Msg):
	"""
	Delay text in game.

	Args:
		Msg: Message to delay.
	"""

	msg_len = len(str(Msg))
	if rimuru.text_delay:
		if msg_len > 100:
			sleep_time = 1
		elif msg_len > 70 and msg_len > 80:
			sleep_time = 4
		elif msg_len > 50 and msg_len > 40:
			sleep_time = 3
		elif msg_len > 40 and msg_len > 20:
			sleep_time = 2
		elif msg_len < 10:
			sleep_time = 2
		elif msg_len < 5:
			sleep_time = 1
		else:
			sleep_time = 1
	else:
		sleep_time = 0

	print(Msg, '\n')
	sleep(sleep_time)


def show_help(*args):
	"""Shows help page."""

	print("""
    Commands:
        target TARGET(s)            -- Target mobs. E.g. 'target tempest serpent'
        attack with SKILL			-- Attack targeted. E.g. 'attack with water blade'
        use SKILL                	-- Use a skill. E.g. 'use sense heat source'
        stats                       -- Show yours skills and resistances. 
          - stats TARGET            -- Stats for monsters you have predated. E.g. 'stats tempest serpent'
        inv                         -- Show inventory.
        info                        -- Show info on skill, item or character. E.g. 'info great sage, 'info hipokte grass', 'info tempest serpent'
        help                        -- Show this help page.
        exit                        -- Exit game.

    Abilities:
        mimic ___                   -- Mimics appearance of of predated. E.g. 'mimic tempest serpent'
          - info mimic              -- Shows available mimicries.
          - mimic reset             -- Resets mimic (Back to slime).
        predate                     -- Predate target(s). Can only predate mobs that are focused.

    Game Dialogue:
        ~Message~                   -- Telepathy, thought communication.
        *Message*                   -- Story context.
        <Message>                   -- Game info, acquisition, etc.
        <<Message>>                 -- Great Sage (Raphael, Ciel).
        <<<Message>>>               -- Voice of the World.

    HUD:
        Target: Currently Focused Target(s)
        Actions: (ACTION(s)) | MIMIC, (Extra Actions)
      E.g.
        Target: Giant Bat, Black Spider
        Actions: (*Attack), (*Move on) | Tempest Serpent, (stats, inv, help)

    Level/Ranking:
       Level      Rank         Risk
        11.     Special S   Catastrophe
        10.     S           Disaster
        9.      Special A   Calamity
        8.      A+          Tragedy
        7.      A           Hazard
        6.      A-          Danger
        5.      B           Pro
        4.      C           Advance
        3.      D           Intermediate
        2.      E           Beginner
        1.      F           Novice
    """)
