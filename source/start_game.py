import pathlib, sys, os
from game_files.functions import show_start_banner, game_load, get_any, ask_on_off, update_rimuru_output
from chapters.tensei_0 import ch0

__version__ = "5.1 Alpha"
__author__ = "D Thomas"
__email__ = "dt01@pm.me"
__license__ = "GPL 3"
__status__ = "Development"

def help_page():
    print("""
    -h      --  This help page.
    -f      --  Fast mode, goes through storyline actions as quick as possible. Also disables text crawl and ascii art.
    -t      --  Disable text crawl effect.
    -a      --  Hides ASCII art.
    -hud    --  Hide game HUD.
    -hard   --  Enable Hardcore mode.
    -hints  --  Hide game hints.
    -slime  --  Enables: hud, hints | Disables: textcrawl, art, hardcore
    """)
    exit(0)

if __name__ == '__main__':
    if '-h' in sys.argv: help_page()

    save_path = os.path.dirname(os.path.abspath(__file__)) + '/game.save'

    # Loads game save and updates rimuru object from game_functions.
    rimuru = game_load(save_path)
    rimuru.source_folder_path = str(pathlib.Path(__file__).parent.absolute())
    update_rimuru_output(rimuru)  # Updates rimuru object for ouput.py file... idk, idk.

    if get_any(sys.argv, ['-f', '-fast', '-fastmode']): rimuru.fast_mode = True
    if get_any(sys.argv, ['-t', '-text', '-textcrawl']): rimuru.textcrawl = False
    if get_any(sys.argv, ['-a', '-art', '-hideart']): rimuru.show_art = False
    if get_any(sys.argv, ['-hud', '-hidehud']): rimuru.show_actions = True
    if '-hard' in sys.argv: rimuru.hardcore = True
    if '-hints' in sys.argv: rimuru.show_hints = False
    if '-slime' in sys.argv:  # For debug.
        rimuru.textcrawl = rimuru.show_art = rimuru.hardcore = False
        rimuru.show_actions = rimuru.show_hints = True

    # Only asks player if variables are not already set.
    if rimuru.textcrawl is None:
        rimuru.textcrawl = ask_on_off('textcrawl', 'Enable textcrawl effect (Recommended for easier reading)')
    if rimuru.show_actions is None:
        rimuru.show_actions = ask_on_off('Show Actions', "Show playable actions? (Recommended for first timers)")

    show_start_banner()
    ch0(rimuru)  # Can be used for debugging.
    rimuru.current_location_object(rimuru)
