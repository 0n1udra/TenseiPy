import pickle, time, sys, os
import game_files.art as game_art
import game_files.characters as mobs
from game_files.extra import *

# I'm not exactly sure what actions will be taken in debug_mode, but so far it does get to the end of a chapter.
rimuru = None
on_subs = ['activate', 'true', 'enable', 'on', '1']
off_subs = ['deactivate', 'false', 'disable', 'off', '0']


# start_game.py will load game save if user has one, if not it'll create one.
# Then pass that into update_character which will update the rimuru variable to be used here.
def update_rimuru(rimuru_object):
    global rimuru
    rimuru = rimuru_object
    return rimuru

def game_hud(actions):
    if rimuru.show_hud is False: return

    if rimuru.current_mimic or rimuru.targeted_mobs or rimuru.show_hud: print()  # Adds extra space when needed.

    if rimuru.current_mimic and not rimuru.hardcore:
        print(f"Mimic: [{rimuru.current_mimic.name}]", end='')

    if rimuru.targeted_mobs and not rimuru.hardcore:
        # Adds (Dead) status to corresponding
        targets = ', '.join([(f'{mob[1]}({mob[0].name})' if mob[0].is_alive else f'X-{mob[1]}({mob[0].name})') for mob in rimuru.targeted_mobs])
        print(f'Target: {targets}', end='')

    if rimuru.show_hud and not rimuru.hardcore:
        # Formats actions available to user. Replaces _ with spaces and adds commas when needed.
        actions_for_hud = ' '.join([f"({action.replace('_', ' ').strip()})" for action in actions if 'hfunc' not in action])
        print(f"\nActions: {actions_for_hud}", end='')

def game_action(level=None):
    global onetime
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

    game_hud(actions)

    # ========== Debug Mode
    # Runs first available action that will progress the storyline.
    if rimuru.fast_mode is True:
        for action in actions:
            if action[0] == '_':
                user_input = action.replace('_', ' ').strip()
    else:
        user_input = input("\n> ").strip().lower()
        if 'hfunc' in user_input: game_action(level)
    print()

    # Separates user input into command and command arguments.
    split_user_input = user_input.split(' ')
    command, parameters = split_user_input[0], ' '.join(split_user_input[1:])
    character = rimuru

    game_actions = [
        [rimuru.show_info, ['info', 'data', 'detail', 'details']],
        [rimuru.show_inventory, ['inv', 'inventory', 'stomach']],
        [rimuru.show_attributes, ['stats', 'skills', 'attrs', 'attributes']],
        [rimuru.set_targets, ['target', 'focus']],
        [rimuru.attack, [parameters], ['attack']],
        [rimuru.use_skill, [parameters, character], ['use']],
        [rimuru.craft_item, ['craft', 'make', 'create']],
        [rimuru.eat_targets, ['eat', 'predate', 'predation']],
        [rimuru.use_mimic, ['mimic', 'mimicry']],
        [rimuru.get_location, ['location']],
        [rimuru.use_skill, ['sense heat source', character], ['nearby', 'sense heat sources']],
        [show_help, ['help', 'commands']],
        [show_settings, ['settings', 'options']],
        [show_rank_chart, ['showrank', 'showranking', 'showlevel']],
        [game_set_art, ['art', 'ascii', 'showart']],
        [game_set_hud, ['hud', 'showhud', 'gamehud']],
        [game_set_hints, ['hints', 'show hints', 'showhints', 'gamehints']],
        [game_set_textcrawl, ['textcrawl', 'slowtext']],
        [game_set_hardcore, ['hardcore', 'hardmode']],
        [show_history, ['history']],
        [game_restart, ['restart']],
        [game_exit, ['exit', 'quit', 'stop']],
        ]

    # Passes in user inputted arguments as parameters and runs corresponding action.
    for action in game_actions:
        if len(action) == 3:
            if command in action[2]:
                action[0](*action[1])
        if command in action[1]:
            action[0](parameters)

    for action in actions:
        # Currently need two evals to find __subs for action.
        try:
            action_subs = eval(f"level.{action}.{action}__subs")
        except:
            action_subs = []
        try:
            action_subs = eval(f"level.{action}._{action}__subs")
        except: pass

        if 'ACTIONBLOCKED' in action_subs:
            continue

        # Adds action's class name to subs list, so you don't have to add it yourself in the chapter files.
        action_subs.append(action.replace('_', ' ').strip().lower())

        if get_any(user_input, action_subs):
            eval(f"level.{action}()")

    game_action(level)


