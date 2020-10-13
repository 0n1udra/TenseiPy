import os, sys, time, pickle
import game_files.game_art as art
import game_files.game_characters as mobs

# I'm not exactly sure what actions will be taken in debug_mode, but so far it does get to the end of a chapter.
rimuru = debug_mode = None
# start_game.py will load game save if user has one, if not it'll create one.
# Then pass that into update_character which will update the rimuru variable to be used here.
def update_variables(rimuru_object, debug):
    global rimuru, debug_mode
    rimuru, debug_mode = rimuru_object, debug
    return rimuru


def action_menu(level=None):
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

    # ========== HUD
    print()
    if rimuru.targeted_mobs:
        # Adds (Dead) status to corresponding
        targets = ', '.join([(mob.name if mob.is_alive else f'{mob.name}(Dead)') for mob in rimuru.targeted_mobs])
        print(f'\nTarget: {targets}')
    # Formats actions available to user. Replaces _ with spaces and adds commas when needed.
    actions_for_hud = ', '.join([f"({action.replace('_', ' ').strip()})" for action in actions])
    print(f"Actions: {actions_for_hud} | (stats, inv, help)")

    # ========== Debug Mode
    # Runs first available action that will progress the storyline.
    if debug_mode:
        for action in actions:
            if action[0] == '_':
                user_input = action.replace('_', ' ').strip()
    else:
        user_input = input("\n> ").lower()
        print()

    # Separates user input into command and command arguments.
    split_user_input = user_input.split(' ')
    command = split_user_input[0]
    parameter = ' '.join(split_user_input[1:])
    character = rimuru

    level_actions = {
        'stats': rimuru.show_attributes,
        'target': rimuru.set_targets,
        'mimic': rimuru.use_mimic,
        'predate': rimuru.predate_targets,
        'inv': rimuru.show_inventory,
        'info': rimuru.show_info,
        'craft': rimuru.craft_item,
        'map': rimuru.get_map,
        'help': show_help,
        'save': game_save,
        'exit': game_exit,
    }
    if 'attack' in command:
        if rimuru.attack(parameter): user_input = 'attack'  # Runs correlating function if attack was successful, if not it'll just loop.
    elif 'use' in command: rimuru.use_skill(character, parameter)
    elif 'location' in command: rimuru.get_location()

    # Passes in user inputted arguments as parameters and runs corresponding action.
    for action_string, action in level_actions.items():
        if action_string in command: action(parameter)

    loop = True
    for action in actions:
        if action.replace('_', ' ').strip() in user_input:
            if action[0] == '_': loop = False  # Checks if action will progress storyline.
            eval(f"level.{action}()")

    if loop: action_menu(level)


#                    ========== Level Functions ==========
def new_active_mob(characters):
    """
    Mob is alive on current level.

    Args:
        characters: Mob character(s) to add to current level. Can be single mob (string) or multiple (list).

    Usage:
        new_active_mob('tempest serpent')
        new_active_mob(['tempest serpent', 'giant bat'])
    """
    if type(characters) is list:
        for mob in characters:
            if mob := rimuru.get_object(mob, new=True):
                rimuru.active_mobs.append(mob)
    # Adds singular mob object to current level.
    else: rimuru.active_mobs.append(rimuru.get_object(characters, new=True))


def mob_status(target):
    """
    Returns whether mob in active_mobs list is is_alive.

    Args:
        target: Target to check is_alive status.

    Usage:
        mob_status('tempest serpent')
    """

    for i in rimuru.active_mobs:
        if target.lower() in i.get_name():
            return i.is_alive


def cleared_all_mobs():
    """
    Checks if mobs on current level are all dead.

    Returns:
        boolean: If all mobs in active_mobs are dead.

    Usage:
        if cleared_all_mobs():
    """

    for mob in rimuru.active_mobs:
        if mob.is_alive: return False
    else: return True


#                    ========== Extra ==========
def tbc():
    """ To Be Continued message.."""

    print("---TO BE CONTINUED---")
    input("Press Enter to exit > ")


#                    ========== Game Saves ==========
def game_exit(*args):
    """Saves game using pickle, then exits."""

    game_save()
    exit(0)

def game_save(*args):
    """Pickels Rimuru_Tempest object."""

    pickle.dump(rimuru, open(rimuru.save_path, 'wb'))
    print("Game Saved.\n")


