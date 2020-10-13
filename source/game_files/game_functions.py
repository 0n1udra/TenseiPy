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
        targets = ', '.join([(mob.name if mob.is_alive else f'{mob.name} (Dead)') for mob in rimuru.targeted_mobs])
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

    level_actions = {
        'stats': rimuru.show_attributes,
        'target': rimuru.set_targets,
        'mimic': rimuru.use_mimic,
        'use': rimuru.use_skill,
        'predate': rimuru.predate_targets,
        'inv': rimuru.show_inventory,
        'info': rimuru.show_info,
        'craft': rimuru.craft_item,
        'map': rimuru.get_map,
        'help': show_help,
        'exit': exit,
    }
    if 'attack' in command:
        # Runs function if attack was successful, if not it'll just loop.
        if rimuru.attack(parameter): user_input = 'attack'
    elif 'location' in command:
        rimuru.get_location()

    # Passes in user inputted arguments as parameters and runs corresponding action.
    for action_string, action in level_actions.items():
        if action_string in command:
            action(parameter)

    loop = True
    for action in actions:
        if action.replace('_', ' ').strip() in user_input:
            if action[0] == '_': loop = False  # Checks if action will progress storyline.
            eval(f"level.{action}()")

    if loop: action_menu(level)


#                    ========== Level Functions ==========
def add_level_mob(characters):
    """
    Adds new mob to current level in game.

    Args:
        characters: Mob character(s) to add to current level. Can be single mob (string) or multiple (list).

    Usage:
        add_level_mob('tempest serpent')
        add_level_mob(['tempest serpent', 'giant bat'])
    """
    if type(characters) is list:
        for mob in characters:
            mob = rimuru.get_object(mob, new=True)
            if mob: rimuru.current_level_mobs.append(mob)
    # Adds singular mob object to current level.
    else: rimuru.current_level_mobs.append(rimuru.get_object(characters, new=True))


def get_mob_status(target):
    """
    Returns whether mob in current_mob list is is_alive.

    Args:
        target: Target to check is_alive status.

    Usage:
        get_mob_status('tempest serpent')
    """

    for i in rimuru.current_level_mobs:
        if target.lower() in i.get_name():
            return i.is_alive


def check_cleared_mobs():
    """
    Checks if mobs on current level are all dead.

    Returns:
        Boolean: If all mobs in current_level_mobs are dead.

    Usage:
        if check_cleared_mobs():
    """

    for mob in rimuru.current_level_mobs:
        if mob.is_alive: return False
    else: return True


#                    ========== Extra ==========
def tbc():
    """ To Be Continued function."""
    print("---TO BE CONTINUED---")
    input("Press Enter to exit > ")


#                    ========== Game Saves ==========
def save_game():
    """Pickels Rimuru_Tempest object."""

    pickle.dump(rimuru, open(rimuru.save_path, 'wb'))
    print("Game saved to player_save.p\n")


def load_save_game(path):
    """
    Load game save.

    Args:
        path: Path of game save.

    Returns:
        Loaded game save object.
    """

    # Tries loading game. If can't, creates new Rimuru_Tempest object.
    # Rimuru_Tempest object stores all game data like progress, inventory, stats, etc.
    try:
        rimuru = pickle.load(open(path, 'rb'))
        print("Loaded Player Save\n")
    except:
        rimuru = mobs.Rimuru_Tempest()
        # Sets file save path for later retrieval.
        rimuru.save_path = path

        # Adds first chapter.
        import chapters.tensei_1 as tensei1
        rimuru.story_progress[0] = tensei1.Chapter1

    return rimuru


def delete_game_save(rimuru_object):
    """Deletes pickle save file."""

    os.remove(rimuru.save_path)
    print("Resetting Game. Deleted player_save.p\n")


def continue_story(next_chapter):
    """
    Continues story progress from last save point.

    Args:
        next_chapter: Next chapter to play.
    """

    print("\nContinue to next chapter?")
    user_input = input("Y/N > ")
    rimuru.story_progress.append(next_chapter)
    save_game()
    if user_input.lower() == 'y':
        next_chapter(rimuru)
    else: exit()


#                    ========== Game Functions ==========
def show_start_banner(rimuru):
    """Show game title, tips, and player stats/inv."""

    print("\n----------Tensei Shitara Slime Datta Ken (That Time I Got Reincarnated as a Slime)----------\n")
    instructions = """
    NOTE: 
    - Set window fullscreen for ASCII art.
    - Use 'help' command for game commands and more.
    - Actions with a '*' will advance the story (do NOT actually input *). Try the other actions first maybe, see what happens.
    - Delete player_save.p to reset game progress, inventory and skills.
    """
    print(instructions)
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

        sleep_time = total_time / message_length

        for letter in stripped_message:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(sleep_time)
        print()
    else: print(message)


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
