class Combat:
    def set_targets(self, targets):
        """
        Adds inputted targets to targeted_mobs list from user input.

        Separates user inputted targets by ',' then checks to see if mob is in current_level_mobs list.
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
                    # If can able to target, by checking if in current_level_mobs list.
                    if i.get_name() in target:
                        self.targeted_mobs.add(i)

    def attack(self, user_input):
        """
        Checks if can attack, and if it was successful.

        First separates the targets and attacks by splitting up targets_and_attacks by commas ','.
        Then Adds the targets and attacks to corresponding lists.
        Checks if target is not too high of a level for attack, then if it has resistance to said attack.
        Will return booleans if attack was attempted and  successful.

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

        # Checks if receiving multiple spells (attacks).
        try:
            attacks.append(attacks.split(','))
        except: attacks.append(user_input)

        # If mob is in current_level_mobs list and is is_alive, adds to focusTarget list.
        for attack in attacks:
            attack = self.get_object(attack)
            if attack is not None:
                skills.append(attack)

        for current_target in targets:
            for current_skill in skills:

                # Checking if have resistance.
                if self.check_resistance(current_skill, current_target):
                    print(f"    << Warning, {current_target.name} has resistance to {current_skill.damage_type}. >>")
                    return False

                # If target is lower level.
                if current_target.level <= current_skill.damage_level:
                    print(f"    < {current_target.name} level too for that attack. >")
                    return False

                current_target.is_alive = False
                attack_success = True
                print(f"    < Eliminated {current_target.name}. >\n")

        return attack_success
