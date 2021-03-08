class Attributes:
    def attributes_generator(self, output=False):
        """
        Yields character's attributes game objects (skills/resistances).

        Args:
            output: Yields friendly string for in game printing.

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
                if output is False:
                    yield skill_object

                if skill_object.status:
                    yield f'    {skill_name} ({skill_object.status})'
                else:
                    yield f'    {skill_name}'

    def show_attributes(self, *args):
        """
        Prints out attribute of player or specified character. Includes info like Mimcking, Location, Full Name, etc.

        Usage:
            .show_attributes()
            .show_attributes('tempest serpent')

            > stats
            > stats tempest serpent
        """

        print("-----Attributes/Skills-----")
        print(f"Name: [{(self.name + ' ' + self.family_name).strip()}]")
        if self.current_mimic:
            print(f"Mimicking: [{self.current_mimic.name}]")  # If currently using Mimic.
        print(f"Location: {self.current_location}\n")

        # Print out skill category and corresponding skills indented.
        for i in self.attributes_generator(output=True):
            print(i)

    def add_attribute(self, attribute, show_acquired_msg=True, show_skill_info=False, top_newline=True, bot_newline=True):
        """
        Adds attribute to character.

        Args:
            attribute: Attribute to add to character.
            show_acquired_msg: Shows skill acquired message.
            show_skill_info: Shows skill information page.

        Usage:
            .add_attribute('rimuru', 'water blade')
        """

        # Checks if already acquired.
        if self.check_acquired(attribute):
            return False

        if attribute := self.get_object(attribute, new=True):
            self.attributes[attribute.skill_level][attribute.name] = attribute
            if show_acquired_msg:
                if top_newline: print()
                print(f"    < Acquired: {attribute.skill_level} [{attribute.name}] >")
                if bot_newline: print()
            if show_skill_info:
                self.show_info(attribute.name)

            return True
        return False

    def remove_attribute(self, attribute):
        """
        Removes attribute.

        Args:
            attribute: Attribute to remove.

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
            skill_from: Skill to upgrade from.
            skill_to str: Skill to upgrade to.

        Usage:
            .upgrade_attribute('sage', 'great sage')
        """

        skill_from = self.get_object(skill_from)
        skill_to = self.get_object(skill_to, new=True)
        if not skill_from and not skill_to:
            print("    < Error Evolving Skill >")
            return False

        print(f"    < Evolving {skill_from.skill_level} [{skill_from.name}] >")
        if self.remove_attribute(skill_from) and self.add_attribute(skill_to, show_acquired_msg=False):
            print(f"    < Evolution Successful {skill_from.skill_level} [{skill_from.name}] >>> {skill_to.skill_level} [{skill_to.name}] >")

    def check_resistance(self, attack, target=None):
        """
        Checks if character has resistance.

        Gets character object from parameter target, whether it's a string or already game object.
        Returns True if target has resistance to inputted attack.


        Args:
            attack: Attack to check resistance to.
            target: Check if specified target has resistance.

        Usage:
            .check_resistance('resist pain')
            .check_resistance('resist pain', 'ranga')
        """

        if type(target) == str:
            target = self.get_object(target)
        if not target:
            target = self

        # Checks if character has resistances.
        for resist_name, resist_object in target.attributes['Resistance'].items():
            for resist in resist_object.resist_types:
                if attack.damage_type in resist:
                    return True

    def use_skill(self, skill, character=None):
        """
        Uses spell and passes arguments to spell's corresponding function.

        Args:
            skill: Skill to use.
            character: Character that will use skill.

        Usage:
            > use sense heat source
        """

        if character is None:
            character = self

        if skill_object := self.get_object(skill):
            try:
                skill_object.use_skill(character)
                self.last_skill = skill_object
            except:
                return False
        else:
            return False
        print()
