import os
from time import sleep
import game_files.game_functions as game_funcs
import chapters.tensei_1 as tensei1

if __name__ == '__main__':
    # Get file path depending on Windows or not
    save_path = os.path.dirname(os.path.abspath(__file__)) + '/player_save.p'

    rimuru = game_funcs.update_character(game_funcs.load_save_game(save_path))

    rimuru.save_path = save_path
    game_funcs.show_start_banner(rimuru)

    print("\nEnable text crawl? (Recommended for easier reading)")
    setSleep = str(input("no/yes or Enter > "))
    if setSleep.lower() in ['n', 'no']:
        print("Text Delay: DISABLED")
        rimuru.text_delay = False
    else:
        print("Text Delay: ENABLED")
    sleep(1)
    print("\n\n")

    rimuru.story_progress[0] = tensei1.Chapter1
    rimuru.story_progress[-1](rimuru)
