from .game_location import Game_Location
from game_files.game_functions import *

class Sealed_Cave_Start(Game_Location):

    __location = 'Sealed Cave'

class Sealed_Cave(Game_Location):
    __location = 'Sealed Cave'

    def predate_grass(self):
        ssprint("Yay, even more grass!")
        rimuru.add_inventory('Hipokte Grass')
