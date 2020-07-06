def ssprint(Msg):
    print(f'    {Msg}\n')


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

        # Specify character other than Rimuru.
        if character:
            character = self.get_object(character).attributes
        else:
            character = self.attributes

        for skill_type, skills in character.items():
            if output and skills:
                # Prints out skill category (Ultimate, Unique, etc) type also for printing in game.
                yield f'{skill_type}:'
            for skill_name, skill_object in skills.items():
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
            .show('tempest serpent')

            > stats
            > stats tempest serpent
        """

        # If no character was specified, else show player stats (rimuru)

        try:
            character = self.get_object(character)
        except:
            pass

        print(f"""
  -----Attributes/Skills-----
  Name: {self.name} {self.family_name}""")

        for i in self.attributes_generator(character, output=True):
            print(i)

        # Only shows mimicry info when not looking at stats of other monsters and is currently using mimicry
        if self.current_mimic:
            print("\n\t-----Mimicry-----")
            print(f"Mimicking: {character.current_mimic.name}\n")
            for j in self.attributes_generator(characterr.current_mimic, True):
                print(f'\t{j}')

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
            if not self.check_mob_has(attribute):
                self.attributes[attribute.skill_level][attribute.name] = attribute
            if show_acquired_msg:
                attribute.show_acquired_msg()
            if show_skill_info:
                # Shows skill info
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
            del self.attributes[attribute.attributeLevel][attribute.name]
        except:
            print("ERROR Deleting attribute. If you're seeing this message, please let developer know")

    def upgrade_attribute(self, skill_from, skill_to):
        """
        Upgrades skill.

        Args:
            skill_from: Skill to upgrade from.
            skill_to (str): Skill to upgrade to.

        Usage:
            .upgrade(skill_from, skill_to)
        """

        skill_from = self.get_object(skill_from)
        skill_to = self.get_object(skill_to, new=True)
        if skill_to and skill_from:
            self.remove_attribute(skill_from)
            ssprint(f'<<{skill_from.skill_level} [{skill_from}] evolving to {skill_to.skill_level} [{skill_to}]...>>')
            self.add_attribute(skill_to)

    def check_resistance(self, damage_type, target=None):
        """
        Checks if character has resistance.

        Args:
            damage_type: Damage type to check resistance to.
            target: Check if specified target has resistance.

        Usage:
            .check_resistance('resist pain')
            .check_resistance('resist pain', 'ranga')
        """

        if target:
            target = self.get_object(target)
        else:
            target = self

        # Checks if character has resistance attribute
        for resist_name, resist_object in target.attributes['Resistance'].items():
            for resist in resist_object.resistTypes:
                if resist.lower() == attack.lower():
                    return True
