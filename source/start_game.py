import os, sys
from time import sleep
import game_files.game_functions as game_funcs

__version__ = "3.1 Alpha"
__author__ = "D Thomas"
__email__ = "dt01@pm.me"
__license__ = "GPL 3"
__status__ = "Development"

if __name__ == '__main__':

    # Enable debug mode and disable text crawl.
    debug = False
    set_text_crawl = True
    if '-d' in sys.argv:
        debug = True
        set_text_crawl = False
    if '-t' in sys.argv:
        set_text_crawl = False

    save_path = os.path.dirname(os.path.abspath(__file__)) + '/game.save'

    # Loads game save and updates rimuru object in game_functions alongside debug variable, and shows start banner.
    rimuru = game_funcs.update_variables(game_funcs.game_load(save_path), debug)
    game_funcs.show_start_banner(rimuru)

    # Text output is slowed and looks like it's being typed out character by character. For dramatic effect.
    if set_text_crawl is False:
        rimuru.text_crawl = False
    else:
        print("\nEnable text crawl? (Recommended for easier reading)")
        if str(input("No/Yes or Enter > ")).lower() in ['n', 'no']:
            print("Text Delay: DISABLED")
            rimuru.text_crawl = False
            sleep(2)
        else:
            rimuru.text_crawl = True
            game_funcs.sprint("Text Delay: ENABLED\n\n")

    rimuru.story_progress[-1](rimuru)
