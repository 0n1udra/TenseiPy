import game_files.functions as game
from game_files.output import dots, idots
from game_maps.locations import dwargon_weapons_shop
import game_files.extra as extra


def ch0(rimuru):
    #rimuru.add_inventory('hipokte grass')
    class foo():
        desc = 'bobbbbbbbb'
        def __init__(self): print("OK")

        def barf(self): print("BARF")
    def tester():
        __x = foo()
        class fa:
            class bar:
                def __init__(self): print(fa.__x)
        return fa

    def tester2():
        __x = foo()
        class fa:
            class bar:
                def __init__(self): print(fa.__x)
        return fa

    class bam(tester()):
        def __init__(self):
            game.actions(self)

    class test(dwargon_weapons_shop):
        def __init__(self):
            game.actions(self)

    #bam()
    test()
    pass
