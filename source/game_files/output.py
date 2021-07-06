import time, sys, re
import game_files.art as game_art
from game_files.extra import *

#                    ========== Printing ==========
def update_rimuru_output(rimuru_obj):
    """Updates rimuru object to be used here."""
    
    global rimuru
    rimuru = rimuru_obj

def parse_name(text):
    """
    Replaces $NAME$ in storyline text with correct corresponding character's set name that player has given.
    e.g. Why $Gobta$?! Why?! > Why Dumbo? Why?!
    """

    return_text = []
    # Splits up by words while preserving spacing (including newlines)
    for word in re.split(r'(\s+)', text):
        if word.startswith('$'):
            # Gets name, e.g. $Gobta$ > Gobta
            placeholder = re.search('\$(.*?)\$', word).groups()[0]
            # Finds corresponding character from canon name.
            if name := rimuru.get_subordinate(str(placeholder), use_canon_name=True):
                # Only replaces what's in between $, preserves symbols e.g. $Gobta$!
                return_text.append(re.sub('\$(.*?)\$', str(name), word))
            # This means there's something wrong with the storyline. Need to fix the story to fix this not the code itself.
            else: game_error()
        else: return_text.append(word)
    return ''.join(return_text)

def sprint(message, add_indent=False, use_textcrawl=True, log_output=True):
    """
    Text crawling. Slowly print out text to console. Kinda like typewriter effect.

    Args:
        message str: Message to delay print.
        from_ssprint bool(False): Variable used to properly print out lines for 'history' game commmand.
        from_iprint bool(False): If coming from iprint function.
        showing_history bool(False): Variable used to make sure 'history' command doesn't effect itself.
    """

    # Adds indent to even if message starts with '\n'.
    if add_indent:
        if message[0] == '\n':
            message = message[0] + '    ' + message[1:]
        else: message = '    ' + message
    message = message + '\n'

    # Hides game tutorial and hints.
    if ('< Hint:' in message or '< Tutorial' in message) and (not rimuru.show_hints or rimuru.hardcore): return

    # Let's you use $NAME$ to get corresponding character's name from canon name (is just to make it easier to write the storyline).
    message = parse_name(message)

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

def print_header(text, multiplier=10, char='-', newline=False):
    """
    Prints header for in-game interfaces, like inv, stats, reputation, etc.

    E.g. '---------- Inventory ----------'

    Args:
        text str: Title of interface, e.g. 'Inventory', 'Attributes'.
        multiplier int(10: Number of lines on both sides of text.
        char str('-'): Character to make line from.
        newline bool(False): Add newline under header.
    """

    print('    ' + char * multiplier, end='')
    print(f' {text} ', end='')
    print(char * multiplier)
    if newline: print()


#                    ========== Extra ==========
def show_version(game_version, version_date):
    """Shows game version."""

    print(f"\n    Version: {game_version} ({version_date})")
    exit(0)

def show_sysargs():
    """Shows available runtime arguments."""

    print("""
    --help      --  This help page.
    --version   --  Show version.
    --nocrawl   --  Disable text crawl effect.
    --noart     --  Diable ASCII art.
    --nohud     --  Disable game HUD.
    --nohints   --  Disable game hints.
    --hardcore  --  Enable Hardcore mode.
    --fastmode  --  Enable Fast mode, goes through storyline actions as quick as possible. Also disables text crawl and ascii art.
    --slime     --  Enables: hud, hints | Disables: textcrawl, art, hardcore""")
    exit(0)

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

def show_history(arg):
    """
    Shows history of x lines from storyline dialogue.

    Args:
        arg int: Lines to show. Default is 5.
    """

    # Show game event log instead of game storyline (voicelines)
    if 'game' in arg:
        log_data = rimuru.game_log
    else: log_data = rimuru.storyline_log

    # Defaults to 5 lines to show of dialog history.
    try: lines = int(arg[-2:])
    except: lines = 5

    print_header('History', 35)
    for line in log_data[-lines:]: print(line, end='')

