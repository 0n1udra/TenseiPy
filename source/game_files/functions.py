import pickle, time, sys, os
import game_files.art as game_art
from game_files.extra import *
from game_files.characters import Rimuru_Tempest


# I'm not exactly sure what actions will be taken in debug_mode, but so far it does get to the end of a chapter.
rimuru = Rimuru_Tempest()


# start_game.py will load game save if user has one, if not it'll create one.
# Then pass that into update_character which will update the rimuru variable to be used here and any other file that imports this file.
def update_rimuru(rimuru_object):
    """Update rimuru object to be used in rest of game files."""

    global rimuru
    rimuru = rimuru_object
    return rimuru


#                    ========== Level Functions ==========
def game_hud(actions):
    """Show game HUD, includes current mimic, mobs targeted, and available actions."""

    if rimuru.show_hud is False or rimuru.hardcore is True: return

    if rimuru.current_mimic or rimuru.targeted_mobs or rimuru.show_hud: print()  # Adds extra space when needed.

    if rimuru.current_mimic:
        print(f"Mimic: [{rimuru.current_mimic.name}]")  # Only show if currently using mimic.

    if rimuru.targeted_mobs:
        # Adds X status to corresponding targets that are dead.
        targets = ', '.join([(f'x{mob[1]}({mob[0].name})' if mob[0].is_alive else f'Dead-x{mob[1]}({mob[0].name})') for mob in rimuru.targeted_mobs])
        print(f'Target: {targets}')

    if rimuru.show_hud:
        # Formats actions available to user. Replaces _ with spaces and adds commas when needed.
        actions_for_hud = ' '.join([f"({action.replace('_', ' ').strip()})" for action in actions if 'hfunc' not in action])
        print(f"Actions: {actions_for_hud}", end='')

def game_action(level=None):
    """
    Updates player's location, Shows HUD, takes user input and runs corresponding actions.

    Args:
        level obj: Current story progress class object.

    Usage:
        > inv
        > stats
        > attack tempest serpent with water blade
    """

    rimuru.update_location(rimuru.get_location_variable(level))  # Updates player's location.

    actions = []
    for action in dir(level):  # Gets subclass functions.
        if '__' in action: continue  # Filters out unwanted variables and functions.
        actions.append(action)

    game_hud(actions)

    # ========== Debug Mode
    # Runs first available action that will progress the storyline.
    if rimuru.fast_mode is True:
        for action in actions:
            if action[0] == '_':
                user_input = action.replace('_', ' ').strip()
    else:
        user_input = input("\n> ").strip().lower()
        if 'hfunc' in user_input: game_action(level)  # So user can't so easily activate 'hfunc' actions.
        # Removes anything that's not alpha-numeric, easier for making __subs.
        user_input = ''.join(i for i in user_input if i.isalnum() or ' ')
        print()

    # Separates user input into command and command arguments.
    split_user_input = user_input.split(' ')
    command, parameters = split_user_input[0], ' '.join(split_user_input[1:])
    user = rimuru

    # [correspond_game_function, [optional_parameters], ['user_input_to_match_to']
    game_actions = [
        [rimuru.show_info, ['info']],
        [rimuru.show_inventory, ['inv']],
        [rimuru.show_attributes, ['stats']],
        [rimuru.set_targets, ['target']],
        [rimuru.attack, [parameters], ['attack']],
        [rimuru.use_action, [parameters, user], ['use']],
        [rimuru.craft_item, ['craft']],
        [rimuru.remove_inventory, ['remove']],
        [rimuru.eat_targets, ['eat', 'predate']],
        [rimuru.use_mimic, ['mimic']],
        [rimuru.show_mimics, ['mimics', 'mimicries']],
        [rimuru.show_nearby, ['nearby']],
        [rimuru.get_location, ['location']],
        [show_help, ['help']],
        [change_settings, ['settings', 'options']],
        [show_history, ['history']],
        [game_restart, ['restart']],
        [game_exit, ['exit']],
    ]

    # Passes in user inputted arguments as parameters and runs corresponding action.
    for action in game_actions:
        # If action needs custom parameters passed in.
        if len(action) == 3 and command in action[2]:
            action[0](*action[1])

        # Run matched corresponding game function and pass rest of user input as parameter.
        if command in action[1]:
            action[0](parameters)

    for action in actions:
        # Currently need two evals to find __subs for action.
        try: action_subs = eval(f"level.{action}.{action}__subs")
        except: action_subs = []
        try: action_subs = eval(f"level.{action}._{action}__subs")
        except: pass

        # Usually used for when you want an action to be used only once.
        if 'ACTIONBLOCKED' in action_subs: continue

        # Adds action's class name to subs list, so you don't have to add it yourself in the chapter files.
        action_subs.append(action.replace('_', ' ').strip().lower())

        # play game action.
        if get_any(user_input, action_subs):
            rimuru.add_played_action(action_subs[-1])  # Check using game_cond('action_name') function.
            eval(f"level.{action}()")

    game_action(level)

