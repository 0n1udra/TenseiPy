class Attributes:
    def attributes_generator(self, character=None, output=False):
        """
        Yields character's attributes game objects (skills/resistances).

        Args:
            character: Specifies character to get attributes from, default is Rimuru (player).
            output: Yields friendly string for in game printing.

        Usage:
            .attributes_generator('ranga', output=True)
        """

        if character is None: character = self

        for skill_type, skills in character.attributes.items():

            # Prints out skill category (Ultimate, Unique, etc)
            # So far it's easier to put the code for printing user stat info here.
            if output and skills: yield f'[{skill_type}]'

            for skill_name, skill_object in skills.items():

                # Yields skill game object if not in printing mode.
                if not output: yield skill_object

                # Prints skill's active or passive status.
                if skill_object.active:
                    yield f'    {skill_name} (Active)'
                elif skill_object.passive:
                    yield f'    {skill_name} (Passive)'
                else: yield f'    {skill_name}'

    def show_attributes(self, character=None):
        """
        Prints out attribute of player or specified character.

        Args:
            character: Character's attributes to show.

        Usage:
            .show_attributes()
            .show_attributes('tempest serpent')

            > stats
            > stats tempest serpent
        """

        character = self.get_object(character, mimic=True)
        if character is None: character = self
        if character.game_object_type != 'character': return

        print("-----Attributes/Skills-----")
        # Prints character's name. Without the if statement if the character doesn't have a family_name it'll show an extra space in the [] at the end, doesn't look so pretty.
        print(f"Name: [{character.name}{' ' + character.family_name if character.family_name else ''}]")
        print(f"Location: {character.current_location}\n")

        for i in self.attributes_generator(character, output=True): print(i)

        # Only shows mimicry info when not looking at stats of other monsters and if currently using mimicry
        if self.current_mimic:
            print(f"\nMimicking: [{self.current_mimic.name}]")
            for j in self.attributes_generator(self.current_mimic, output=True):
                print(f'{j}')
        print()

    def add_attribute(self, attribute, show_acquired_msg=True, show_skill_info=False):
        """
        Adds attribute to character.

        Args:
            attribute: Attribute to add to character.
            show_acquired_msg: Shows skill acquired message.
            show_skill_info: Shows skill information page.

        Usage:
            .add_attribute('rimuru', 'water blade')
        """

        attribute = self.get_object(attribute, new=True)
        if not attribute: return

        self.attributes[attribute.skill_level][attribute.name] = attribute
        if show_acquired_msg:
            attribute.show_acquired_msg()
        if show_skill_info:
            self.show_info(attribute.name)

    def remove_attribute(self, attribute):
        """
        Removes attribute.

        Args:
            attribute: Attribute to remove.

        Usage:
            .remove_attribute('resist poison')
        """

        attribute = self.get_object(attribute)
        if not attribute: return

        del self.attributes[attribute.skill_level][attribute.name]

    def upgrade_attribute(self, skill_from, skill_to):
        """
        Upgrades skill.

        Grabs game object for skill_from, and creates new game object for skill_to.
        Removes old skill and adds new skill.

        Args:
            skill_from: Skill to upgrade from.
            skill_to (str): Skill to upgrade to.

        Usage:
            .upgrade_attribute('sage', 'great sage')
        """

        skill_from = self.get_object(skill_from)
        skill_to = self.get_object(skill_to, new=True)
        if not skill_to and not skill_from: return

        self.remove_attribute(skill_from)
        print(f"\n    << {skill_from.skill_level} [{skill_from.name}] evolving to {skill_to.skill_level} [{skill_to.name}]... >>")
        self.add_attribute(skill_to)

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

        if type(target) == str: target = self.get_object(target)
        if not target: target = self

        # Checks if character has resistances.
        for resist_name, resist_object in target.attributes['Resistance'].items():
            for resist in resist_object.resist_types:
                if attack.damage_type in resist:
                    return True

    def use_skill(self, skill, *args):
        """
        Uses spell and passes arguments to spell's corresponding function.

        Args:
            skill: Skill to use.

        Usage:
            > use sense heat source
        """

        skill = self.get_object(skill)
        if not skill: return False

        try: skill.use_skill(args)
        except: pass
