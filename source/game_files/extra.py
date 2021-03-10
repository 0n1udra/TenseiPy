import random, sys


def get_random(min_int=1, max_int=100, target=None, bigger_than=None, return_int=False):
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
        get_random(10, 50, range=20)
    """

    # Default is the middle of min and max.
    if target is None:
        target = int(round(max_int / 2))

    rand = random.randint(min_int, max_int)

    if bigger_than and rand >= bigger_than:
        # Return random integer along with boolean.
        if return_int:
            return True, rand
        return True

    if rand == target:
        if return_int:
            return True, rand
        return True

    return False


def get_any(match_to, input_list):
    """
    Returns True if found a match from input_list with match_to.

    Args:
        match_to str: String to match with.
        input_list list: List of items to find match with.

    Returns:
        bool: Returns True if match found.
    """

    if any(i.lower() in match_to for i in input_list):
        return True


def on_off(var):
    """Returns string 'on'/'off' based on var."""

    if var:
        return 'on '
    return 'off'


def format_info(name, var):
    """
    Returns object information to be shown in object's info_page.
    If an object's variable is empty or has not been set, corresponding field will be hidden in info_page.

    Args:
        name str: Name of field to show. Ex. 'Name:', 'Description:'.
        var var: Variable data to show.

    Returns:
        str: Returns string to be added to objects info_page variable.
    """

    if not var: return None

    return_data = ''

    # Puts var info on newline and indented from field label.
    if '*' in name:
        return_data += f'\n    {name[1:]}:\n\t'
    else:
        return_data += f"{name}: "

    # If passed in a list. It'll sort, than space it them out with ','.
    if type(var) is list:
        return_data += ", ".join(sorted(var))
    else:
        return_data += str(var).strip()

    return return_data


def tbc():
    """Print part of game/story is in development."""

    print("\n    < ---IN PROGRESS--- >\n")
    input("Press Enter to exit > ")
    sys.exit(0)