def game_cond(game_var, new_value=None):
    """
    Set and fetch game variables.

    Args:
        game_var str: Gameplay variable to find and return.

    Returns:
        str, bool, int, obj: Returns gameplay variable if found or if new one was set.
    """

    # Set new value to a game conditional.
    if new_value:
        rimuru.game_conditions[game_var] = new_value
        return new_value

    # Return game conditional data if found.
    if game_var in rimuru.game_conditions:
        return rimuru.game_conditions[game_var]
    if game_var in rimuru.played_actions:
        return rimuru.played_actions[game_var]
    return False

def played_action(match, amount=1):
    """
    Checks if game action has been played.

    Args:
        match obj: Pass in game level object to check if it has been played already.

    Returns:
        bool True: Returns True if game action has been played.

    Usage:
        played_action(self)
    """

    # Extracts and parses level action name from passed in level object.
    # E.g. Extracts "speak now" from "<class 'chapters.tensei_1.ch1_cave.<locals>.wake_up.speak_now'>"
    match_action = str(match.__class__).split('.')[-1].replace('_', ' ')[:-2].strip()

    # Checks if action has been played more than once.
    if game_cond(match_action) > amount:
        return True

def last_use_skill(skill):
    """
    Checks what was the last successfully used skill.

    Args:
        skill str: Skill to check if that was the last skill used.

    Returns:
        obj: Returns game skill object if match.
        bool False: If not match.
    """

    if not rimuru.last_use_skill: return  # If last_use_skill var is not set.

    if skill.lower() in rimuru.last_use_skill.name.lower():
        return rimuru.last_use_skill
    return False

def mobs_add(add_mobs):
    """
    Add new mob to current level, and able to set name at creation.

    Args:
        add_mobs str: Adds mob objects to active_mobs list.
            'X*mob': Number of that mob to add.
            'mob:name': Set mob's name when game character object is initialized.

    Usage:
        mobs_new(['tempest serpent'])
        mobs_new(['tempest serpent', 'giant bat'])
        mobs_new(['10* goblin', 'goblin: Goblin Chief'])
        mobs_new(['50* goblin: Goblinas'])
    """

    for new_mob in add_mobs:
        amount = 1
        # Add multiple of same mob, e.g. ['5*goblin']
        if '*' in new_mob:
            amount, new_mob = new_mob.split('*')
            try: amount = int(amount)
            except: pass

        # Sets mob name when creating new Character object, e.g. ['goblin name: Goblin Chief']
        if ':' in new_mob:
            new_mob, new_name = new_mob.split(':')
        else: new_name = ''

        if mob_object := rimuru.get_object(new_mob.strip(), new=True):
            rimuru.active_mobs.append([mob_object(new_name.strip()), amount])

def mob_status(target):
    """
    Returns whether mob in active_mobs list is is_alive.
    Returns character objects is_alive var.

    Args:
        target str: Target character to check is_alive status.

    Usage:
        mob_status('tempest serpent')

    Returns:
        Bool: Character's is_alive var.
    """

    for i in rimuru.active_mobs:
        if target.lower() in i[0].name.lower():
            return i[0].is_alive

