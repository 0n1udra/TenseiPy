import os, pickle, time, sys
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
            'craft': rimuru.craft_item,
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


#                    ========== Level Functions ==========
def add_level_mob(characters):
    """
    Adds new mob to current level in game.

    Args:
        level_characters: Mob character(s) to add to current level. Can be single mob (string) or multiple (list).

    Usage:
        add_level_mob('tempest serpent')
        add_level_mob(['tempest serpent', 'giant bat'])
    """
    if type(characters) == list:
        for i in characters:
            mob = rimuru.get_object(i, new=True)
            if mob:
                rimuru.current_level_characters.append(mob)
    else:
        mob = rimuru.get_object(characters, new=True)
        rimuru.current_level_characters.append(mob)

def get_mob_status(target):
    """
    Returns whether mob in current_mob list is alive.

    Args:
        target: Target to check alive status.

    Usage:
        get_mob_status('tempest serpent')
    """

    for i in rimuru.current_level_characters:
        if target.lower() in i.get_name():
            if i.alive:
                return True

def check_cleared_mobs():
    """
    Returns whether all mobs on at current stage are cleared.

    Returns:
        Boolean: If all mobs in current_level_characters are dead.

    Usage:
        if check_cleared_mobs():
    """

    for mob in rimuru.current_level_characters:
        if mob.alive:
            return False
    else:
        return True


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
    print("Game saved to player_save.p\n")

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
    print("Good luck next time!\n")
    exit()

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

    if rimuru.text_delay:
        stripped_message = message.lstrip()
        message_length = len(stripped_message)

        if message_length > 200:
            total_time = 0.1
        elif message_length > 50:
            total_time = 4.5
        elif message_length > 25:
            total_time = 3.5
        elif message_length > 10:
            total_time = 2.5
        else:
            total_time = 2.5

        sleep_time = total_time / message_length

        for letter in stripped_message:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(sleep_time)
        print()
    else:
        print(message)

def show_help(*args):
    """Shows help page."""

    print("""
    Command Required_Parameter [Optional_Parameter]

    Commands:
        target TARGET               -- Target mobs. E.g. 'target tempest serpent', 'target tempest serpent, black spider'
        attack with SKILL	        -- Attack targeted. E.g. 'attack with water blade', 'attack water bullet'
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
        predate                     -- Predate target(s). Can only predate mobs that are targeted and dead.
        craft ITEM                  -- Craft items if have necessary ingredients. E.g. 'craft full potion'
                                         NOTE: Some items are crafted in batches, suggest reading the item's info page for the recipe and more.

    Game Dialogue:
        ~Message~                   -- Telepathy, thought communication.
        *Message*                   -- Story context.
        < Message >                 -- Game info, acquisition, game help, etc.
        << Message >>               -- Great Sage (Raphael, Ciel).
        <<< Message >>>             -- Voice of the World.

    HUD:
        Target: Currently_Focused_Targets
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
