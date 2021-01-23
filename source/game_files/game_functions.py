import keyboard, pickle, time, sys, os
import game_files.game_art as game_art
import game_files.game_characters as mobs

# I'm not exactly sure what actions will be taken in debug_mode, but so far it does get to the end of a chapter.
rimuru = None
fast_mode = False
on_subs = ['activate', 'true', 'enable', 'on', '1']
off_subs = ['deactivate', 'false', 'disable', 'off', '0']
move_subs = ['explore', 'wonder', 'move', 'move on', 'move forward', 'keep moving', 'keep exploring', 'explore more', 'explore further', 'keep fumbling', 'fumble around more', 'fumble more', 'bounce around more', 'keep bouncing', 'just move on', 'keep moving forward', 'continue forward', 'continue exploring']
wait_subs = ['wait', 'stay']

# start_game.py will load game save if user has one, if not it'll create one.
# Then pass that into update_character which will update the rimuru variable to be used here.
def update_rimuru(rimuru_object):
    global rimuru
    rimuru = rimuru_object
    return rimuru

def set_fast_mode():
    global fast_mode
    rimuru.textcrawl = rimuru.show_art = False
    fast_mode = True

def action_menu(level=None, hide_actions=False):
    """
    Updates player's location, Shows HUD, takes user input and runs corresponding actions.


    Args:
        level: Current story progress class object.

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

    if hide_actions is True:
        del actions[actions.index(hide_actions)]  # Removes action so player can't take it.

    # ========== HUD
    if rimuru.current_mimic or rimuru.targeted_mobs or rimuru.show_menu: print()  # Adds extra space when needed.

    if rimuru.current_mimic and not rimuru.hardcore:
        print(f"Mimic: [{rimuru.current_mimic.name}]", end='')

    if rimuru.targeted_mobs and not rimuru.hardcore:
        # Adds (Dead) status to corresponding
        targets = ', '.join([(f'{mob[1]}({mob[0].name})' if mob[0].is_alive else f'X-{mob[1]}({mob[0].name})') for mob in rimuru.targeted_mobs])
        print(f'Target: {targets}', end='')

    if rimuru.show_menu and not rimuru.hardcore:
        # Formats actions available to user. Replaces _ with spaces and adds commas when needed.
        actions_for_hud = ' '.join([f"({action.replace('_', ' ').strip()})" for action in actions if 'hfunc' not in action])
        print(f"Actions: {actions_for_hud}", end='')

    # ========== Debug Mode
    # Runs first available action that will progress the storyline.
    if fast_mode is True:
        for action in actions:
            if action[0] == '_':
                user_input = action.replace('_', ' ').strip()
    else:
        user_input = input("\n> ").strip().lower()
        if 'hfunc' in user_input: action_menu(level)
    print()

    # Separates user input into command and command arguments.
    split_user_input = user_input.split(' ')
    command, parameters = split_user_input[0], ' '.join(split_user_input[1:])
    character = rimuru

    level_actions = {
        'target': rimuru.set_targets,
        'mimic': rimuru.use_mimic,
        'eat': rimuru.eat_targets, 'predate': rimuru.eat_targets,
        'stats': rimuru.show_attributes, 'skills': rimuru.show_attributes, 'attributes': rimuru.show_attributes,
        'inv': rimuru.show_inventory, 'inventory': rimuru.show_inventory,
        'info': rimuru.show_info, 'data': rimuru.show_info,
        'map': rimuru.get_map,
        'craft': rimuru.craft_item,
        'help': show_help,
        'menu': game_set_menu, 'showmenu': game_set_menu,
        'art': game_set_art, 'showart': game_set_art,
        'textcrawl': game_set_textcrawl,
        'hardcore': game_set_hardcore,
        'history': show_history, 'lines': show_history,
        'exit': game_exit, 'stop': game_exit, 'quit': game_exit,
        'restart': game_restart,
    }
    if 'attack' in command:
        if rimuru.attack(parameters):
            user_input = 'attack'  # Runs correlating function if attack was successful, if not it'll just loop.
    elif 'use' in command:
        rimuru.use_skill(parameters, character)
    elif 'location' in command:
        rimuru.get_location()
    elif 'nearby' in command:
        rimuru.use_skill('sense heat source', character)

    # Passes in user inputted arguments as parameters and runs corresponding action.
    for action_string, action in level_actions.items():
        if action_string in command:
            action(parameters)

    valid_action = False

    for action in actions:
        try:
            action_subs = eval(f"level.{action}.{action}__subs")
        except:
            action_subs = []
        try:
            action_subs = eval(f"level.{action}._{action}__subs")
        except: pass

        action_name = action.replace('_', ' ').strip().lower()
        if action_name in user_input or any(i in user_input for i in action_subs):
            eval(f"level.{action}()")
            valid_action = True

    if not valid_action:
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2k')
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2k')
        sys.stdout.write('\x1b[1B')

    action_menu(level)


#                    ========== Level Functions ==========
def game_conditions(value, new_value=None):
    """ Set and fetch game variables. """
    if new_value:
        rimuru.conditional_data[value] = new_value
        return rimuru.conditional_data[value]

    if value in rimuru.conditional_data:
        return rimuru.conditional_data[value]
    else:
        return False

def mobs_new(add_mobs):
    """
    Add new mob to current level, and able to set name at creation.

    Args:
        add_mobs: Adds mob objects to active_mobs list.

    Usage:
        mobs_new(['tempest serpent'])
        mobs_new(['tempest serpent', 'giant bat'])
        mobs_new(['10* goblin', 'goblin: Goblin Chief'])
        mobs_new(['50* goblin: Goblinas'])
    """

    for new_mob in add_mobs:
        amount = 1
        if '*' in new_mob:
            amount, new_mob = new_mob.split('*')  # Add multiple of same mob, e.g. ['5 * goblin']
            try:
                amount = int(amount)
            except:
                pass

        if ':' in new_mob:
            new_mob, new_name = new_mob.split(':')  # Sets mob name when creating new Character object, e.g. ['goblin name: Goblin Chief']
        else:
            new_name = None

        if mob_object := rimuru.get_object(new_mob, new=True):
            if new_name:
                mob_object.name = new_name.strip()

            rimuru.active_mobs.append([mob_object, amount])

def mob_status(target):
    """
    Returns whether mob in active_mobs list is is_alive.

    Args:
        target: Target to check is_alive status.

    Usage:
        mob_status('tempest serpent')
    """

    for i in rimuru.active_mobs:
        if target.lower() in i[0].get_name():
            return i[0].is_alive

def mobs_cleared():
    """
    Checks if mobs on current level are all dead.

    Returns:
        boolean: If all mobs in active_mobs are dead.

    Usage:
        if mobs_cleared():
    """

    for mob in rimuru.active_mobs:
        if mob[0].is_alive:
            return False
    else:
        return True

def mobs_reset():
    """ Resets active_mobs and targeted_mobs list. """

    rimuru.active_mobs.clear()
    rimuru.targeted_mobs.clear()

def continue_to(continue_to):
    """
    Saves game and asks if player wants to continue to next location.

    Args:
        continue_to: Next chapter to play.
    """

    rimuru.current_location_object = continue_to
    game_save()
    try:
        continue_to(rimuru)
    except:
        print("    < Error Loading Next Location >")


#                    ========== Extra ==========
def tbc():
    """ To Be Continued message.."""

    print("\n    < ---IN PREOGRESS--- >\n")
    input("Press Enter to exit > ")

def show_art(art):
    """
    Prints out ASCII art line by line or all at once dependding on textcrawl boolean.

    Args:
        art: Name of variable that is located in game_art.py file. The functions will replace spaces with _ if needed.
        textcrawl [bool:False]: Use textcrawl effect ignoring rimuru.show_art variable.

    """

    if rimuru.show_art is False: return False

    # Gets corresponding variable from within game_art.py file.
    art = eval(f"game_art.{art.lower().strip().replace(' ', '_')}")
    if rimuru.textcrawl is True:
        for line in art.split('\n'):
            time.sleep(0.05)
            print(line)
    else:
        print(art)
    print("OK", rimuru.textcrawl)

def game_set_menu(arg):
    """
    Updates and gets rimuru.show_menu boolean. Shows and hides available actions.

    Args:
        arg: Enable or disable text crawl.

    Usage:
        > menu on
        > menu off
    """

    if rimuru.hardcore is True:
        rimuru.show_menu = False
        print("    < Error: Hardcore mode is active. \n>")
        return

    if arg in on_subs or rimuru.show_menu is True:
        rimuru.show_menu = True
    if arg in off_subs or rimuru.show_menu is False:
        rimuru.show_menu = False
    print(f"    < Action Menu: {'Enabled' if rimuru.show_menu else 'Disabled'} >\n")

def game_set_art(arg):
    """
    Enable/Disable ASCII art.

    Args:
        arg: Enable or disable ASCII art.

    Usage:
        ascii on
        ascii off
    """

    if arg in on_subs or rimuru.show_art is True:
        rimuru.show_art = True
    if arg in off_subs or rimuru.show_art is False:
        rimuru.show_art = False
    print(f"    < ASCII Art: {'Enabled' if rimuru.show_art else 'Disabled'} >\n")

def game_set_textcrawl(arg):
    """
    Updates and gets status for textcrawl.

    Args:
        arg: Enable or disable text crawl.

    Usage:
        > textcrawl
        > textcrawl on
        > textcrawl off
    """

    if arg in on_subs or rimuru.textcrawl is True:
        rimuru.textcrawl = True
    if arg in off_subs or rimuru.textcrawl is False:
        rimuru.textcrawl = False
    print(f"    < Text Crawl: {'Enabled' if rimuru.textcrawl else 'Disabled'} >\n")

def game_set_hardcore(arg):
    """
    Enable/Disable ASCII art.

    Args:
        arg: Enable or disable ASCII art.

    Usage:
        hardcore on
        hardcore off
    """

    if arg in on_subs or rimuru.hardcore is True:
        rimuru.hardcore = True
    if arg in off_subs or rimuru.hardcore is False:
        rimuru.hardcore = False
    print(f"    < Hardcore Mode: {'Enabled' if rimuru.hardcore else 'Disabled'} >\n")

def game_restart(*args):
    print("\n    < Restarting Game... >\n")
    os.execl(sys.executable, sys.executable, *sys.argv)

def game_exit(*args):
    """Saves game using pickle, then exits."""
    game_save()
    exit(0)


#                    ========== Game Saves ==========
def game_save(level=None):
    """Pickels Rimuru_Tempest object."""

    if level:
        rimuru.current_location_object = level
    rimuru.valid_save = True
    pickle.dump(rimuru, open(rimuru.save_path, 'wb'))
    print("\n    < Game Saved >\n")

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
    try:
        rimuru = pickle.load(open(path, 'rb'))
    except:
        rimuru = mobs.Rimuru_Tempest()
        rimuru.save_path = path

        import chapters.tensei_1 as tensei1
        rimuru.current_location_object = tensei1.Chapter1

    if rimuru.valid_save is False:
        os.remove(rimuru.save_path)
        game_load(path)

    return rimuru

def game_over():
    """Deletes pickle save file."""

    rimuru.valid_save = False  # So you can't use copies of game save.
    os.remove(rimuru.save_path)
    print("\n    < GAME OVER >\n")
    exit(0)


#                    ========== Game Functions ==========
def sprint(message, from_ssprint=False, from_iprint=False, showing_history=False):
    """
    Text crawling. Slowly print out text to console.

    Args:
        message: Message to delay.
        from_ssprint [bool:False]: Variable used to properly print out lines for 'history' game commmand.
        from_iprint [bool:False]: If coming from iprint function.
        showing_history [bool:False]: Variable used to make sure 'history' command doesn't effect itself.
    """

    # So user can get the last x lines, in case the screen has been cluttered.
    if showing_history is False:  # Without this, when showing history it'll add onto itself, which creates duplicate lines.
        rimuru.line_history.append([message, from_ssprint, from_iprint])
        rimuru.line_history = rimuru.line_history[-25:]

    if rimuru.textcrawl is True:
        message_length = len(message)

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

        # Prints letter by letter, resulted speed depends on string length.
        sleep_time = total_time / message_length
        for letter in message:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(sleep_time)
        print()
    else:
        print(message)  # Print all lines instantly.

def siprint(message, showing_history=False):
    """Print tabbed in message."""

    if message[0] == '\n':
        print()
    sprint('    ' + message.lstrip(), from_ssprint=True, showing_history=showing_history)

def iprint(message, showing_history=False):
    if message[0] == '\n':
        print()
    print('    ' + message.lstrip(), from_iprint=True, showing_history=showing_history)

def show_history(arg):
    """
    Shows x of last outputted story lines.

    Args:
        arg: Lines to show. Default is 5.
    """

    try:
        lines = int(arg)
    except:
        lines = 5

    for line in rimuru.line_history[-lines:]:
        if line[1] is True:
            siprint(line[0], showing_history=True)
        elif line[2] is True:
            iprint(line[0], showing_history=True)
        else:
            sprint(line[0], showing_history=True)

def dots(times=2, length=5, indent=False):
    """
    Loading dot animation.

    Args:
        times: How many times to do animation.
        length: How many dots per cycle.
        indent: Add 4 spaces.
    """

    if not rimuru.textcrawl:
        print(('    ' if indent else '') + '.' * length)
        return

    for i in range(times):
        if indent:
            print('    ', end='')

        for j in range(length):
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(0.5)

        print()
        if i != (times - 1):  # Keeps on last loop.
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            time.sleep(0.1)

def idots(*args):
    """ Calls and passes arguments to dots() with indent. """

    dots(*args, indent=True)

def show_start_banner():
    """Show game title, tips, and player stats/inv."""

    show_art('great sage')
    print(f"""
    ----------Tensei Shitara Slime Datta Ken (That Time I Got Reincarnated as a Slime)----------
    {game_art.rimuru_art.banner}
    - Basic commands: info, stats, inv, save, and  help for more.
    - Fullscreen recommended.
    """)

    if rimuru.valid_save is True:
        print("\n    < Save Loaded >\n")

def show_help(*args):
    """Shows help page."""

    print("""
    Command Required_Parameter [Optional_Parameter]
    
    Commands:
        inv/inventory               -- Show inventory.
        stats/skills [TARGET]       -- Show yours skills and resistances. attribute also works. E.g. 'stats tempest serpent', 'attributes evil centipede'
        info/data TARGET            -- Show info on skill, item or character. E.g. 'info great sage, 'info hipokte grass', 'info tempest serpent'
        target TARGET(S)            -- Target mobs, target multiple by separating with comma ','. E.g. 'target tempest serpent', 'target tempest serpent, black spider'
        attack with SKILL	        -- Attack targeted_mobs. E.g. 'attack with water blade', 'attack water bullet'
        use SKILL                   -- Use a skill. E.g. 'use sense heat source'
        craft ITEM                  -- Craft items if have necessary ingredients. E.g. 'craft full potion'
                                         NOTE: Some items are crafted in batches, suggest reading the item's info page for the recipe and more.
        help                        -- Show this help page.
        exit                        -- Exits after save.

    Abilities:
        mimic TARGET                -- Mimics appearance of of eatd. E.g. 'mimic tempest serpent'
          - info mimic              -- Shows available mimicries.
          - mimic reset             -- Resets mimic (Back to slime).
        eat                         -- Predate target(s). Can only eat mobs that are targeted_mobs and dead.
        nearby                      -- Once acquired the [sense heat source] skill, you can use nearby instead of typing 'use sense heat source' every time.
                                        
    Game Settings:
        textcrawl <on/off>          -- Enable or disable text crawl effect.
        menu/showmenu <on/off>      -- Show avaliable actions player can take.
        ascii/showart <on/off>      -- Show ASCII art.
        hardcore <on/off>           -- Enable hardcore mode.

    Game Dialogue:
        ~Message~                   -- Telepathy, thought communication.
        *Message*                   -- Story context.
        < Message >                 -- Game info, acquisition, game help, etc.
        << Message >>               -- Great Sage (Raphael, Ciel).
        <<< Message >>>             -- Voice of the World.

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
