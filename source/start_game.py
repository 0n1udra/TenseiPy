import os, sys
from time import sleep
import game_files.game_functions as game_funcs

__version__ = "3.1 Alpha"
__author__ = "D Thomas"
__email__ = "dt01@pm.me"
__license__ = "GPL 3"
__status__ = "Development"

def help_page():
    print("""
    -f  --  Fast mode, goes through storyline actions as quick as possible. Also disables text crawl and ascii art.
    -t  --  Disable text crawl effect.
    -a  --  Hides ASCII art.
    -h  --  This help page.
    """)
    exit(0)

if __name__ == '__main__':
    if '-h' in sys.argv: help_page()

    save_path = os.path.dirname(os.path.abspath(__file__)) + '/game.save'

    # Loads game save and updates rimuru object in game_functions alongside debug variable, and shows start banner.
    rimuru = game_funcs.update_rimuru(game_funcs.game_load(save_path))
    game_funcs.show_start_banner(rimuru)

    if '-f' in sys.argv:
        game_funcs.set_fast_mode()
    if '-t' in sys.argv: rimuru.text_crawl = False
    if '-a' in sys.argv: rimuru.show_ascii = False

    # Text output is slowed and looks like it's being typed out character by character. For dramatic effect.
    if rimuru.text_crawl is None:
        print("\nEnable Text Crawl? (Recommended for easier reading)")
        if str(input("No/Yes or Enter > ")).lower() in ['n', 'no']:
            print("\n    < Text Crawl Deactivated. > ")
            rimuru.text_crawl = False
            sleep(2)
        else:
            rimuru.text_crawl = True
            print()
            game_funcs.ssprint("< Text Crawl Activated. >\n\n")

    rimuru.story_progress[-1](rimuru)
