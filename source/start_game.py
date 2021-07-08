import pathlib, sys, os
from game_files.functions import save_load
from game_files.output import show_start_banner, update_rimuru_output, show_sysargs, show_version
from game_files.extra import ask_on_off
from chapters.tensei_0 import ch0

__version__ = "6.1 Alpha"
__date__ = '7/7/2021'
__author__ = "DT"
__email__ = "dt01@pm.me"
__license__ = "GPL 3"
__status__ = "Development"

if __name__ == '__main__':
    if '--help' in sys.argv: show_sysargs()
    if '--version' in sys.argv: show_version(__version__, __date__)

    save_path = os.path.dirname(os.path.abspath(__file__)) + '/game.save'

    # Loads game save and updates rimuru object from game_functions.
    rimuru = save_load(save_path)
    rimuru.source_folder_path = str(pathlib.Path(__file__).parent.absolute())
    update_rimuru_output(rimuru)  # Updates rimuru object for ouput.py file... idk, idk, you just have to...

    if '--nocrawl' in sys.argv: rimuru.textcrawl = False
    if '--noart' in sys.argv: rimuru.show_art = False
    if '--nohud' in sys.argv: rimuru.show_actions = True
    if '--nohints' in sys.argv: rimuru.show_hints = False
    if '--hardcore' in sys.argv: rimuru.hardcore = True
    # For debugging.
    if '--fastmode' in sys.argv: rimuru.fast_mode = True
    if '--slime' in sys.argv:
        rimuru.textcrawl = rimuru.show_art = rimuru.hardcore = False
        rimuru.show_actions = rimuru.show_hints = True

    # Only asks player if variables are not already set.
    if rimuru.textcrawl is None: rimuru.textcrawl = ask_on_off('textcrawl', 'Enable textcrawl effect (Recommended for easier reading)')
    if rimuru.show_actions is None: rimuru.show_actions = ask_on_off('Show Actions', "Show playable actions? (Recommended for first timers)")

    show_start_banner(__version__, __date__)
    ch0(rimuru)  # Can be used for debugging.
    rimuru.current_location_object(rimuru)