def mobs_cleared():
    """
    Checks if mobs on current level are all dead.

    Returns:
        boolean: If all mobs in active_mobs are dead.

    Usage:
        if mobs_cleared():

    Returns:
        Bool: If all mobs in active_mobs list are dead.
    """

    # If just one mob's is_alive boolean var is True this function will return False.
    for mob in rimuru.active_mobs:
        if mob[0].is_alive: return False
    return True

def mobs_reset():
    """Resets active_mobs and targeted_mobs list."""

    rimuru.active_mobs.clear()
    rimuru.targeted_mobs.clear()

def get_level_mob(mob):
    """
    Get's mob's game object from active_mobs list.

    Args:
        mob str: Name of mob in active_mobs list you want the object of.

    Returns:
        obj: Returns mob's game object if match found.
    """

    # Returns mob's game object. The second item in the list is the number of mobs in gameplay.
    for i in rimuru.active_mobs:
        if mob in i[0].name.lower(): return i[0]

def continue_to(next_location):
    """
    Saves game and continues to next location.

    Args:
        next_location: Next chapter to play.
    """

    rimuru.current_location_object = next_location
    game_save()

    # Loads next story chapter.
    try: next_location()
    except: print("    < Error Loading Next Location >")

def clear_subs(action):
    """
    Clears __subs list of passed in class.
    Adds 'ACTIONBLOCK' string to action's __subs list.
    game_action function will see that 'ACTIONBLOCK' string is in the __subs list and will not allow player to do action.

    Args:
        level: Playable action class object from chapter file.
    """

    for i in dir(action):
        if '__subs' in i: eval(f"action.{i}.append('ACTIONBLOCKED')")


#                    ========== Game Save/Settings ==========
def game_restart(*args):
    """Restart game."""

    print("    < Restarting Game... >")
    os.execl(sys.executable, sys.executable, *sys.argv)

def game_exit(*args):
    """Saves game using pickle, then exits."""

    #game_save()
    exit(0)

def game_save(level=None, show_msg=True):
    """
    Pickels Rimuru_Tempest object.

    Args:
        level [bool]: Update rimuru.current_location_object
        show_msg [bool:True]: Show Game Saved message.
    """

    global rimuru

    # Can specify what level to save at.
    if level: rimuru.current_location_object = level

    # If called from game_over function, the save will no longer be usable.
    if rimuru.valid_save is None:
        rimuru.valid_save = True

    pickle.dump(rimuru, open(rimuru.save_path, 'wb'))

    if show_msg: print("\n    < Game Saved >\n")

def game_load(path):
    """
    Load game save.

    Args:
        path: Path of game save.

    Returns:
        Loaded game save object.
    """

    global rimuru

    # Tries loading game. If can't, creates new Rimuru_Tempest object which contains all game data that will be picked.
    if os.path.isfile(path):
        rimuru = pickle.load(open(path, 'rb'))
        return rimuru

    import chapters.tensei_1 as tensei1
    rimuru.current_location_object = tensei1.ch1_cave
    rimuru.save_path = path

    # If game save is invalid (using game_over function), save file will be deleted and game will restart.
    if rimuru.valid_save is False:
        os.remove(rimuru.save_path)
        game_load(path)

    return rimuru

def game_over():
    """Player died, deletes pickle save file after invalidates it.."""

    global rimuru
    rimuru.valid_save = False  # So you can't use this save file anymore.
    game_save(show_msg=False)

    # Deletes player's save file.
    try: os.remove(rimuru.save_path)
    except: pass

    print("\n    < GAME OVER >\n\nPlay again?")
    if str(input('No / Yes or Enter > ')).lower() in ['n', 'no']:
        exit(0)
    else:
        game_restart()


