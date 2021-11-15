from game_files.functions import rimuru
from game_objects.Vendor import Vendor

class subs:
    attack = ['attack']
    eat = ['predate', 'use predator', 'eat target', 'eat target', 'predate target', 'use predation on target', 'use predation']
    move_on = ['explore', 'wonder', 'move', 'move on', 'move forward', 'keep moving', 'keep exploring', 'explore more', 'explore further', 'keep fumbling', 'fumble around more', 'fumble more',
               'bounce around more', 'keep bouncing', 'just move on', 'keep moving forward', 'continue forward', 'continue exploring', 'continue']
    wait = ['wait', 'stay', 'hold']
    be_nice_subs = ['nice', 'be nice', 'friendly', 'be friendly']

    who = ['who are you', 'who are you guys']
    want = ['what do you want', 'do you want something']
    what = ['what are you', 'what is this']

    activate = ['activate', 'activate it', 'yes activate', 'yes activate it', 'yes please activate']
    do_it = ['do it', 'yes do it', 'please do that', 'please do it', 'yes do that']
    yes = ['yes', 'yes please', 'sure', 'yep', 'affirmative', 'affirmatory', 'i consent', 'i give my consent']
    no = ['no', 'nah', 'negative', "that's a negative", 'that is a negative', 'negatory', 'i refuse', 'denied', 'cancel', 'cancel it',  'no thanks', "don't", "please don't", "don't do it", 'do not do that', 'do not']
    all_yes = activate + do_it + yes + do_it

class Game_Location:
    __location = ''

class cave_actions:
    class eat_grass:
        __subs = ['predate grass', 'eat hipokte grass', 'predate hipokte grass']
        def __init__(self): rimuru.add_inventory('hipokte grass')

    class eat_ore:
        __subs = ['predate ore', 'eat magic ore', 'predate magic ore', 'eat rock', 'predate rock', 'eat magic rock', 'predate magic rock']
        def __init__(self): rimuru.add_inventory('magic ore')
