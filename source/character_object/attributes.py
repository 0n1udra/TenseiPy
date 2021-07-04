from game_files.output import gprint, print_header

class Attributes:
    def attributes_generator(self, printout_mode=False):
        """
        Yields all the character's attributes (skills/resistances).

        Args:
            output bool(False): Yields text for in-game interface.

        Usage:
            .attributes_generator()
            .attributes_generator(printout_mode=True)
        """

        for skill_type, skills_list in self.attributes.items():
            # Prints out skill category (Ultimate, Unique, etc). So far it's easier to put the code for printing user stat info here.
            if printout_mode and skills_list: yield f'    [{skill_type}]'

            for skill_name, skill in skills_list.items():
                # Yields skill game object if not in printing mode.
                if not printout_mode:
                    yield skill
                    continue

                if skill.status:  # e.g. Active, Passive, etc.
                    yield f'        {skill_name} ({skill.status})'
                else: yield f'        {skill_name}'

    def show_attributes(self, mob=None, *args):
        """
        Shows acquired attribute. Might include: Mimicking, Location, etc.

        Usage:
            .show_attributes()
            .show_attributes('tempest serpent')

            > stats
            > stats tempest serpent
        """

        if mob: mob = self.get_object(mob, item_pool=[*self.mimic_generator()], sub_pool=True)
        if not mob: mob = self  # If no specified mob, shows player's stats.

        print_header('Attributes', 10)
        print(f"    Name: [{(mob.name + ' ' + mob.family_name).strip()}]")
        print(f"    Level: {mob.level}")
        print(f"    Location: {mob.current_location}\n")
        # Print out skills organized in corresponding category (Unique Skill, Extra Skill, etc).
        for i in mob.attributes_generator(printout_mode=True): print(i)

        # Shows only if using mimic and if getting stats on thyself.
        if self.current_mimic and self.check_if_player():
            print(f"\n    Mimicking: [{self.current_mimic.name}]\n")
            for i in self.current_mimic.attributes_generator(printout_mode=True): print(i)

    def add_attribute(self, attribute, show_acquired_msg=True, show_skill_info=False):
        """
        Adds attribute to character.

        Args:
            attribute str: Attribute to acquire.
            show_acquired_msg bool(True): Shows skill acquired message.
            show_skill_info bool(False): Shows skill information page after acquisition.

        Usage:
            .add_attribute('rimuru', 'water blade')
        """

        # Checks if already acquired.
        if self.check_acquired(attribute): return True

        if attribute := self.get_object(attribute, new=True):
            # Add to attributes dictionary, sets quantity to 1 so check_acquired func can work properly.
            attribute = attribute(1)
            self.attributes[attribute.skill_level][attribute.name] = attribute

            # Show acquisition message and/or skill's info page.
            if show_acquired_msg: gprint(f"< Acquired: {attribute.skill_level} [{attribute.name}] >")
            if show_skill_info: self.show_info(attribute.name)
            return True

    def remove_attribute(self, attribute):
        """
        Removes attribute.

        Args:
            attribute str: Attribute to remove.

        Usage:
            .remove_attribute('resist poison')
        """

        if attribute := self.get_object(attribute):
            del self.attributes[attribute.skill_level][attribute.name]
            return True

    def upgrade_attribute(self, skill_from, skill_to):
        """
        Evolve skill.

        Args:
            skill_from str: Original skill.
            skill_to str: Skill to upgrade into.

        Usage:
            .upgrade_attribute('sage', 'great sage')
        """

        # Gets skill object from attributes dict, then
        skill_from = self.check_acquired(skill_from)
        skill_to = self.get_object(skill_to, new=True)
        if not skill_from or not skill_to: return False

        gprint(f"< Evolving {skill_from.skill_level} [{skill_from.name}] >")
        # Removes old attribute and adds new one.
        if self.remove_attribute(skill_from) and self.add_attribute(skill_to, show_acquired_msg=False):
            gprint(f"< Evolution Successful: {skill_from.skill_level} [{skill_from.name}] to {skill_to.skill_level} [{skill_to.name}] >")

    def check_resistance(self, attack, target=None):
        """
        Checks if character has resistance.

        Gets character object from parameter target, whether it's a string or already game object.
        Returns True if target has resistance to inputted attack.


        Args:
            attack str: Attack to check resistance to.
            target str(None): Check if specified target has resistance. Can also take game object.

        Usage:
            .check_resistance('resist pain')
            .check_resistance('resist pain', 'ranga')
        """

        if type(target) is str:
            target = self.get_object(target)
        if not target: target = self

        # Checks if character has resistances.
        for resist_name, resist_object in target.attributes['Resistance'].items():
            for resist in resist_object.resist_types:
                if attack.damage_type in resist: return True

    def use_action(self, skill, character=None):
        """
        Uses spell and passes arguments to spell's corresponding function.

        Args:
            skill str: Skill to use.
            character str(None): Character that will use skill.

        Usage:
            > use sense heat source
        """

        if character is None: character = self

        # If using mimicry skill, tries to get skill object from mimicked mob's attributes.
        try: skill_object = self.current_mimic.get_object(skill)
        except: skill_object = character.get_object(skill)

        if not skill_object: return False  # No skill was found.

        # Activates skill and returns any usage data.
        if return_data := skill_object.use_action(character):
            character.last_use_skill = skill_object
            return return_data