def show_start_banner(game_version, version_date):
    """Show game title, tips, and player stats/inv."""

    show_art('great sage')
    print(f"""
    ---------- Tensei Shitara Slime Datta Ken (That Time I Got Reincarnated as a Slime) ----------
    {game_art.rimuru_art.banner}
    - Version: {game_version} ({version_date})
    - Basic commands: stats, inv, info, /settings, /exit, and /help for more commands and help.
    - To set game settings like hardcore mode or hints use '/settings', e.g. '/settings hardcore on'.
    - Game will only save at specific points in the story, look out for '< Game Saved >' message.
    - Fullscreen recommended to show ASCII art correctly.""")

    if rimuru.valid_save is True: gprint("\n< Save Loaded >\n")  # Shows if game was loaded from a save.

def show_settings(*args):
    """Shows game settings and there current on/off state."""

    print(f"""    Game Settings:
        {on_off(rimuru.textcrawl)}\ttextcrawl <on/off>\t-- Enable or disable text crawl effect.
        {on_off(rimuru.show_actions)}\thud/interface <on/off>\t-- Show available actions player can take.
        {on_off(rimuru.show_art)}\tart/ascii <on/off>\t-- Show ASCII art.
        {on_off(rimuru.show_hints)}\thints/clues <on/off>\t-- Show game hints, highly recommended for first timers.
        {on_off(rimuru.hardcore)}\thardcore <on/off>\t-- Hides playable actions, tutorial, and hints.

    Usage:
        /settings COMMAND(S) on/off
        Example: '/settings textcrawl off', '/options hud hints off'""")

def show_help(arg):
    """Shows help page."""

    if get_any(arg, ['rank', 'level', 'ranking', 'showrank', 'showlevel'], strict_match=False):
        show_rank_chart()
        return

    print("""    Command Required_Parameter [Optional_Parameter]

    Commands:
        inv                     -- Show inventory.
        stats [TARGET]          -- Show skills and resistances. E.g. 'stats tempest serpent'
        info TARGET             -- Show info on skill/item/mob. E.g. 'info great sage'
        target TARGET(S)        -- Target mob. E.g. 'target tempest serpent', 'target tempest serpent, black spider'
          - target all          -- Target all nearby targetable mobs.
          - target reset        -- Clear targeted.
        attack SKILL/ITEM 	    -- Attack targeted mob(s) with skill/item. E.g. 'attack water blade'
        use SKILL/ITEM          -- Use a skill. E.g. 'use sense heat source'
        craft ITEM [amount]     -- Craft items. E.g. 'craft full potion', 'craft full potion 5'
                                   Note: Some items are crafted in batches, suggest reading the item's info page for the recipe and more.
        mimic TARGET            -- Mimics appearance and attributes of analysed mob. E.g. 'mimic tempest serpent'
          - mimics              -- Shows available mimicries.
          - mimic reset         -- Resets mimic (Back to slime).
        eat                     -- Predate target(s). Can only eat mobs that are targeted_mobs and also dead. can also use 'predate'.
        nearby                  -- Shows nearby mobs if acquired [Magic Perception] skill. Same as 'use magic perception'.
        subordinates/sub        -- Show subordinates you have named.
        reputations/rep         -- Show factions/characters standing with player.
        /log [LINES]            -- Shows x dialogue line history. E.g. '/log', '/log 10', '/log game 15'
          - /log game [LINES]   -- Shows x game event history log (skill/item acquisitions, hints, etc).
        /help                   -- Show this help page.
          - /help rank          -- Show game level, rank, risk chart.
        /settings               -- Shows or change game settings. E.g. '/settings', '/settings hud off', '/options hud hints on'
        /reset                  -- Deletes player save and restarts game.
        /exit                   -- Exits after save.

    Game Dialogue:
            Message             -- Indented messages are inner thoughts.
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