#                    ========== Game Printing/Output ==========
def sprint(message, from_print='sprint', showing_history=False, no_crawl=False):
    """
    Text crawling. Slowly print out text to console. Kinda like typewriter effect.

    Args:
        message str: Message to delay print.
        from_ssprint bool(False): Variable used to properly print out lines for 'history' game commmand.
        from_iprint bool(False): If coming from iprint function.
        showing_history bool(False): Variable used to make sure 'history' command doesn't effect itself.
    """

    # Will not use textcrawl effect on gameplay hint printouts.
    if ('< Hint:' in message) and (not rimuru.show_hints or rimuru.hardcore): return

    # So user can get the last x lines, in case the screen has been cluttered.
    # Without this, when showing history it'll add onto itself, which creates duplicate lines.
    if showing_history is False:
        rimuru.line_history.append([message, from_print])
        rimuru.line_history = rimuru.line_history[-25:]

    if rimuru.textcrawl is True and no_crawl is False:
        message_length = len(message)

        # Textcrawl speed based on message character length.
        if message_length > 200:
            total_time = 0.1
        elif message_length > 50:
            total_time = 3
        elif message_length > 25:
            total_time = 1.5
        elif message_length > 10:
            total_time = 1
        else:
            total_time = 2

        # Use sys module to print letter by letter and time module for delay between each letter.
        sleep_time = total_time / message_length
        for letter in message:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(sleep_time)
        print()

    else:
        print(message)  # Print instantly.

def siprint(message, showing_history=False):
    """sprint with indent."""

    if message[0] == '\n': print()
    sprint('    ' + message.lstrip(), from_print='siprint', showing_history=showing_history)

def iprint(message, showing_history=False):
    """Print without textcrawl and with indent."""
    if message[0] == '\n': print()
    sprint('    ' + message.lstrip(), no_crawl=True, showing_history=showing_history)

def dots(length=5, times=1, indent=False):
    """
    Loading dot animation.

    Args:
        times int(3): How many times to do animation.
        length int(5): How many dots per cycle.
        indent bool(False): Add 4 spaces.
    """

    # If textcrawl boolean is False, it'll just print the dots once.
    if not rimuru.textcrawl:
        print(('    ' if indent else '') + '.' * length)
        return

    for _ in range(times):
        if indent: print('    ', end='')  # Print out dots instantly instead.

        for _ in range(length):
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(0.5)
        print()

def idots(*args):
    """Prints dots but wth indent."""

    dots(*args, indent=True)

def show_art(art):
    """
    Prints out ASCII art line by line or all at once depending on textcrawl boolean.

    Args:
        art str: Name of variable that is located in art.py file. The functions will replace spaces with _ if needed.
    """

    if rimuru.show_art is False: return False

    # Gets corresponding variable from within art.py file.
    art = eval(f"game_art.{art.lower().strip().replace(' ', '_')}")

    if rimuru.textcrawl or rimuru.textcrawl is None:
        # Print ASCII art line by line with quick textcrawl effect.
        for line in art.split('\n'):
            time.sleep(0.05)
            print(line)
    else:
        print(art)  # Instantly print out ASCII art to screen.

def show_history(arg):
    """
    Shows x of last outputted story lines.

    Args:
        arg: Lines to show. Default is 5.
    """

    # Defaults to 5 lines to show of dialog history.
    try: lines = int(arg)
    except: lines = 5

    # Runs corresponding function to print out gameplay dialog based on what was used in hard code.
    for line in rimuru.line_history[-lines:]:
        if line[1] == 'iprint':
            iprint(line[0], showing_history=True)
        elif line[1] == 'iprint':
            sprint(line[0], showing_history=True)
        elif line[1] == 'siprint':
            siprint(line[0], showing_history=True)
        else:
            print(line[0])

def show_start_banner():
    """Show game title, tips, and player stats/inv."""

    show_art('great sage')
    print(f"""
    ----------Tensei Shitara Slime Datta Ken (That Time I Got Reincarnated as a Slime)----------
    {game_art.rimuru_art.banner}
    - Basic commands: stats, inv, info, settings, and help for more.
    - Fullscreen recommended.
    """)

    if rimuru.valid_save is True:
        print("\n    < Save Loaded >\n")  # Show's if game was loaded from a save.