#                    ========== Game Settings, Saves, Etc ==========
def game_restart(*args):
    print("\n    < Restarting Game... >\n")
    os.execl(sys.executable, sys.executable, *sys.argv)

def game_exit(*args):
    """Saves game using pickle, then exits."""
    game_save()
    exit(0)

def game_save(level=None):
    """Pickels Rimuru_Tempest object."""

    if level:
        rimuru.current_location_object = level

    if rimuru.valid_save is None:
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
        rimuru.current_location_object = tensei1.ch1_cave

    if rimuru.valid_save is False:
        os.remove(rimuru.save_path)
        game_load(path)

    return rimuru

def game_over():
    """Deletes pickle save file."""

    rimuru.valid_save = False  # So you can't use copies of game save.
    game_save()

    try:
        os.remove(rimuru.save_path)
    except: pass

    print("\n    < GAME OVER >\n")
    print("Play again?")
    if str(input('No / Yes or Enter > ')).lower() in ['n', 'no']:
        exit(0)
    else:
        game_restart()

def game_set_hud(arg):
    """
    Updates and gets rimuru.show_hud boolean. Shows and hides available actions.

    Args:
        arg: Enable or disable text crawl.

    Usage:
        > menu on
        > menu off
    """

    if rimuru.hardcore is True:
        rimuru.show_hud = False
        print("    < Error: Hardcore mode is active. \n>")
        return

    if arg in on_subs or rimuru.show_hud is True:
        rimuru.show_hud = True
    if arg in off_subs or rimuru.show_hud is False:
        rimuru.show_hud = False
    print(f"    < Action Menu: {'Enabled' if rimuru.show_hud else 'Disabled'} >\n")

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

def game_set_hints(arg):
    """ Enable/Disable game hints. """

    if rimuru.hardcore is True:
        rimuru.show_hud = False
        print("    < Error: Hardcore mode is active. \n>")
        return

    if arg in on_subs or rimuru.show_hints is True:
        rimuru.show_hints = True
    if arg in off_subs or rimuru.show_hints is False:
        rimuru.show_hints = False
    print(f"    < Hints: {'Enabled' if rimuru.show_hints else 'Disabled'} >\n")

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

#                    ========== Level Functions ==========
def game_cond(value, new_value=None):
    """ Set and fetch game variables. """
    if new_value:
        rimuru.conditional_data[value] = new_value
        return new_value

    if value in rimuru.conditional_data:
        return rimuru.conditional_data[value]
    else:
        return False

def mobs_add(add_mobs):
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

def continue_to(next_location):
    """
    Saves game and continues to next location.

    Args:
        continue_to: Next chapter to play.
    """

    rimuru.current_location_object = continue_to
    game_save()
    try:
        next_location(rimuru)
    except:
        print("    < Error Loading Next Location >")

def clear_subs(level):
    """
    Clears __subs list of passed in class.

    Args:
        level: Playable action class object from chapter file.
    """

    for i in dir(level):
        if '__subs' in i:
            eval(f"level.{i}.append('ACTIONBLOCKED')")


#                    ========== Game Functions ==========
def sprint(message, from_print='sprint', showing_history=False, no_crawl=False):
    """
    Text crawling. Slowly print out text to console.

    Args:
        message: Message to delay.
        from_ssprint [bool:False]: Variable used to properly print out lines for 'history' game commmand.
        from_iprint [bool:False]: If coming from iprint function.
        showing_history [bool:False]: Variable used to make sure 'history' command doesn't effect itself.
    """

    if ('< Hint:' in message) and (not rimuru.show_hints or rimuru.hardcore):
        return

    # So user can get the last x lines, in case the screen has been cluttered.
    if showing_history is False:  # Without this, when showing history it'll add onto itself, which creates duplicate lines.
        rimuru.line_history.append([message, from_print])
        rimuru.line_history = rimuru.line_history[-25:]

    if rimuru.textcrawl is True and no_crawl is False:
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
    sprint('    ' + message.lstrip(), from_print='siprint', showing_history=showing_history)

