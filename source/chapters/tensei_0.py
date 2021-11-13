import game_files.functions as game
from game_files.output import dots, idots
from game_maps.game_location import dwargon_shops
import game_files.extra as extra


def ch0(rimuru):
    #rimuru.add_inventory('hipokte grass')
    class test(dwargon_shops):
        def __init__(self):
            game.actions(self)

    test()
    pass
