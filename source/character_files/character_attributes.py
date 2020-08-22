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
            .attributes_generator('ranga', output=True)
        """

        if character is None:
            character = self

        for skill_type, skills in character.attributes.items():
            if output and skills:
                # Prints out skill category (Ultimate, Unique, etc)
                # So far it's easier to put the code for printing user stat info here.
                yield f'[{skill_type}]'
            for skill_name, skill_object in skills.items():
                # Prints if skill is active or passive
                if output:
                    if skill_object.active:
                        yield f'    {skill_name} (Active)'
                    elif skill_object.passive:
                        yield f'    {skill_name} (Passive)'
                    else:
                        yield f'    {skill_name}'
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

        # Checks whether or not you have analyzed the target before (using mimicry functions), if not it'll return None.


        character = self.get_object(character, mimic=True)

        # If no character was specified show player stats (rimuru)
        if character is None:
            character = self

        # Only allow Character objects.
        if character.game_object_type != 'character':
            return

        print("-----Attributes/Skills-----")
        # Prints character's name. Without the if statement if the character doesn't have a family_name it'll show an extra space in the [] at the end, doesn't look so pretty.
        print(f"Name: [{character.name}{' '+character.family_name if character.family_name else ''}]\n")

        for i in self.attributes_generator(character, output=True):
            print(i)

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

        attribute = self.get_object(attribute)
        if attribute:
            del self.attributes[attribute.skill_level][attribute.name]

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
            print(f"    << {skill_from.skill_level} [{skill_from.name}] evolving to {skill_to.skill_level} [{skill_to.name}]... >>")
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

        if type(target) == str:
            target = self.get_object(target)
        if not target:
            target = self

        # Checks if character has resistance attribute
        for resist_name, resist_object in target.attributes['Resistance'].items():
            for resist in resist_object.resist_types:
                if attack.damage_type in resist:
                    return True

    def use_skill(self, skill, user=None, target=None):
        """
        Use skill.

        Args:
            skill: Skill to use.

        Usage:
            > use sense heat source
        """

        # Set default user of skill and target of skill.
        if user is None:
            user = self
        if target is None:
            target = self

        skill = self.get_object(skill)
        if skill:
            skill.use_skill(user=user, target=target)


