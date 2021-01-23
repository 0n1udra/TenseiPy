from game_files.game_functions import *

on_subs = ['activate', 'true', 'enable', 'on', '1']
off_subs = ['deactivate', 'false', 'disable', 'off', '0']
move_on_subs = ['explore', 'wonder', 'move', 'move on', 'move forward', 'keep moving', 'keep exploring', 'explore more', 'explore further', 'keep fumbling', 'fumble around more', 'fumble more', 'bounce around more', 'keep bouncing', 'just move on', 'keep moving forward', 'continue forward', 'continue exploring']
wait_subs = ['wait', 'stay']
activate_subs = ['activate', 'activate it', 'yes activate', 'yes activate it', 'yes please activate']
do_it_subs = ['do it', 'yes do it', 'please do that', 'please do it', 'yes do that']
yes_subs = ['yes', 'yes please', 'sure', 'yep', 'affirmative', 'affirmatory', 'i consent', 'i give my consent']
all_yes_subs = activate_subs + do_it_subs + yes_subs
no_subs = ['negative', "that's a negative", 'that is a negative', 'negatory', 'i refuse', 'denied', 'cancel', 'cancel it' 'no', 'no thanks', 'nah', "don't", "please don't", "don't do it", 'do not do that', 'do not']

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
