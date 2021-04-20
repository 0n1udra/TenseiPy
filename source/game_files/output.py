import time, sys

def update_rimuru_output(rimuru_obj):
    global rimuru
    rimuru = rimuru_obj

def sprint(message, add_indent=False, use_textcrawl=True, log_output=True):
    """
    Text crawling. Slowly print out text to console. Kinda like typewriter effect.

    Args:
        message str: Message to delay print.
        from_ssprint bool(False): Variable used to properly print out lines for 'history' game commmand.
        from_iprint bool(False): If coming from iprint function.
        showing_history bool(False): Variable used to make sure 'history' command doesn't effect itself.
    """

    if add_indent:
        if message[0] == '\n':
            message = message[0] + '    ' + message[1:]
        else: message = '    ' + message
    message = message + '\n'

    # Will not use textcrawl effect on gameplay hint printouts.
    if ('< Hint:' in message) and (not rimuru.show_hints or rimuru.hardcore): return

    # So user can get the last x lines, in case the screen has been cluttered.
    # Makes sure when showing history it won't add onto itself. Also, checks if line has already been logged (if player played action multiple times).
    if log_output and message not in rimuru.storyline_log:
        rimuru.storyline_log.append(message)
        rimuru.storyline_log = rimuru.storyline_log[-99:]

    if rimuru.textcrawl and use_textcrawl:
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
        else: total_time = 2

        # Use sys module to print letter by letter and time module for delay between each letter.
        sleep_time = total_time / message_length
        for letter in message:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(sleep_time)
        print()

    else: print(message, end='')  # Print instantly.

    return message

def siprint(message, use_textcrawl=True):
    """sprint with adds indent and textcrawl."""

    sprint(message, add_indent=True, use_textcrawl=use_textcrawl)

def iprint(message):
    """Print with adds indent and disabled textcrawl."""

    sprint(message, add_indent=True, use_textcrawl=False)

def gprint(message):
    """For game events. Adds indent, disables and textcrawl. Appends to game_log list."""

    rimuru.game_log.append(sprint(message, add_indent=True, use_textcrawl=False))

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


def show_history(arg):
    """
    Shows x of last outputted story lines.

    Args:
        arg: Lines to show. Default is 5.
    """

    # Show game event log instead of game storyline (voicelines)
    if 'game' in arg:
        log_data = rimuru.game_log
    else: log_data = rimuru.storyline_log

    # Defaults to 5 lines to show of dialog history.
    try: lines = int(arg[-2:])
    except: lines = 5

    print('-------------------- History --------------------\n')
    for line in log_data[-lines:]: print(line, end='')
    print('\n-------------------- History --------------------')

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
    else: print(art)  # Instantly print out ASCII art to screen.