def change_settings(user_input):
    """
    Show or change game settings.

    Args:
        user_input: Get input from game_action function.

    Usage:
        > settings
        > settings hud on
        > options hud hints off
    """

    new_value = None
    # Tries to extract game settings and on/off section from user_input.
    try:
        split_input = user_input.split()
        # Checks if player wants to enable/disable a setting.
        if get_any(split_input[-1], off_subs):
            new_value = False
        elif get_any(split_input[-1], on_subs):
            new_value = True
        # User can change multiple game settings with one go.
        settings_input = ''.join(user_input[:-1])
    except: new_value = None

    # If not detected game settings with usable on/off data from user_input.
    if not user_input or new_value is None:
        show_settings()
        return

    if 'textcrawl' in settings_input:
        rimuru.textcrawl = new_value
    if 'hardcore' in settings_input:
        rimuru.hardcore = new_value
    # strict_match is false so user can change multiple game settings in one go.
    if get_any(settings_input, ['hud', 'interface'], strict_match=False):
        rimuru.show_hud = new_value
    if get_any(settings_input, ['art', 'ascii'], strict_match=False):
        rimuru.show_art = new_value
    if get_any(settings_input, ['hints', 'clues'], strict_match=False):
        rimuru.show_hints = new_value

    show_settings()


def show_settings(*args):
    """Shows game settings and there current on/off state."""

    print(f"""    Game Settings:
        {on_off(rimuru.textcrawl)}\ttextcrawl <on/off>\t-- Enable or disable text crawl effect.
        {on_off(rimuru.show_hud)}\thud/interface <on/off>\t-- Show available actions player can take.
        {on_off(rimuru.show_art)}\tart/ascii <on/off>\t-- Show ASCII art.
        {on_off(rimuru.show_hints)}\thints/clues <on/off>\t\t-- Show game hints, highly recommended for first timers.
        {on_off(rimuru.hardcore)}\thardcore <on/off>\t-- Enable hardcore mode.
    
    Change Settings:
        settings/options COMMAND(S) on/off
        Example: 'settings textcrawl off', 'options hud hints off'""")

def show_help(arg):
    """Shows help page."""

    if get_any(arg, ['rank', 'level', 'ranking', 'showrank', 'showlevel'], strict_match=False):
        show_rank_chart()
        return

    print("""    Command Required_Parameter [Optional_Parameter]
    
    Commands:
        inv                     -- Show inventory.
        stats [TARGET]          -- Show skills and resistances. attribute also works.
                                   Example: 'stats tempest serpent', 'attributes evil centipede'
        info TARGET             -- Show info on skill, item or character. 
                                   Example: 'info great sage, 'info hipokte grass', 'info tempest serpent'
        target TARGET(S)        -- Target mob(s), to be able to use skills/abilities/etc on them.
                                   Example: 'target tempest serpent', 'target tempest serpent, black spider'
          - target nearby       -- Target nearby mobs.
          - target reset        -- Clear targeted.
        attack SKILL/ITEM 	    -- Attack targeted_mobs. 
                                   Example: 'attack water blade'
        use SKILL/ITEM          -- Use a skill.
                                   Example: 'use sense heat source'
        craft ITEM [amount]     -- Craft items if have necessary ingredients. 
                                   Example: 'craft full potion', 'craft full potion 10'
                                   Note: Some items are crafted in batches, suggest reading the item's info page for the recipe and more.
        mimic TARGET            -- Mimics appearance and attributes of analysed mob.
                                   Example: 'mimic tempest serpent'
          - info mimic          -- Shows available mimicries.
          - mimic reset         -- Resets mimic (Back to slime).
        eat/predate             -- Predate target(s). Can only eat mobs that are targeted_mobs and dead.
        nearby                  -- Show's neearby mobs if acquired [Magic Perception] skill.
        help                    -- Show this help page.
          - help rank           -- Show game level, rank, risk chart.
        settings                -- Show commands to change/set game settings, like textcrawl, hardcore, art, and menu.
                                Example: 'settings hud off', 'options hud hints on'
        exit                    -- Exits after save.

    Game Dialogue:
        ~ Message ~             -- Telepathy, thought communication.
        * Message *             -- Story context.
        < Message >             -- Game info, acquisition, game help, etc.
        << Message >>           -- Great Sage (Raphael, Ciel).
        <<< Message >>>         -- Voice of the World.""")

def show_rank_chart(*args):
    """In universe ranking chart."""

    print("""    Level/Ranking:
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
        1.      F           Novice""")
