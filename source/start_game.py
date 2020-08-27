import os, sys
from time import sleep
import game_files.game_functions as game_funcs

if __name__ == '__main__':

    debug = False
    set_text_crawl = True
    if '-d' in sys.argv: debug = True
    if '-t' in sys.argv: set_text_crawl = False

    save_path = os.path.dirname(os.path.abspath(__file__)) + '/player_save.p'

    # Loads game save and updates rimuru object in game_functions alongside debug variable.
    rimuru = game_funcs.update_variables(game_funcs.load_save_game(save_path), debug)

    game_funcs.show_start_banner(rimuru)

    # Text crawl for those who don't understand. It's kinda like a typewriter effect,
    # text output is slowed and looks like it's being typed out character by character. For dramatic effect.
    if set_text_crawl:
        print("\nEnable text crawl? (Recommended for easier reading)")
        set_text_crawl = str(input("no/yes or Enter > "))
        #set_text_crawl = 'n'
        if set_text_crawl.lower() in ['n', 'no']:
            print("Text Delay: DISABLED")
            rimuru.text_crawl = False
            sleep(2)
        else:
            rimuru.text_crawl = True
            game_funcs.sprint("Text Delay: ENABLED")
        print("\n\n")
    else: rimuru.text_crawl = set_text_crawl

    rimuru.story_progress[-1](rimuru)