def game_load(path):
    """
    Load game save.

    Args:
        path: Path of game save.

    Returns:
        Loaded game save object.
    """

    # Tries loading game. If can't, creates new Rimuru_Tempest object which contains all game data that will be picked.
    try: rimuru = pickle.load(open(path, 'rb'))
    except:
        rimuru = mobs.Rimuru_Tempest()
        rimuru.save_path = path

        import chapters.tensei_1 as tensei1
        rimuru.story_progress[0] = tensei1.Chapter1

    if rimuru.valid_save:
        print("Loaded Game Save.\n")
    else:
        os.remove(rimuru.save_path)
        game_load(path)

    return rimuru


def game_over():
    """Deletes pickle save file."""

    rimuru.valid_save = False  # So you can't use copies of game save.
    os.remove(rimuru.save_path)
    print("GAME OVER.\n")
    exit(0)


def continue_story(next_chapter):
    """
    Continues story progress from last save point.

    Args:
        next_chapter: Next chapter to play.
    """

    # Adds next chapter of game, and saves current progress.
    rimuru.story_progress.append(next_chapter)
    game_save()

    print("\nContinue to next chapter?")
    if str(input("No/Yes or Enter > ")).lower() in ['n', 'no']:
        exit(0)
    else: next_chapter(rimuru)


#                    ========== Game Functions ==========
def show_start_banner(rimuru):
    """Show game title, tips, and player stats/inv."""

    print(f"""
    ----------Tensei Shitara Slime Datta Ken (That Time I Got Reincarnated as a Slime)----------
    
    NOTE: 
    - Some basic commands: help, info, stats, inv, save, and exit.
    - Fullscreen recommended.
    """)
    rimuru.show_attributes()
    rimuru.show_inventory()
    print()


def ssprint(message):
    """Print tabbed in message."""
    print('    ', end='')
    sprint(message)


def sprint(message):
    """
    Text crawling. Slowly print out text to console.

    Args:
        message: Message to delay.
    """

    if rimuru.text_crawl:
        stripped_message = message.lstrip()
        message_length = len(stripped_message)

        if message_length > 200: total_time = 0.1
        elif message_length > 50: total_time = 4.5
        elif message_length > 25: total_time = 3.5
        elif message_length > 10: total_time = 2.5
        else: total_time = 2.5

        # Prints letter by letter, resulted speed depends on string length.
        sleep_time = total_time / message_length
        for letter in stripped_message:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(sleep_time)
        print()

    else: print(message)  # Print all lines instantly.


def show_help(*args):
    """Shows help page."""

    print("""
    Command Required_Parameter [Optional_Parameter]

    Commands:
        target TARGET(S)            -- Target mobs, target multiple by separating with comma ','. E.g. 'target tempest serpent', 'target tempest serpent, black spider'
        attack with SKILL	        -- Attack targeted_mobs. E.g. 'attack with water blade', 'attack water bullet'
        use SKILL                   -- Use a skill. E.g. 'use sense heat source'
        stats [TARGET]              -- Show yours skills and resistances. E.g. 'stats tempest serpent'
        inv                         -- Show inventory.
        info TARGET                 -- Show info on skill, item or character. E.g. 'info great sage, 'info hipokte grass', 'info tempest serpent'
        save                        -- Saves current game state.
        help                        -- Show this help page.
        exit                        -- Exit game.

    Abilities:
        mimic TARGET                -- Mimics appearance of of predated. E.g. 'mimic tempest serpent'
          - info mimic              -- Shows available mimicries.
          - mimic reset             -- Resets mimic (Back to slime).
        predate                     -- Predate target(s). Can only predate mobs that are targeted_mobs and dead.
        craft ITEM                  -- Craft items if have necessary ingredients. E.g. 'craft full potion'
                                         NOTE: Some items are crafted in batches, suggest reading the item's info page for the recipe and more.

    Game Dialogue:
        ~Message~                   -- Telepathy, thought communication.
        *Message*                   -- Story context.
        < Message >                 -- Game info, acquisition, game help, etc.
        << Message >>               -- Great Sage (Raphael, Ciel).
        <<< Message >>>             -- Voice of the World.

    HUD:
        Target: Currently_targeted_mobs
        Actions: (Actions) | Mimic, (Extra_Actions)
    Example HUD:
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
