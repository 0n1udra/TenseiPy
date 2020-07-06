import os, pickle
from time import sleep
import chapters.tensei_1 as tensei1
import mobs

debug_mode = False

#                    ========== Game Input ==========
def action_menu(current_class):
    """
    Takes user input and runs corresponding actions.


    Args:
        current_class (obj):
            Current story progress class object.

    Usage:
        > inv
        > stats
        > attack tempest serpent with water blade
    """

    # Gets class functions and subclasses if it doesn't start with __
    class_funcs = [i for i in dir(current_class) if i[1] != '_']
    funcs = [i.replace('_', ' ') for i in class_funcs]
    # Functions starting with _ replaced with *, then replaces _ with space
    actions = [('*' + i[1:]) if i[0] == '_' else i for i in class_funcs]
    actions = [i.replace('_', ' ') for i in actions]

    show_hud(actions)

    if debug_mode:
        print(current_class)
        user_input = class_funcs[0].replace('_', ' ')[1:]
    else:
        user_input = input("\n> ").lower()
        print()

    # Get info on skills, times, etc
    split_user_input = ' '.join(user_input.split()[1:])
    level_actions = {
        'stats': mobs.rimuru.show,
        'target': mobs.rimuru.set_target,
        'predate': mobs.rimuru.predate_targets,
        'mimic': mobs.rimuru.use_mimic,
        'help': show_help,
        'inv': mobs.rimuru.show,
        'exit': exit
    }

    for k, v in level_actions.items():
        if k in user_input:
            v(split_user_input)

    if 'info' in user_input:
        mobs.rimuru.show_info(split_user_input)
    if 'use' in user_input:
        skill_success = mobs.rimuru.use_skill(split_user_input)
    if 'attack' in user_input:
        attacked, attack_success = mobs.rimuru.can_attack(split_user_input)
    try:
        pass
    except:
        pass

    loop = True
    attacked = attack_success = skill_success = False
    # If action has *, continues story
    for i in actions:
        current_action = i.replace('*', '_').replace(' ', '_')
        run_action = f'current_class.{current_action}()'
        if i[0] == '*':
            if user_input.lower() == i.lower()[1:]:

                eval(run_action)
                try:
                    pass
                except:
                    pass
                loop = False
                break
        else:
            if user_input.lower() == i.lower():
                eval(run_action)

    if skill_success or (attacked and attack_success):
        pass
        loop = False
    elif attacked and not attack_success:
        attackFail()

    if loop:
        action_menu(current_class)


def show_hud(actions):
    '''Shows user HUD with available actions and targets (if any).'''

    # Adds () around actions, (*action)
    options = ', '.join('(' + i + ')' for i in actions)
    mimicking = mobs.rimuru.current_mimic_name
    try:
        targets, = ', '.join([(i.name if i.alive else f'{i.name}(Dead)') for i in mobs.rimuru.focused_targets]),
    except:
        targets = None

    if targets:
        # print(f'\nTarget:', str(targets))
        print(f'\nTarget: {targets}\nActions:', options, f'| {mimicking}, (stats, inv, help)')
    else:
        print("\nActions:", options, f'| {mimicking}, (stats, inv, help)')


def show_help(*args):
    '''Shows help page.'''

    print("""
    Commands:
        target TARGET(s)            -- Target commands and abilities. E.g. 'target tempest serpent'
        attack <TARGET> with SKILL  -- Attack target(s) (if not already targeting) with skill(s). E.g. 'attack with water blade', 'attack tempest serpent with water blade'
          - Multiple targets and/or attacks separated by comma. E.g. 'attack tempest serpent, black spider with water blade, poisonous breath'
        use SKILL(s)                -- Use skill/items. E.g. 'use sense heat source'
        stats                       -- Show yours skills and resistances. 
          - stats TARGET            -- Stats for monsters you have predated. E.g. 'stats tempest serpent'
        inv                         -- Show inventory.
        info                        -- Show info on skill, item or character. E.g. 'info great sage, 'info hipokte grass', 'info tempest serpent'
                                       NOTE: To get info on skills from a monster, have to be mimicking corresponding monster. E.g. 'info sense heat source'
        help                        -- Show this help page.
        exit                        -- Exit game.

    Abilities:
        mimic ___                   -- Mimics appearance of of predated. E.g. 'mimic tempest serpent'
          - info mimic              -- Shows available mimicries.
          - mimic reset             -- Resets mimic (Back to slime)
        predate                     -- Predate target(s). Can only be used while you have target(s) command. E.g. 'predate'
        
    Game Dialogue:
        ~Message~                   -- Telepathy
        *Message*                   -- Story progression
        <Message>                   -- Acquired item, information, etc
        <<Message>>                 -- Great Sage (Raphael, Ciel)
        <<<Message>>>               -- Voice of the World

    HUD:
        Target: Currently Focused Target(s)
        Actions: (ACTION(s)) | MIMIC, (Extra Actions)
      E.g.
        Target: Giant Bat, Black Spider
        Actions: (*Attack), (*Move on) | Tempest Serpent, (stats, inv, help)

    Level/Ranking:
       Level      Rank         Risk
        11.     Special S   Catastrophe
        10.     S           Disaster
        9.      Special A   Calamity
        8.      A+          Tragedy
        7.      A           Hazard
        6.      A-          Danger
        5.      B           Pro
        4.      C           Advance
        3.      D           Intermediate
        2.      E           Beginner
        1.      F           Novice
    """)


