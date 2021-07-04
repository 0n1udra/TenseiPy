from game_files.extra import get_any, mob_list_adder
from game_files.output import gprint

class Combat:
    def attack(self, user_input, user=None):
        """
        Checks if can attack, and if it was successful.

        Args:
            user_input str: Targets to attack, if multiple, separated by comma ','.
            user obj(None): The one who is attacking.

        Returns:
            bool: If attack was successful.

        Usage:
            > attack water blade
            > attack magic sword
        """

        attack_success = False
        skills = []
        if not user: user = self
        # If using mimic, allows usage of skills/attributes from mimicked mob.

        # TODO set combat to use get_random

        # Parse what attack(s) user wants to use.
        for current_attack in user_input.split(','):
            attack = user.get_object(current_attack)
            # If using mimic but player already has skill, will use player's skill instead of mimicked mob's.
            if not attack:
                try: attack = self.current_mimic.get_object(current_attack)
                except: pass

            if attack:
                # Adds skill to list of attacks to use against enemies.
                if attack.game_object_type == 'attribute':
                    skills.append(attack)
                if attack.game_object_type == 'item':
                    if attack.item_type == 'Weapon': skills.append(attack)
                if attack.game_object_type == 'character': continue
            else: continue

        for current_target in self.targeted_mobs:
            if not current_target[0].is_alive: continue
            for current_skill in skills:
                # If target is too high of a level to damage with skill.
                if current_target[0].level > current_skill.damage_level: continue

                # Checking if have resistance.
                if self.check_resistance(current_skill, current_target[0]):
                    gprint(f"<< Warning, {current_target.name} has resistance to {current_skill.damage_type}. >>")
                    continue

                self.data['kills'] += 1
                current_target[0].is_alive = False
                current_target[0].status = 'Dead'
                attack_success = True

        return attack_success
