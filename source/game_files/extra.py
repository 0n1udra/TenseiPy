import random, sys, os

# Input substitutes used for enabling/disabling game settings.
on_subs = ['activate', 'true', 'enable', 'on', 'yes', '1', 'y']
off_subs = ['deactivate', 'false', 'disable', 'off', 'no',  '0', 'n']

def get_random(min_int=1, max_int=2, target=None, bigger_than=None, return_int=False):
    """
    Generate random number and check if matches passed in target parameter, returns True if so.

    Args:
        min int(1): Starting number for randint function.
        max int(100): End number for randint function.
        target int(None): Target number to match to random number.
        bigger_than int(None): Check if random number is bigger or equal to target.
        return_int bool(False): Return randomly generated integer alongside boolean.

    Returns:
        bool: Returns True or False if target matches random number.
        bool, int: Returns bool and integer of random number that was generated if return_int is True.

    Usage:
        get_random(1, 1_000, 666)
        get_random(1, 50)
        get_random(10, 50)
    """

    return_bool = False

    # Default target set to half of max, 50/50 chance.
    if target is None: target = int(round(max_int / 2))
    rand = random.randint(min_int, max_int)

    if bigger_than and rand >= bigger_than:
        return_bool = True
    elif rand == target:
        return_bool = True

    # Return random integer along with boolean.
    if return_int:
        return return_bool, rand
    return return_bool

def get_any(match_target, input_list, strict_match=True):
    """
    Returns True if found a match from input_list with match_to.

    Args:
        match_to str: String to match with.
        input_list list: List of items to find match with.

    Returns:
        bool: Returns True if match found.
    """

    # Will only accept strings.
    if type(match_target) is not str: return False
    match_to = match_target.lower().strip()

    for i in input_list:
        i.lower().strip()
        if strict_match:
            if i == match_to: return True
        else:
            if i in match_to: return True

def get_class_var(class_obj, var_name):
    """
    Gets a __variable name from class object.
    Args:
        class_obj obj: Class object that contains __location variable.
        var_name str: variable to locate and return data.

    Returns:
        None: If variable not found.
    """

    if class_obj is None: return None

    for thing in dir(class_obj):
        if var_name in thing:
            return eval(f"class_obj.{thing}")

def on_off(var):
    """Returns string 'on'/'off' based on received boolean variable."""

    if var: return 'on '
    return 'off'

def ask_on_off(variable, text):
    """
    Asks player if they want to enable or disable.

    Args:
        variable str: Variable name to show in message once variable has been updated. Ex. 'textcrawl'
        text str: Description text.

    Returns:
        bool: Returns True/False depending on if user typed in anything from off_subs or pressed Enter.

    Usage:
        rimuru.textcrawl = ask_on_off('textcrawl', 'Enable textcrawl effect? (Recommended for slower reading)')
    """

    # User will have to type in anything that matches in off_subs to disable.
    print('\n' + text)
    if str(input("No / Yes or Enter > ")).lower() in off_subs:
        print(f"\n    < {variable}: Disabled >")
        return False
    else:
        print(f"\n    < {variable}: Enabled >")
        return True

def format_info(name, var):
    """
    Returns object information to be shown in object's info_page.
    If an object's variable is empty or has not been set, corresponding field will be hidden in info_page.

    Args:
        name str: Name of field to show. E.g. 'Name:', 'Description:'.
        var var: Variable data to show.

    Returns:
        str: Returns string to be added to objects info_page variable.
    """

    if not var: return None

    return_data = ''

    # Puts var info on newline and indented from field label.
    if '*' in name:
        return_data += f'\n    {name[1:]}:\n\t'
    else: return_data += f"{name}: "

    # If passed in a list. It'll sort, than space it them out with ','.
    if type(var) is list:
        return_data += ", ".join(sorted(var))
    else: return_data += str(var).strip()

    return return_data

def set_action_subs(action, action_subs):
    """
    Formats inputted action __subs list to be used to check play action match from user input.

    Args:
        action str: Current action's name.
        action_subs list: __subs list of corresponding action.

    Returns:
        list: Returns newly formated __subs list to be used to check user input match.

    """

    # If action name has _x in it it'll extract the important part of the action name to add to subs list.
    if 'x_' in action[:3]:
        action_subs = [' '.join(list(filter(None, action.split('_')))[1:])] + action_subs
    # Adds action's class name to list of subs for possible user input matches.
    else: action_subs.append(action.replace('_', ' ').strip().lower())

    return action_subs

def mob_list_adder(item, input_list, amount_mode=False):
    """
    Special list adder for mob two-dimensional lists.
    e.g. [[game_game_objects, quantity_integer],...]

    Args:
        input_list list: List to add game mob to.
        amount_mode bool(False): Able to add to quantity of mobs (second object in list).
    """

    # Only able to target mobs in active_mobs list.
    for i in input_list:
        if i[0].name == item[0].name:
            # Adds the quantity integer in list.
            if amount_mode: i[1] += item[1]
            return True

    input_list.append(item)

def parse_input(user_input):
    """
    Extracts item name and amount from user input. (Use only in try/except).

    E.g. 'remove hipokte grass 100' returns str('Hipokte Grass'), int(100)

    Args:
        user_input str: User inputted command.

    Returns:
        list: Returns item name, and amount integer.
    """

    split_data = user_input.split()
    return ' '.join(split_data[:-1]), int(split_data[-1])

def tbc():
    """Print part of game/story is in development."""

    print("\n    < ----- SECTION IN PROGRESS ----- >\n")
    print("\nPlay again?")
    if str(input('No / Yes or Enter > ')).lower() in ['n', 'no']: exit(0)
    else: os.execl(sys.executable, sys.executable, *sys.argv)

def game_error():
    """
    Exit game when error that needs to be fixed is found.
    If the game is coded correctly, you shouldn't ever see this message.
    """

    print("\n    < GAME ERROR FOUND >")
    print("    If you are seeing this, please contact the dumb developer that let this happen. Oh the shame that developer must be feelin!\n")