# Checks if mob is alive
def get_mob_status(target):
    """
    Returns whether mob in current_mob list is alive.


    """
    try:
        for i in mobs.rimuru.current_level_characters:
            if target.lower() in i.get_name():
                return True
    except:
        pass


def add_level_mob(level_characters):
    """
    Adds new mob to current level in game.

    Args:
        level_characters: Mob character(s) to add to current level. Can be single mob (string) or multiple (list).

    Usage:
        .add_level_mob('tempest serpent')
        .add_level_mob(['tempest serpent', 'giant bat'])
    """
    if type(level_characters) == list:
        for i in level_characters:
            mob = mobs.rimuru.get_object(i, new=True)
            if mob:
                mobs.rimuru.current_level_characters.append(mob)
    else:
        mob = mobs.rimuru.get_object(level_characters, new=True)
        mobs.rimuru.current_level_characters.append(mobs.rimuru.get_object(mob, new=True))


#                    ========== Extra ==========
def tbc():
    ''' To Be Continued function.'''
    print("---TO BE CONTINUED---")
    input("Press Enter to exit > ")


#                    ========== Game Saves ==========
def load_save_game(path):
    try:
        rimuru = pickle.load(open(path, 'rb'))
        print("Loaded Player Save\n")
    except:
        rimuru = mobs.Rimuru_Tempest()
    return rimuru


def save_game(rimuru_object):
    pickle.dump(rimuru_object, open(rimuru_object.save_path, 'wb'))
    print("Game Saved To: player_save.p")


def delete_game_save(rimuru_object):
    try:
        os.remove(rimuru_object.save_path)
        print("Resetting Game. Deleted player_save.p")
    except:
        pass


def continue_story(rimuru_object, next_chapter):
    print("Continue to next chapter?")
    user_input = input("Y/N > ")
    rimuru_object.story_progress.append(next_chapter)
    save_game(rimuru_object)
    if user_input.lower() == 'y':
        next_chapter(rimuru_object)
    else:
        exit()


#                    ========== Game Functions ==========
def show_start_banner():
    print("\n----------Tensei Shitara Slime Datta Ken (That Time I Got Reincarnated as a Slime)----------\n")
    instructions = """
    NOTE: 
    - Set window size for ASCII art accordingly (Fullscreen recommended)
    - Access help, inventory and skills with help, inv and stats
    - * actions continues story (do NOT actually input *, or ()). Try the other actions first maybe, see what happens
    - Delete player_save.p to reset game progress (includes player inventory and skills)
    """
    print(instructions)
    mobs.rimuru.show()
    mobs.rimuru.show()
    print()


# ========== Printing
def sprint(Msg):
    msgLen = len(str(Msg))
    if mobs.rimuru.text_delay:
        if msgLen > 100:
            sTime = 1
        elif msgLen > 70 and msgLen > 80:
            sTime = 4
        elif msgLen > 50 and msgLen > 40:
            sTime = 3
        elif msgLen > 40 and msgLen > 20:
            sTime = 2
        elif msgLen < 10:
            sTime = 2
        elif msgLen < 5:
            sTime = 1
        else:
            sTime = 1
    else:
        sTime = 0

    print(Msg, '\n')
    sleep(sTime)


def ssprint(Msg):
    sprint(f'    {Msg}')


if __name__ == '__main__':
    # Get file path depending on Windows or not
    save_path = os.path.dirname(os.path.abspath(__file__)) + '/player_save.p'

    rimuru = mobs.update_character(load_save_game(save_path))
    rimuru.save_path = save_path
    show_start_banner()

    print("\nDisable text delay? (Recommend leaving enabled for easier reading)")
    setSleep = str(input("(Y)es/(N)o > "))
    if setSleep.lower() in ['yes', 'y']:
        print("Text Delay: DISABLED")
        mobs.rimuru.text_delay = False
    else:
        print("Text Delay: ENABLED")
    sleep(1)
    print("\n\n")

    rimuru.story_progress[0] = tensei1.Chapter1
    rimuru.story_progress[-1](mobs.rimuru)