def iprint(message, showing_history=False):
    if message[0] == '\n':
        print()
    sprint('    ' + message.lstrip(), no_crawl=True, showing_history=showing_history)

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
        if line[1] == 'iprint':
            iprint(line[0], showing_history=True)
        elif line[1] == 'iprint':
            sprint(line[0], showing_history=True)
        elif line[1] == 'siprint':
            siprint(line[0], showing_history=True)
        else:
            print(line[0])

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

def idots(*args):
    """ Calls and passes arguments to dots() with indent. """

    dots(*args, indent=True)

def show_start_banner():
    """ Show game title, tips, and player stats/inv. """

    print("OK")
    show_art('great sage')
    print(f"""
    ----------Tensei Shitara Slime Datta Ken (That Time I Got Reincarnated as a Slime)----------
    {game_art.rimuru_art.banner}
    - Basic commands: stats, inv, save, info, and  help for more.
    - Fullscreen recommended.
    """)

    if rimuru.valid_save is True:
        print("\n    < Save Loaded >\n")

def show_art(art):
    """
    Prints out ASCII art line by line or all at once dependding on textcrawl boolean.

    Args:
        art: Name of variable that is located in art.py file. The functions will replace spaces with _ if needed.
        textcrawl [bool:False]: Use textcrawl effect ignoring rimuru.show_art variable.

    """

    if rimuru.show_art is False: return False
    print("OK")

    # Gets corresponding variable from within art.py file.
    art = eval(f"game_art.{art.lower().strip().replace(' ', '_')}")
    if rimuru.textcrawl or rimuru.textcrawl is None:
        for line in art.split('\n'):
            time.sleep(0.05)
            print(line)
    else:
        print(art)

def show_settings(*args):
    print(f"""
    Game Settings:
        {on_off(rimuru.textcrawl)}\ttextcrawl <on/off>\t-- Enable or disable text crawl effect.
        {on_off(rimuru.show_hud)}\thud/showhud <on/off>\t-- Show available actions player can take.
        {on_off(rimuru.show_art)}\tascii/showart <on/off>\t-- Show ASCII art.
        {on_off(rimuru.hardcore)}\thardcore <on/off>\t-- Enable hardcore mode.
        {on_off(rimuru.show_hints)}\thints <on/off>\t\t-- Show game hints, highly recommended for first timers.
    """)

def show_help(*args):
    """ Shows help page. """

    print("""
    Command Required_Parameter [Optional_Parameter]
    
    Commands:
        inv/inventory               -- Show inventory.
        stats/skills [TARGET]       -- Show skills and resistances. attribute also works.
                                       Example: 'stats tempest serpent', 'attributes evil centipede'
        info/data TARGET            -- Show info on skill, item or character. 
                                       Example: 'info great sage, 'info hipokte grass', 'info tempest serpent'
        target TARGET(S)            -- Target mob(s), to be able to use skills/abilities/etc on them.
                                       Example: 'target tempest serpent', 'target tempest serpent, black spider'
          - target nearby           -- Target nearby mobs.
          - target reset            -- Clear targeted.
        attack SKILL	            -- Attack targeted_mobs. 
                                       Example: 'attack water blade'
        use SKILL                   -- Use a skill.
                                       Example: 'use sense heat source'
        craft ITEM [amount]         -- Craft items if have necessary ingredients. 
                                       Example: 'craft full potion', 'craft full potion 10'
                                       Note: Some items are crafted in batches, suggest reading the item's info page for the recipe and more.
        mimic TARGET                -- Mimics appearance of of eatd.
                                       Example: 'mimic tempest serpent'
          - info mimic              -- Shows available mimicries.
          - mimic reset             -- Resets mimic (Back to slime).
        eat/predate                 -- Predate target(s). Can only eat mobs that are targeted_mobs and dead.
        nearby                      -- Once acquired [Sense Heat Source] skill, you can use nearby instead of typing 'use sense heat source' every time.
        help                        -- Show this help page.
        settings                    -- Show commands to change/set game settings, like textcrawl, hardcore, art, and menu.
        showrank                    -- Show mob level chart and corresponding ranking.
        exit                        -- Exits after save.

    Game Dialogue:
        ~Message~                   -- Telepathy, thought communication.
        *Message*                   -- Story context.
        < Message >                 -- Game info, acquisition, game help, etc.
        << Message >>               -- Great Sage (Raphael, Ciel).
        <<< Message >>>             -- Voice of the World.
    """)

def show_rank_chart(*args):
    print("""
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
