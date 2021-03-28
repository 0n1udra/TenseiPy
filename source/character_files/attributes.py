class Attributes:
    def attributes_generator(self, output=False):
        """
        Yields character's attributes game objects (skills/resistances).

        Args:
            output bool(False): Yields friendly string for in game printing.

        Usage:
            .attributes_generator()
            .attributes_generator(output=True)
        """

        for skill_type, skills in self.attributes.items():
            # Prints out skill category (Ultimate, Unique, etc). So far it's easier to put the code for printing user stat info here.
            if output and skills:
                yield f'[{skill_type}]'

            for skill_name, skill_object in skills.items():
                # Yields skill game object if not in printing mode.
                if not output:
                    yield skill_object

                if skill_object.status:
                    yield f'    {skill_name} ({skill_object.status})'
                else:
                    yield f'    {skill_name}'

    def show_attributes(self, mob=None, *args):
        """
        Prints out attribute of player or specified character. Includes info like Mimicking, Location, Full Name, etc.

        Usage:
            .show_attributes()
            .show_attributes('tempest serpent')

            > stats
            > stats tempest serpent
        """

        if mob:
            mob = self.get_object(mob, item_pool=[*self.mimic_generator()])
        if not mob: mob = self


        print("----- Skills -----")
        print(f"Name: [{(mob.name + ' ' + mob.family_name).strip()}]")
        print(f"Level: {mob.level}")
        print(f"Location: {mob.current_location}\n")

        # Print out skill category and corresponding skills indented.
        for i in mob.attributes_generator(output=True):print(i)

        if self.current_mimic:
            print("\n----- Mimicked Attributes -----")
            print(f"Mimicking: [{self.current_mimic.name}]")  # If currently using Mimic.
            for i in self.current_mimic.attributes_generator(output=True):print(i)

    def add_attribute(self, attribute, show_acquired_msg=True, show_skill_info=False):
        """
        Adds attribute to character.

        Args:
            attribute str: Attribute to add to character.
            show_acquired_msg bool(True): Shows skill acquired message.
            show_skill_info bool(False): Shows skill information page.
            top_newline bool(True): Print newline beforehand.

        Usage:
            .add_attribute('rimuru', 'water blade')
        """

        # Checks if already acquired.
        if self.check_acquired(attribute): return False

        if attribute := self.get_object(attribute, new=True):
            # Adds item to character's attributes dictionary, sets quantity so check_acquired func can work.
            if not attribute.initialized:
                attribute = attribute()
                attribute.quantity = 1
            self.attributes[attribute.skill_level][attribute.name] = attribute

            # If want to show acquisition message and/or skill's info page.
            if show_acquired_msg:
                print(f"    < Acquired: {attribute.skill_level} [{attribute.name}] >")
            if show_skill_info:
                self.show_info(attribute.name)

            return True
        return False

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
        Upgrades skill.

        Grabs game object for skill_from, and creates new game object for skill_to.
        Removes old skill and adds new skill.

        Args:
            skill_from str: Skill to upgrade from.
            skill_to str: Skill to upgrade to.

        Usage:
            .upgrade_attribute('sage', 'great sage')
        """

        skill_from = self.check_acquired(skill_from)
        skill_to = self.get_object(skill_to, new=True)
        if not skill_from or not skill_to: return False

        print(f"    < Evolving {skill_from.skill_level} [{skill_from.name}] >")
        if self.remove_attribute(skill_from) and self.add_attribute(skill_to, show_acquired_msg=False):
            print(f"    < Evolution Successful: {skill_from.skill_level} [{skill_from.name}] to {skill_to.skill_level} [{skill_to.name}] >")

    def check_resistance(self, attack, target=None):
        """
        Checks if character has resistance.

        Gets character object from parameter target, whether it's a string or already game object.
        Returns True if target has resistance to inputted attack.


        Args:
            attack str: Attack to check resistance to.
            target str ,obj: Check if specified target has resistance.

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
                if attack.damage_type in resist:
                    return True

    def use_action(self, skill, character=None):
        """
        Uses spell and passes arguments to spell's corresponding function.

        Args:
            skill str: Skill to use.
            character str: Character that will use skill.

        Usage:
            > use sense heat source
        """

        if character is None: character = self

        if skill_object := character.get_object(skill):
            if return_data := skill_object.use_action(character):
                character.last_use_skill = skill_object
                return return_data
            print()
