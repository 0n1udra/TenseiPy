class Attributes:
    def __init__(self):
        self.attributes = {
            'Ultimate Skill': {},
            'Unique Skill': {},
            'Special Skill': {},
            'Extra Skill': {},
            'Intrinsic Skill': {},
            'Common Skill': {},
            'Daily Skill': {},
            'Composite Skill': {},
            'Resistance': {},
            'Attribute': {},
            'Manas': {},
        }

    def attributes_generator(self, character=None, output=False):
        """
        Yields character's attributes (skills/resistances).

        Args:
            character: Specifies character to get attributes from, default is Rimuru (player).
            output: Yields friendly string for in game printing.

        Usage:
            .attributes_generator('ranga', True)
        """

        for skill_type, skills in character.attributes.items():
            if output and skills:
                # Prints out skill category (Ultimate, Unique, etc)
                yield f'[{skill_type}]'

            for skill_name, skill_object in skills.items():
                # Prints if skill is active or passive
                if output:
                    if skill_object.active:
                        yield f'\t{skill_name} (Active)'
                    elif skill_object.passive:
                        yield f'\t{skill_name} (Passive)'
                    else:
                        yield f'\t{skill_name}'
                else:
                    yield skill_object

    def show_attributes(self, character=None):
        """
        Shows character's attributes if data is available.

        Args:
            character: Character's attributes to show.

        Usage:
            .show_attributes()
            .show_attributes('tempest serpent')

            > stats
            > stats tempest serpent
        """

        # If no character was specified, else show player stats (rimuru)
        try:
            character = self.get_object(character, mimic=True)
        except:
            pass
        if character is None:
            character = self


        print("-----Attributes/Skills-----")
        print(f"[{character.name} {character.family_name}]\n")

        for i in self.attributes_generator(character, output=True):
            print(i)

        # Only shows mimicry info when not looking at stats of other monsters and is currently using mimicry
        if self.current_mimic:
            print("\n-----Mimicry-----")
            print(f"Mimicking: [{character.current_mimic.name}]\n")
            for j in self.attributes_generator(character.current_mimic, True):
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
        if attribute:
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

        try:
            attribute = self.get_object(attribute)
            del self.attributes[attribute.skill_level][attribute.name]
        except:
            print("<Error removing attribute.>")

    def upgrade_attribute(self, skill_from, skill_to):
        """
        Upgrades skill.

        Args:
            skill_from: Skill to upgrade from.
            skill_to (str): Skill to upgrade to.

        Usage:
            .upgrade_attribute(skill_from, skill_to)
        """

        skill_from = self.get_object(skill_from)
        skill_to = self.get_object(skill_to, new=True)
        if skill_to and skill_from:
            self.remove_attribute(skill_from)
            print(f'    <<{skill_from.skill_level} [{skill_from}] evolving to {skill_to.skill_level} [{skill_to}]...>>')
            self.add_attribute(skill_to)

    def check_resistance(self, attack, target=None):
        """
        Checks if character has resistance.

        Args:
            attack: Attack to check resistance to.
            target: Check if specified target has resistance.

        Usage:
            .check_resistance('resist pain')
            .check_resistance('resist pain', 'ranga')
        """

        if self.is_str(target):
            target = self.get_object(target)
        if not target:
            target = self

        # Checks if character has resistance attribute
        for resist_name, resist_object in target.attributes['Resistance'].items():
            for resist in resist_object.resist_types:
                if attack.damage_type in resist:
                    return True

    def use_skill(self, skill, character=None):
        """
        Use skill.

        Args:
            skill: Skill to use.
            character: Character to use skill.

        Usage:
            > use sense heat source
        """
        try:
            self.current_mimic.get_object(skill).use_skill(character)
        except:
            try:
                self.get_object(skill).use_skill(character)
            except:
                pass


