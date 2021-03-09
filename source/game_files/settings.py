import os, sys, pickle
from game_files.characters import Rimuru_Tempest

on_subs = ['activate', 'true', 'enable', 'on', '1']
off_subs = ['deactivate', 'false', 'disable', 'off', '0']


def game_restart(*args):
    """ Restart game. """

    print("    < Restarting Game... >")
    os.execl(sys.executable, sys.executable, *sys.argv)

def game_exit(*args):
    """ Saves game using pickle, then exits. """
    game_save()
    exit(0)

def game_save(level=None, show_msg=True):
    """
    Pickels Rimuru_Tempest object.

    Args:
        level [bool]: Update rimuru.current_location_object
        show_msg [bool:True]: Show Game Saved message.
    """

    if level:
        rimuru.current_location_object = level

    if rimuru.valid_save is None:
        rimuru.valid_save = True

    pickle.dump(rimuru, open(rimuru.save_path, 'wb'))
    if show_msg:
        print("\n    < Game Saved >\n")

def game_load(path):
    """
    Load game save.

    Args:
        path: Path of game save.

    Returns:
        Loaded game save object.
    """

    global rimuru

    # Tries loading game. If can't, creates new Rimuru_Tempest object which contains all game data that will be picked.
    try:
        rimuru = pickle.load(open(path, 'rb'))
    except:
        rimuru = Rimuru_Tempest()
        rimuru.save_path = path

        import chapters.tensei_1 as tensei1
        rimuru.current_location_object = tensei1.ch1_cave

    if rimuru.valid_save is False:
        os.remove(rimuru.save_path)
        game_load(path)

    return rimuru

def game_over():
    """ Deletes pickle save file. """

    rimuru.valid_save = False  # So you can't use copies of game save.
    game_save(show_msg=False)

    try:
        os.remove(rimuru.save_path)
    except:
        pass

    print("\n    < GAME OVER >\n")
    print("Play again?")
    if str(input('No / Yes or Enter > ')).lower() in ['n', 'no']:
        exit(0)
    else:
        game_restart()

def set_hud(arg):
    """
    Updates and gets rimuru.show_hud boolean. Shows and hides available actions.

    Args:
        arg: Enable or disable text crawl.

    Usage:
        > menu on
        > menu off
    """

    if rimuru.hardcore is True:
        rimuru.show_hud = False
        print("    < Error: Hardcore mode is active. \n>")
        return

    if arg in on_subs or rimuru.show_hud is True:
        rimuru.show_hud = True
    if arg in off_subs or rimuru.show_hud is False:
        rimuru.show_hud = False
    print(f"    < Action Menu: {'Enabled' if rimuru.show_hud else 'Disabled'} >\n")

def set_art(arg):
    """
    Enable/Disable ASCII art.

    Args:
        arg: Enable or disable ASCII art.

    Usage:
        ascii on
        ascii off
    """

    if arg in on_subs or rimuru.show_art is True:
        rimuru.show_art = True
    if arg in off_subs or rimuru.show_art is False:
        rimuru.show_art = False
    print(f"    < ASCII Art: {'Enabled' if rimuru.show_art else 'Disabled'} >\n")

def set_textcrawl(arg):
    """
    Updates and gets status for textcrawl.

    Args:
        arg: Enable or disable text crawl.

    Usage:
        > textcrawl
        > textcrawl on
        > textcrawl off
    """

    if arg in on_subs or rimuru.textcrawl is True:
        rimuru.textcrawl = True
    if arg in off_subs or rimuru.textcrawl is False:
        rimuru.textcrawl = False
    print(f"    < Text Crawl: {'Enabled' if rimuru.textcrawl else 'Disabled'} >\n")

def set_hints(arg):
    """ Enable/Disable game hints. """

    if rimuru.hardcore is True:
        rimuru.show_hud = False
        print("    < Error: Hardcore mode is active. \n>")
        return

    if arg in on_subs or rimuru.show_hints is True:
        rimuru.show_hints = True
    if arg in off_subs or rimuru.show_hints is False:
        rimuru.show_hints = False
    print(f"    < Hints: {'Enabled' if rimuru.show_hints else 'Disabled'} >\n")

def set_hardcore(arg):
    """
    Enable/Disable ASCII art.

    Args:
        arg: Enable or disable ASCII art.

    Usage:
        hardcore on
        hardcore off
    """

    if arg in on_subs or rimuru.hardcore is True:
        rimuru.hardcore = True
    if arg in off_subs or rimuru.hardcore is False:
        rimuru.hardcore = False
    print(f"    < Hardcore Mode: {'Enabled' if rimuru.hardcore else 'Disabled'} >\n")
