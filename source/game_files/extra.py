import random

def get_random(min=1, max=100, target=None, range=None, return_int=False):
    """
    Generate random number and check if matches passed in target parameter, returns True if so.

    Args:
        min [int:1]: Starting number for randint function.
        max [int:100]: End number for randint function.
        target: Target number to match to random number.
        range: Check if random number is bigger or equal to target.
        return_int: Return randomly generated integer alongside boolean.

    Returns:
        bool: Returns True or False if target matches random number.
        bool, int: Returns bool and integer of random number that was generated if return_int is True.

    Usage:
        get_random(1, 1_000, 666)
        get_random(1, 50)
        get_random(10, 50, range=20)
    """

    if target is None:
        target = int(round(max / 2))

    rand = random.randint(min, max)
    if range:
        if rand >= rand:
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
        match_to: String to match with.
        input_list: List of items to find match with.

    Returns:
        bool: Returns True if match found.
    """

    if any(i in match_to for i in input_list):
        return True

def on_off(var):
    if var is True:
        return 'on '
    elif var is False:
        return 'off'
    else:
        return 'n/a'

def tbc():
    """ To Be Continued message.."""

    print("\n    < ---IN PREOGRESS--- >\n")
    input("Press Enter to exit > ")
