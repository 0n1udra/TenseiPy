import os, sys
from time import sleep
import game_files.game_functions as game_funcs

__version__ = "4.0 Alpha"
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
    -hard   --  Hardcore mode.
    """)
    exit(0)


if __name__ == '__main__':
    if '-h' in sys.argv: help_page()

    save_path = os.path.dirname(os.path.abspath(__file__)) + '/game.save'

    # Loads game save and updates rimuru object in game_functions alongside debug variable, and shows start banner.
    rimuru = game_funcs.update_rimuru(game_funcs.game_load(save_path))

    if '-f' in sys.argv: rimuru.fast_mode = True
    if '-t' in sys.argv: rimuru.textcrawl = False
    if '-a' in sys.argv: rimuru.show_art = False
    if '-m' in sys.argv: rimuru.show_menu = True
    if '-hard' in sys.argv: rimuru.hardcore = True
    if '-hints' in sys.argv: rimuru.show_hints = False

    game_funcs.show_start_banner()

    # Text output is slowed and looks like it's being typed out character by character. For dramatic effect.
    if rimuru.textcrawl is None:
        print("\nEnable Text Crawl? (Recommended for easier reading)")
        if str(input("No / Yes or Enter > ")).lower() in ['n', 'no']:
            print("\n    < Text Crawl Deactivated >\n")
            rimuru.textcrawl = False
            sleep(1)
        else:
            rimuru.textcrawl = True
            print()
            game_funcs.siprint("< Text Crawl Activated >\n\n")

    if rimuru.show_hints is None:
        print("\nShow game hints? Suggest leave enabled if first time playing.")
        if str(input("No / Yes or Enter > ")).lower() in ['n', 'no']:
            print("\n    < Hints: Enabled >\n")
            rimuru.show_hints = False
        else:
            rimuru.show_hints = True
            game_funcs.siprint("\n < Hints: Disabled >\n")

    rimuru.current_location_object(rimuru)
