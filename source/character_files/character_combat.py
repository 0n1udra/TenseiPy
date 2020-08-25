class Combat:
    def set_targets(self, targets):
        """
        Adds inputted targets to targeted_mobs list from user input.

        Separates user inputted targets via ',' then checks to see if mob is in current_level_mobs list.
        If so, adds to setTargets list.

        Args:
            targets: String of target(s) to add to targeted_mobs (list)

        Usage:
            > target tempest serpent, giant bat
        """

        if 'reset' in targets:
            self.targeted_mobs.clear()
        else:
            for target in targets.split(','):
                for i in self.current_level_mobs:
                    # Checks if target is targetable by checking if in current_level_mobs list.
                    if i.get_name() in target:
                        self.targeted_mobs.add(i)

    def attack(self, user_input):
        """
        Checks if can attack, and if it was successful.

        First separates the targets and attacks via splitting up targets_and_attacks by commas ','.
        Then Adds the targets and attacks to corresponding lists.
        Checks if target is not too high of a level for attack and doesn't have resistance to said attack.
        Will return booleans for if attack was attempted and if attack was successful.

        Args:
            user_input: Targets to attack, if multiple, separated by comma ','.

        Returns:
            attacked: If attack was attempted.
            attack_success: If attack was successful.

        Usage:
            > attack with water blade
            > attack water blade
        """

        attacks = skills = []
        targets = self.targeted_mobs
        attack_success = False

        # Tries to split up the inputted attacks.
        try:
            attacks.append(attacks.split(','))
        except AttributeError:
            attacks.append(user_input)

        # If mob is in current_level_mobs list and is is_alive, adds to focusTarget list.
        for attack in attacks:
            attack = self.get_object(j)
            if attack is not None:
                skills.append(attack)

        for current_target in targets:
            for current_skill in skills:
                if not self.check_resistance(current_skill, current_target):
                    if current_target.level <= current_skill.damage_level:
                        current_target.is_alive = False
                        attack_success = True
                        print(f"    < Eliminated {current_target.name}. >\n")
                    else:
                        print(f"    < {current_target.name} level too for that attack. >")
                else:
                    print(f"    << Warning, {current_target.name} has resistance to {current_skill.damage_type}. >>")

        return attack_success
