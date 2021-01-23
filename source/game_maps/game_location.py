from game_files.game_functions import *

class Game_Location:
    pass

class cave_actions:
    class eat_grass:
        __subs = ['predate grass', 'eat hipokte grass', 'predate hipokte grass']
        def __init__(self):
            rimuru.add_inventory('hipokte grass')

    class eat_ore:
        __subs = ['predate ore', 'eat magic ore', 'predate magic ore', 'eat rock', 'predate rock', 'eat magic rock', 'predate magic rock']
        def __init__(self):
            rimuru.add_inventory('magic ore')
